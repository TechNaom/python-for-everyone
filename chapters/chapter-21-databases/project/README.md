# Chapter 21 Project: Student Record Management System

A menu-driven mini-app built **around this chapter's core tools** as its
organizing principle — a mock database layer (`FakeConnection`/`FakeCursor`)
that implements `mysql-connector-python`'s real interface (`cursor()`,
`execute(sql, params)`, `fetchall()`, `fetchone()`, `commit()`) closely
enough to demonstrate genuine CRUD operations, parameterized-query
safety, and reporting — all without a live MySQL server. No real network
access or database connection happens anywhere in this file, so it runs
identically for every learner, every time.

## What you'll build

A menu loop offering ten real operations:

1. List all students
2. Find a student by ID
3. Add a new student
4. Update a student's grade
5. Delete a student
6. Show class average
7. Show honor roll (grade >= 90)
8. Export all students as JSON
9. Show why SQL injection matters (a safe, never-executed demo)
10. Quit

Built from these pieces:

- `FakeConnection`/`FakeCursor` — a mock database layer whose method
  names and call shapes exactly match a real `mysql-connector-python`
  connection and cursor: `.cursor()`, `.execute(sql, params)`,
  `.fetchall()`, `.fetchone()`, `.commit()`. Only the underlying "server"
  differs (a plain Python list of dicts instead of a live MySQL
  instance) — everything a caller writes against it is genuine
  `mysql-connector-python` usage.
- `add_student()` / `list_students()` / `find_student()` /
  `update_grade()` / `delete_student()` — the four CRUD operations, each
  built on a parameterized query (`%s` placeholders, values passed
  separately) rather than string-building, so the pattern this chapter
  teaches as safe is the only pattern this project ever uses.
- `class_average()` / `honor_roll()` — small reporting functions built on
  top of `list_students()`, tying database querying back to Chapter 9's
  aggregation habits.
- `export_to_json()` — dumps every student record with `json.dumps(..., indent=2)`,
  tying back to Chapter 19's `json` module.
- `build_unsafe_search_query()` — builds (but never executes) the
  vulnerable f-string version of a query, so menu option 9 can show
  exactly what an injection attempt would do to it, side by side with the
  safe parameterized query this project actually runs.

Example run:

```text
=== Student Record Management System ===

1. List all students
2. Find a student by ID
3. Add a new student
4. Update a student's grade
5. Delete a student
6. Show class average
7. Show honor roll (grade >= 90)
8. Export all students as JSON
9. Show why SQL injection matters (safe demo, no execution)
10. Quit
Choose an option (1-10): 1

  [1] Ana Torres: 91
  [2] Ben Osei: 78
  [3] Chen Wu: 88

...
Choose an option (1-10): 3

New student's name: Dana Kim
New student's grade: 95
Added Dana Kim.

...
Choose an option (1-10): 6

Class average: 88.0

...
Choose an option (1-10): 10

Goodbye!
```

## How to run it

```bash
cd chapters/chapter-21-databases/project
python3 starter.py
```

Fill in the numbered `# TODO` sections in `starter.py`. Want to see one
finished version first? Run `python3 solution.py` (also from inside this
folder).

## Ideas to make it your own (optional stretch goals)

- Add a "search by name" option using a genuinely parameterized query
  (`WHERE name = %s`), rather than only searching by ID.
