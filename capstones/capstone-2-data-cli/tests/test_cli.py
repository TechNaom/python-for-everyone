"""
test_cli.py -- pytest suite for datacli.cli, the argparse entry point.

Drives main() with an argv list and captures stdout/exit codes, the
same way Chapter 27 tests a CLI without spawning a real subprocess.
"""

import json

import pytest

from datacli.cli import main


@pytest.fixture
def sales_csv(tmp_path):
    path = tmp_path / "sales.csv"
    path.write_text(
        "product,region,revenue\n"
        "Widget,East,1200\n"
        "Gadget,West,950\n"
        "Gizmo,East,1830\n"
    )
    return path


def test_analyze_happy_path(sales_csv, capsys):
    exit_code = main(["analyze", str(sales_csv), "--group-by", "product", "--value-column", "revenue"])

    out = capsys.readouterr().out
    assert exit_code == 0
    assert "Total revenue" in out
    assert "3,980.00" in out


def test_analyze_missing_column_returns_nonzero(sales_csv, capsys):
    exit_code = main(["analyze", str(sales_csv), "--group-by", "Regoin", "--value-column", "revenue"])

    assert exit_code == 1


def test_report_happy_path(sales_csv, capsys):
    exit_code = main(["report", str(sales_csv), "--group-by", "product", "--value-column", "revenue", "--top", "2"])

    out = capsys.readouterr().out
    assert exit_code == 0
    assert "Top 2 product by revenue" in out
    assert "Summary Statistics" in out


def test_export_json(sales_csv, tmp_path):
    out_path = tmp_path / "summary.json"

    exit_code = main(
        [
            "export", str(sales_csv),
            "--group-by", "product",
            "--value-column", "revenue",
            "--format", "json",
            "-o", str(out_path),
        ]
    )

    assert exit_code == 0
    payload = json.loads(out_path.read_text())
    assert payload["total"] == 3980.0
    assert payload["breakdown"]["Gizmo"] == 1830.0


def test_export_csv(sales_csv, tmp_path):
    out_path = tmp_path / "summary.csv"

    exit_code = main(
        [
            "export", str(sales_csv),
            "--group-by", "product",
            "--value-column", "revenue",
            "--format", "csv",
            "-o", str(out_path),
        ]
    )

    assert exit_code == 0
    content = out_path.read_text()
    assert "product,revenue" in content
    assert "TOTAL,3980.0" in content
