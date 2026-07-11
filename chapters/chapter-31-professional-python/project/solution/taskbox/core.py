"""
taskbox.core -- the actual task-management logic.

Deliberately kept separate from cli.py: this module knows nothing about
argparse, sys.argv, or printing to a terminal. It reads/writes a JSON
file and raises plain Python exceptions on bad input. That separation
means core.py could be reused by a future GUI, a web API, or a test
suite without dragging any command-line concerns along with it.
"""

import json
import logging
from datetime import datetime, timezone
from pathlib import Path

logger = logging.getLogger(__name__)

DEFAULT_TASKS_FILE = Path.home() / ".taskbox" / "tasks.json"


class TaskboxError(Exception):
    """Raised for any user-facing task error (bad id, corrupt file, etc.)."""


def _now_iso():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def load_tasks(tasks_file: Path) -> list[dict]:
    """Load the task list from disk. Returns [] if the file doesn't exist yet."""
    if not tasks_file.exists():
        logger.debug("Tasks file %s does not exist yet -- starting empty", tasks_file)
        return []

    logger.debug("Loading tasks from %s", tasks_file)
    try:
        raw = tasks_file.read_text(encoding="utf-8")
    except OSError as exc:
        raise TaskboxError(f"Could not read tasks file {tasks_file}: {exc}") from exc

    if not raw.strip():
        return []

    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise TaskboxError(
            f"Tasks file {tasks_file} is not valid JSON (corrupted?): {exc}"
        ) from exc

    if not isinstance(data, list):
        raise TaskboxError(f"Tasks file {tasks_file} does not contain a JSON list.")

    return data


def save_tasks(tasks_file: Path, tasks: list[dict]) -> None:
    """Write the task list back to disk, creating the parent folder if needed."""
    logger.debug("Saving %d task(s) to %s", len(tasks), tasks_file)
    tasks_file.parent.mkdir(parents=True, exist_ok=True)
    try:
        tasks_file.write_text(json.dumps(tasks, indent=2) + "\n", encoding="utf-8")
    except OSError as exc:
        raise TaskboxError(f"Could not write tasks file {tasks_file}: {exc}") from exc


def add_task(tasks_file: Path, title: str, priority: str = "normal") -> dict:
    """Add a new task and persist it. Returns the created task dict."""
    title = title.strip()
    if not title:
        raise TaskboxError("Task title cannot be empty.")

    valid_priorities = {"low", "normal", "high"}
    if priority not in valid_priorities:
        raise TaskboxError(
            f"Invalid priority {priority!r}. Choose from: {', '.join(sorted(valid_priorities))}."
        )

    tasks = load_tasks(tasks_file)
    next_id = (max((t["id"] for t in tasks), default=0)) + 1
    task = {
        "id": next_id,
        "title": title,
        "priority": priority,
        "done": False,
        "created_at": _now_iso(),
        "completed_at": None,
    }
    tasks.append(task)
    save_tasks(tasks_file, tasks)
    logger.info("Added task #%d: %s", next_id, title)
    return task


def list_tasks(tasks_file: Path, show_done: bool = True, priority: str | None = None) -> list[dict]:
    """Return tasks, optionally filtered by completion state and/or priority."""
    tasks = load_tasks(tasks_file)
    if not show_done:
        tasks = [t for t in tasks if not t["done"]]
    if priority is not None:
        tasks = [t for t in tasks if t["priority"] == priority]
    logger.debug("Listing %d task(s) (show_done=%s, priority=%s)", len(tasks), show_done, priority)
    return tasks


def _find_task(tasks: list[dict], task_id: int) -> dict:
    for t in tasks:
        if t["id"] == task_id:
            return t
    raise TaskboxError(f"No task with id {task_id}.")


def complete_task(tasks_file: Path, task_id: int) -> dict:
    """Mark a task done. Returns the updated task dict."""
    tasks = load_tasks(tasks_file)
    task = _find_task(tasks, task_id)
    if task["done"]:
        logger.warning("Task #%d was already marked done", task_id)
    task["done"] = True
    task["completed_at"] = _now_iso()
    save_tasks(tasks_file, tasks)
    logger.info("Marked task #%d done: %s", task_id, task["title"])
    return task


def delete_task(tasks_file: Path, task_id: int) -> dict:
    """Delete a task by id. Returns the removed task dict."""
    tasks = load_tasks(tasks_file)
    task = _find_task(tasks, task_id)
    tasks = [t for t in tasks if t["id"] != task_id]
    save_tasks(tasks_file, tasks)
    logger.info("Deleted task #%d: %s", task_id, task["title"])
    return task
