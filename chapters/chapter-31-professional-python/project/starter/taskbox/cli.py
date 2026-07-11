"""
taskbox.cli -- the argparse entry point.

TODO chapter 31: build the argparse parser and wire it up to the
functions in core.py. This module should only handle parsing argv,
configuring logging, and printing results -- no task logic here.

Run it with:  python3 -m taskbox.cli --help
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
    # TODO 15: add a top-level --file option (type=Path,
    #   default=DEFAULT_TASKS_FILE) so every subcommand can be pointed
    #   at a different tasks file -- this is also what makes the tool
    #   testable without touching the learner's real ~/.taskbox file.

    # TODO 16: add a top-level -v/--verbose flag (action="store_true")
    #   that raises the log level to DEBUG.

    subparsers = parser.add_subparsers(dest="command", required=True)

    # TODO 17: add an "add" subparser with:
    #   - a required positional "title" argument
    #   - an optional --priority argument, choices=["low","normal","high"],
    #     default="normal"

    # TODO 18: add a "list" subparser with:
    #   - an --all flag (action="store_true") to include completed tasks
    #   - an optional --priority filter, same choices as above, default None

    # TODO 19: add a "done" subparser with one required positional
    #   "id" argument, type=int.

    # TODO 20: add a "delete" subparser with one required positional
    #   "id" argument, type=int.

    return parser


def configure_logging(verbose: bool) -> None:
    """
    Configure the taskbox logger only -- deliberately NOT the root logger.

    TODO 21: create a logging.StreamHandler, give it a
    logging.Formatter("%(levelname)s: %(message)s"), attach it to the
    module-level `logger`, set the logger's level to DEBUG if verbose
    else INFO, and set logger.propagate = False.

    Why not logging.basicConfig()? That configures the ROOT logger,
    which every imported library's logger also flows into by default --
    so --verbose would flood the terminal with debug output from every
    dependency this tool imports, not just taskbox's own messages.
    Attaching a handler to the "taskbox" logger by name keeps --verbose
    scoped to this tool.
    """
    raise NotImplementedError("configure_logging: fill in TODO 21")


def _print_task(task: dict) -> None:
    status = "x" if task["done"] else " "
    print(f"[{status}] #{task['id']} ({task['priority']}) {task['title']}")


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    configure_logging(args.verbose)

    # TODO 22: wrap everything below in try/except TaskboxError. On
    #   TaskboxError, log the error message with logger.error(str(exc))
    #   and return 1 instead of letting the exception crash the program
    #   with a raw traceback.

    if args.command == "add":
        # TODO 23: call add_task(args.file, args.title, args.priority)
        #   and print "Added task #<id>: <title>"
        pass

    elif args.command == "list":
        # TODO 24: call list_tasks(args.file, show_done=args.all,
        #   priority=args.priority). If empty, print "No tasks found.".
        #   Otherwise print each task with _print_task (already written
        #   for you).
        pass

    elif args.command == "done":
        # TODO 25: call complete_task(args.file, args.id) and print
        #   "Marked done: #<id> <title>"
        pass

    elif args.command == "delete":
        # TODO 26: call delete_task(args.file, args.id) and print
        #   "Deleted: #<id> <title>"
        pass

    return 0


if __name__ == "__main__":
    sys.exit(main())
