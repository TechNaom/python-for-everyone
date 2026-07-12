# Capstone 4: Personal Finance Tracker

A small, real, installable command-line personal finance tracker. This
capstone is graded on object-oriented design, not just working code — so
this README leads with the class hierarchy, not the CLI.

## The class hierarchy (read this first)

```text
Transaction (base class)
├── @property amount / @amount.setter   -- rejects amount <= 0, ValueError
├── @staticmethod is_valid_category(name)
├── @classmethod from_row(cls, db_row)  -- alternate constructor from SQLite
├── signed_amount(self)                 -- base: returns self.amount
├── describe(self)                      -- base: shared summary line
└── __str__(self)

Income(Transaction)
├── __init__(...) -> super().__init__(...), then sets self._source
├── signed_amount() -> +self.amount      (money coming in)
└── describe() -> super().describe() + " from {source}"

Expense(Transaction)
├── __init__(...) -> super().__init__(...), then sets self._payment_method
├── signed_amount() -> -self.amount      (money going out)
└── describe() -> super().describe() + " via {payment_method}"
```

**`signed_amount()` is the whole payoff of this design.** A running
balance across a mixed list of `Income` and `Expense` objects is one
line, with zero type-checking:

```python
def balance(transactions):
    return sum(t.signed_amount() for t in transactions)
```

Every `Transaction` in the list answers `signed_amount()` for itself —
`Income` returns `+amount`, `Expense` returns `-amount` — so `reports.py`
never has to ask "is this an Income or an Expense?" before deciding how
to add it up. That's exactly the guarantee Chapter 16's Vehicle project
demonstrates with `calculate_rental_cost()`: the loop is written once,
and stays correct even if a new transaction type gets added later (see
"If I added a `Transfer` subclass tomorrow" below).

## Chapter 15 tools, and what each one protects against

- **`@property amount` / `@amount.setter`** — every write path (the
  constructor, `from_row()`, or a direct `transaction.amount = ...`
  reassignment after construction) funnels through one validated setter
  that raises `ValueError` on `0` or a negative number. This is the same
  pattern as `BankAccount.balance` rejecting a negative value — the
  validation lives in the setter itself, not just in `__init__`, so
  nothing can silently corrupt a transaction's amount later.
- **`@staticmethod is_valid_category(name)`** — a pure format/membership
  check with no instance needed, exactly like
  `BankAccount.is_valid_account_number`. `Transaction.__init__` calls it
  to reject a bogus category before an object is ever built.
- **`@classmethod from_row(cls, db_row)`** — an alternate constructor
  that builds a `Transaction` subclass instance from a raw SQLite row,
  mirroring `BankAccount.open_new_account`'s "build the object a
  different way than a plain constructor call" pattern. Because `cls` is
  bound to `Income` or `Expense` (never called on bare `Transaction`
  directly), the same base implementation correctly builds either
  subclass, and the amount still goes through `@amount.setter` — a
  corrupted row with a non-positive amount raises `ValueError` from
  `from_row()` exactly as it would from a fresh, hand-built object.

## If I added a `Transfer` subclass tomorrow

Nothing in `reports.py` or `db.py`'s `fetch_all()`/`insert_transaction()`
would need to change. A `Transfer(Transaction)` would just define its own
`signed_amount()` (probably `0` at the top level, since a transfer
between two of your own accounts is neither real income nor a real
expense) and its own `describe()`. `balance()`, `totals_by_category()`,
and `monthly_summary()` would immediately handle `Transfer` objects
correctly the first time they ran, with zero edits — because they were
never written to check `isinstance(t, Income)` in the first place.

## Architecture

```text
finance_tracker/
├── pyproject.toml           <- [project.scripts] finance = "finance_tracker.cli:main"
├── requirements.txt         <- stdlib-only; pytest only needed to run tests/
├── finance_tracker/
│   ├── __init__.py
│   ├── models.py             <- Transaction (base), Income, Expense
│   ├── db.py                 <- SQLite layer: init_db, insert_transaction,
│   │                             fetch_all, fetch_by_category, delete_transaction
│   ├── reports.py             <- balance(), totals_by_category(), monthly_summary()
│   └── cli.py                 <- ONLY file that touches argparse/print()
└── tests/
    ├── conftest.py            <- fresh_db / sample_transactions fixtures
    ├── test_models.py         <- Transaction/Income/Expense unit tests
    ├── test_db.py             <- CRUD tests against a real SQLite connection
    └── test_reports.py        <- balance/category-total/monthly-summary tests
```

`cli.py` parses arguments, then calls `db.py` (which constructs real
`Income`/`Expense` objects via `Transaction.from_row()` on reads, and
pulls `.amount`/`.category`/etc. off a `Transaction` object on writes),
which persists/retrieves rows from SQLite. `reports.py` only ever sees
lists of real `Transaction` objects — never a raw SQLite row — so the
polymorphism built into the class hierarchy is what actually powers every
report.

## A note on parameterized queries

Every single SQL statement in `db.py` uses `?` placeholders with values
passed as a separate tuple — never an f-string or `.format()` call
building the query text. Even in a personal, single-user project with no
untrusted input, building SQL by string-concatenation recreates the exact
injection risk Chapter 21's "Show why SQL injection matters" demo covers:
a value that happens to contain a stray `'` or `;` should never be able
to change what a query does, and `?` placeholders are what guarantee
that no matter what the value contains.

