# Chapter 22 Project: Task Manager REST API — Flask & FastAPI

**A note on this project's file structure, before anything else:** this
chapter explicitly teaches two frameworks side by side, so this project
deviates from CONTRIBUTING.md's single `starter.py`/`solution.py`
convention on purpose — there are **two parallel pairs** of files
instead of one:

- `starter_flask.py` / `solution_flask.py` — the Flask version
- `starter_fastapi.py` / `solution_fastapi.py` — the FastAPI version

Both build the exact same task manager, so the contrast between the two
frameworks stays concrete and side by side, rather than forcing one
chapter's project to arbitrarily pick only one of the two frameworks it
just taught.

## What you'll build (twice)

A **Task Manager REST API** — CRUD on an in-memory list of tasks, doing
Create, Read, Update, and Delete — built once in Flask, once in FastAPI:

- **Flask version:** built as a small JSON API (`/api/tasks/...` routes,
  returning dicts that Flask auto-converts to JSON) **plus** one
  server-rendered HTML page at `/`, showing Flask's classic idiom
  clearly alongside its JSON capability.
- **FastAPI version:** built as a pure, typed JSON API using Pydantic
  models for request validation — no HTML page at all, matching
  FastAPI's idiom and this chapter's "what's next" point that a JSON API
  is meant to be consumed by something else, not displayed directly.

Both versions do the same five operations:

1. List all tasks (optionally filtered by `done`)
2. Get one task by ID
3. Create a new task
4. Update a task's `done` status
5. Delete a task

## Why this project can't start a live server, and what it does instead

This course has no backend of its own and Pyodide's in-browser sandbox
can't run a real Flask or FastAPI server — but Flask and FastAPI are
real frameworks that need `pip install flask` / `pip install fastapi
uvicorn` and an actual running process to serve HTTP. Both files handle
this honestly:

- Every route is written as **real**, complete Flask/FastAPI code —
  genuine `@app.route()`/`@app.get()`/`@app.post()` decorators, a real
  Pydantic `BaseModel`, and (commented out) a real `app.run()` /
  `uvicorn.run()` call, exactly what you'd type and run locally.
- Each route is a **thin wrapper** around a plain Python function
  (`_list_tasks_data()`, `_add_task_data()`, etc.) holding the actual
  logic — these plain functions are what get exercised when you run
  `python3 solution_flask.py` or `python3 solution_fastapi.py` directly,
  with no server needed at all.
- Running either file directly prints a demonstration of every
  operation's real output, so the project still does something
  meaningful in this course's no-server environment, while the
  commented-out `app.run()`/`uvicorn.run()` line is there for you to
  uncomment and actually run for real, locally, once you have Flask or
  FastAPI+uvicorn installed.

## Example run

```text
=== Task Manager REST API -- Flask version ===
Demonstration (no live server, calling the same logic the routes use):
GET /api/tasks       -> [{'id': 1, 'title': 'Write the report', 'done': False}, {'id': 2, 'title': 'Review pull request', 'done': True}]
GET /api/tasks/1     -> {'id': 1, 'title': 'Write the report', 'done': False}
POST /api/tasks      -> {'id': 3, 'title': 'Water the plants', 'done': False}
PATCH /api/tasks/1   -> {'id': 1, 'title': 'Write the report', 'done': True}
DELETE /api/tasks/2  -> True
GET /api/tasks (after changes) -> [{'id': 1, 'title': 'Write the report', 'done': True}, {'id': 3, 'title': 'Water the plants', 'done': False}]

To run this as a live server locally (pip install flask):
  uncomment the app.run() line below, then: python3 starter_flask.py
```

The FastAPI version prints the same shape of demonstration, using
`/tasks` paths and real `Task`/`TaskCreate`/`TaskUpdate` Pydantic model
instances instead of plain dicts.

## How to run it

```bash
cd chapters/chapter-22-web-apis-flask-fastapi/project
python3 starter_flask.py      # or starter_fastapi.py
```

Fill in the numbered `# TODO` sections in whichever starter file you
want to build first (or both). Want to see a finished version? Run
`python3 solution_flask.py` or `python3 solution_fastapi.py`.

