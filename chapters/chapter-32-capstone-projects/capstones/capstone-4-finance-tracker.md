# Capstone 4: Personal Finance Tracker

## Overview

A genuinely new project — not a repackaging of an earlier one — that
proves you can design real object-oriented code, not just fill in a
template. A base `Transaction` class with `Income` and `Expense`
subclasses (polymorphic, per Chapter 16's exact pattern) gets persisted to
a real SQLite database (per Chapter 21), backed by a full pytest suite
(per Chapter 27), and shipped as an installable CLI package (per Chapter
31). This is the capstone that answers: "can you design a class
hierarchy where inheritance and polymorphism are doing real work, not
just present for their own sake?"

## Skills this combines

- **Chapter 14 (OOP Basics)** — general class definitions: `Transaction`'s
  `__init__` setting instance attributes (amount, category, date,
  description), instance methods, and `__str__`/`__repr__` for readable
  printing — the same shape as `Book`'s `__init__`/`check_out`/`__str__`.
- **Chapter 15 (OOP Deeper)** — `@property`/`@x.setter` validation
  (an `amount` that can never be set to a non-positive number, exactly
  like `BankAccount.balance` rejecting negative values), a `@staticmethod`
  for format-only validation (e.g. `is_valid_category(name)`, no instance
  needed, mirroring `is_valid_account_number`), and a `@classmethod`
  alternative constructor (`Transaction.from_csv_row(cls, row)` or
  `from_row(cls, db_row)`, mirroring `BankAccount.open_new_account`).
  Encapsulation follows the same single-leading-underscore convention
  (`_amount`, `_category`) as `BankAccount`.
- **Chapter 16 (Inheritance & Polymorphism)** — `Income(Transaction)` and
  `Expense(Transaction)` both call `super().__init__()` for shared setup
  (mirroring `Car`/`Motorcycle`/`Truck` all calling
  `super().__init__(make, model, daily_rate)`), and each overrides a
  method with genuinely different behavior — `signed_amount()` (an
  `Income` returns `+amount`, an `Expense` returns `-amount`, so a running
  balance is just `sum(t.signed_amount() for t in transactions)`) and
  `describe()` (extending the base string via `super().describe()`,
  exactly like every `Vehicle` subclass does). The reporting code loops
  over one mixed list of `Transaction` objects and calls
  `signed_amount()`/`describe()` polymorphically, with **no
  `if isinstance(t, Income): ... elif ...` chain** for computing totals —
  `isinstance()` is reserved for the one place a real type check is
  needed (a "show income only" / "show expenses only" filter), exactly
  matching the Vehicle project's own `isinstance()`-for-counting pattern.
- **Chapter 21 (Databases)** — a `transactions` table (or a mocked
  `FakeCursor`-style layer if a real `sqlite3` connection isn't
  available in your environment), CRUD built entirely on parameterized
  queries (`?` placeholders for SQLite, never f-string SQL), and
  `cursor()`/`execute()`/`fetchall()`/`commit()` — the same rhythm the
  Chapter 21 project's `FakeConnection`/`FakeCursor` established, applied
  to real `sqlite3` this time since SQLite needs no server to run.
- **Chapter 27 (Testing)** — a pytest suite covering happy paths (adding
  income/expense, computing balance, category totals), edge cases
  (zero/negative amount rejected by the property setter, an empty
  transaction list, two transactions on the same date), and fixtures
  (`fresh_db`/`sample_transactions`) that give every test a clean,
  isolated database — mirroring the Chapter 27 project's `manager`
  fixture giving every test a fresh `TaskManager`.
- **Chapter 31 (Professional Python)** — packaged as an installable CLI
  (`pyproject.toml`, `[project.scripts]`, `pip install -e .`) with a
  `core.py`/`cli.py`-style split (the `Transaction` hierarchy and the
  database layer never import `argparse` or call `print()`) and real
  `logging` instead of scattered `print()` calls for diagnostics.

## Prerequisites

Complete these chapters first:

- [Chapter 14: OOP Basics](../../chapter-14-oop-basics/lesson.html)
- [Chapter 15: OOP Deeper](../../chapter-15-oop-deeper/lesson.html)
- [Chapter 16: Inheritance & Polymorphism](../../chapter-16-inheritance-polymorphism/lesson.html)
- [Chapter 21: Databases](../../chapter-21-databases/lesson.html)
- [Chapter 27: Testing Your Code](../../chapter-27-testing-your-code/lesson.html)
- [Chapter 31: Professional Python](../../chapter-31-professional-python/lesson.html)

Read the [Library Management System](../../chapter-14-oop-basics/project/README.md),
[Bank Account System](../../chapter-15-oop-deeper/project/README.md), and
[Vehicle Rental System](../../chapter-16-inheritance-polymorphism/project/README.md)
READMEs closely — this capstone's `Transaction`/`Income`/`Expense`
hierarchy is a direct structural descendant of the Vehicle project's
`Vehicle`/`Car`/`Motorcycle`/`Truck` hierarchy, with the Bank Account
project's property-validation and classmethod patterns layered on top.
Also read the [Student Record Management System](../../chapter-21-databases/project/README.md)
for the parameterized-query CRUD pattern and the [pytest test suite](../../chapter-27-testing-your-code/project/README.md)
for the fixture/AAA testing pattern.

## Architecture

```text
finance_tracker/
├── pyproject.toml              <- [project.scripts] finance = "finance_tracker.cli:main"
├── requirements.txt            <- stdlib only (sqlite3, argparse, logging are all built in)
├── finance_tracker/
│   ├── __init__.py
│   ├── models.py                <- Transaction (base), Income, Expense
│   ├── db.py                    <- SQLite layer: init_db, insert_transaction,
│   │                                fetch_all, fetch_by_category, delete_transaction
│   ├── reports.py                <- balance(), totals_by_category(), monthly_summary()
│   │                                — all built on polymorphic signed_amount() calls
│   └── cli.py                    <- ONLY file that touches argparse/sys.argv/print()
└── tests/
    ├── conftest.py               <- fresh_db / sample_transactions fixtures
    ├── test_models.py            <- Transaction/Income/Expense unit tests
    ├── test_db.py                <- CRUD tests against a real (temp-file or :memory:) DB
    └── test_reports.py           <- balance/category-total tests
```

**Class hierarchy** (the actual OOP design this capstone is graded on):

```text
Transaction (base class)
├── __init__(self, amount, category, date, description="")
│     - amount routed through @amount.setter (rejects <= 0, raises ValueError)
│     - category validated via Transaction.is_valid_category() @staticmethod
├── @property amount / @amount.setter        (Ch15: validated, never negative/zero)
├── @staticmethod is_valid_category(name)     (Ch15: no instance needed)
├── @classmethod from_row(cls, db_row)        (Ch15: alternate constructor from a
│                                                sqlite3.Row / tuple fetched from the DB)
├── signed_amount(self)                       (Ch16: base returns self.amount;
│                                                overridden by both subclasses)
├── describe(self)                            (Ch16: base returns a shared summary line;
│                                                overridden, calling super().describe())
└── __str__(self)

Income(Transaction)
├── __init__(self, amount, category, date, description="", source="")
│     - calls super().__init__(...) first, then sets self._source
├── signed_amount(self) -> +self.amount        (override: money coming in)
└── describe(self) -> super().describe() + source detail

Expense(Transaction)
├── __init__(self, amount, category, date, description="", payment_method="")
│     - calls super().__init__(...) first, then sets self._payment_method
├── signed_amount(self) -> -self.amount         (override: money going out)
└── describe(self) -> super().describe() + payment-method detail
```

**Why `signed_amount()` is the design's real payoff:** a running balance
is just `sum(t.signed_amount() for t in all_transactions)` — one line,
zero `if isinstance(t, Income)` branching, and it stays correct forever
even if a third transaction type (`Transfer`? `Refund`?) gets added later,
exactly the same guarantee the Vehicle project's polymorphic
`calculate_rental_cost()` loop provides.

**Data flow:** `cli.py` parses arguments → calls into `db.py` (which
constructs `Income`/`Expense` objects via `Transaction.from_row()` when
reading, and calls `.signed_amount()`/`.amount` when writing) → `db.py`
persists/retrieves rows from SQLite using parameterized queries →
`reports.py` consumes lists of `Transaction` objects (never raw DB rows)
for balance/category/monthly calculations, staying entirely at the
object level so it never has to know SQL exists.

## Step-by-step roadmap

**Phase 1: Design and build the class hierarchy in isolation (~2.5
hours).** Write `models.py` with no database and no CLI involved yet —
just `Transaction`, `Income`, `Expense`, and a plain Python list in a
scratch script to sanity-check `signed_amount()` and `describe()` work
polymorphically. Confirm the `@amount.setter` actually raises
`ValueError` on `0` and on a negative number before moving on — this is
the property-validation pattern from Chapter 15's `BankAccount.balance`,
and it's the single most important correctness guarantee in this project.

**Phase 2: SQLite persistence (~2.5 hours).** Build `db.py`: a
`transactions` table (`id`, `type` ["income"/"expense"], `amount`,
`category`, `date`, `description`, plus `source` or `payment_method`),
`init_db()` creating the table if it doesn't exist, and CRUD functions
using `?` parameterized queries exclusively (never f-string SQL, per
Chapter 21's core lesson). `insert_transaction()` takes a `Transaction`
object and pulls its fields; `fetch_all()` returns real `Income`/`Expense`
objects built via `Transaction.from_row()` (or two separate
`Income.from_row`/`Expense.from_row` classmethods, routed by the stored
`type` column) — never raw tuples/dicts leaking out of `db.py`.

**Phase 3: Reports built on polymorphism (~1.5 hours).** Write
`reports.py`: `balance(transactions)` (the one-line `sum(...)` from the
architecture section above), `totals_by_category(transactions)` (a dict
built the same accumulate-and-count way earlier chapters' projects
build dicts), and `monthly_summary(transactions, year, month)`. None of
these functions should ever check `type(t) is Income` — if you find
yourself writing that, the class design needs an unimplemented shared
method, not a type check.

**Phase 4: pytest suite (~2.5 hours).** Write `conftest.py` with a
`fresh_db` fixture (temp-file or `:memory:` SQLite connection, torn down
per test — no shared state between tests, per Chapter 27's isolation
principle) and a `sample_transactions` fixture. Cover: happy paths
(add income, add expense, balance with a mix of both), edge cases (zero
and negative amounts rejected, empty transaction list balance is `0`, two
transactions on the same date both counted), and at least one test that
directly exercises polymorphism (a list containing both `Income` and
`Expense` objects, asserting `balance()` is correct without the test
itself needing to know which type contributed what).

**Phase 5: CLI and packaging (~2 hours).** Build `cli.py` with
subcommands (`finance add-income`, `finance add-expense`, `finance
list`, `finance balance`, `finance report --month 2026-07`), following
taskbox's `core.py`/`cli.py` separation and `logging` conventions
exactly. Write `pyproject.toml`, install with `pip install -e .` in a
fresh venv, and confirm `finance --help` and every subcommand work as a
real installed command.

**Phase 6: README (~1 hour).** Document the class hierarchy explicitly
(a reader should understand `signed_amount()`'s purpose without reading
the code), plus real terminal output from an actual run.

## MVP vs. stretch goals

**MVP (required to call this capstone done):**

- `Transaction` base class plus `Income`/`Expense` subclasses, both
  calling `super().__init__()` and both overriding `signed_amount()`
  and `describe()` with genuinely different logic.
- `@property`/`@x.setter` on `amount` that rejects non-positive values.
- At least one `@staticmethod` (format/category validation) and one
  `@classmethod` alternate constructor (`from_row`), matching Chapter
  15's patterns.
- Real SQLite persistence via `sqlite3`, all queries parameterized, data
  surviving a program restart.
- `balance()` and at least one category/summary report, computed
  polymorphically with no `isinstance`/`type()` branching for the math.
- A pytest suite with fixtures, covering happy paths and at least 3
  genuine edge cases, all passing (`python3 -m pytest -v`).
- Installable via `pip install -e .`, runnable as a real `finance`
  command.

**Stretch goals:**

- A third subclass, `Transfer(Transaction)` (money moving between two
  of your own accounts — `signed_amount()` returns `0` at the top level
  since it's neither real income nor expense) — added specifically to prove
  the existing report code needs zero changes to support it, the same
  "add a `Van(Vehicle)` and confirm nothing else breaks" exercise the
  Vehicle project's own stretch goals suggest.
- A `--budget` feature: a category-level spending cap stored in a
  separate table, with a report flagging categories over budget for the
  month.
- A `recurring` flag on `Expense` (e.g. a monthly subscription) and a
  command that auto-generates the current month's instance of it.
- Export to CSV (Chapter 13's `csv.writer`) for a chosen date range, tying
  this capstone back to an even earlier chapter.
- A `@pytest.mark.parametrize` test sweeping many amount values (valid
  and invalid) through the `@amount.setter` in one test function, per
  Chapter 27's own stretch-goal pattern.

## What a strong README for this capstone looks like

- **Lead with the class hierarchy, not the CLI.** This capstone is
  graded on OOP design — show the `Transaction`/`Income`/`Expense`
  diagram (or a text version of it) near the top, and explain
  `signed_amount()`'s purpose in one or two sentences before showing any
  terminal output.
- **Explicitly call out which Chapter-15 tools appear where** — name the
  exact `@property`, `@staticmethod`, and `@classmethod` you used and
  what each protects against, the same level of specificity the Bank
  Account System's own README uses for `balance`/`is_valid_account_number`/
  `open_new_account`.
- **Show the polymorphism payoff concretely** — a short "if I added a
  `Transfer` subclass tomorrow, here's what would and wouldn't need to
  change" paragraph, mirroring the Vehicle project's own "that's the
  whole point of polymorphism" callout.
- **Real, copy-pasted terminal output**, including the pytest run
  (`python3 -m pytest -v`, full pass output) and at least one real CLI
  session, matching taskbox's "run for real, not invented for the docs"
  standard.
- **A note on parameterized queries** — one or two sentences on why every
  SQL statement in `db.py` uses `?` placeholders, tying back explicitly
  to Chapter 21's SQL-injection lesson.
- **A short "what's tested and why" section** summarizing the pytest
  suite's coverage (happy paths, edge cases, the isolation fixture) —
  not the full test code, just what's covered and what a broken change
  would be caught by.

## Common pitfalls

- **Modeling `Income` and `Expense` as separate, unrelated classes
  instead of using inheritance.** This is the single biggest way to miss
  the point of this capstone — if `Income` and `Expense` don't share a
  `Transaction` base class via `super().__init__()`, there's no
  polymorphism to demonstrate, and every report function ends up needing
  two near-duplicate code paths (or an `isinstance` chain) instead of one
  polymorphic loop.
- **Putting the "never negative" amount check in `__init__` instead of
  the `@amount.setter`.** If validation only happens at construction
  time, nothing stops `transaction.amount = -50` later from silently
  producing a corrupt balance — the whole reason Chapter 15 teaches
  properties is so *every* write path (construction included) funnels
  through one validated setter, exactly like `BankAccount.balance`.
- **Letting `db.py` leak raw SQLite rows (tuples/`sqlite3.Row`) into
  `reports.py` instead of real `Transaction` objects.** If reports
  compute totals directly off raw row data instead of calling
  `.signed_amount()` on real `Income`/`Expense` instances, the
  polymorphism built into the class hierarchy never actually gets used
  — the database layer must reconstruct real objects (via
  `Transaction.from_row()`) before handing data to anything else.
- **Building SQL queries with f-strings/`.format()` instead of `?`
  placeholders.** Even in a personal project with no untrusted input,
  this recreates the exact injection risk Chapter 21's project spent a
  whole menu option (`Show why SQL injection matters`) demonstrating —
  every `execute()` call in `db.py` should look like
  `cursor.execute("INSERT INTO transactions VALUES (?, ?, ?)", (a, b, c))`,
  never a manually built string.
- **Tests that share one database file/connection across test
  functions.** Without a fresh, isolated fixture per test (Chapter 27's
  `manager` fixture pattern — `fresh_db` here), one test's leftover data
  can make a later test pass or fail for the wrong reason; use a
  `:memory:` SQLite connection or a fresh `tmp_path`-based file per test,
  torn down automatically.

## Self-assessment checklist

- [ ] `Transaction` is a real base class; `Income` and `Expense` both
      inherit from it and both call `super().__init__()`.
- [ ] `signed_amount()` and `describe()` are overridden in both
      subclasses with genuinely different behavior (not just returning
      the same thing as the base class).
- [ ] `amount` is a `@property` with a `@amount.setter` that raises
      `ValueError` on zero or negative values, and every construction
      path (including `from_row`) goes through it.
- [ ] At least one `@staticmethod` and one `@classmethod` exist and are
      used for real (not decorative).
- [ ] `balance()`/category totals are computed with a polymorphic loop
      over mixed `Transaction` objects — no `isinstance`/`type()` branch
      used for the arithmetic itself.
- [ ] `isinstance()` (if used at all) appears only for a genuine
      filtering need (e.g. "income only" view), matching the Vehicle
      project's own restrained use of it.
- [ ] SQLite persistence works across a program restart; every query
      uses `?` parameterized placeholders, none use f-string SQL.
- [ ] `python3 -m pytest -v` passes, with fixtures providing test
      isolation and at least 3 genuine edge cases covered.
- [ ] Installable via `pip install -e .`; the `finance` command works
      from any directory.
- [ ] README leads with the class hierarchy and includes real,
      copy-pasted terminal output (CLI session and pytest run).
