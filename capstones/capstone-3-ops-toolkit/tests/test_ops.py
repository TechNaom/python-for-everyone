"""
Basic tests for the ops engine modules (logs.py, scan.py, fetch.py).

Stdlib-only (unittest), matching this capstone's "no third-party
dependencies" stance. These exercise the engine modules directly --
no argparse, no subprocess -- exactly the "core.py is reusable/testable
without a terminal attached" point the roadmap makes about the
core.py/cli.py split.

Run with:  python3 -m unittest discover -s tests -v
"""

import csv
import json
import tempfile
import unittest
from pathlib import Path

from ops import OpsError
from ops.fetch import fetch_quote, fetch_weather, format_quote, format_weather, parse_quote, parse_weather
from ops.logs import count_by_level, export_summary, load_log_lines, most_common_error, search_lines
from ops.scan import ResumeScanner, load_resume

SAMPLE_LOG = """\
2026-07-10 08:01:12 INFO Server started
2026-07-10 08:07:19 ERROR Database connection timeout
2026-07-10 08:07:20 ERROR Database connection timeout
2026-07-10 08:12:33 WARNING High memory usage
"""


class LoadLogLinesTests(unittest.TestCase):
    def test_missing_file_raises_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            load_log_lines("/tmp/definitely_missing_ops_test.log")

    def test_loads_stripped_nonblank_lines(self):
        with tempfile.NamedTemporaryFile("w", suffix=".log", delete=False) as f:
            f.write(SAMPLE_LOG)
            path = f.name
        try:
            lines = load_log_lines(path)
            self.assertEqual(len(lines), 4)
        finally:
            Path(path).unlink()


class CountByLevelTests(unittest.TestCase):
    def test_counts_each_level(self):
        lines = SAMPLE_LOG.strip().splitlines()
        counts = count_by_level(lines)
        self.assertEqual(counts, {"INFO": 1, "WARNING": 1, "ERROR": 2})


class SearchLinesTests(unittest.TestCase):
    def test_case_insensitive_search(self):
        lines = SAMPLE_LOG.strip().splitlines()
        matches = search_lines(lines, "timeout")
        self.assertEqual(len(matches), 2)

    def test_empty_keyword_raises_opserror(self):
        lines = SAMPLE_LOG.strip().splitlines()
        with self.assertRaises(OpsError):
            search_lines(lines, "  ")


class MostCommonErrorTests(unittest.TestCase):
    def test_finds_most_frequent_error(self):
        lines = SAMPLE_LOG.strip().splitlines()
        message, count = most_common_error(lines)
        self.assertEqual(message, "Database connection timeout")
        self.assertEqual(count, 2)

    def test_no_errors_returns_none_zero(self):
        message, count = most_common_error(["2026-07-10 INFO all good"])
        self.assertIsNone(message)
        self.assertEqual(count, 0)


class ExportSummaryTests(unittest.TestCase):
    def test_writes_valid_csv(self):
        lines = SAMPLE_LOG.strip().splitlines()
        with tempfile.TemporaryDirectory() as tmpdir:
            report_path = Path(tmpdir) / "summary.csv"
            export_summary(lines, report_path)
            with open(report_path, newline="") as f:
                rows = list(csv.reader(f))
            self.assertEqual(rows[0], ["category", "label", "count"])
            self.assertTrue(any(row[:2] == ["level", "ERROR"] for row in rows))


class ResumeScannerTests(unittest.TestCase):
    def test_word_boundary_sql_does_not_match_mysql(self):
        scanner = ResumeScanner("Experience with MySQL and NoSQL databases.")
        found = scanner.find_keyword_matches(["SQL"])
        self.assertEqual(found, [])

    def test_word_boundary_sql_matches_standalone_sql(self):
        scanner = ResumeScanner("Comfortable with SQL and Git.")
        found = scanner.find_keyword_matches(["SQL"])
        self.assertEqual(found, ["SQL"])

    def test_match_report_percent(self):
        scanner = ResumeScanner("Python and SQL experience.")
        report = scanner.match_report(["Python", "SQL", "Docker"])
        self.assertEqual(report["found"], ["Python", "SQL"])
        self.assertEqual(report["missing"], ["Docker"])
        self.assertAlmostEqual(report["percent"], 66.66666666666667)

    def test_match_report_empty_keywords_raises(self):
        scanner = ResumeScanner("anything")
        with self.assertRaises(OpsError):
            scanner.match_report([])

    def test_find_emails_and_phones(self):
        text = "Reach me at jane.doe@example.com or (555) 123-4567."
        scanner = ResumeScanner(text)
        self.assertEqual(scanner.find_emails(), ["jane.doe@example.com"])
        self.assertEqual(scanner.find_phones(), ["(555) 123-4567"])

    def test_load_resume_missing_file_raises(self):
        with self.assertRaises(FileNotFoundError):
            load_resume("/tmp/definitely_missing_ops_resume.txt")


class FetchWeatherTests(unittest.TestCase):
    def test_ok_response_parses_and_formats(self):
        raw = fetch_weather("Austin")
        weather = parse_weather(raw)
        self.assertEqual(weather["city"], "Austin")
        text = format_weather(weather)
        self.assertIn("Austin", text)

    def test_simulated_error_raises_opserror(self):
        raw = fetch_weather("Nowhere", simulate_error=True)
        with self.assertRaises(OpsError):
            parse_weather(raw)


class FetchQuoteTests(unittest.TestCase):
    def test_valid_index_parses_and_formats(self):
        raw = fetch_quote(0)
        quote = parse_quote(raw)
        text = format_quote(quote)
        self.assertIn(quote["author"], text)

    def test_out_of_range_index_raises_opserror(self):
        raw = fetch_quote(99)
        with self.assertRaises(OpsError):
            parse_quote(raw)


if __name__ == "__main__":
    unittest.main()
