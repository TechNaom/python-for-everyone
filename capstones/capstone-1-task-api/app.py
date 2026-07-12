"""
Capstone 1: Full-Stack Task API -- Flask version.

This is Chapter 22's Flask solution turned into something you could
actually deploy: the in-memory TASKS dict is gone, replaced by real
sqlite3 persistence through db.py. The "thin route, plain function
underneath" shape from Chapter 22 is kept on purpose -- every route below
is a few lines that parse the request and call a plain `_..._data()`
function, and every one of those plain functions is what test_app.py
calls directly or indirectly through Flask's test client.

Run it for real:
    pip install -r requirements-dev.txt
    python3 app.py
    # visit http://localhost:5000/api/tasks
"""

from flask import Flask, jsonify, request

from db import get_connection, init_db


def create_app(db_path="tasks.db"):
    """Application factory.

    Taking db_path as a parameter (instead of hardcoding "tasks.db") is
    what lets test_app.py hand this function ":memory:" and get a Flask
    app wired to a completely separate, throwaway database -- see the
    README's "test isolation strategy" section.
    """
    app = Flask(__name__)

    conn = get_connection(db_path)
    init_db(conn)
    app.config["DB_CONN"] = conn

    # --- Plain functions holding each route's real logic. Every one
    # takes the connection explicitly rather than reaching for a global,
    # so they're easy to call directly in tests without going through
    # HTTP at all if you ever want to. ---

    def _list_tasks_data(done=None):
        if done is None:
            rows = conn.execute("SELECT id, title, done FROM tasks ORDER BY id").fetchall()
        else:
            rows = conn.execute(
                "SELECT id, title, done FROM tasks WHERE done = ? ORDER BY id",
                (1 if done else 0,),
            ).fetchall()
        return [_row_to_task(row) for row in rows]

    def _get_task_data(task_id):
        row = conn.execute(
            "SELECT id, title, done FROM tasks WHERE id = ?", (task_id,)
        ).fetchone()
        return _row_to_task(row) if row else None

    def _add_task_data(title):
        cursor = conn.execute(
            "INSERT INTO tasks (title, done) VALUES (?, ?)", (title, 0)
        )
        conn.commit()
        return _get_task_data(cursor.lastrowid)

    def _update_task_data(task_id, done):
        if _get_task_data(task_id) is None:
            return None
        conn.execute(
            "UPDATE tasks SET done = ? WHERE id = ?", (1 if done else 0, task_id)
        )
        conn.commit()
        return _get_task_data(task_id)

    def _delete_task_data(task_id):
        cursor = conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        conn.commit()
        return cursor.rowcount > 0

    # --- Real Flask routes. Each one is a thin wrapper: read the
    # request, call a plain function above, shape the response. ---

    @app.route("/api/tasks", methods=["GET"])
    def api_list_tasks():
        done_param = request.args.get("done")
        done = None
        if done_param is not None:
            done = done_param.lower() == "true"
        return jsonify({"tasks": _list_tasks_data(done=done)})

    @app.route("/api/tasks/<int:task_id>", methods=["GET"])
    def api_get_task(task_id):
        task = _get_task_data(task_id)
        if task is None:
            return jsonify({"error": "not found"}), 404
        return jsonify(task)

    @app.route("/api/tasks", methods=["POST"])
    def api_create_task():
        data = request.get_json(silent=True) or {}
        title = data.get("title", "")
        if not isinstance(title, str) or not title.strip():
            return jsonify({"error": "title is required"}), 400
        task = _add_task_data(title.strip())
        return jsonify(task), 201

    @app.route("/api/tasks/<int:task_id>", methods=["PATCH"])
    def api_update_task(task_id):
        data = request.get_json(silent=True) or {}
        if "done" not in data or not isinstance(data["done"], bool):
            return jsonify({"error": "done (boolean) is required"}), 400
        task = _update_task_data(task_id, data["done"])
        if task is None:
            return jsonify({"error": "not found"}), 404
        return jsonify(task)

    @app.route("/api/tasks/<int:task_id>", methods=["DELETE"])
    def api_delete_task(task_id):
        deleted = _delete_task_data(task_id)
        if not deleted:
            return jsonify({"error": "not found"}), 404
        return jsonify({"deleted": task_id})

    return app


def _row_to_task(row):
    return {"id": row["id"], "title": row["title"], "done": bool(row["done"])}


if __name__ == "__main__":
    app = create_app("tasks.db")
    app.run(debug=True)
