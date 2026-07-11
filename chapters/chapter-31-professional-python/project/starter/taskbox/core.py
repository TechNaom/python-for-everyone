"""
taskbox.core -- the actual task-management logic.

TODO chapter 31: fill in the functions below. Keep this module free of
argparse/sys.argv/print() -- it should only know how to read/write the
JSON file and raise TaskboxError on bad input. cli.py (the other file)
is where terminal-facing concerns like printing belong.

Run `python3 -m taskbox.cli --help` from this folder as you go to test
each piece as you finish it.
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
    # TODO 1: if tasks_file doesn't exist, log a debug message
    #   ("Tasks file ... does not exist yet -- starting empty") and
    #   return an empty list -- this is the normal "first run" case,
    #   not an error.

    # TODO 2: read the file's text. Wrap the read in try/except OSError
    #   and raise TaskboxError with a clear message if it fails.

    # TODO 3: if the file is empty/blank, return [].

    # TODO 4: json.loads() the text. Wrap it in try/except
    #   json.JSONDecodeError and raise TaskboxError with a clear
    #   "not valid JSON (corrupted?)" message -- don't let a raw
    #   JSONDecodeError traceback reach the user.

    # TODO 5: if the parsed data isn't a list, raise TaskboxError too
    #   (a tasks file should always be a JSON list of task dicts).

    raise NotImplementedError("load_tasks: fill in TODOs 1-5")


def save_tasks(tasks_file: Path, tasks: list[dict]) -> None:
    """Write the task list back to disk, creating the parent folder if needed."""
    # TODO 6: log a debug message with how many tasks are being saved
    #   and to which path.

    # TODO 7: create tasks_file's parent folder if it doesn't exist yet
    #   (tasks_file.parent.mkdir(parents=True, exist_ok=True)).

    # TODO 8: write the JSON (use json.dumps(tasks, indent=2)) to
    #   tasks_file. Wrap it in try/except OSError and raise
    #   TaskboxError on failure.

    raise NotImplementedError("save_tasks: fill in TODOs 6-8")


def add_task(tasks_file: Path, title: str, priority: str = "normal") -> dict:
    """Add a new task and persist it. Returns the created task dict."""
    # TODO 9: strip() the title and raise TaskboxError if it's empty
    #   after stripping.

    # TODO 10: validate priority is one of {"low", "normal", "high"};
    #   raise TaskboxError with a clear message listing the valid
    #   choices if not.

    # TODO 11: load existing tasks, compute the next id (1 higher than
    #   the current max id, or 1 if there are no tasks yet), build a
    #   task dict with keys: id, title, priority, done (False),
    #   created_at (_now_iso()), completed_at (None). Append it, save,
    #   log an info message, and return the new task dict.

    raise NotImplementedError("add_task: fill in TODOs 9-11")


def list_tasks(tasks_file: Path, show_done: bool = True, priority: str | None = None) -> list[dict]:
    """Return tasks, optionally filtered by completion state and/or priority."""
    # TODO 12: load tasks. If show_done is False, filter out tasks
    #   where task["done"] is True. If priority is not None, filter to
    #   only tasks matching that priority. Log a debug message with the
    #   resulting count, then return the filtered list.

    raise NotImplementedError("list_tasks: fill in TODO 12")


def _find_task(tasks: list[dict], task_id: int) -> dict:
    for t in tasks:
        if t["id"] == task_id:
            return t
    raise TaskboxError(f"No task with id {task_id}.")


def complete_task(tasks_file: Path, task_id: int) -> dict:
    """Mark a task done. Returns the updated task dict."""
    # TODO 13: load tasks, find the task with _find_task (already
    #   written above for you -- it raises TaskboxError if not found).
    #   If it's already done, log a warning (not an error -- it's not
    #   fatal). Set done=True and completed_at=_now_iso(), save, log an
    #   info message, and return the task.

    raise NotImplementedError("complete_task: fill in TODO 13")


def delete_task(tasks_file: Path, task_id: int) -> dict:
    """Delete a task by id. Returns the removed task dict."""
    # TODO 14: load tasks, find the task with _find_task (raises
    #   TaskboxError if missing), rebuild the list without that task's
    #   id, save, log an info message, and return the removed task.

    raise NotImplementedError("delete_task: fill in TODO 14")
