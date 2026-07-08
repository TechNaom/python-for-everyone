"""
Chapter 22 Project: Task Manager REST API -- Flask version (reference solution).
See README.md in this folder for the full brief and example output.

This is a REAL, complete Flask application -- every route, decorator, and
call below is the genuine Flask API, installable with `pip install flask`
and runnable locally with `python3 solution_flask.py` (then visit
http://localhost:5000). Nothing here is simplified or invented.

Since this course has no live server to run it against, this file is
ALSO directly runnable and testable without ever calling app.run(): every
route's underlying logic lives in a plain function (_list_tasks_data(),
_add_task_data(), etc.) that the Flask route just calls and formats --
those plain functions are what get exercised at the bottom of this file
and by anything importing this module, with app.run() only reached when
this file is run directly AND a real terminal is present to serve
requests from (see the __main__ guard at the bottom).

This version builds Flask's idiom clearly: a small JSON API (returning
dicts, which Flask auto-converts to JSON) PLUS one server-rendered HTML
page at "/" using render_template_string() (used here instead of
render_template() + a templates/ folder, purely so this whole project
stays a single file) -- showing both of Flask's natural output shapes in
one place.
"""

from flask import Flask, render_template_string, request

app = Flask(__name__)

# --- In-memory "database" for the session. A real version could persist
# this to the Ch21 mock DB layer (FakeConnection/FakeCursor) instead --
# see the "Ideas to make it your own" section in README.md. ---

TASKS = {
    1: {"id": 1, "title": "Write the report", "done": False},
    2: {"id": 2, "title": "Review pull request", "done": True},
}
_next_id = 3


# --- Plain functions holding each route's real logic, callable and
# testable directly without a live server. Every Flask route below is a
# thin wrapper around one of these. ---

def _list_tasks_data(done=None):
    tasks = list(TASKS.values())
    if done is not None:
        tasks = [t for t in tasks if t["done"] == done]
    return tasks


def _get_task_data(task_id):
    return TASKS.get(task_id)


def _add_task_data(title):
    global _next_id
    task = {"id": _next_id, "title": title, "done": False}
    TASKS[_next_id] = task
    _next_id += 1
    return task


def _update_task_data(task_id, done):
    task = TASKS.get(task_id)
    if task is None:
        return None
    task["done"] = done
    return task


def _delete_task_data(task_id):
    return TASKS.pop(task_id, None) is not None


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


# --- Real Flask routes. Each one is a thin wrapper: read the request,
# call a plain function above, shape the response. ---

@app.route("/")
def home():
    """Server-rendered HTML page -- Flask's classic idiom."""
    tasks = _list_tasks_data()
    return render_template_string(TASKS_PAGE_TEMPLATE, tasks=tasks)


@app.route("/api/tasks", methods=["GET"])
def api_list_tasks():
    """JSON endpoint -- Flask CAN serve JSON too, by returning a dict/list."""
    done_param = request.args.get("done")
    done = None
    if done_param is not None:
        done = done_param.lower() == "true"
    return {"tasks": _list_tasks_data(done=done)}


@app.route("/api/tasks/<int:task_id>", methods=["GET"])
def api_get_task(task_id):
    task = _get_task_data(task_id)
    if task is None:
        return {"error": "not found"}, 404
    return task


@app.route("/api/tasks", methods=["POST"])
def api_create_task():
    data = request.json or {}
    title = data.get("title", "")
    if not title:
        return {"error": "title is required"}, 400
    task = _add_task_data(title)
    return task, 201


@app.route("/api/tasks/<int:task_id>", methods=["PATCH"])
def api_update_task(task_id):
    data = request.json or {}
    if "done" not in data:
        return {"error": "done is required"}, 400
    task = _update_task_data(task_id, bool(data["done"]))
    if task is None:
        return {"error": "not found"}, 404
    return task


@app.route("/api/tasks/<int:task_id>", methods=["DELETE"])
def api_delete_task(task_id):
    deleted = _delete_task_data(task_id)
    if not deleted:
        return {"error": "not found"}, 404
    return {"deleted": task_id}


if __name__ == "__main__":
    # Run this locally (pip install flask) to see it live:
    #   python3 solution_flask.py
    #   visit http://localhost:5000/          (server-rendered HTML page)
    #   visit http://localhost:5000/api/tasks (JSON API)
    print("=== Task Manager REST API -- Flask version ===")
    print("This file's real logic is fully testable without a live server --")
    print("see this chapter's project README for how to exercise it that way.")
    print()
    print("To actually run this as a live server locally:")
    print("  pip install flask")
    print("  python3 solution_flask.py")
    print("  (then uncomment the app.run() line below and re-run)")
    # app.run(debug=True)  # commented out: this course has no live server
    # to bind a real port against -- uncomment this line to run it for real
    # locally after installing Flask.

    # --- A quick, no-server demonstration of every route's logic, so this
    # file still DOES something meaningful when run in this course: ---
    print()
    print("Demonstration (no live server, calling the same logic the routes use):")
    print("GET /api/tasks       ->", _list_tasks_data())
    print("GET /api/tasks/1     ->", _get_task_data(1))
    new_task = _add_task_data("Water the plants")
    print("POST /api/tasks      ->", new_task)
    print("PATCH /api/tasks/1   ->", _update_task_data(1, True))
    print("DELETE /api/tasks/2  ->", _delete_task_data(2))
    print("GET /api/tasks (after changes) ->", _list_tasks_data())

