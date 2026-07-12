"""
test_core.py -- pytest suite for datacli.core.

Tests the analysis logic directly (no argparse, no subprocess), the
same "core.py is testable without a terminal attached" point the
README's architecture section makes about the core.py/cli.py split.

Follows the AAA pattern (Arrange, Act, Assert) from Chapter 27.
"""

import pandas as pd
import pytest

from datacli.core import (
    DataCliError,
    compute_total,
    flag_outliers,
    format_report,
    load_csv,
    summary_stats,
    top_n,
)


@pytest.fixture
def sales_df():
    return pd.DataFrame(
        {
            "product": ["Widget", "Gadget", "Gizmo", "Widget", "Gadget"],
            "region": ["East", "West", "East", "West", "East"],
            "revenue": [1200, 950, 1830, 540, 1254],
        }
    )


# --- load_csv --------------------------------------------------------------


def test_load_csv_happy_path(tmp_path):
    csv_path = tmp_path / "data.csv"
    csv_path.write_text("a,b\n1,2\n3,4\n")

    df = load_csv(csv_path)

    assert list(df.columns) == ["a", "b"]
    assert len(df) == 2


def test_load_csv_missing_file_raises(tmp_path):
    missing = tmp_path / "nope.csv"

    with pytest.raises(DataCliError, match="File not found"):
        load_csv(missing)


def test_load_csv_empty_file_raises(tmp_path):
    empty = tmp_path / "empty.csv"
    empty.write_text("")

    with pytest.raises(DataCliError, match="empty"):
        load_csv(empty)


def test_load_csv_required_columns_missing_raises(tmp_path):
    csv_path = tmp_path / "data.csv"
    csv_path.write_text("a,b\n1,2\n")

    with pytest.raises(DataCliError, match="Regoin"):
        load_csv(csv_path, required_columns=["a", "Regoin"])


# --- compute_total -----------------------------------------------------


def test_compute_total_grand_total(sales_df):
    total = compute_total(sales_df, "revenue")

    assert total == pytest.approx(5774)


def test_compute_total_grouped(sales_df):
    totals = compute_total(sales_df, "revenue", group_by="product")

    assert totals["Widget"] == pytest.approx(1740)
    assert totals["Gadget"] == pytest.approx(2204)
    assert totals["Gizmo"] == pytest.approx(1830)
    # sorted descending
    assert list(totals.index) == ["Gadget", "Gizmo", "Widget"]


def test_compute_total_non_numeric_column_raises(sales_df):
    with pytest.raises(DataCliError, match="non-numeric"):
        compute_total(sales_df, "product")


def test_compute_total_missing_column_raises(sales_df):
    with pytest.raises(DataCliError, match="not found"):
        compute_total(sales_df, "profit")


# --- top_n ---------------------------------------------------------------


def test_top_n_returns_requested_count(sales_df):
    result = top_n(sales_df, group_by="product", value_column="revenue", n=2)

    assert len(result) == 2
    assert list(result.index) == ["Gadget", "Gizmo"]


def test_top_n_non_positive_n_raises(sales_df):
    with pytest.raises(DataCliError, match="positive integer"):
        top_n(sales_df, group_by="product", value_column="revenue", n=0)


# --- flag_outliers ---------------------------------------------------------


def test_flag_outliers_below(sales_df):
    flagged = flag_outliers(sales_df, "revenue", threshold=1000, mode="below")

    assert set(flagged["product"]) == {"Gadget", "Widget"}


def test_flag_outliers_above(sales_df):
    flagged = flag_outliers(sales_df, "revenue", threshold=1000, mode="above")

    assert set(flagged["product"]) == {"Widget", "Gizmo", "Gadget"}
    assert len(flagged) == 3


def test_flag_outliers_invalid_mode_raises(sales_df):
    with pytest.raises(DataCliError, match="mode must be"):
        flag_outliers(sales_df, "revenue", threshold=1000, mode="sideways")


# --- summary_stats -----------------------------------------------------


def test_summary_stats_values(sales_df):
    stats = summary_stats(sales_df, "revenue")

    assert stats["count"] == 5
    assert stats["min"] == 540
    assert stats["max"] == 1830
    assert stats["mean"] == pytest.approx(sales_df["revenue"].mean())


def test_summary_stats_single_row_std_is_zero():
    df = pd.DataFrame({"x": [5]})

    stats = summary_stats(df, "x")

    assert stats["std"] == 0.0


# --- format_report -----------------------------------------------------


def test_format_report_contains_all_sections(sales_df):
    report = format_report(sales_df, group_by="product", value_column="revenue", top=2)

    assert "=== Total revenue ===" in report
    assert "=== Top 2 product by revenue ===" in report
    assert "=== Summary Statistics for revenue ===" in report
    assert "=== Flagged Rows" in report


def test_format_report_no_flagged_rows_says_none():
    df = pd.DataFrame({"g": ["a", "b"], "v": [10, 10]})

    report = format_report(df, group_by="g", value_column="v", outlier_threshold=0)

    assert "(none)" in report
