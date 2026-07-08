# Chapter 21 Practice Bank: Working with Databases

A deeper set of practice problems, organized by topic, on top of the main
`exercises/` folder — including scenario-based problems written in the
same style you'll see in real interviews. This is the chapter where
`mysql-connector-python`'s and `pymongo`'s real interfaces become
allowed, on top of everything from Chapters 1-20. Every "database" here
is a `FakeConnection`/`FakeCursor` or `FakeCollection` class standing in
for the real drivers' interfaces — no live MySQL/MongoDB server or
installed driver is needed anywhere in this bank. No import beyond
`json`/`os`/`re`/`math`/`datetime`/`random`/`csv`/`threading`/`concurrent.futures`.

## How to run

```bash
cd practice
python3 starter.py
```

## Topic 1: What a Database Connection Is, and Why a Driver

1. Decide whether a system needs a driver library.
2. List the shared connect-run-read shape both drivers follow.
3. **Debug the Code:** fix a claim that a driver stores the whole database in Python's memory.
4. **Scenario — Choosing Whether a Driver Is Needed:** write `does_this_tool_need_a_driver()`.
5. **Scenario — Interview Prep:** explain why Python can't talk to a database the way it opens a file.

## Topic 2: Connecting to MySQL & Cursors

1. Get a connection and a cursor.
2. Write a reusable `run_query()` helper.
3. Count matching rows from a query.
4. **Debug the Code:** fix code that called `.execute()` directly on a connection instead of a cursor.
5. **Scenario — Reusable Query Helper:** write `fetch_students_above()`.
6. **Scenario — Interview Prep:** explain the cursor vs. connection distinction.

## Topic 3: Parameterized Queries & SQL Injection

1. Build a parameterized query as a (sql, params) tuple.
2. Write a rough "looks like an injection attempt" check.
3. **Debug the Code:** fix an f-string-built query back to parameterized form.
4. **Scenario — Reviewing a Teammate's Query Code:** write `review_teammates_query()`.
5. **Scenario — Interview Prep:** explain why checking input for quotes isn't a real defense.

## Topic 4: MongoDB & Documents

1. Insert documents with different shapes into the same collection.
2. Check whether a document has a given field.
3. **Debug the Code:** fix a claim that every document must share the same fields.
4. **Scenario — Modeling a Product Catalog:** write `explain_product_catalog_fit()`.
5. **Scenario — Interview Prep:** explain the tradeoff of a flexible schema.

## Topic 5: CRUD with pymongo

1. Insert several documents and count them.
2. Update a document's field with `{"$set": ...}`.
3. Delete a document and confirm the rest remain.
4. **Debug the Code:** fix an update call missing the `"$set"` wrapper.
5. **Scenario — A Simple Inventory Tracker:** write `restock_item()`.
6. **Scenario — Interview Prep:** explain `update_one`/`delete_one` vs. `update_many`/`delete_many`.

## Topic 6: Relational vs. Document Data

1. Decide whether relational fits a given shape of data better.
2. Describe what a join does.
3. **Debug the Code:** fix an overstated claim about relational databases and varying-shape data.
4. **Scenario — Choosing a Model for a New Feature:** write `recommend_model_for_user_profiles()`.
5. **Scenario — Interview Prep:** give a 30-second relational-vs-document comparison.

## Topic 7: Cloud-Hosted Connections & Environment Variables

1. Build a config dict backed by environment variables.
2. Write a rough "is this a hardcoded secret" check.
3. **Debug the Code:** fix a hardcoded password back to reading from `os.environ`.
4. **Scenario — Reviewing a Deployment Config:** write `review_hardcoded_password()`.
5. **Scenario — Interview Prep:** explain what TLS adds beyond environment-variable credentials.

## Checking your work

Compare your output against `solution.py`. Your exact wording doesn't
need to match — the goal is that your program runs without errors and
does what each TODO asks. One exception: Topic 2's debug task
intentionally demonstrates a real `AttributeError` (caught and printed)
before it's fixed — that's the whole point of that task. Every other
task's output is exactly reproducible.
