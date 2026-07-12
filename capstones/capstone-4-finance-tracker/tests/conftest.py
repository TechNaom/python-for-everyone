"""
Shared pytest fixtures for finance_tracker's test suite.

fresh_db gives every test its own isolated, in-memory SQLite connection
(:memory:), created fresh and torn down per test -- no shared state, no
shared file, no leftover rows from a previous test leaking into the next
one. This mirrors Chapter 27's `manager` fixture giving every test a
brand-new TaskManager.

sample_transactions gives every test that needs one a fresh, deterministic
mixed list of Income and Expense objects, so tests reading it never
accidentally share (and mutate) the same list instance.
"""

import pytest

from finance_tracker.db import init_db
from finance_tracker.models import Expense, Income
import sqlite3


@pytest.fixture
def fresh_db():
    """A brand-new, isolated in-memory SQLite connection for a single
    test. Nothing persists after the test ends -- the connection (and
    with it, the in-memory database) is closed in teardown."""
    connection = sqlite3.connect(":memory:")
    init_db(connection)
    yield connection
    connection.close()


@pytest.fixture
def sample_transactions():
    """A fresh mixed list of Income and Expense objects. Freshly built on
    every call, so no test can mutate a shared list and affect another
    test."""
    return [
        Income(2000.0, "salary", "2026-07-01", description="July paycheck", source="employer"),
        Expense(500.0, "housing", "2026-07-02", description="rent", payment_method="bank_transfer"),
        Income(150.0, "freelance", "2026-07-05", description="logo design", source="client X"),
        Expense(75.50, "food", "2026-07-06", description="groceries", payment_method="credit_card"),
        Expense(40.0, "food", "2026-08-01", description="restaurant", payment_method="cash"),
    ]
