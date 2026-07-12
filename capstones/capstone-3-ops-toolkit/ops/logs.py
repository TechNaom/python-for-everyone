"""
ops.logs -- the log-analysis engine, ported from Chapter 13's Log-File
Analyzer (load_log_lines, count_by_level, search_lines,
most_common_error, export_summary).

Deliberately kept separate from cli.py: this module knows nothing about
argparse or print(). It reads a log file and a CSV export target,
returns plain Python data structures, and raises exceptions on bad
input -- exactly the "engine vs. dashboard" split taskbox's core.py
established. FileNotFoundError propagates unchanged (open() already
raises it); anything else that's a legitimate "bad input" case (an
empty log file) raises OpsError instead of a silent empty result.
"""

from __future__ import annotations

import csv
import logging
from pathlib import Path

from ops import OpsError

logger = logging.getLogger(__name__)

LOG_LEVELS = ("INFO", "WARNING", "ERROR")


def load_log_lines(log_filename: str | Path) -> list[str]:
    """Return a list of stripped, non-blank lines from log_filename.

    Raises FileNotFoundError if the file doesn't exist -- callers
    (cli.py) are expected to catch it themselves.
    """
    logger.debug("Loading log lines from %s", log_filename)
    with open(log_filename) as file:
        lines = [line.strip() for line in file if line.strip()]
    logger.debug("Loaded %d line(s)", len(lines))
    return lines


def count_by_level(lines: list[str]) -> dict[str, int]:
    """Return a dict of {level: count} for INFO/WARNING/ERROR lines."""
    counts = {level: 0 for level in LOG_LEVELS}
    for line in lines:
        for level in counts:
            if f" {level} " in line:
                counts[level] += 1
                break
    return counts


def search_lines(lines: list[str], keyword: str) -> list[str]:
    """Return every line containing keyword (case-insensitive).

    Raises OpsError if keyword is blank -- an empty keyword would
    "match" every line, which is almost never what the caller wants.
    """
    if not keyword or not keyword.strip():
        raise OpsError("Search keyword cannot be empty.")
    matches = [line for line in lines if keyword.lower() in line.lower()]
    logger.debug("search_lines(%r) matched %d line(s)", keyword, len(matches))
    return matches


def most_common_error(lines: list[str]) -> tuple[str | None, int]:
    """Return (message, count) for the most frequent ERROR message.

    Returns (None, 0) if there are no ERROR lines at all -- this is a
    legitimate, expected result (not an error condition), so it is
    returned rather than raised.
    """
    error_counts: dict[str, int] = {}
    for line in lines:
        if " ERROR " in line:
            message = line.split("ERROR", 1)[1].strip()
            error_counts[message] = error_counts.get(message, 0) + 1

    if not error_counts:
        return None, 0

    best_message = None
    best_count = 0
    for message, count in error_counts.items():
        if count > best_count:
            best_message = message
            best_count = count
    return best_message, best_count


def export_summary(lines: list[str], report_filename: str | Path) -> Path:
    """Write a CSV summary of level counts and error-message counts.

    Returns the Path the report was written to. Raises OpsError if the
    destination can't be written (e.g. an invalid directory).
    """
    level_counts = count_by_level(lines)

    error_counts: dict[str, int] = {}
    for line in lines:
        if " ERROR " in line:
            message = line.split("ERROR", 1)[1].strip()
            error_counts[message] = error_counts.get(message, 0) + 1

    report_path = Path(report_filename)
    try:
        with open(report_path, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["category", "label", "count"])
            for level, count in level_counts.items():
                writer.writerow(["level", level, count])
            for message, count in error_counts.items():
                writer.writerow(["error_message", message, count])
    except OSError as exc:
        raise OpsError(f"Could not write report file {report_path}: {exc}") from exc

    logger.info("Exported summary to %s", report_path)
    return report_path
