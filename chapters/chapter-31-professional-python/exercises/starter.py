"""
Chapter 31 Exercises: Professional Python
See README.md in this folder for full instructions.
Run this from inside the exercises/ folder: python3 starter.py

Uses only the standard library -- no installs needed.
"""

import argparse
import logging


# TODO 1: Write make_logger(name, level=logging.INFO). Create and
# return a logger with logging.getLogger(name), set its level, and
# attach a single StreamHandler with formatter "%(levelname)s:
# %(message)s" -- but only add the handler if the logger doesn't
# already have one (check logger.handlers first), so calling this
# twice with the same name doesn't print every message twice.


# TODO 2: Write safe_divide(logger, a, b). If b is 0, log an error
# with logger.error(...) describing the attempted division and return
# None. Otherwise, compute the result, log it at INFO level with
# logger.info(...), and return it.


# TODO 3: Write build_greet_parser(). Return an argparse.ArgumentParser
# with prog="greet", one required positional argument "name", one
# optional argument -g/--greeting with default "Hello", and one
# optional argument -n/--times with type=int and default=1. Give every
# argument a help= string.


# TODO 4: Write build_greeting(args). Given a parsed argparse Namespace
# (from TODO 3's parser), return a string repeating "{greeting},
# {name}!" on its own line, args.times times, joined with newlines.


# TODO 5: Write build_task_parser(). Return an argparse.ArgumentParser
# with prog="taskcli" and two subcommands, using
# add_subparsers(dest="command", required=True):
#   - "add", with one required positional argument "description"
#   - "list", with one optional flag --all using action="store_true"


# TODO 6 (Debug the Code): this logger setup is supposed to print
# WARNING-level messages and above to the console, but it currently
# prints NOTHING no matter what level you log at. Find and fix the
# bug -- don't change the intended behavior (WARNING and up should
# still be the threshold), just fix what's broken.
def broken_logger_setup():
    logger = logging.getLogger("broken")
    logger.setLevel(logging.WARNING)
    handler = logging.StreamHandler()
    handler.setLevel(logging.CRITICAL)  # bug is somewhere in this function
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

    fixed = broken_logger_setup()
    fixed.warning("This should print once you've fixed TODO 6")
