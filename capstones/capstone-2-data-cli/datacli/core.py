"""
datacli.core -- the actual data-analysis logic.

Deliberately kept separate from cli.py: this module knows nothing about
argparse, sys.argv, or printing to a terminal. It reads a CSV with
pandas, computes totals/breakdowns/outliers, and raises plain Python
exceptions on bad input. That separation means core.py could be reused
by a future web dashboard, a notebook, or a test suite without dragging
any command-line concerns along with it.

Every function that needs a column name takes it as a parameter --
nothing in this file is hardcoded to any one dataset's column names
(no 'product', 'region', 'revenue', etc.). That's what lets the same
functions work on a sales CSV, an expense CSV, or a weather CSV.
"""

import logging
from pathlib import Path

import pandas as pd

logger = logging.getLogger(__name__)


class DataCliError(Exception):
    """Raised for any user-facing error (missing file, missing column, bad data)."""


def _require_columns(df: pd.DataFrame, columns: list[str], source: str) -> None:
    """
    Raise a clear DataCliError if any of `columns` is not in `df`.

    This is what stands between a user's typo (e.g. --group-by Regoin)
    and a raw pandas KeyError traceback -- it names both what was
    requested and what columns actually exist in the file.
    """
    available = list(df.columns)
    missing = [c for c in columns if c not in available]
    if missing:
        missing_str = ", ".join(repr(c) for c in missing)
        available_str = ", ".join(repr(c) for c in available)
        raise DataCliError(
            f"Column(s) {missing_str} not found in {source}. "
            f"Available columns are: {available_str}."
        )


def load_csv(path: str | Path, required_columns: list[str] | None = None) -> pd.DataFrame:
    """
    Load a CSV file into a DataFrame.

    `required_columns`, if given, is validated immediately so a missing
    or misspelled column is reported clearly at load time rather than
    surfacing later as a confusing error deep inside a groupby.
    """
    path = Path(path)
    logger.debug("Loading CSV from %s", path)

    if not path.exists():
        raise DataCliError(f"File not found: {path}")

    try:
        df = pd.read_csv(path)
    except pd.errors.EmptyDataError as exc:
        raise DataCliError(f"File {path} is empty or contains no columns.") from exc
    except pd.errors.ParserError as exc:
        raise DataCliError(f"File {path} could not be parsed as CSV: {exc}") from exc

    if df.empty:
        logger.warning("Loaded %s but it has no data rows.", path)

    logger.debug("Loaded %d row(s), columns: %s", len(df), list(df.columns))

    if required_columns:
        _require_columns(df, required_columns, source=str(path))

    return df


def _numeric_series(df: pd.DataFrame, column: str, source: str) -> pd.Series:
    """
    Return `df[column]` coerced to numeric, raising a clear error if the
    column can't reasonably be treated as numbers (e.g. it's full of
    text, or a currency-formatted string like "$1,234.56").

    pandas would otherwise silently turn unparseable values into NaN
    and let totals/comparisons quietly go wrong -- we'd rather fail
    loudly and name the offending column.
    """
    _require_columns(df, [column], source)
    series = df[column]
    if pd.api.types.is_numeric_dtype(series):
        return series

    coerced = pd.to_numeric(series, errors="coerce")
    bad_count = coerced.isna().sum() - series.isna().sum()
    if bad_count > 0:
        raise DataCliError(
            f"Column {column!r} in {source} contains non-numeric values "
            f"that can't be used for calculations (e.g. currency symbols, "
            f"commas, or text). {bad_count} row(s) failed to convert. "
            f"Clean the column first (e.g. strip '$' and ',' characters)."
        )
    return coerced


def compute_total(df: pd.DataFrame, value_column: str, group_by: str | None = None):
    """
    Compute the sum of `value_column`.

    If `group_by` is given, returns a pandas Series of per-group totals
    (index = group value, value = summed total), matching Chapter 24's
    .groupby().sum() pattern. Otherwise returns a single float: the
    grand total across the whole column.
    """
    source = "the loaded data"
    values = _numeric_series(df, value_column, source)

    if group_by is None:
        total = float(values.sum())
        logger.debug("Computed grand total for %s: %s", value_column, total)
        return total

    _require_columns(df, [group_by], source)
    working = df.copy()
    working[value_column] = values
    totals = working.groupby(group_by)[value_column].sum().sort_values(ascending=False)
    logger.debug("Computed %d group total(s) for %s by %s", len(totals), value_column, group_by)
    return totals


