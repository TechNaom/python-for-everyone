"""
Chapter 22 Project: Task Manager REST API -- FastAPI version (reference solution).
See README.md in this folder for the full brief and example output.

This is a REAL, complete FastAPI application -- every decorator, Pydantic
model, and call below is the genuine FastAPI/Pydantic API, installable
with `pip install fastapi uvicorn` and runnable locally with
`uvicorn solution_fastapi:app --reload` (then visit
http://localhost:8000/docs for the automatic interactive docs). Nothing
here is simplified or invented.

Since this course has no live server to run it against, this file is
ALSO directly runnable and testable without ever starting uvicorn: every
route's underlying logic lives in a plain function (_list_tasks_data(),
_add_task_data(), etc.) that the FastAPI route just calls and formats --
those plain functions are what get exercised at the bottom of this file.

Unlike the Flask version, this is built as a pure typed JSON API -- no
HTML page at all -- matching FastAPI's idiom and Sub-topic 7's point
that a JSON API is meant to be consumed by something else (a frontend,
mobile app, or script), not displayed directly.
"""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Task Manager API", description="A small REST API for managing tasks, built with FastAPI.")


# --- Pydantic models: these describe the exact shape of request/response
# data, and FastAPI uses them to validate requests AND generate /docs
# automatically -- no separate validation code or documentation needed. ---

class TaskCreate(BaseModel):
    title: str


class TaskUpdate(BaseModel):
    done: bool


class Task(BaseModel):
    id: int
    title: str
    done: bool = False


# --- In-memory "database" for the session. A real version could persist
# this to the Ch21 mock DB layer (FakeConnection/FakeCursor) instead --
# see the "Ideas to make it your own" section in README.md. ---

TASKS: dict[int, Task] = {
    1: Task(id=1, title="Write the report", done=False),
    2: Task(id=2, title="Review pull request", done=True),
}
_next_id = 3


# --- Plain functions holding each route's real logic, callable and
# testable directly without a live server. Every FastAPI route below is a
# thin wrapper around one of these. ---

def _list_tasks_data(done=None):
    tasks = list(TASKS.values())
    if done is not None:
        tasks = [t for t in tasks if t.done == done]
    return tasks


def _get_task_data(task_id):
    return TASKS.get(task_id)


def _add_task_data(title):
    global _next_id
    task = Task(id=_next_id, title=title, done=False)
    TASKS[_next_id] = task
    _next_id += 1
    return task


def _update_task_data(task_id, done):
    task = TASKS.get(task_id)
    if task is None:
        return None
    task.done = done
    return task


def _delete_task_data(task_id):
    return TASKS.pop(task_id, None) is not None


# --- Real FastAPI routes. Path/query params and Pydantic models are
# handled automatically -- validation and /docs both come from these
# same type-hinted signatures, with no extra code required. ---

@app.get("/tasks")
def list_tasks(done: bool | None = None):
    """done is a QUERY parameter (?done=true) since it has a default value."""
    return {"tasks": _list_tasks_data(done=done)}


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    """task_id is a PATH parameter, auto-converted to int by its type hint."""
    task = _get_task_data(task_id)
    if task is None:
        return {"error": "not found"}
    return task


@app.post("/tasks", status_code=201)
def create_task(task: TaskCreate):
    """FastAPI validates the request body against TaskCreate automatically
    before this function ever runs -- a missing "title" never reaches here."""
    created = _add_task_data(task.title)
    return created


@app.patch("/tasks/{task_id}")
def update_task(task_id: int, update: TaskUpdate):
    task = _update_task_data(task_id, update.done)
    if task is None:
        return {"error": "not found"}
    return task


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    deleted = _delete_task_data(task_id)
    if not deleted:
        return {"error": "not found"}
    return {"deleted": task_id}


if __name__ == "__main__":
    # Run this locally (pip install fastapi uvicorn) to see it live:
    #   uvicorn solution_fastapi:app --reload
    #   visit http://localhost:8000/docs (automatic interactive docs)
    #   visit http://localhost:8000/tasks (the JSON API itself)
    print("=== Task Manager REST API -- FastAPI version ===")
    print("This file's real logic is fully testable without a live server --")
    print("see this chapter's project README for how to exercise it that way.")
    print()
    print("To actually run this as a live server locally:")
    print("  pip install fastapi uvicorn")
    print("  uvicorn solution_fastapi:app --reload")
    # import uvicorn
    # uvicorn.run(app, host="127.0.0.1", port=8000)  # commented out: this
    # course has no live server to bind a real port against -- uncomment
    # this (and the import above) to run it for real locally after
    # installing fastapi and uvicorn.

    # --- A quick, no-server demonstration of every route's logic, so this
    # file still DOES something meaningful when run in this course: ---
    print()
    print("Demonstration (no live server, calling the same logic the routes use):")
    print("GET /tasks           ->", _list_tasks_data())
    print("GET /tasks/1         ->", _get_task_data(1))
    new_task = _add_task_data("Water the plants")
    print("POST /tasks          ->", new_task)
    print("PATCH /tasks/1       ->", _update_task_data(1, True))
    print("DELETE /tasks/2      ->", _delete_task_data(2))
    print("GET /tasks (after changes) ->", _list_tasks_data())
