"""
db.py -- the persistence layer for the Task API.

This module is intentionally small and boring: it opens a real sqlite3
connection to a file (or ":memory:") and makes sure the `tasks` table
exists. Every other module (app.py, test_app.py) calls into this one
instead of touching sqlite3 directly, so there is exactly one place that
knows how the database is shaped.

Every query anywhere in this project uses `?` placeholders with values
passed as a separate tuple -- never an f-string or `.format()` call built
into the SQL text. That is the single most important rule in this file
and in app.py; see the README's "Architecture decisions" section for why.
"""

import sqlite3

DEFAULT_DB_PATH = "tasks.db"


def get_connection(db_path=DEFAULT_DB_PATH):
    """Open a sqlite3 connection to db_path.

    check_same_thread=False is set deliberately, not to silence an error
    we didn't understand: this app keeps ONE long-lived connection per
    Flask app instance (see app.py's create_app()), and Flask's
    development server can dispatch requests on more than one thread.
    sqlite3 connections aren't thread-safe to share by default, so without
    this flag a second thread touching the same connection would raise.
    We accept the tradeoff here (a portfolio-scale app with light traffic)
    rather than opening a brand-new connection per request, which would
    also break the ":memory:" test database (a fresh connection to
    ":memory:" is a brand-new, empty database every time -- it does NOT
    share state with any other connection to ":memory:").
    """
    conn = sqlite3.connect(db_path, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn


def init_db(conn):
    """Create the tasks table if it doesn't already exist.

    Must be called once before the first query against `conn` -- a fresh
    sqlite3 file (or a fresh ":memory:" connection) has no tables at all
    until this runs, which is why create_app() always calls init_db()
    right after get_connection().
    """
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            done INTEGER NOT NULL DEFAULT 0
        )
        """
    )
    conn.commit()
