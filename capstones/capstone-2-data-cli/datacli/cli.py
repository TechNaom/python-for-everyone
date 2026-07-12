"""
datacli.cli -- the argparse entry point.

This module's only job is: parse sys.argv, configure logging, call into
core.py, and turn the result (or a DataCliError) into clear terminal
output or an output file. No analysis logic lives here, and this is
the only file in the package that touches pandas' results for display
or writes to the terminal/filesystem -- that split is what keeps
core.py testable and reusable without a terminal attached.
"""

import argparse
import json
import logging
import sys
from pathlib import Path

from datacli.core import (
    DataCliError,
    compute_total,
    format_report,
    load_csv,
    summary_stats,
)

logger = logging.getLogger("datacli")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="datacli",
        description="Turn any CSV file into totals, top-N breakdowns, and flagged outliers.",
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="show debug-level logging (file paths, row counts, column checks, etc.)",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    # analyze
    analyze_parser = subparsers.add_parser(
        "analyze", help="print the total and per-group breakdown for a value column"
    )
    analyze_parser.add_argument("csv_path", type=Path, help="path to the CSV file to analyze")
    analyze_parser.add_argument(
        "--group-by", required=True, help="column to group by (e.g. product, category, city)"
    )
    analyze_parser.add_argument(
        "--value-column", required=True, help="numeric column to total/aggregate (e.g. revenue, amount)"
    )

    # report
    report_parser = subparsers.add_parser(
        "report", help="print the full report: total, top-N groups, summary stats, and flagged rows"
    )
    report_parser.add_argument("csv_path", type=Path, help="path to the CSV file to analyze")
    report_parser.add_argument(
        "--group-by", required=True, help="column to group by (e.g. product, category, city)"
    )
    report_parser.add_argument(
        "--value-column", required=True, help="numeric column to total/aggregate (e.g. revenue, amount)"
    )
    report_parser.add_argument(
        "--top", type=int, default=5, help="how many top groups to show (default: 5)"
    )
    report_parser.add_argument(
        "--threshold", type=float, default=None,
        help="flag rows with value-column below this number (default: the column's mean)",
    )

    # export
    export_parser = subparsers.add_parser(
        "export", help="write the computed summary (total + per-group breakdown) to a file"
    )
    export_parser.add_argument("csv_path", type=Path, help="path to the CSV file to analyze")
    export_parser.add_argument(
        "--group-by", required=True, help="column to group by (e.g. product, category, city)"
    )
    export_parser.add_argument(
        "--value-column", required=True, help="numeric column to total/aggregate (e.g. revenue, amount)"
    )
    export_parser.add_argument(
        "--format", choices=["json", "csv"], required=True, help="output file format"
    )
    export_parser.add_argument(
        "-o", "--output", required=True, type=Path, help="path to write the output file to"
    )

    return parser


def configure_logging(verbose: bool) -> None:
    """
    Configure the datacli logger only -- deliberately NOT the root
    logger, so --verbose doesn't flood the terminal with debug output
    from pandas/numpy's own loggers, only datacli's own log calls.
    """
    level = logging.DEBUG if verbose else logging.INFO
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))
    logger.addHandler(handler)
    logger.setLevel(level)
    logger.propagate = False


def _cmd_analyze(args: argparse.Namespace) -> None:
    df = load_csv(args.csv_path, required_columns=[args.group_by, args.value_column])
    grand_total = compute_total(df, args.value_column)
    print(f"=== Total {args.value_column} ===")
    print(f"{grand_total:,.2f}")
    print()
    print(f"=== {args.group_by} breakdown by {args.value_column} ===")
    breakdown = compute_total(df, args.value_column, group_by=args.group_by)
    for key, total in breakdown.items():
        print(f"{key}: {total:,.2f}")


def _cmd_report(args: argparse.Namespace) -> None:
    df = load_csv(args.csv_path, required_columns=[args.group_by, args.value_column])
    report = format_report(
        df,
        group_by=args.group_by,
        value_column=args.value_column,
        top=args.top,
        outlier_threshold=args.threshold,
    )
    print(report)


def _cmd_export(args: argparse.Namespace) -> None:
    df = load_csv(args.csv_path, required_columns=[args.group_by, args.value_column])
    grand_total = compute_total(df, args.value_column)
    breakdown = compute_total(df, args.value_column, group_by=args.group_by)
    stats = summary_stats(df, args.value_column)

    args.output.parent.mkdir(parents=True, exist_ok=True)

    if args.format == "json":
        payload = {
            "source_csv": str(args.csv_path),
            "group_by": args.group_by,
            "value_column": args.value_column,
            "total": round(grand_total, 2),
            "breakdown": {str(k): round(v, 2) for k, v in breakdown.items()},
            "summary_stats": {k: round(v, 2) for k, v in stats.items()},
        }
        args.output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    else:  # csv
        lines = [f"{args.group_by},{args.value_column}"]
        for key, total in breakdown.items():
            lines.append(f"{key},{round(total, 2)}")
        lines.append(f"TOTAL,{round(grand_total, 2)}")
        args.output.write_text("\n".join(lines) + "\n", encoding="utf-8")

    logger.info("Wrote %s summary to %s", args.format, args.output)
    print(f"Exported {args.format} summary to {args.output}")


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    configure_logging(args.verbose)

    try:
        if args.command == "analyze":
            _cmd_analyze(args)
        elif args.command == "report":
            _cmd_report(args)
        elif args.command == "export":
            _cmd_export(args)
    except DataCliError as exc:
        logger.error(str(exc))
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
