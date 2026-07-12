"""
ops.cli -- the argparse entry point.

This module's only job is: parse sys.argv, configure logging, call into
logs.py / scan.py / fetch.py, and turn the result (or an OpsError /
FileNotFoundError) into clear terminal output. No log-analysis,
resume-scanning, or fetch logic lives here -- that split is what keeps
the engine modules testable and reusable without a terminal attached,
exactly like taskbox's core.py/cli.py split.

Subcommand tree (two levels of subparsers -- a domain subparser, and
each domain's own action subparser):

    ops logs analyze <file> [--level] [--keyword] [--export FILE]
    ops scan resume <file> --keywords a,b,c
    ops scan contacts <file>
    ops fetch weather <city> [--simulate-error]
    ops fetch quote [--index N]

Error-handling convention (shared across all three domains): every
handler below has exactly one try/except wrapper that catches
(OpsError, FileNotFoundError), logs an "ERROR:"-prefixed message via
logging, and returns exit code 1. No handler invents its own error
style.
"""

from __future__ import annotations

import argparse
import logging
import sys

from ops import OpsError
from ops.fetch import fetch_quote, fetch_weather, format_quote, format_weather, parse_quote, parse_weather
from ops.formatting import format_kv, format_list, format_table
from ops.logs import count_by_level, export_summary, load_log_lines, most_common_error, search_lines
from ops.scan import ResumeScanner, load_resume

logger = logging.getLogger("ops")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="ops",
        description=(
            "A unified ops toolkit: log analysis, resume scanning, and a "
            "mocked weather/quote fetch pipeline behind one command."
        ),
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="show debug-level logging across every subcommand",
    )

    domain_subparsers = parser.add_subparsers(dest="domain", required=True)

    # --- ops logs ... ---
    logs_parser = domain_subparsers.add_parser("logs", help="log-file analysis")
    logs_action_subparsers = logs_parser.add_subparsers(dest="action", required=True)

    analyze_parser = logs_action_subparsers.add_parser(
        "analyze", help="show level counts, search, and (optionally) export a CSV summary"
    )
    analyze_parser.add_argument("file", help="path to the log file to analyze")
    analyze_parser.add_argument(
        "--level", action="store_true",
        help="show counts by log level (INFO/WARNING/ERROR)",
    )
    analyze_parser.add_argument(
        "--keyword", default=None,
        help="search for lines containing this keyword (case-insensitive)",
    )
    analyze_parser.add_argument(
        "--export", metavar="FILE", default=None,
        help="write a CSV summary (level counts + error-message counts) to this file",
    )

    # --- ops scan ... ---
    scan_parser = domain_subparsers.add_parser("scan", help="resume scanning")
    scan_action_subparsers = scan_parser.add_subparsers(dest="action", required=True)

    resume_parser = scan_action_subparsers.add_parser(
        "resume", help="scan a resume for required keywords"
    )
    resume_parser.add_argument("file", help="path to the resume .txt file")
    resume_parser.add_argument(
        "--keywords", required=True,
        help="comma-separated list of required skills, e.g. Python,SQL,Docker",
    )

    contacts_parser = scan_action_subparsers.add_parser(
        "contacts", help="extract email addresses and phone numbers from a resume"
    )
    contacts_parser.add_argument("file", help="path to the resume .txt file")

    # --- ops fetch ... ---
    fetch_parser = domain_subparsers.add_parser("fetch", help="mocked weather / quote fetch pipeline")
    fetch_action_subparsers = fetch_parser.add_subparsers(dest="action", required=True)

    weather_parser = fetch_action_subparsers.add_parser(
        "weather", help="fetch (mocked) current weather and forecast for a city"
    )
    weather_parser.add_argument("city", help="city name")
    weather_parser.add_argument(
        "--simulate-error", action="store_true",
        help="simulate a bad API response, to exercise the error-handling path",
    )

    quote_parser = fetch_action_subparsers.add_parser(
        "quote", help="fetch (mocked) a quote of the day"
    )
    quote_parser.add_argument(
        "--index", type=int, default=0,
        help="which mocked quote to fetch (0, 1, or 2; default: 0)",
    )

    return parser


def configure_logging(verbose: bool) -> None:
    """
    Configure the "ops" logger only -- deliberately NOT the root logger,
    same reasoning as taskbox's configure_logging(): --verbose should
    only affect ops's own log calls, not every imported library's.
    """
    level = logging.DEBUG if verbose else logging.INFO
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))
    logger.addHandler(handler)
    logger.setLevel(level)
    logger.propagate = False


# --- Handlers: one per leaf subcommand. Each does exactly three things:
# call into the engine module(s), format the result via formatting.py,
# and print(). No engine logic lives here. ---

def handle_logs_analyze(args: argparse.Namespace) -> None:
    lines = load_log_lines(args.file)
    print(f"Loaded {len(lines)} line(s) from '{args.file}'.")

    # Default to showing level counts if the user didn't ask for
    # anything more specific -- matches the original project's "show
    # counts by level" as the first, most common menu option.
    show_level = args.level or (not args.keyword and not args.export)

    if show_level:
        counts = count_by_level(lines)
        print()
        print("Counts by level:")
        print(format_table([[level, count] for level, count in counts.items()], ["level", "count"]))

        message, count = most_common_error(lines)
        print()
        if message is None:
            print("No ERROR lines found in this log.")
        else:
            print(f"Most common error: '{message}' ({count} occurrence(s))")

    if args.keyword:
        matches = search_lines(lines, args.keyword)
        print()
        if not matches:
            print(f"No lines matched '{args.keyword}'.")
        else:
            print(f"{len(matches)} matching line(s):")
            print(format_list(matches))

    if args.export:
        report_path = export_summary(lines, args.export)
        print()
        print(f"Summary written to '{report_path}'.")


def handle_scan_resume(args: argparse.Namespace) -> None:
    text = load_resume(args.file)
    keywords = [kw.strip() for kw in args.keywords.split(",") if kw.strip()]
    scanner = ResumeScanner(text)
    report = scanner.match_report(keywords)

    print(
        f"Matched {len(report['found'])}/{len(keywords)} required skill(s) "
        f"({report['percent']:.0f}%)."
    )
    print()
    print(format_kv([
        ("Found", ", ".join(report["found"]) if report["found"] else "none"),
        ("Missing", ", ".join(report["missing"]) if report["missing"] else "none"),
    ]))


def handle_scan_contacts(args: argparse.Namespace) -> None:
    text = load_resume(args.file)
    scanner = ResumeScanner(text)
    emails = scanner.find_emails()
    phones = scanner.find_phones()

    print("Emails found:")
    print(format_list(emails))
    print()
    print("Phone numbers found:")
    print(format_list(phones))


def handle_fetch_weather(args: argparse.Namespace) -> None:
    raw_text = fetch_weather(args.city, simulate_error=args.simulate_error)
    weather = parse_weather(raw_text)
    print(format_weather(weather))


def handle_fetch_quote(args: argparse.Namespace) -> None:
    raw_text = fetch_quote(args.index)
    quote = parse_quote(raw_text)
    print(format_quote(quote))


HANDLERS = {
    ("logs", "analyze"): handle_logs_analyze,
    ("scan", "resume"): handle_scan_resume,
    ("scan", "contacts"): handle_scan_contacts,
    ("fetch", "weather"): handle_fetch_weather,
    ("fetch", "quote"): handle_fetch_quote,
}


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    configure_logging(args.verbose)

    handler = HANDLERS[(args.domain, args.action)]

    try:
        handler(args)
    except (OpsError, FileNotFoundError) as exc:
        logger.error(str(exc))
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