def top_n(df: pd.DataFrame, group_by: str, value_column: str, n: int = 5) -> pd.Series:
    """
    Return the top `n` groups by summed `value_column`, descending.

    Reuses Chapter 24's groupby + sum + sort_values(ascending=False)
    pipeline, generalized to any group/value column pair.
    """
    if n <= 0:
        raise DataCliError(f"--top must be a positive integer, got {n}.")

    totals = compute_total(df, value_column, group_by=group_by)
    result = totals.head(n)
    logger.debug("top_n: returning %d of %d group(s)", len(result), len(totals))
    return result


def flag_outliers(df: pd.DataFrame, column: str, threshold: float, mode: str = "below") -> pd.DataFrame:
    """
    Return the rows of `df` whose (numeric) `column` value is below
    (mode="below", the default) or above (mode="above") `threshold`.

    Chapter 24's boolean-filtering pattern (df[df['revenue'] < threshold]),
    generalized to any column and either direction.
    """
    if mode not in ("below", "above"):
        raise DataCliError(f"flag_outliers mode must be 'below' or 'above', got {mode!r}.")

    source = "the loaded data"
    values = _numeric_series(df, column, source)
    working = df.copy()
    working[column] = values

    if mode == "below":
        flagged = working[working[column] < threshold]
    else:
        flagged = working[working[column] > threshold]

    logger.debug("flag_outliers: %d row(s) flagged (%s %s)", len(flagged), mode, threshold)
    return flagged


def summary_stats(df: pd.DataFrame, column: str) -> dict:
    """
    NumPy-backed summary statistics (mean, median, std, min, max) for a
    numeric column -- the Chapter 23 stretch goal, reusing pandas'
    NumPy-backed aggregate methods on a Series.
    """
    values = _numeric_series(df, column, "the loaded data")
    return {
        "count": int(values.count()),
        "mean": float(values.mean()),
        "median": float(values.median()),
        "std": float(values.std()) if values.count() > 1 else 0.0,
        "min": float(values.min()),
        "max": float(values.max()),
    }


def format_report(
    df: pd.DataFrame,
    group_by: str,
    value_column: str,
    top: int = 5,
    outlier_threshold: float | None = None,
) -> str:
    """
    Combine total + top-N breakdown + flagged outliers into one
    readable, multi-section report string -- Chapter 24's
    format_report(), generalized to any group/value column pair.
    """
    lines: list[str] = []

    grand_total = compute_total(df, value_column, group_by=None)
    lines.append(f"=== Total {value_column} ===")
    lines.append(f"{grand_total:,.2f}")
    lines.append("")

    lines.append(f"=== Top {top} {group_by} by {value_column} ===")
    ranked = top_n(df, group_by, value_column, n=top)
    if len(ranked) == 0:
        lines.append("(no data)")
    else:
        for key, total in ranked.items():
            lines.append(f"{key}: {total:,.2f}")
    lines.append("")

    stats = summary_stats(df, value_column)
    lines.append(f"=== Summary Statistics for {value_column} ===")
    lines.append(
        f"count={stats['count']}, mean={stats['mean']:,.2f}, "
        f"median={stats['median']:,.2f}, std={stats['std']:,.2f}, "
        f"min={stats['min']:,.2f}, max={stats['max']:,.2f}"
    )
    lines.append("")

    if outlier_threshold is None:
        outlier_threshold = stats["mean"]
    lines.append(f"=== Flagged Rows ({value_column} < {outlier_threshold:,.2f}) ===")
    weak = flag_outliers(df, value_column, outlier_threshold, mode="below")
    if len(weak) == 0:
        lines.append("(none)")
    else:
        for _, row in weak.iterrows():
            lines.append(", ".join(f"{col}={row[col]}" for col in df.columns))

    return "\n".join(lines)
