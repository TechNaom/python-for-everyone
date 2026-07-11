"""Tests for expense_tracker.report."""

from expense_tracker.models import Expense
from expense_tracker.report import summary_lines
from expense_tracker.tracker import ExpenseTracker


def test_summary_lines_no_expenses():
    t = ExpenseTracker()
    lines = summary_lines(t)
    assert lines[0] == "Total spent: $0.00"
    assert "No expenses recorded yet." in lines


def test_summary_lines_includes_category_breakdown():
    t = ExpenseTracker()
    t.add(Expense(amount=15, category="entertainment"))
    lines = summary_lines(t)
    assert "By category:" in lines
    assert any("entertainment" in line for line in lines)


def test_summary_lines_reports_over_budget():
    t = ExpenseTracker(monthly_budget=10)
    t.add(Expense(amount=25, category="food"))
    lines = summary_lines(t)
    assert any("Over budget" in line for line in lines)


def test_summary_lines_reports_remaining_budget():
    t = ExpenseTracker(monthly_budget=100)
    t.add(Expense(amount=25, category="food"))
    lines = summary_lines(t)
    assert any("Remaining budget: $75.00" in line for line in lines)
