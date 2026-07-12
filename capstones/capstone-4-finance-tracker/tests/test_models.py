"""
Tests for finance_tracker.models -- the Transaction/Income/Expense
hierarchy. AAA (Arrange, Act, Assert) pattern throughout, per Chapter 27.
"""

import pytest

from finance_tracker.models import Expense, Income, Transaction


# --- inheritance shape ---------------------------------------------------

def test_income_and_expense_both_inherit_from_transaction():
    income = Income(100, "salary", "2026-07-01")
    expense = Expense(50, "food", "2026-07-01")

    assert isinstance(income, Transaction)
    assert isinstance(expense, Transaction)


def test_income_and_expense_call_super_init_and_get_shared_attributes():
    # If Income/Expense didn't call super().__init__(), category/date/
    # description wouldn't exist on them at all.
    income = Income(100, "salary", "2026-07-01", description="paycheck")

    assert income.amount == 100
    assert income.category == "salary"
    assert income.date == "2026-07-01"
    assert income.description == "paycheck"


# --- @property / @amount.setter validation -------------------------------

def test_amount_setter_rejects_zero_at_construction():
    with pytest.raises(ValueError):
        Income(0, "salary", "2026-07-01")


def test_amount_setter_rejects_negative_at_construction():
    with pytest.raises(ValueError):
        Expense(-10, "food", "2026-07-01")


def test_amount_setter_rejects_zero_after_construction():
    # Edge case called out explicitly in the roadmap: validation must live
    # in the setter, not just __init__, so mutating an existing object is
    # still caught.
    transaction = Income(100, "salary", "2026-07-01")

    with pytest.raises(ValueError):
        transaction.amount = 0


def test_amount_setter_rejects_negative_after_construction():
    transaction = Expense(50, "food", "2026-07-01")

    with pytest.raises(ValueError):
        transaction.amount = -50


def test_amount_setter_accepts_a_valid_reassignment():
    transaction = Income(100, "salary", "2026-07-01")

    transaction.amount = 250
    assert transaction.amount == 250


# --- @staticmethod --------------------------------------------------------

def test_is_valid_category_accepts_known_category():
    assert Transaction.is_valid_category("salary") is True


def test_is_valid_category_rejects_unknown_category():
    assert Transaction.is_valid_category("not_a_real_category") is False


def test_constructing_with_invalid_category_raises():
    with pytest.raises(ValueError):
        Income(100, "not_a_real_category", "2026-07-01")


# --- @classmethod from_row -------------------------------------------------

def test_income_from_row_rebuilds_a_real_income_object():
    row = (1, "income", 300.0, "salary", "2026-07-10", "bonus", "employer")

    rebuilt = Income.from_row(row)

    assert isinstance(rebuilt, Income)
    assert rebuilt.amount == 300.0
    assert rebuilt.category == "salary"
    assert rebuilt.source == "employer"


def test_expense_from_row_rebuilds_a_real_expense_object():
    row = (2, "expense", 45.0, "food", "2026-07-11", "lunch", "cash")

    rebuilt = Expense.from_row(row)

    assert isinstance(rebuilt, Expense)
    assert rebuilt.amount == 45.0
    assert rebuilt.payment_method == "cash"


def test_from_row_still_enforces_amount_validation():
    # A corrupted row with a non-positive amount should still raise --
    # from_row() gives no special bypass around the amount setter.
    bad_row = (3, "income", 0, "salary", "2026-07-10", "", "employer")

    with pytest.raises(ValueError):
        Income.from_row(bad_row)


# --- Chapter 16 polymorphism: signed_amount() / describe() ---------------

def test_income_signed_amount_is_positive():
    income = Income(100, "salary", "2026-07-01")
    assert income.signed_amount() == 100


def test_expense_signed_amount_is_negative():
    expense = Expense(100, "food", "2026-07-01")
    assert expense.signed_amount() == -100


def test_income_and_expense_describe_differ_genuinely():
    # Not just cosmetic -- Income's describe() and Expense's describe()
    # must actually differ, and both must differ from a would-be identical
    # base-only string, proving each override does real work.
    income = Income(100, "salary", "2026-07-01", source="employer")
    expense = Expense(100, "food", "2026-07-01", payment_method="cash")

    assert income.describe() != expense.describe()
    assert "INCOME" in income.describe()
    assert "EXPENSE" in expense.describe()
    assert "employer" in income.describe()
    assert "cash" in expense.describe()


def test_describe_extends_base_via_super_not_replaces_it():
    # Both subclasses' describe() must still contain the base class's
    # summary content (category/date/amount), proving they call
    # super().describe() rather than writing a fully separate string.
    income = Income(100, "salary", "2026-07-01")
    base = Transaction.describe(income)

    assert base in income.describe()


def test_str_delegates_to_describe():
    income = Income(100, "salary", "2026-07-01", source="employer")
    assert str(income) == income.describe()