- Track a simple audit log (a Python list of strings) recording every
  add/update/delete with a timestamp (Chapter 11's `datetime` module),
  and add a menu option to display it.
- Add basic validation rejecting a grade outside `0-100`, raising a
  custom exception (Chapter 12) with a clear message instead of silently
  accepting bad data.

## Why this project matters

Every real student information system, HR platform, and customer
database is, underneath its user interface, exactly this pattern: CRUD
operations built on parameterized queries against a relational database.
This project's mock database layer uses the genuine
`mysql-connector-python` method names and call shapes throughout, so
everything learned here — the cursor/execute/fetchall/commit rhythm, and
the parameterized-query habit that closes off SQL injection — transfers
directly to a real MySQL-backed application, changing only the
connection details (Sub-topic 8's cloud-hosted, environment-variable-backed
`connect()` call) rather than any of the query logic itself.

## More project ideas (build one of these instead, or after)

From Chapter 7 onward, you get a genuine choice of what to build. The
Student Record Management System above is fully built out with a starter
and reference solution — the four ideas below are not. Each is a real,
grounded use case solvable with only what's been taught through Chapter 21
(everything through Chapter 20's threading, plus this chapter's database
concepts). No starter or solution files are provided on purpose —
building one of these unassisted is the point.

### 1. MongoDB-Style Document-Store Inventory Tracker (Mocked)

**Problem:** A small warehouse needs to track inventory items whose
attributes genuinely vary by category (electronics need a
`warranty_years` field, groceries need an `expiration_date` field,
clothing needs a `size` field) — a fixed-column table would need many
unused columns per item.

**What it should do:** Build a `FakeCollection` class (following this
chapter's `insert_one`/`find`/`update_one`/`delete_one` pattern) storing
inventory items as plain dicts with only the fields relevant to each
item's own category. Menu options: add an item (of any category, with
whatever fields make sense for it), search by category, update an item's
quantity with `{"$set": ...}`, and list everything.

**Suggested approach:** Reuse this project's exact CRUD-function naming
convention, swapping the MySQL-style `FakeCursor` for a `FakeCollection`
— the shape doesn't change based on which database style is mocked, only
the underlying storage and query methods.

### 2. Cloud Connection-String Config Validator

**Problem:** Before a real deployment, a team wants a small tool that
checks whether all required database configuration is actually present
as environment variables, without ever connecting to a real database.

**What it should do:** Build a function `validate_db_config(required_keys)`
that checks `os.environ` for every key in `required_keys`, returning a
report of which are present and which are missing — plus a check flagging
any value that looks like it might be an actual hardcoded secret
accidentally left in a config file rather than a real environment
variable reference. Menu options: run a validation check and print a
report, and simulate "fixing" a missing variable by setting it (for
demonstration only, never simulating what a real production credential
would be).

**Suggested approach:** Tie this directly to Sub-topic 8 — the entire
tool is a small, practical extension of "credentials should come from
`os.environ`, not be hardcoded," turned into something a team could
actually run before a deployment.

### 3. A Simple ORM-Lite Wrapper Exercise

**Problem:** Writing raw parameterized SQL for every single query gets
repetitive — a very small "ORM-lite" (Object-Relational Mapper) could
wrap common patterns into reusable functions.

**What it should do:** Build a small `Table` class wrapping a
`FakeConnection`/`FakeCursor` pair, with methods like
`.all()`, `.find_by_id(id)`, `.insert(**fields)`, `.update(id, **fields)`,
and `.delete(id)` — each internally building the exact same parameterized
queries this chapter's project uses, just exposed through a friendlier,
more reusable interface. Menu options: demonstrate each method against a
students table built with this new wrapper.

**Suggested approach:** This is a good chance to note, in your own
README, that real ORMs (like SQLAlchemy for Python) do exactly this at a
much larger scale — generating parameterized SQL automatically from
higher-level method calls, which is part of why they're popular for
avoiding hand-written SQL injection risks by default.

### 4. Library Checkout System with Two Mock Backends

**Problem:** A library wants to compare a relational design (books and
checkouts as separate related tables) against a document design (each
book's checkout history nested directly inside its own document) for the
exact same real-world data.

**What it should do:** Build the same checkout system twice: once using
a MySQL-style `FakeCursor` with a separate `checkouts` table joined by
`book_id` (mimicking a real join in Python), and once using a
`FakeCollection` where each book document has a nested `checkout_history`
list. Menu options let a user check a book in/out and view its history,
through either backend, so the exact same feature is visibly implemented
two different ways.

**Suggested approach:** This is the most direct way to build Sub-topic 7's
relational-vs-document comparison yourself instead of just reading about
it — write a short README section stating which backend felt simpler for
which specific operation, and why.
