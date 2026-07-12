"""
finance_tracker.db -- SQLite persistence layer.

Follows Chapter 21's core lesson exactly: every single SQL statement uses
`?` parameterized placeholders, values passed separately from the query
string, never an f-string or `.format()` building SQL text. That is the
one habit that closes off SQL injection, even in a personal, single-user
project with no untrusted input -- writing it any other way here would
recreate the exact risk Chapter 21's "Show why SQL injection matters" demo
warns about.

This module also never lets a raw SQLite row (a tuple or sqlite3.Row)
leak past its own boundary: fetch_all()/fetch_by_category() reconstruct
real Income/Expense objects via Transaction.from_row() before returning
anything, so reports.py -- and every other caller -- only ever sees real
Transaction objects, never database rows.

No argparse, no print() -- this module is reused unchanged by both cli.py
and the pytest suite.
"""

import logging
import sqlite3
from pathlib import Path

from finance_tracker.models import Expense, Income

logger = logging.getLogger(__name__)

DEFAULT_DB_PATH = Path.home() / ".finance_tracker" / "finance.db"

_CREATE_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT NOT NULL CHECK (type IN ('income', 'expense')),
    amount REAL NOT NULL,
    category TEXT NOT NULL,
    date TEXT NOT NULL,
    description TEXT NOT NULL DEFAULT '',
    extra TEXT NOT NULL DEFAULT ''
)
"""


def init_db(connection: sqlite3.Connection) -> None:
    """Create the transactions table if it doesn't exist yet. Safe to call
    every time the program starts -- CREATE TABLE IF NOT EXISTS is a
    no-op once the table is already there."""
    connection.execute(_CREATE_TABLE_SQL)
    connection.commit()
    logger.debug("Ensured transactions table exists")


def connect(db_path: Path = DEFAULT_DB_PATH) -> sqlite3.Connection:
    """Open a SQLite connection to `db_path`, creating the parent folder
    and the table if needed. Callers own the connection and should close
    it when done (a `with connect(...) as conn:` block works too, since
    sqlite3.Connection is a context manager for the transaction, not the
    connection close -- call .close() explicitly, or use contextlib)."""
    if db_path != ":memory:":
        db_path.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(db_path)
    init_db(connection)
    return connection


def _extra_field(transaction) -> str:
    """Pull the one field that differs between Income (source) and
    Expense (payment_method) into the single shared `extra` column."""
    if isinstance(transaction, Income):
        return transaction.source
    if isinstance(transaction, Expense):
        return transaction.payment_method
    return ""


def insert_transaction(connection: sqlite3.Connection, transaction) -> int:
    """Persist a Transaction (Income or Expense) object. Returns the new
    row's id. Pulls every value from the object's own properties -- it
    never touches a raw dict or tuple representation."""
    kind = "income" if isinstance(transaction, Income) else "expense"
    cursor = connection.execute(
        "INSERT INTO transactions (type, amount, category, date, description, extra) "
        "VALUES (?, ?, ?, ?, ?, ?)",
        (
            kind,
            transaction.amount,
            transaction.category,
            transaction.date,
            transaction.description,
            _extra_field(transaction),
        ),
    )
    connection.commit()
    logger.info("Inserted %s #%d (%s, $%.2f)", kind, cursor.lastrowid, transaction.category, transaction.amount)
    return cursor.lastrowid


def _row_to_transaction(row):
    """Reconstruct a real Income/Expense object from one raw SQLite row.
    This is the ONLY place in this module that touches a raw row's
    fields directly -- every other function in this module, and every
    function in reports.py, works with real Transaction objects instead."""
    row_id, kind, amount, category, date, description, extra = row
    # Route through Transaction.from_row() (Chapter 15's classmethod
    # alternate-constructor pattern), with cls bound to the correct
    # subclass so the 5th positional field lands as `source` for Income
    # and `payment_method` for Expense.
    if kind == "income":
        return Income.from_row(row)
    if kind == "expense":
        return Expense.from_row(row)
    raise ValueError(f"Unknown transaction type in database: {kind!r} (row id {row_id})")


def fetch_all(connection: sqlite3.Connection) -> list:
    """Return every transaction as a list of real Income/Expense objects,
    ordered by date. Never returns raw rows/tuples."""
    cursor = connection.execute(
        "SELECT id, type, amount, category, date, description, extra "
        "FROM transactions ORDER BY date, id"
    )
    rows = cursor.fetchall()
    logger.debug("Fetched %d transaction(s)", len(rows))
    return [_row_to_transaction(row) for row in rows]


def fetch_by_category(connection: sqlite3.Connection, category: str) -> list:
    """Return every transaction in a given category as real Transaction
    objects, using a parameterized WHERE clause."""
    cursor = connection.execute(
        "SELECT id, type, amount, category, date, description, extra "
        "FROM transactions WHERE category = ? ORDER BY date, id",
        (category,),
    )
    rows = cursor.fetchall()
    return [_row_to_transaction(row) for row in rows]


def delete_transaction(connection: sqlite3.Connection, transaction_id: int) -> bool:
    """Delete a transaction by id. Returns True if a row was actually
    removed, False if no row with that id existed."""
    cursor = connection.execute(
        "DELETE FROM transactions WHERE id = ?",
        (transaction_id,),
    )
    connection.commit()
    deleted = cursor.rowcount > 0
    if deleted:
        logger.info("Deleted transaction #%d", transaction_id)
    else:
        logger.warning("No transaction found with id #%d", transaction_id)
    return deleted
