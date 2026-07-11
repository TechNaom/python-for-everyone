# Capstone 1: Full-Stack Task API

## Overview

You already built a Task Manager REST API twice back in Chapter 22 — once
in Flask, once in FastAPI — both holding tasks in a plain in-memory list
that resets every time the process restarts. This capstone turns that
prototype into something you could actually deploy: tasks persist to a
real SQLite database, a genuine pytest suite proves every endpoint works
(and keeps working as you change things), and a GitHub Actions workflow
runs that suite automatically on every push. This is the single most
common shape of a real-world backend job — a persisted API with an
automated safety net — which makes it a strong, recognizable portfolio
piece for anyone evaluating your GitHub profile.

## Skills this combines

- **Chapter 21 (Databases)** — CRUD operations built on parameterized
  queries against a real database, instead of an in-memory dict. Chapter
  21's project used a *mocked* `mysql-connector-python`-style layer
  (`FakeConnection`/`FakeCursor`) with `.cursor()`, `.execute(sql,
  params)`, `.fetchall()`, `.fetchone()`, `.commit()` — this capstone
  swaps that mock for Python's real built-in `sqlite3` module, which
  exposes that exact same `connect()` → `cursor()` → `execute()` →
  `fetchall()`/`fetchone()` → `commit()` rhythm against a real `.db` file
  on disk. The parameterized-query habit (`?` placeholders for `sqlite3`,
  values passed separately — never f-string-building SQL) carries over
  unchanged.