## What's tested, and why

37 tests across three files, using a `fresh_db` fixture that opens a
brand-new in-memory (`:memory:`) SQLite connection per test — no test
shares a database or connection with any other, so one test's leftover
data can never make a later test pass or fail for the wrong reason.

- **`test_models.py`** — the `@amount.setter` rejects zero/negative both
  at construction *and* on a later reassignment (the roadmap's single
  most important correctness guarantee); category validation; the
  `@staticmethod`/`@classmethod` both work for real; and — critically —
  `Income.describe()` and `Expense.describe()` genuinely differ from
  each other and both extend (not replace) `Transaction.describe()` via
  `super()`.
- **`test_db.py`** — insert/fetch/delete against a real `sqlite3`
  connection, `fetch_all()` never returning a raw tuple, two
  transactions on the same date both being counted, and persistence
  surviving across two separate connections to the same file (simulating
  a program restart).
- **`test_reports.py`** — `balance()` on an empty list is `0`;
  `balance()` on a genuinely mixed `Income`+`Expense` list is correct
  *without the test itself checking which type contributed what* (the
  direct polymorphism test the roadmap asks for); category totals and
  a monthly summary both compute correctly.

A broken change any of these would catch: someone routing the amount
check back into only `__init__`, someone making `Income`/`Expense`
unrelated classes instead of subclasses, someone leaking a raw SQLite
row into `reports.py`, or someone rewriting a query with an f-string.

## Running it

```bash
# Install (from inside this folder, ideally in a virtualenv)
pip install -e .

# Run the test suite
python3 -m pytest -v

# Use the CLI
finance add-income 2000 salary 2026-07-01 --description "July paycheck" --source employer
finance add-expense 500 housing 2026-07-02 --description rent --payment-method bank_transfer
finance list
finance balance
finance report
finance report --month 2026-07
```

### Real terminal output

```text
$ python3 -m pytest -v
============================= test session starts ==============================
collected 37 items

tests/test_db.py::test_fresh_db_starts_empty PASSED                      [  2%]
tests/test_db.py::test_insert_income_then_fetch_all_returns_a_real_income_object PASSED [  5%]
...
tests/test_reports.py::test_monthly_summary_for_month_with_no_transactions_is_all_zero PASSED [100%]

============================== 37 passed in 0.25s ==============================
```

```text
$ finance --db /tmp/ft_cli_test.db add-income 2000 salary 2026-07-01 --description "July paycheck" --source employer
INFO: Inserted income #1 (salary, $2000.00)
Added income #1: INCOME  [salary] 2026-07-01: $2,000.00 from employer

$ finance --db /tmp/ft_cli_test.db add-expense 500 housing 2026-07-02 --description rent --payment-method bank_transfer
INFO: Inserted expense #2 (housing, $500.00)
Added expense #2: EXPENSE [housing] 2026-07-02: $500.00 via bank_transfer

$ finance --db /tmp/ft_cli_test.db add-expense 75.50 food 2026-07-06 --description groceries --payment-method credit_card
INFO: Inserted expense #3 (food, $75.50)
Added expense #3: EXPENSE [food] 2026-07-06: $75.50 via credit_card

$ finance --db /tmp/ft_cli_test.db add-income 150 freelance 2026-07-05 --description "logo design" --source "client X"
INFO: Inserted income #4 (freelance, $150.00)
Added income #4: INCOME  [freelance] 2026-07-05: $150.00 from client X

$ finance --db /tmp/ft_cli_test.db list
  INCOME  [salary] 2026-07-01: $2,000.00 from employer
  EXPENSE [housing] 2026-07-02: $500.00 via bank_transfer
  INCOME  [freelance] 2026-07-05: $150.00 from client X
  EXPENSE [food] 2026-07-06: $75.50 via credit_card

$ finance --db /tmp/ft_cli_test.db balance
Current balance: $1,574.50

$ finance --db /tmp/ft_cli_test.db report
Totals by category (all time):
  food            $-75.50
  freelance       $150.00
  housing         $-500.00
  salary          $2,000.00

$ finance --db /tmp/ft_cli_test.db report --month 2026-07
Report for 2026-07:
  Transactions: 4
  Income:  $2,150.00
  Expense: $-575.50
  Net:     $1,574.50
```

Each of the eight CLI calls above ran as a **separate process** against
the same `--db` file, so this is a real demonstration of data surviving
a program restart, not a single in-memory session.

## Prerequisites

- [Chapter 14: OOP Basics](../../chapters/chapter-14-oop-basics/lesson.html)
- [Chapter 15: OOP Deeper](../../chapters/chapter-15-oop-deeper/lesson.html)
- [Chapter 16: Inheritance & Polymorphism](../../chapters/chapter-16-inheritance-polymorphism/lesson.html)
- [Chapter 21: Databases](../../chapters/chapter-21-databases/lesson.html)
- [Chapter 27: Testing Your Code](../../chapters/chapter-27-testing-your-code/lesson.html)
- [Chapter 31: Professional Python](../../chapters/chapter-31-professional-python/lesson.html)
