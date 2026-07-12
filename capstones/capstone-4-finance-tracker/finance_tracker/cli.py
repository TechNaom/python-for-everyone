"""
finance_tracker.cli -- the argparse entry point.

This is the ONLY file in finance_tracker that touches argparse, sys.argv,
or print(). It parses arguments, configures logging, calls into db.py and
reports.py, and turns the result (or a ValueError from the model layer)
into clear terminal output. No model or persistence logic lives here --
that split (mirroring taskbox's core.py/cli.py separation) is what keeps
models.py/db.py/reports.py reusable and testable without a terminal
attached.
"""

from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path

from finance_tracker.db import DEFAULT_DB_PATH, connect, fetch_all, insert_transaction
from finance_tracker.models import Expense, Income
from finance_tracker.reports import balance, monthly_summary, totals_by_category

logger = logging.getLogger("finance_tracker")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="finance",
        description="A small command-line personal finance tracker backed by SQLite.",
    )
    parser.add_argument(
        "--db",
        type=Path,
        default=DEFAULT_DB_PATH,
        help=f"path to the SQLite database file (default: {DEFAULT_DB_PATH})",
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="show debug-level logging",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    add_income = subparsers.add_parser("add-income", help="record a new income transaction")
    add_income.add_argument("amount", type=float, help="amount received (must be positive)")
    add_income.add_argument("category", help="category, e.g. salary, freelance, investment")
    add_income.add_argument("date", help="date as YYYY-MM-DD")
    add_income.add_argument("--description", default="", help="optional free-text note")
    add_income.add_argument("--source", default="", help="where the income came from")

    add_expense = subparsers.add_parser("add-expense", help="record a new expense transaction")
    add_expense.add_argument("amount", type=float, help="amount spent (must be positive)")
    add_expense.add_argument("category", help="category, e.g. food, housing, transportation")
    add_expense.add_argument("date", help="date as YYYY-MM-DD")
    add_expense.add_argument("--description", default="", help="optional free-text note")
    add_expense.add_argument("--payment-method", default="", help="e.g. credit_card, cash")

    subparsers.add_parser("list", help="list every transaction")
    subparsers.add_parser("balance", help="show the current overall balance")

    report_parser = subparsers.add_parser("report", help="show a category breakdown, or a monthly summary")
    report_parser.add_argument(
        "--month",
        metavar="YYYY-MM",
        default=None,
        help="restrict the report to one calendar month (default: all-time category totals)",
    )

    return parser


def configure_logging(verbose: bool) -> None:
    """Configure the finance_tracker logger only (not the root logger), so
    --verbose stays scoped to this tool's own messages, exactly like
    taskbox.cli.configure_logging."""
    level = logging.DEBUG if verbose else logging.INFO
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))
    logger.addHandler(handler)
    logger.setLevel(level)
    logger.propagate = False


def _parse_month(month_str: str):
    year_str, month_num_str = month_str.split("-")
    return int(year_str), int(month_num_str)


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    configure_logging(args.verbose)

    connection = connect(args.db)
    try:
        if args.command == "add-income":
            transaction = Income(
                args.amount, args.category, args.date,
                description=args.description, source=args.source,
            )
            new_id = insert_transaction(connection, transaction)
            print(f"Added income #{new_id}: {transaction.describe()}")

        elif args.command == "add-expense":
            transaction = Expense(
                args.amount, args.category, args.date,
                description=args.description, payment_method=args.payment_method,
            )
            new_id = insert_transaction(connection, transaction)
            print(f"Added expense #{new_id}: {transaction.describe()}")

        elif args.command == "list":
            transactions = fetch_all(connection)
            if not transactions:
                print("No transactions found.")
            else:
                for transaction in transactions:
                    # Polymorphic call: every transaction answers describe()
                    # its own way, no matter whether it's Income or Expense.
                    print(f"  {transaction.describe()}")

        elif args.command == "balance":
            transactions = fetch_all(connection)
            total = balance(transactions)
            print(f"Current balance: ${total:,.2f}")

        elif args.command == "report":
            transactions = fetch_all(connection)
            if args.month:
                year, month = _parse_month(args.month)
                summary = monthly_summary(transactions, year, month)
                print(f"Report for {year:04d}-{month:02d}:")
                print(f"  Transactions: {summary['count']}")
                print(f"  Income:  ${summary['total_income']:,.2f}")
                print(f"  Expense: ${summary['total_expense']:,.2f}")
                print(f"  Net:     ${summary['net']:,.2f}")
            else:
                totals = totals_by_category(transactions)
                if not totals:
                    print("No transactions found.")
                else:
                    print("Totals by category (all time):")
                    for category, total in sorted(totals.items()):
                        print(f"  {category:15s} ${total:,.2f}")

    except ValueError as exc:
        logger.error(str(exc))
        return 1
    finally:
        connection.close()

    return 0


if __name__ == "__main__":
    sys.exit(main())
