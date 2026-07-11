"""Tests for expense_tracker.models.Expense."""

from datetime import date

import pytest

from expense_tracker.models import Expense


def test_expense_holds_fields_correctly():
    e = Expense(amount=12.50, category="food", note="lunch")
    assert e.amount == 12.50
    assert e.category == "food"
    assert e.note == "lunch"


def test_expense_defaults_to_today():
    e = Expense(amount=5, category="other")
    assert e.on == date.today()


def test_expense_rejects_zero_amount():
    with pytest.raises(ValueError):
        Expense(amount=0, category="food")


def test_expense_rejects_negative_amount():
    with pytest.raises(ValueError):
        Expense(amount=-10, category="food")


def test_expense_rejects_unknown_category():
    with pytest.raises(ValueError):
        Expense(amount=10, category="crypto")


def test_expense_to_dict_serializes_all_fields():
    e = Expense(amount=20, category="transport", note="bus fare", on=date(2026, 1, 5))
    d = e.to_dict()
    assert d == {
        "amount": 20,
        "category": "transport",
        "note": "bus fare",
        "on": "2026-01-05",
    }
