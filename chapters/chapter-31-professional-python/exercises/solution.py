"""
Chapter 31 Exercises: Professional Python -- reference solution.
Run this from inside the exercises/ folder: python3 solution.py

Every function here was actually run and verified, including every
argparse call via an explicit args list (no stdin needed).
"""

import argparse
import logging


# TODO 1
def make_logger(name, level=logging.INFO):
    logger = logging.getLogger(name)
    logger.setLevel(level)
    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))
        logger.addHandler(handler)
    return logger


# TODO 2
def safe_divide(logger, a, b):
    if b == 0:
        logger.error("Attempted division by zero: %s / %s", a, b)
        return None
    result = a / b
    logger.info("Divided %s / %s = %s", a, b, result)
    return result


# TODO 3
def build_greet_parser():
    parser = argparse.ArgumentParser(prog="greet", description="Greet someone by name.")
    parser.add_argument("name", help="the person's name")
    parser.add_argument("-g", "--greeting", default="Hello", help="greeting word (default: Hello)")
    parser.add_argument("-n", "--times", type=int, default=1, help="how many times to repeat (default: 1)")
    return parser


# TODO 4
def build_greeting(args):
    return "\n".join(f"{args.greeting}, {args.name}!" for _ in range(args.times))


# TODO 5
def build_task_parser():
    parser = argparse.ArgumentParser(prog="taskcli", description="Manage a simple task list.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="add a new task")
    add_parser.add_argument("description", help="what the task is")

    list_parser = subparsers.add_parser("list", help="list tasks")
    list_parser.add_argument("--all", action="store_true", help="include completed tasks")

    return parser


# TODO 6 (Debug the Code)
#
# The bug: the HANDLER's level was set to logging.CRITICAL, which is
# stricter than the logger's own WARNING level. A message has to pass
# BOTH the logger's level check AND every handler's own level check --
# whichever is stricter wins. Fix: set the handler's level to
# logging.WARNING (matching the logger), not CRITICAL.
def fixed_logger_setup():
    logger = logging.getLogger("fixed")
    logger.setLevel(logging.WARNING)
    handler = logging.StreamHandler()
    handler.setLevel(logging.WARNING)  # fixed: was logging.CRITICAL
    logger.addHandler(handler)
    return logger


if __name__ == "__main__":
    logger = make_logger("demo")
    print(safe_divide(logger, 10, 2))
    print(safe_divide(logger, 5, 0))

    greet_parser = build_greet_parser()
    args = greet_parser.parse_args(["Ada", "--greeting", "Hi", "--times", "2"])
    print(build_greeting(args))

    task_parser = build_task_parser()
    task_args = task_parser.parse_args(["add", "Ship v1.0"])
    print(task_args)

    fixed = fixed_logger_setup()
    fixed.info("this should NOT print (below WARNING)")
    fixed.warning("this SHOULD print (fix confirmed)")