- **Chapter 22 (Flask & FastAPI)** — the CRUD routes themselves (list,
  get-by-id, create, update, delete) and the "thin route, plain function
  underneath" pattern both chapters' solutions used. Pick **one**
  framework to carry forward for this capstone (Flask or FastAPI,
  whichever you're more comfortable with) rather than building both —
  Chapter 22 already made the side-by-side comparison; this capstone is
  about going deep on one.
- **Chapter 27 (Testing)** — the AAA pattern (Arrange, Act, Assert),
  fixtures that return fresh state per test (no shared state leaking
  between tests), and testing real code rather than toy examples. This
  capstone's version of "the external dependency to isolate" is the
  database itself: just like Chapter 27 mocked `NotificationSender` so
  tests never sent a real notification, this capstone uses a **separate
  test database** so tests never touch your real data.
- **Chapter 30 (CI/CD)** — the two-job workflow pattern (a `lint` job
  running `ruff check .`, a `test` job running `pytest`), triggers on
  both `push` and `pull_request`, and the core habit that a workflow
  should only ever run commands you've already run and verified
  yourself, locally, first.

## Prerequisites

Complete these chapters before starting (or at least skim their
lesson/project again if it's been a while):

- [Chapter 21: Databases](../../chapter-21-databases/lesson.html)
- [Chapter 22: Web APIs — Flask & FastAPI](../../chapter-22-web-apis-flask-fastapi/lesson.html)
- [Chapter 27: Testing Your Code](../../chapter-27-testing-your-code/lesson.html)
- [Chapter 30: CI/CD Pipelines](../../chapter-30-cicd-pipelines/lesson.html)

## Architecture

```text
                     HTTP requests (GET/POST/PATCH/DELETE)
                                   |
                                   v
                     Flask or FastAPI routes (thin wrappers)
                        /api/tasks, /api/tasks/{id}
                                   |
                                   v
                    Plain Python functions (the real logic)
                 list_tasks() / get_task() / add_task() / ...
                                   |
                                   v
                sqlite3 connection  ---->  tasks.db (real file on disk)
                (parameterized queries, same rhythm as Ch21's
                 FakeConnection/FakeCursor, just against a real DB)

Two separate SQLite files, never confused with each other:
  tasks.db        <- what the running app actually uses
  test_tasks.db (or an in-memory ":memory:" DB) <- what pytest uses,
                     created fresh and torn down every test run

                                   |
                                   v
                pytest test suite (test_app.py)
        Flask's app.test_client() or FastAPI's TestClient
        hits every route the same way a real HTTP client would,
        but in-process, no real server needed to run the tests
                                   |
                                   v
              .github/workflows/ci.yml (GitHub Actions)
        lint job (ruff check .) + test job (pytest -v)
        triggers on push and pull_request, runs the exact
        same commands you already run locally
```

The key architectural decision this capstone forces you to make and
defend: **how does the test suite avoid touching your real `tasks.db`?**
The two common answers are (a) point the app at an in-memory
`sqlite3.connect(":memory:")` database during tests via a pytest
fixture, or (b) point it at a throwaway file path and delete it after
each test. Either is fine — just pick one, understand why it's needed,
and say so in your README.

## Step-by-step roadmap

**Phase 1: Add real persistence (~2-3 hours)**
1. Copy your Chapter 22 solution (Flask or FastAPI, your choice) into
   this capstone's project folder as your starting point.
2. Write a small `db.py` module: a function that opens a `sqlite3`
   connection to a given file path, and a `init_db(conn)` function that
   creates the `tasks` table (`id`, `title`, `done`) if it doesn't
   already exist.
3. Replace the in-memory list/dict in every route's underlying function
   with real `sqlite3` calls — `SELECT` for list/get, `INSERT` for
   create, `UPDATE` for the done-status change, `DELETE` for delete.
   Every query uses `?` placeholders with values passed separately,
   never an f-string building SQL directly into the query.
4. Manually verify: start the app, hit a few endpoints with `curl` or
   your browser, stop the app, restart it, and confirm your data is
   still there. That "survives a restart" moment is the actual point of
   this phase.

**Phase 2: Write the pytest suite (~2-3 hours)**
5. Decide on your test-database strategy (in-memory `:memory:` or a
   throwaway file) and wire it into a pytest fixture that gives your app
   a fresh, empty database for every test — no test should be able to
   see data left behind by a previous test.
6. Write a happy-path test for every endpoint: list tasks, get one task
   by ID, create a task, update a task's done status, delete a task.
7. Write at least one error-case test per endpoint: getting a
   nonexistent ID (expect a 404), creating a task with a missing/empty
   title (expect a 400/422), deleting a nonexistent ID.
8. Run `pytest -v` locally and confirm every test passes, then
   deliberately break one route (e.g. comment out the `?` placeholder
   safety and hardcode a wrong status code) and confirm the
   corresponding test actually fails — a test suite you haven't watched
   fail at least once is a test suite you don't fully trust yet.

**Phase 3: Wire up CI (~1-2 hours)**
9. Add a `requirements-dev.txt` (or extend `pyproject.toml`) listing
   `pytest`, `ruff`, and your chosen framework (`flask` or `fastapi` +
   `uvicorn` + `httpx` for FastAPI's `TestClient`).
10. Write `.github/workflows/ci.yml` following Chapter 30's two-job
    pattern: a `lint` job running `ruff check .`, a `test` job running
    `pytest -v`, both triggered `on: [push, pull_request]`.
11. Run `ruff check .` locally first and fix every violation it reports
    — don't let CI be the first place you discover a lint error.
12. Push to a real GitHub repo (this is the one capstone step that
    genuinely needs a live push, since Actions only runs on GitHub's
    servers) and confirm the Actions tab shows both jobs passing.

**Phase 4: Polish and document (~1 hour)**
13. Write the README (see the section below).
14. Add a CI status badge to the top of your README.

## MVP vs. stretch goals

**MVP — must work to call this done:**
- All five original CRUD operations (list, get-by-id, create, update
  done-status, delete) persist to a real SQLite database and survive an
  app restart.
- Every query uses parameterized SQL — no string-built queries anywhere.
- A pytest suite covers the happy path for every endpoint, plus at least
  one error case per endpoint, and runs against a separate test database
  (never the real `tasks.db`).
- `.github/workflows/ci.yml` exists, runs lint + test on push/PR, and
  you have a real screenshot or link showing it passing on GitHub.
- A README explaining the architecture and how to run it locally.

**Stretch goals (optional, for learners who want to go further):**
- Add a `PUT /tasks/{id}` full-replace route alongside the existing
  `PATCH` partial-update route (an idea Chapter 22 already floated).
- Add pagination to the list endpoint (`?limit=&offset=`).
- Add a second resource (e.g. `categories` that tasks belong to,
  `FOREIGN KEY`-linked in SQLite) to prove the pattern generalizes.
- Add basic API-key auth (a required header checked against an
  environment variable) and a test proving requests without it are
  rejected.
- Add a `build` job to CI (following Chapter 30's stretch idea) that
  packages the app, or a `docker build` job if you're comfortable
  reaching slightly beyond this course.

## What a strong README for this capstone looks like

- **State your architecture decisions explicitly**, not just what the
  app does: which framework you chose and why, raw `sqlite3` vs. an ORM
  (and why you didn't reach for SQLAlchemy if you didn't — "this course
  taught raw parameterized `sqlite3`, so that's what I used" is a
  completely honest and sufficient answer), and how your test suite
  avoids touching the real database.
- **Disclose real limitations honestly** — no auth (anyone can hit any
  route), no input length limits, SQLite doesn't handle high concurrent
  write load well (fine for a portfolio project, worth naming so a
  reviewer knows you know it). A README that pretends there are no
  limitations reads as less credible than one that names them plainly.
- **Show a real example run** — actual `curl` commands and their actual
  output (or a FastAPI `/docs` screenshot), not invented sample output.
- **Include the CI badge** and a one-line note on what "green" actually
  verifies (lint passes, and every endpoint's happy path + error cases
  pass against a fresh database).

## Common pitfalls

- **Running the pytest suite against your real `tasks.db`.** If your
  fixture doesn't properly isolate the test database, running the tests
  will silently pollute (or wipe) your actual data. This is the single
  most important thing to get right and verify — after running
  `pytest`, check that `tasks.db` still has exactly the data you expect
  and no test-only "Test task 1" rows leaked in.
- **Forgetting `init_db()` needs to run before the first request.**
  Unlike the in-memory dict from Chapter 22 (which just existed the
  moment the module loaded), a SQLite table has to actually be created
  with `CREATE TABLE IF NOT EXISTS` before any query against it will
  work — easy to forget until you get a `no such table: tasks` error on
  a fresh clone.
- **String-formatting SQL "just this once."** It's tempting to build a
  dynamic `WHERE` clause (e.g. for a `?done=true` filter) with an
  f-string because parameterizing an optional filter feels awkward.
  Resist it — build the query and parameter list together
  conditionally, but never interpolate a value directly into the SQL
  string, even for a filter that seems harmless.
- **Sharing one SQLite connection across concurrent requests
  incorrectly.** `sqlite3` connections aren't safe to share across
  threads by default; if your framework runs requests on multiple
  threads, either open a new connection per request or pass
  `check_same_thread=False` deliberately and understand the tradeoff —
  don't just silence the error without knowing what it means.
- **Writing a CI workflow you never ran locally first.** Chapter 30
  already named this as the single most common real-world CI mistake —
  a typo in a script name or a missing dependency in
  `requirements-dev.txt` only surfaces after a push. Run `ruff check .`
  and `pytest -v` locally, from a clean clone if possible, before
  trusting what the workflow reports.

## Self-assessment checklist

- [ ] I can stop and restart my app and my tasks are still there.
- [ ] Every SQL query in my code uses `?` placeholders — I grepped for
      f-strings and `.format()` near any `execute()` call to be sure.
- [ ] `pytest -v` passes locally, covering every endpoint's happy path
      and at least one error case each.
- [ ] I deliberately broke one route and watched its test fail, then
      fixed it and watched the test pass again.
- [ ] My test suite never touches my real `tasks.db` — I verified this
      by checking the file's contents/timestamp before and after a test
      run.
- [ ] `ruff check .` reports zero violations.
- [ ] `.github/workflows/ci.yml` exists and I've seen it actually run
      and pass on a real push to GitHub (not just "it looks right").
- [ ] My README explains my architecture choices and honestly lists
      what this project doesn't do (auth, pagination, etc., unless I
      built them as stretch goals).
- [ ] A stranger cloning my repo could get this running locally from
      the README alone, with no extra context from me.
