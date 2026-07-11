"""Tests for expense_tracker.tracker.ExpenseTracker."""

import pytest

from expense_tracker.models import Expense
from expense_tracker.tracker import ExpenseTracker


def make_tracker_with_expenses():
    t = ExpenseTracker(monthly_budget=100)
    t.add(Expense(amount=30, category="food"))
    t.add(Expense(amount=20, category="transport"))
    t.add(Expense(amount=10, category="food"))
    return t


def test_add_rejects_non_expense():
    t = ExpenseTracker()
    with pytest.raises(TypeError):
        t.add("not an expense")


def test_total_with_no_expenses_is_zero():
    t = ExpenseTracker()
    assert t.total() == 0


def test_total_sums_all_expenses():
    t = make_tracker_with_expenses()
    assert t.total() == 60


def test_total_by_category():
    t = make_tracker_with_expenses()
    assert t.total_by_category("food") == 40
    assert t.total_by_category("transport") == 20
    assert t.total_by_category("housing") == 0


def test_by_category_groups_correctly():
    t = make_tracker_with_expenses()
    assert t.by_category() == {"food": 40, "transport": 20}


def test_count():
    t = make_tracker_with_expenses()
    assert t.count() == 3


def test_is_over_budget_false_when_no_budget_set():
    t = ExpenseTracker()
    t.add(Expense(amount=99999, category="other"))
    assert t.is_over_budget() is False


def test_is_over_budget_true_when_exceeded():
    t = ExpenseTracker(monthly_budget=50)
    t.add(Expense(amount=60, category="food"))
    assert t.is_over_budget() is True


def test_remaining_budget_none_when_no_budget_set():
    t = ExpenseTracker()
    assert t.remaining_budget() is None


def test_remaining_budget_computed_correctly():
    t = make_tracker_with_expenses()
    assert t.remaining_budget() == 40


def test_largest_expense_returns_none_when_empty():
    t = ExpenseTracker()
    assert t.largest_expense() is None


def test_largest_expense_returns_correct_expense():
    t = make_tracker_with_expenses()
    largest = t.largest_expense()
    assert largest.amount == 30
    assert largest.category == "food"
