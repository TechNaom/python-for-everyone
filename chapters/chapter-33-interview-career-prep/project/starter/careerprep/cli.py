"""
careerprep.cli -- the argparse entry point.

TODO chapter 33: build the argparse parser and wire it up to the
functions in interview.py / checklist.py. This module should only handle
parsing argv, configuring logging, collecting terminal input, and
printing results -- no question-bank or scanning logic here.

Run it with:  python3 -m careerprep.cli --help
"""

import argparse
import logging
import sys
import textwrap
from pathlib import Path

from careerprep.checklist import (
    CareerPrepError as ChecklistError,
    auto_items,
    manual_items,
    scan_directory,
)
from careerprep.interview import (
    CareerPrepError as InterviewError,
    DEFAULT_ANSWERS_FILE,
    get_questions,
    get_review,
    pick_random_question,
    record_answer,
)

logger = logging.getLogger("careerprep")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="careerprep",
        description="A mock-interview drill tool and portfolio-readiness checklist scanner.",
    )
    # TODO 11: add a top-level --file option (type=Path,
    #   default=DEFAULT_ANSWERS_FILE) so interview commands can be
    #   pointed at a different answers file -- this is also what makes
    #   the tool testable without touching the learner's real
    #   ~/.careerprep file.

    # TODO 12: add a top-level -v/--verbose flag (action="store_true")
    #   that raises the log level to DEBUG.

    subparsers = parser.add_subparsers(dest="command", required=True)

    # -- interview subcommands --------------------------------------
    interview_parser = subparsers.add_parser("interview", help="mock-interview drill tool")
    interview_sub = interview_parser.add_subparsers(dest="interview_command", required=True)

    # TODO 13: add an "list" subparser under interview_sub with one
    #   optional --category argument, choices=["behavioral","technical"],
    #   default=None.

    # TODO 14: add a "random" subparser under interview_sub with the same
    #   optional --category argument as TODO 13.

    # TODO 15: add a "review" subparser under interview_sub with an
    #   optional --category argument (same choices as above) AND an
    #   optional --question-id argument (type=int, default=None).

    # -- checklist subcommands ----------------------------------------
    checklist_parser = subparsers.add_parser("checklist", help="portfolio-readiness checklist")
    checklist_sub = checklist_parser.add_subparsers(dest="checklist_command", required=True)

    # TODO 16: add a "list" subparser under checklist_sub (no extra
    #   arguments -- it just prints the full checklist).

    # TODO 17: add a "scan" subparser under checklist_sub with one
    #   required positional "path" argument, type=Path.

    return parser


def configure_logging(verbose: bool) -> None:
    """
    Configure the careerprep logger only -- deliberately NOT the root
    logger.

    TODO 18: create a logging.StreamHandler, give it a
    logging.Formatter("%(levelname)s: %(message)s"), attach it to the
    module-level `logger`, set the logger's level to DEBUG if verbose
    else INFO, and set logger.propagate = False.

    Why not logging.basicConfig()? That configures the ROOT logger,
    which every imported library's logger also flows into by default --
    so --verbose would flood the terminal with debug output from every
    dependency this tool imports, not just careerprep's own messages.
    Attaching a handler to the "careerprep" logger by name keeps
    --verbose scoped to this tool.
    """
    raise NotImplementedError("configure_logging: fill in TODO 18")


def read_multiline_answer() -> str:
    """
    Collect a typed/pasted answer from the terminal. Reads lines until a
    blank line is entered (or stdin closes), then joins them with newlines
    -- this lets a learner write a real multi-paragraph STAR-method answer
    instead of being limited to one line.
    """
    print("(Type or paste your answer. Press Enter on a blank line when you're done.)")
    # TODO 19: build up a list of lines by calling input() in a loop.
    #   Catch EOFError and break out of the loop when it's raised (stdin
    #   closed). If a line is "" and you already have at least one line
    #   collected, treat that as "the learner is done" and break. If a
    #   line is "" and you have nothing collected yet, skip it (don't
    #   append an empty first line) and keep looping. Otherwise append
    #   the line. After the loop, return "\n".join(lines).

    raise NotImplementedError("read_multiline_answer: fill in TODO 19")


def _print_question(question: dict) -> None:
    print(f"#{question['id']} [{question['category']}] {question['text']}")


def _run_interview(args: argparse.Namespace) -> int:
    if args.interview_command == "list":
        # TODO 20: call get_questions(args.category). If empty, print
        #   "No questions found.". Otherwise print each question with
        #   _print_question (already written for you).
        pass

    elif args.interview_command == "random":
        # TODO 21: call pick_random_question(args.category) to get one
        #   question. Print a "=" * 60 divider line, then the question
        #   with _print_question, then another divider. Call
        #   read_multiline_answer() to collect the learner's answer, then
        #   record_answer(args.file, question, answer_text) to save it.
        #   Print a confirmation message including the saved entry's
        #   question_id and answered_at.
        pass

    elif args.interview_command == "review":
        # TODO 22: call get_review(args.file, category=args.category,
        #   question_id=args.question_id). If empty, print "No saved
        #   answers found.". Otherwise, for each saved answer (numbered
        #   starting at 1), print a "--- Answer N of TOTAL ---" header, a
        #   line with the timestamp/id/category/question text, and the
        #   answer text indented (textwrap.indent(entry["answer"], "  ")
        #   is already imported for you via the textwrap module).
        pass

    return 0


def _run_checklist(args: argparse.Namespace) -> int:
    if args.checklist_command == "list":
        # TODO 23: print "Auto-checkable items ...", then a "[ ] label"
        #   line for each item from auto_items(). Then print "Manual
        #   self-assessment items ...", then a "[ ] label" line for each
        #   item from manual_items().
        pass

    elif args.checklist_command == "scan":
        # TODO 24: call scan_directory(args.path) to get the results
        #   dict. Print a header line showing what's being scanned. For
        #   each item in auto_items(), look up whether it passed in the
        #   results dict and print "[x] label" or "[ ] label"
        #   accordingly. Then print the manual_items() the same way
        #   TODO 23 did (always unchecked -- these are never auto-scored).
        pass

    return 0


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    configure_logging(args.verbose)

    # TODO 25: wrap the dispatch below in try/except (InterviewError,
    #   ChecklistError). On a caught error, log the error message with
    #   logger.error(str(exc)) and return 1 instead of letting the
    #   exception crash the program with a raw traceback.

    if args.command == "interview":
        return _run_interview(args)
    elif args.command == "checklist":
        return _run_checklist(args)

    return 0


if __name__ == "__main__":
    sys.exit(main())