**To actually run either one as a live server** (optional, needs a real
install): `pip install flask` (or `pip install fastapi uvicorn`),
uncomment the `app.run()` (or `uvicorn.run()`) line at the bottom of the
file, then run it and visit `http://localhost:5000/` (Flask) or
`http://localhost:8000/docs` (FastAPI's automatic interactive docs).

## Ideas to make it your own (optional stretch goals)

- Persist tasks to Chapter 21's mock DB layer (`FakeConnection`/
  `FakeCursor` or `FakeCollection`) instead of a plain in-memory dict —
  swap `TASKS[task_id] = ...` for `cursor.execute("INSERT ...", ...)`
  calls, the same pattern Chapter 21's project used.
- Add a `PUT /tasks/{id}` route that replaces a task's title AND done
  status together, contrasted with `PATCH`'s partial update.
- Add basic validation rejecting an empty or whitespace-only title, with
  a clear error message either as a Flask `400` response or a Pydantic
  field validator in the FastAPI version.

## Why this project matters

Nearly every mobile app backend and modern web application is, at its
core, exactly this pattern: CRUD operations exposed over HTTP as a small
set of routes. Building the same feature twice — once in Flask's
simpler, HTML-first style and once in FastAPI's typed, JSON-first,
auto-documented style — makes the tradeoff from Sub-topic 6 concrete
instead of abstract: the same five operations, expressed two genuinely
different ways, each fitting a different real-world situation.

## More project ideas (build one of these instead, or after)

From Chapter 7 onward, you get a genuine choice of what to build. The
Task Manager REST API above is fully built out with starter and
reference solution files for both frameworks — the four ideas below are
not. Each is a real, grounded use case solvable with only what's been
taught through Chapter 22. No starter or solution files are provided on
purpose — building one of these unassisted is the point.

### 1. A Simple Blog API

**Problem:** A blogging platform needs a backend API for creating,
listing, and reading blog posts.

**What it should do:** Build a FastAPI (or Flask) API with routes for
listing posts, getting one post by ID, and creating a new post (title +
body), using a Pydantic model (or Flask's `request.json`) for the
create route. Store posts in an in-memory list, like this chapter's
project stores tasks.

**Suggested approach:** Reuse this project's exact CRUD-route structure
and plain-function-per-route pattern, swapping "task" for "post" and
adding a `body` field alongside `title`.

### 2. A URL Shortener API

**Problem:** A URL shortener needs an API that accepts a long URL and
returns a short code, then redirects that short code back to the
original URL.

**What it should do:** Build a POST route that accepts a long URL and
returns a randomly generated short code (Chapter 11's `random` module),
storing the mapping in an in-memory dict. Build a GET route
`/{short_code}` that looks up the original URL (in a real deployment,
this would issue an HTTP redirect; here, returning the original URL as
JSON is a safe stand-in, matching this chapter's no-live-server
convention).

**Suggested approach:** This is a great fit for FastAPI's path
parameters — `/{short_code}` is exactly the kind of thing Sub-topic 4
covered.

### 3. A Bookmark Manager with Tags

**Problem:** A bookmark manager needs to store URLs the user wants to
keep, each tagged with one or more categories, and support filtering by
tag.

**What it should do:** Build CRUD routes for bookmarks (`url`, `title`,
`tags: list[str]`), plus a filtering query parameter
(`GET /bookmarks?tag=python`) that returns only bookmarks with a
matching tag — a direct extension of this chapter's `done` query
parameter filter, applied to a list field instead of a boolean.

**Suggested approach:** A Pydantic model field can be typed
`tags: list[str]` directly — FastAPI validates that it's genuinely a
list of strings, the same way it validates any other typed field.

### 4. A Personal Expense Tracker API

**Problem:** Someone wants a small API to log personal expenses and see
a running total, without a spreadsheet.

**What it should do:** Build routes to add an expense (`amount`,
`category`, optional `note`), list all expenses (optionally filtered by
`category`, the same query-parameter pattern this chapter's project
uses for `done`), and a `GET /expenses/total` route returning the sum of
all logged amounts — tying back to Chapter 9's aggregation habits.

**Suggested approach:** Build this one in whichever framework you found
more comfortable in this chapter's main project, as a chance to go
deeper in just one rather than splitting effort across both again.
