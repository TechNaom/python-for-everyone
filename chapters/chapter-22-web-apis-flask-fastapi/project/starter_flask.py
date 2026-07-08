"""
Chapter 22 Project: Task Manager REST API -- Flask version.
See README.md in this folder for the full brief and example output.

Run this from inside this folder: python3 starter_flask.py
(Requires `pip install flask` to actually import Flask -- but every TODO
below is testable by calling the plain _*_data() functions directly,
without ever needing app.run() or a live server.)
"""

from flask import Flask, render_template_string, request

app = Flask(__name__)

TASKS = {
    1: {"id": 1, "title": "Write the report", "done": False},
    2: {"id": 2, "title": "Review pull request", "done": True},
}
_next_id = 3


# TODO 1: Write _list_tasks_data(done=None). Return a list of every dict
# in TASKS.values(); if done is not None, only return tasks whose "done"
# field equals done.


# TODO 2: Write _get_task_data(task_id). Return TASKS.get(task_id).


# TODO 3: Write _add_task_data(title). Create a new task dict
# {"id": _next_id, "title": title, "done": False}, store it in TASKS,
# increment the module-level _next_id (use `global _next_id`), and
# return the new task.


# TODO 4: Write _update_task_data(task_id, done). Look up the task in
# TASKS; if it exists, set its "done" field and return it; otherwise
# return None.


# TODO 5: Write _delete_task_data(task_id). Remove task_id from TASKS if
# present (TASKS.pop(task_id, None)) and return True if it was removed,
# False otherwise.


TASKS_PAGE_TEMPLATE = """
<!doctype html>
<title>Tasks</title>
<h1>Task Manager (Flask, server-rendered)</h1>
<ul>
{% for task in tasks %}
  <li>#{{ task.id }} {{ task.title }} -- {{ "Done" if task.done else "Pending" }}</li>
{% endfor %}
</ul>
"""


# TODO 6: Write the "/" route (@app.route("/")) named home(). Get every
# task with _list_tasks_data(), then return
# render_template_string(TASKS_PAGE_TEMPLATE, tasks=tasks).


# TODO 7: Write the "/api/tasks" GET route (@app.route("/api/tasks",
# methods=["GET"])) named api_list_tasks(). Read an optional "done"
# query parameter from request.args (a string "true"/"false" or missing),
# convert it to a real bool or None, call _list_tasks_data(done=...), and
# return {"tasks": <the list>}.


# TODO 8: Write the "/api/tasks/<int:task_id>" GET route named
# api_get_task(task_id). Call _get_task_data(task_id); if None, return
# ({"error": "not found"}, 404); otherwise return the task.


# TODO 9: Write the "/api/tasks" POST route named api_create_task(). Read
# request.json (or {} if None), get "title"; if missing/empty, return
# ({"error": "title is required"}, 400); otherwise call
# _add_task_data(title) and return (task, 201).


# TODO 10: Write the "/api/tasks/<int:task_id>" PATCH route named
# api_update_task(task_id). Read request.json (or {}); if "done" isn't a
# key, return ({"error": "done is required"}, 400); otherwise call
# _update_task_data(task_id, bool(data["done"])); if None, return
# ({"error": "not found"}, 404); otherwise return the updated task.


# TODO 11: Write the "/api/tasks/<int:task_id>" DELETE route named
# api_delete_task(task_id). Call _delete_task_data(task_id); if it
# returns False, return ({"error": "not found"}, 404); otherwise return
# {"deleted": task_id}.


if __name__ == "__main__":
    print("=== Task Manager REST API -- Flask version ===")
    print("Demonstration (no live server, calling the same logic the routes use):")
    print("GET /api/tasks       ->", _list_tasks_data())
    print("GET /api/tasks/1     ->", _get_task_data(1))
    new_task = _add_task_data("Water the plants")
    print("POST /api/tasks      ->", new_task)
    print("PATCH /api/tasks/1   ->", _update_task_data(1, True))
    print("DELETE /api/tasks/2  ->", _delete_task_data(2))
    print("GET /api/tasks (after changes) ->", _list_tasks_data())
    print()
    print("To run this as a live server locally (pip install flask):")
    print("  uncomment the app.run() line below, then: python3 starter_flask.py")
    # app.run(debug=True)
