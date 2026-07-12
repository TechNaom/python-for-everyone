# Capstone 1: Full-Stack Task API

A small, real Flask REST API for managing tasks, persisted to SQLite,
covered by a pytest suite, and checked on every push by a two-job
GitHub Actions workflow (lint + test).

This is the reference implementation for
[Capstone 1 in the Python for Everyone course](../../chapters/chapter-32-capstone-projects/capstones/capstone-1-task-api.md) —
it turns Chapter 22's in-memory Flask prototype into something that
actually persists data and proves itself with automated tests.

<!--
CI badge placeholder: this project has not been pushed to a live GitHub
repo yet, so there is no real Actions run to link a badge to. A faked
badge (one that always shows "passing" without a real workflow behind
it) would be dishonest, so instead of embedding one, here's exactly
what to do once this is pushed:

  1. Push this folder to a GitHub repo.
  2. Confirm the Actions tab shows both the `lint` and `test` jobs
     passing on a real run.
  3. Replace this comment with:
     ![CI](https://github.com/<you>/<repo>/actions/workflows/ci.yml/badge.svg)

Until that happens, this section stays a placeholder on purpose rather
than a green badge that isn't backed by a real run.
-->

**CI status:** not yet pushed to a live repo — see the note above.

## What this is

Five CRUD operations over a `tasks` resource:

| Method | Path              | Does what                          |
|--------|-------------------|-------------------------------------|
| GET    | `/api/tasks`      | list all tasks (optional `?done=`)  |
| GET    | `/api/tasks/<id>` | get one task by id                  |
| POST   | `/api/tasks`      | create a task (`{"title": "..."}`)  |
| PATCH  | `/api/tasks/<id>` | update done status (`{"done": true}`)|
| DELETE | `/api/tasks/<id>` | delete a task                       |

## Architecture decisions

**Framework: Flask, not FastAPI.** Chapter 22 built this same API in both
frameworks to compare them side by side. For this capstone I picked
Flask to go deep on one: it needed no extra Pydantic model layer for a
resource this small, and Flask's `app.test_client()` is a very direct
match for the AAA-style tests this project needed. FastAPI's automatic
`/docs` page and request validation are genuinely nicer for a larger
API, but weren't worth the extra moving parts here.

**Raw `sqlite3`, not an ORM.** This course taught raw parameterized
`sqlite3` (Chapter 21), so that's what this project uses — no
SQLAlchemy or other ORM. `db.py` is intentionally tiny: `get_connection()`
opens a file (or `:memory:`), `init_db()` creates the `tasks` table if
it's missing. Every query in `app.py` and `db.py` uses `?` placeholders
with values passed as a separate tuple, never an f-string or
`.format()` call building SQL text directly — verified by grepping the
whole project for that pattern (see "Verification" below).

**One shared connection, not one per request.** `create_app()` opens a
single `sqlite3` connection when the app starts and reuses it for every
request, with `check_same_thread=False` set deliberately (Flask's dev
server can dispatch requests on more than one thread, and sqlite3
connections aren't thread-safe to share by default without that flag).
The alternative — a fresh connection per request — would also silently
break the test database: a new connection to `:memory:` is a brand-new,
empty database every time, so per-request connections would mean every
request sees an empty `tasks` table. Sharing one connection across the
app's lifetime is what makes `:memory:` behave like a real persistent
database within a single run.

**Test isolation strategy: `:memory:`, not a throwaway file.** The
`client` fixture in `test_app.py` calls `create_app(":memory:")` for
every single test, giving each test its own brand-new, empty database
with zero setup/teardown file cleanup needed — no `os.remove()` calls,
no risk of a leftover `test_tasks.db` file lingering after a crashed
test run. The tradeoff: `:memory:` databases disappear the instant the
connection closes, so this strategy couldn't be used to test genuine
"survives a process restart" behavior — that's why the restart check
below was done manually against the real `tasks.db` file instead.

## Honest limitations

- **No authentication.** Any client can list, create, update, or delete
  any task. There's no user concept and no API key check.
- **No pagination.** `GET /api/tasks` returns every row in one response.
  Fine at the scale of a portfolio project; would need `?limit=&offset=`
  before this could hold thousands of rows.
- **No input length limits.** A task title can be arbitrarily long (or,
  short of empty/whitespace-only, arbitrarily weird) — nothing here
  caps it.
- **SQLite doesn't handle concurrent writes well.** A single writer at a
  time is fine for this project's scale; a real high-traffic API with
  many concurrent writers would want Postgres or MySQL instead. Worth
  naming plainly rather than pretending it doesn't matter.
- **One process, one connection.** This app isn't built to run as
  multiple worker processes behind a load balancer — see the
  "one shared connection" note above.

None of these were built as stretch goals in this pass (see the MVP vs.
stretch section of the capstone brief for what they'd involve).

## Running it locally

```bash
git clone <this-repo>
cd capstones/capstone-1-task-api
python3 -m venv .venv
source .venv/bin/activate       # Windows: .venv\Scripts\activate
pip install -r requirements-dev.txt
python3 app.py                  # serves on http://127.0.0.1:5000
```

## Real example run

This is an actual captured session: the server was started, hit with
real `curl` commands, stopped, and restarted, to prove data survives a
restart (the whole point of Phase 1 in the capstone brief).

```
$ python3 app.py
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
```

```
$ curl -s http://127.0.0.1:5000/api/tasks
{
  "tasks": []
}

$ curl -s -X POST http://127.0.0.1:5000/api/tasks \
    -H "Content-Type: application/json" \
    -d '{"title":"Write the capstone README"}'
{
  "done": false,
  "id": 1,
  "title": "Write the capstone README"
}

$ curl -s -X POST http://127.0.0.1:5000/api/tasks \
    -H "Content-Type: application/json" \
    -d '{"title":"Review pull request"}'
{
  "done": false,
  "id": 2,
  "title": "Review pull request"
}

$ curl -s http://127.0.0.1:5000/api/tasks/1
{
  "done": false,
  "id": 1,
  "title": "Write the capstone README"
}

$ curl -s -w "\nHTTP_STATUS:%{http_code}\n" http://127.0.0.1:5000/api/tasks/999
{
  "error": "not found"
}
HTTP_STATUS:404

$ curl -s -X PATCH http://127.0.0.1:5000/api/tasks/1 \
    -H "Content-Type: application/json" -d '{"done":true}'
{
  "done": true,
  "id": 1,
  "title": "Write the capstone README"
}

$ curl -s -w "\nHTTP_STATUS:%{http_code}\n" -X POST http://127.0.0.1:5000/api/tasks \
    -H "Content-Type: application/json" -d '{}'
{
  "error": "title is required"
}
HTTP_STATUS:400

$ curl -s -X DELETE http://127.0.0.1:5000/api/tasks/2
{
  "deleted": 2
}

$ curl -s http://127.0.0.1:5000/api/tasks
{
  "tasks": [
    {
      "done": true,
      "id": 1,
      "title": "Write the capstone README"
    }
  ]
}
```

Then the server was stopped (`Ctrl-C` / `pkill`) and restarted fresh:

```
$ (server stopped, process confirmed gone via `ps aux | grep app.py`)

$ python3 app.py
 * Running on http://127.0.0.1:5000

$ curl -s http://127.0.0.1:5000/api/tasks
{
  "tasks": [
    {
      "done": true,
      "id": 1,
      "title": "Write the capstone README"
    }
  ]
}
```

Same task, same `done: true` state, after a full process restart —
that's the real `tasks.db` file on disk doing its job.

## Running the tests

```bash
pytest -v
```

Real captured output from this repo:

```
collected 14 items

test_app.py::test_list_tasks_happy_path_empty PASSED                     [  7%]
test_app.py::test_list_tasks_happy_path_after_create PASSED              [ 14%]
test_app.py::test_list_tasks_filter_by_done_status PASSED                [ 21%]
test_app.py::test_get_task_happy_path PASSED                             [ 28%]
test_app.py::test_get_task_nonexistent_id_returns_404 PASSED             [ 35%]
test_app.py::test_create_task_happy_path PASSED                          [ 42%]
test_app.py::test_create_task_missing_title_returns_400 PASSED           [ 50%]
test_app.py::test_create_task_empty_title_returns_400 PASSED             [ 57%]
test_app.py::test_update_task_happy_path PASSED                          [ 64%]
test_app.py::test_update_task_nonexistent_id_returns_404 PASSED          [ 71%]
test_app.py::test_update_task_missing_done_field_returns_400 PASSED      [ 78%]
test_app.py::test_delete_task_happy_path PASSED                          [ 85%]
test_app.py::test_delete_task_nonexistent_id_returns_404 PASSED          [ 92%]
test_app.py::test_data_persists_across_requests_on_same_app PASSED       [100%]

============================== 14 passed in 2.58s ==============================
```

Every endpoint has a happy-path test and at least one error-case test
(404 for a nonexistent id, 400 for a missing/empty title, 400 for a
missing `done` field on update). The list endpoint has no natural 4xx
case in this design, so it's instead covered for both the empty-result
and filtered-result happy paths.

I also deliberately broke `POST /api/tasks` (changed its success status
code from `201` to `200`) and re-ran `pytest -v`: exactly one test
failed —

```
FAILED test_app.py::test_create_task_happy_path - assert 200 == 201
1 failed, 13 passed in 7.05s
```

— then reverted the change and confirmed all 14 tests passed again.
That's the self-assessment checklist's "watch a test actually fail"
step, done for real, not skipped.

**Test database isolation, verified for real:** before running
`pytest`, `tasks.db`'s mtime, size, and md5 hash were recorded and its
one row (`id=1, done=1`) read back. After running the full test suite,
all three were identical and the row was unchanged — the test suite
never opened, wrote to, or created `tasks.db`. No `test_tasks.db` file
appears on disk either, confirming the `:memory:` strategy leaves
nothing behind.

## Linting

```bash
ruff check .
```

Real output: `All checks passed!`

## CI

This project lives inside the `python-for-everyone` monorepo, and
GitHub Actions only discovers workflow files at a repo's actual root
`.github/workflows/` directory — not in subfolders. So this project's
CI workflow lives at the repo root,
[`.github/workflows/capstone-1-task-api-ci.yml`](../../.github/workflows/capstone-1-task-api-ci.yml),
scoped to this folder with a `paths:` filter (only triggers on changes
under `capstones/capstone-1-task-api/`) and a `working-directory:
capstones/capstone-1-task-api` default so every step runs relative to
this project, not the repo root. If you fork just this folder out into
its own standalone repo, move that workflow file to `.github/workflows/ci.yml`
at your new repo's root and drop the `paths:` filter and
`working-directory` setting — they won't be needed once this is the
only project in the repo.

It runs two jobs on every `push` and `pull_request` to `main` that
touches this folder, following Chapter 30's pattern:

- **lint** — installs `requirements-dev.txt`, runs `ruff check .`
- **test** — installs `requirements-dev.txt`, runs `pytest -v` across a
  Python 3.11 / 3.12 matrix

Both jobs were verified to run these exact commands successfully
locally first (see above) before being wired into the workflow, and the
workflow file itself was parsed with `yaml.safe_load()` to confirm it's
valid YAML with `lint` and `test` jobs and `push`/`pull_request`
triggers on `main`.

"Green" on this workflow means: `ruff check .` reports zero violations,
and every endpoint's happy path plus at least one error case passes
against a fresh `:memory:` database on both supported Python versions.

## Project layout

```
capstone-1-task-api/
├── app.py                       # Flask app factory + routes + plain logic functions
├── db.py                        # sqlite3 connection + init_db()
├── test_app.py                  # pytest suite (Flask test client, :memory: db)
├── requirements-dev.txt         # flask, pytest, ruff
├── pyproject.toml               # ruff config
└── .gitignore                   # excludes tasks.db, .venv, caches
```

(CI workflow lives at the repo root — see the CI section above.)
