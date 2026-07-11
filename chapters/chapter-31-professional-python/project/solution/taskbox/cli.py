"""
taskbox.cli -- the argparse entry point.

This module's only job is: parse sys.argv, configure logging, call into
core.py, and turn the result (or a TaskboxError) into clear terminal
output. No task-management logic lives here -- that split is what makes
core.py testable and reusable without a terminal attached.
"""

import argparse
import logging
import sys
from pathlib import Path

from taskbox.core import (
    DEFAULT_TASKS_FILE,
    TaskboxError,
    add_task,
    complete_task,
    delete_task,
    list_tasks,
)

logger = logging.getLogger("taskbox")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="taskbox",
        description="A small command-line task manager backed by a JSON file.",
    )
    parser.add_argument(
        "--file",
        type=Path,
        default=DEFAULT_TASKS_FILE,
        help=f"path to the tasks JSON file (default: {DEFAULT_TASKS_FILE})",
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="show debug-level logging (task file paths, filtering details, etc.)",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="add a new task")
    add_parser.add_argument("title", help="the task's title (required, positional)")
    add_parser.add_argument(
        "--priority",
        choices=["low", "normal", "high"],
        default="normal",
        help="task priority (default: normal)",
    )

    list_parser = subparsers.add_parser("list", help="list tasks")
    list_parser.add_argument(
        "--all", action="store_true",
        help="include already-completed tasks (default: only show pending)",
    )
    list_parser.add_argument(
        "--priority",
        choices=["low", "normal", "high"],
        default=None,
        help="only show tasks with this priority",
    )

    done_parser = subparsers.add_parser("done", help="mark a task complete")
    done_parser.add_argument("id", type=int, help="the task's numeric id")

    delete_parser = subparsers.add_parser("delete", help="delete a task")
    delete_parser.add_argument("id", type=int, help="the task's numeric id")

    return parser


def configure_logging(verbose: bool) -> None:
    """
    Configure the taskbox logger only -- deliberately NOT the root logger.

    logging.basicConfig() configures the root logger, which every
    imported library's logger also flows into by default. Doing that
    here would mean --verbose floods the terminal with debug output
    from every dependency this tool ever imports, not just taskbox's
    own messages. Attaching a handler to the "taskbox" logger by name
    keeps --verbose scoped to this tool's own log calls.
    """
    level = logging.DEBUG if verbose else logging.INFO
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))
    logger.addHandler(handler)
    logger.setLevel(level)
    logger.propagate = False


def _print_task(task: dict) -> None:
    status = "x" if task["done"] else " "
    print(f"[{status}] #{task['id']} ({task['priority']}) {task['title']}")


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    configure_logging(args.verbose)

    try:
        if args.command == "add":
            task = add_task(args.file, args.title, args.priority)
            print(f"Added task #{task['id']}: {task['title']}")

        elif args.command == "list":
            tasks = list_tasks(args.file, show_done=args.all, priority=args.priority)
            if not tasks:
                print("No tasks found.")
            else:
                for task in tasks:
                    _print_task(task)

        elif args.command == "done":
            task = complete_task(args.file, args.id)
            print(f"Marked done: #{task['id']} {task['title']}")

        elif args.command == "delete":
            task = delete_task(args.file, args.id)
            print(f"Deleted: #{task['id']} {task['title']}")

    except TaskboxError as exc:
        logger.error(str(exc))
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
