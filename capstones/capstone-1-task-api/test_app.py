"""
test_app.py -- pytest suite for the Task API.

Test isolation strategy: every test gets a brand-new Flask app wired to
an in-memory sqlite3 database (":memory:") via the `client` fixture
below. Flask's app.test_client() drives real HTTP-shaped requests
in-process (no server needs to be running), and because create_app()
opens a fresh ":memory:" connection per app instance, no test can ever
see data left behind by another test -- and none of this ever touches
the real tasks.db file that `python3 app.py` writes to. See the
README's "Test isolation strategy" section for the fuller explanation of
why ":memory:" was chosen over a throwaway file.

Follows the AAA pattern (Arrange, Act, Assert) from Chapter 27.
"""

import pytest

from app import create_app


@pytest.fixture
def client():
    """Arrange: a fresh app + fresh in-memory database for every test."""
    app = create_app(":memory:")
    app.testing = True
    return app.test_client()


def _create(client, title="Write the report"):
    return client.post("/api/tasks", json={"title": title})


# --- GET /api/tasks (list) -----------------------------------------------


def test_list_tasks_happy_path_empty(client):
    resp = client.get("/api/tasks")
    assert resp.status_code == 200
    assert resp.get_json() == {"tasks": []}


def test_list_tasks_happy_path_after_create(client):
    _create(client, "Task A")
    _create(client, "Task B")

    resp = client.get("/api/tasks")

    assert resp.status_code == 200
    titles = [t["title"] for t in resp.get_json()["tasks"]]
    assert titles == ["Task A", "Task B"]


def test_list_tasks_filter_by_done_status(client):
    # There's no invalid input for a plain GET /api/tasks -- the closest
    # thing to an "error case" for list is the ?done= filter matching
    # nothing, which should still be a valid 200 with an empty list, not
    # an error. Covering that behavior here instead of a 4xx.
    _create(client, "Pending task")

    resp = client.get("/api/tasks?done=true")

    assert resp.status_code == 200
    assert resp.get_json() == {"tasks": []}


# --- GET /api/tasks/<id> --------------------------------------------------


def test_get_task_happy_path(client):
    created = _create(client, "Water the plants").get_json()

    resp = client.get(f"/api/tasks/{created['id']}")

    assert resp.status_code == 200
    assert resp.get_json() == created


def test_get_task_nonexistent_id_returns_404(client):
    resp = client.get("/api/tasks/999")

    assert resp.status_code == 404
    assert resp.get_json() == {"error": "not found"}


# --- POST /api/tasks (create) --------------------------------------------


def test_create_task_happy_path(client):
    resp = _create(client, "Buy groceries")

    assert resp.status_code == 201
    body = resp.get_json()
    assert body["title"] == "Buy groceries"
    assert body["done"] is False
    assert isinstance(body["id"], int)


def test_create_task_missing_title_returns_400(client):
    resp = client.post("/api/tasks", json={})

    assert resp.status_code == 400
    assert resp.get_json() == {"error": "title is required"}


def test_create_task_empty_title_returns_400(client):
    resp = client.post("/api/tasks", json={"title": "   "})

    assert resp.status_code == 400
    assert resp.get_json() == {"error": "title is required"}


# --- PATCH /api/tasks/<id> (update done status) --------------------------


def test_update_task_happy_path(client):
    created = _create(client, "Review pull request").get_json()

    resp = client.patch(f"/api/tasks/{created['id']}", json={"done": True})

    assert resp.status_code == 200
    assert resp.get_json()["done"] is True


def test_update_task_nonexistent_id_returns_404(client):
    resp = client.patch("/api/tasks/999", json={"done": True})

    assert resp.status_code == 404
    assert resp.get_json() == {"error": "not found"}


def test_update_task_missing_done_field_returns_400(client):
    created = _create(client, "Needs a done flag").get_json()

    resp = client.patch(f"/api/tasks/{created['id']}", json={})

    assert resp.status_code == 400
    assert resp.get_json() == {"error": "done (boolean) is required"}


# --- DELETE /api/tasks/<id> -----------------------------------------------


def test_delete_task_happy_path(client):
    created = _create(client, "Temporary task").get_json()

    resp = client.delete(f"/api/tasks/{created['id']}")

    assert resp.status_code == 200
    assert resp.get_json() == {"deleted": created["id"]}
    assert client.get(f"/api/tasks/{created['id']}").status_code == 404


def test_delete_task_nonexistent_id_returns_404(client):
    resp = client.delete("/api/tasks/999")

    assert resp.status_code == 404
    assert resp.get_json() == {"error": "not found"}


# --- Persistence sanity check ---------------------------------------------


def test_data_persists_across_requests_on_same_app(client):
    """Not a restart test (that's done manually, see README) -- just
    confirms the in-memory connection genuinely holds state across
    multiple requests within one app/test, the way a real file-backed
    connection would across multiple requests while the process is up."""
    created = _create(client, "Persisted task").get_json()

    first = client.get(f"/api/tasks/{created['id']}").get_json()
    second = client.get(f"/api/tasks/{created['id']}").get_json()

    assert first == second == created
