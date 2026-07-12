"""
Tests for finance_tracker.reports -- balance()/totals_by_category()/
monthly_summary(), all computed via polymorphic signed_amount() calls
over plain lists of Transaction objects (no database involved).
"""

from finance_tracker.models import Expense, Income
from finance_tracker.reports import balance, monthly_summary, totals_by_category


# --- balance(): happy path + edge cases -----------------------------------

def test_balance_with_mixed_income_and_expense(sample_transactions):
    # The key polymorphism test: this test never inspects which items in
    # the list are Income vs. Expense -- it just trusts balance() to call
    # signed_amount() polymorphically and get the right answer.
    result = balance(sample_transactions)

    expected = 2000.0 - 500.0 + 150.0 - 75.50 - 40.0
    assert result == expected


def test_balance_of_empty_list_is_zero():
    # Edge case explicitly required by the roadmap.
    assert balance([]) == 0


def test_balance_of_all_income_is_positive_sum():
    transactions = [
        Income(100, "salary", "2026-07-01"),
        Income(50, "freelance", "2026-07-02"),
    ]
    assert balance(transactions) == 150


def test_balance_of_all_expense_is_negative_sum():
    transactions = [
        Expense(30, "food", "2026-07-01"),
        Expense(20, "food", "2026-07-02"),
    ]
    assert balance(transactions) == -50


def test_balance_does_not_care_about_list_order():
    # Another angle on the same polymorphism guarantee: shuffling a mixed
    # list must not change the total, since each object contributes its
    # own signed_amount() independent of position.
    a = [Income(100, "salary", "2026-07-01"), Expense(40, "food", "2026-07-02")]
    b = [Expense(40, "food", "2026-07-02"), Income(100, "salary", "2026-07-01")]

    assert balance(a) == balance(b)


# --- totals_by_category() -------------------------------------------------

def test_totals_by_category_groups_and_sums_correctly(sample_transactions):
    totals = totals_by_category(sample_transactions)

    assert totals["salary"] == 2000.0
    assert totals["housing"] == -500.0
    assert totals["freelance"] == 150.0
    # Two food entries: -75.50 and -40.0, netted together.
    assert totals["food"] == -115.50


def test_totals_by_category_empty_list_returns_empty_dict():
    assert totals_by_category([]) == {}


# --- monthly_summary() -----------------------------------------------------

def test_monthly_summary_filters_to_requested_month(sample_transactions):
    # sample_transactions has 4 July entries and 1 August entry.
    summary = monthly_summary(sample_transactions, 2026, 7)

    assert summary["count"] == 4
    assert summary["total_income"] == 2000.0 + 150.0
    assert summary["total_expense"] == -500.0 - 75.50
    assert summary["net"] == (2000.0 + 150.0) + (-500.0 - 75.50)


def test_monthly_summary_for_month_with_no_transactions_is_all_zero(sample_transactions):
    summary = monthly_summary(sample_transactions, 2026, 12)

    assert summary["count"] == 0
    assert summary["total_income"] == 0
    assert summary["total_expense"] == 0
    assert summary["net"] == 0
