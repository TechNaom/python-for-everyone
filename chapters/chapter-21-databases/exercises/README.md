# Chapter 21 Exercises: Working with Databases

These exercises use what Chapter 21 covered: connecting and querying with
`mysql-connector-python`'s real interface (`connect()`, `.cursor()`,
`.execute()`, `.fetchall()`/`.fetchone()`), why parameterized queries
prevent SQL injection, `pymongo`'s CRUD methods
(`insert_one`/`find`/`update_one`/`delete_one`), and reading cloud
credentials from environment variables. Every "database" here is a
`FakeConnection`/`FakeCursor` or `FakeCollection` class -- small stand-ins
matching the real drivers' method names and call shapes, so nothing in
this folder needs a live MySQL/MongoDB server or either driver installed.

## How to run

Run this **from inside this `exercises/` folder**:

```bash
cd exercises
python3 starter.py
```

## Task 1 — Querying with a parameterized WHERE clause

Find `# TODO 1`. Get a connection and cursor from `FakeConnection(STUDENTS_TABLE)`,
run `cursor.execute("SELECT * FROM students WHERE grade > %s", (80,))`, and
print each matching row's `"name"`.

## Task 2 — `fetchone()`

Find `# TODO 2`. Run a parameterized query matching one student by name and
print `cursor.fetchone()`.

## Task 3 — Building an unsafe query (to see the danger)

Find `# TODO 3`. Write `build_unsafe_query(name)` and call it with a
malicious input to see exactly how SQL injection changes the query's
meaning -- this task only builds and prints the string, it never executes
it against anything.

## Task 4 — The parameterized fix

Find `# TODO 4`. Write `build_safe_query_and_params(name)` -- the same
malicious input, but now harmless, since it's kept as data in a separate
params tuple instead of being glued into the SQL string.

## Task 5 — MongoDB `insert_one` and `find`

Find `# TODO 5`. Insert two documents into a `FakeCollection()` and print
every document currently stored.

## Task 6 — MongoDB `update_one`

Find `# TODO 6`. Update one document's `grade` field using `{"$set": ...}`
and confirm the change with `find_one`.

## Task 7 — MongoDB `delete_one`

Find `# TODO 7`. Delete one document and confirm only the other one
remains.

## Task 8 — Cloud credentials via environment variables

Find `# TODO 8`. Write `build_connection_info()` that reads database
connection details from `os.environ` instead of hardcoding them.

## Task 9 — Debug the Code

Find `# TODO 9`. This is supposed to look up "Ben Osei" by name, but it
builds the SQL string with an f-string instead of a parameterized query
-- the SQL injection risk from Sub-topic 4. It also just returns the
wrong row here (`FakeCursor` doesn't recognize the f-string's shape, so
it falls back to returning every row, and `fetchone()` grabs the first
one instead). Find and fix it.

## Checking your work

Compare your output against `solution.py`. Every task's output is exactly
reproducible, every time -- nothing in this chapter's exercises depends on
timing or a live database.
