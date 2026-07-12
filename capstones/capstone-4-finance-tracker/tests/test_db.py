"""
Tests for finance_tracker.db -- SQLite CRUD, using the fresh_db fixture
(an isolated :memory: connection per test, per Chapter 27's isolation
principle -- no test shares a database or connection with any other).
"""

from finance_tracker.db import (
    delete_transaction,
    fetch_all,
    fetch_by_category,
    insert_transaction,
)
from finance_tracker.models import Expense, Income


def test_fresh_db_starts_empty(fresh_db):
    assert fetch_all(fresh_db) == []


def test_insert_income_then_fetch_all_returns_a_real_income_object(fresh_db):
    income = Income(2000, "salary", "2026-07-01", source="employer")

    insert_transaction(fresh_db, income)
    results = fetch_all(fresh_db)

    assert len(results) == 1
    fetched = results[0]
    # db.py must hand back a real Income object, not a raw row/tuple.
    assert isinstance(fetched, Income)
    assert fetched.amount == 2000
    assert fetched.category == "salary"
    assert fetched.source == "employer"


def test_insert_expense_then_fetch_all_returns_a_real_expense_object(fresh_db):
    expense = Expense(75.5, "food", "2026-07-06", payment_method="credit_card")

    insert_transaction(fresh_db, expense)
    results = fetch_all(fresh_db)

    assert len(results) == 1
    fetched = results[0]
    assert isinstance(fetched, Expense)
    assert fetched.amount == 75.5
    assert fetched.payment_method == "credit_card"


def test_insert_transaction_returns_new_row_id(fresh_db):
    first_id = insert_transaction(fresh_db, Income(100, "salary", "2026-07-01"))
    second_id = insert_transaction(fresh_db, Income(200, "salary", "2026-07-02"))

    assert second_id == first_id + 1


def test_two_transactions_same_date_both_counted(fresh_db):
    # Edge case explicitly called out in the roadmap.
    insert_transaction(fresh_db, Income(100, "salary", "2026-07-01"))
    insert_transaction(fresh_db, Expense(30, "food", "2026-07-01"))

    results = fetch_all(fresh_db)

    assert len(results) == 2
    assert all(t.date == "2026-07-01" for t in results)


def test_fetch_by_category_only_returns_matching_transactions(fresh_db):
    insert_transaction(fresh_db, Income(100, "salary", "2026-07-01"))
    insert_transaction(fresh_db, Expense(30, "food", "2026-07-02"))
    insert_transaction(fresh_db, Expense(15, "food", "2026-07-03"))

    food_only = fetch_by_category(fresh_db, "food")

    assert len(food_only) == 2
    assert all(t.category == "food" for t in food_only)


def test_delete_transaction_removes_it(fresh_db):
    new_id = insert_transaction(fresh_db, Income(100, "salary", "2026-07-01"))

    deleted = delete_transaction(fresh_db, new_id)

    assert deleted is True
    assert fetch_all(fresh_db) == []


def test_delete_transaction_returns_false_for_unknown_id(fresh_db):
    # Edge case: deleting an id that was never inserted.
    deleted = delete_transaction(fresh_db, 9999)
    assert deleted is False


def test_data_survives_across_two_connections_to_the_same_file(tmp_path):
    # Confirms persistence works with a real file (not just :memory:),
    # simulating a program restart: one connection writes, a brand-new
    # connection to the same path reads it back.
    from finance_tracker.db import connect

    db_path = tmp_path / "finance.db"

    conn1 = connect(db_path)
    insert_transaction(conn1, Income(500, "salary", "2026-07-01", source="employer"))
    conn1.close()

    conn2 = connect(db_path)
    results = fetch_all(conn2)
    conn2.close()

    assert len(results) == 1
    assert results[0].amount == 500
    assert isinstance(results[0], Income)


def test_fetch_all_never_returns_raw_tuples(fresh_db):
    insert_transaction(fresh_db, Income(100, "salary", "2026-07-01"))
    insert_transaction(fresh_db, Expense(20, "food", "2026-07-02"))

    results = fetch_all(fresh_db)

    for item in results:
        assert not isinstance(item, tuple)
        assert hasattr(item, "signed_amount")
