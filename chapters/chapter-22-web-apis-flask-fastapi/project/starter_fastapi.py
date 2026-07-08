"""
Chapter 22 Project: Task Manager REST API -- FastAPI version.
See README.md in this folder for the full brief and example output.

Run this from inside this folder: python3 starter_fastapi.py
(Requires `pip install fastapi uvicorn` to actually import FastAPI -- but
every TODO below is testable by calling the plain _*_data() functions
directly, without ever needing a live uvicorn server.)
"""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Task Manager API", description="A small REST API for managing tasks, built with FastAPI.")


# TODO 1: Define a Pydantic model TaskCreate(BaseModel) with one required
# field: title: str.


# TODO 2: Define a Pydantic model TaskUpdate(BaseModel) with one required
# field: done: bool.


# TODO 3: Define a Pydantic model Task(BaseModel) with fields: id: int,
# title: str, done: bool = False.


TASKS = {
    1: {"id": 1, "title": "Write the report", "done": False},
    2: {"id": 2, "title": "Review pull request", "done": True},
}
_next_id = 3


# TODO 4: Write _list_tasks_data(done=None). Return a list of every dict
# in TASKS.values(); if done is not None, only return tasks whose "done"
# field equals done.


# TODO 5: Write _get_task_data(task_id). Return TASKS.get(task_id).


# TODO 6: Write _add_task_data(title). Create a new task dict
# {"id": _next_id, "title": title, "done": False}, store it in TASKS,
# increment the module-level _next_id (use `global _next_id`), and
# return the new task.


# TODO 7: Write _update_task_data(task_id, done). Look up the task in
# TASKS; if it exists, set its "done" field and return it; otherwise
# return None.


# TODO 8: Write _delete_task_data(task_id). Remove task_id from TASKS if
# present (TASKS.pop(task_id, None)) and return True if it was removed,
# False otherwise.


# TODO 9: Write the GET "/tasks" route (@app.get("/tasks")) named
# list_tasks(done: bool | None = None) -- done is a QUERY parameter since
# it has a default. Return {"tasks": _list_tasks_data(done=done)}.


# TODO 10: Write the GET "/tasks/{task_id}" route named
# get_task(task_id: int) -- task_id is a PATH parameter. Call
# _get_task_data(task_id); if None, return {"error": "not found"};
# otherwise return the task.


# TODO 11: Write the POST "/tasks" route named create_task(task:
# TaskCreate), with status_code=201 in the decorator
# (@app.post("/tasks", status_code=201)). Call
# _add_task_data(task.title) and return the result.


# TODO 12: Write the PATCH "/tasks/{task_id}" route named
# update_task(task_id: int, update: TaskUpdate). Call
# _update_task_data(task_id, update.done); if None, return
# {"error": "not found"}; otherwise return the updated task.


# TODO 13: Write the DELETE "/tasks/{task_id}" route named
# delete_task(task_id: int). Call _delete_task_data(task_id); if False,
# return {"error": "not found"}; otherwise return {"deleted": task_id}.


if __name__ == "__main__":
    print("=== Task Manager REST API -- FastAPI version ===")
    print("Demonstration (no live server, calling the same logic the routes use):")
    print("GET /tasks           ->", _list_tasks_data())
    print("GET /tasks/1         ->", _get_task_data(1))
    new_task = _add_task_data("Water the plants")
    print("POST /tasks          ->", new_task)
    print("PATCH /tasks/1       ->", _update_task_data(1, True))
    print("DELETE /tasks/2      ->", _delete_task_data(2))
    print("GET /tasks (after changes) ->", _list_tasks_data())
    print()
    print("To run this as a live server locally (pip install fastapi uvicorn):")
    print("  uvicorn starter_fastapi:app --reload")
    print("  then visit http://localhost:8000/docs")
