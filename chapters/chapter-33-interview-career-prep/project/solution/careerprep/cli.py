"""
careerprep.cli -- the argparse entry point.

This module's only job is: parse sys.argv, configure logging, collect
terminal input (input() for typed answers), call into interview.py /
checklist.py, and turn the result (or a CareerPrepError) into clear
terminal output. No question-bank or scanning logic lives here.
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
    parser.add_argument(
        "--file",
        type=Path,
        default=DEFAULT_ANSWERS_FILE,
        help=f"path to the saved-answers JSON file (default: {DEFAULT_ANSWERS_FILE})",
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="show debug-level logging (file paths, filtering details, etc.)",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    # -- interview subcommands --------------------------------------
    interview_parser = subparsers.add_parser("interview", help="mock-interview drill tool")
    interview_sub = interview_parser.add_subparsers(dest="interview_command", required=True)

    list_parser = interview_sub.add_parser("list", help="list all questions")
    list_parser.add_argument(
        "--category", choices=["behavioral", "technical"], default=None,
        help="only list questions in this category",
    )

    random_parser = interview_sub.add_parser("random", help="answer one random question")
    random_parser.add_argument(
        "--category", choices=["behavioral", "technical"], default=None,
        help="only pick from this category",
    )

    review_parser = interview_sub.add_parser("review", help="show previously saved answers")
    review_parser.add_argument(
        "--category", choices=["behavioral", "technical"], default=None,
        help="only show answers in this category",
    )
    review_parser.add_argument(
        "--question-id", type=int, default=None,
        help="only show answers to this specific question id",
    )

    # -- checklist subcommands ----------------------------------------
    checklist_parser = subparsers.add_parser("checklist", help="portfolio-readiness checklist")
    checklist_sub = checklist_parser.add_subparsers(dest="checklist_command", required=True)

    checklist_sub.add_parser("list", help="print the full checklist (auto + manual items)")

    scan_parser = checklist_sub.add_parser("scan", help="scan a real directory and auto-check what's checkable")
    scan_parser.add_argument("path", type=Path, help="path to the project directory to scan")

    return parser


def configure_logging(verbose: bool) -> None:
    """
    Configure the careerprep logger only -- deliberately NOT the root
    logger. logging.basicConfig() configures the root logger, which every
    imported library's logger also flows into by default, so --verbose
    would flood the terminal with debug output from every dependency this
    tool imports, not just careerprep's own messages.
    """
    level = logging.DEBUG if verbose else logging.INFO
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))
    logger.addHandler(handler)
    logger.setLevel(level)
    logger.propagate = False


def read_multiline_answer() -> str:
    """
    Collect a typed/pasted answer from the terminal. Reads lines until a
    blank line is entered (or stdin closes), then joins them with newlines
    -- this lets a learner write a real multi-paragraph STAR-method answer
    instead of being limited to one line.
    """
    print("(Type or paste your answer. Press Enter on a blank line when you're done.)")
    lines: list[str] = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        if line == "" and lines:
            break
        if line == "" and not lines:
            continue
        lines.append(line)
    return "\n".join(lines)


def _print_question(question: dict) -> None:
    print(f"#{question['id']} [{question['category']}] {question['text']}")


def _run_interview(args: argparse.Namespace) -> int:
    if args.interview_command == "list":
        questions = get_questions(args.category)
        if not questions:
            print("No questions found.")
        else:
            for question in questions:
                _print_question(question)

    elif args.interview_command == "random":
        question = pick_random_question(args.category)
        print("=" * 60)
        _print_question(question)
        print("=" * 60)
        answer_text = read_multiline_answer()
        entry = record_answer(args.file, question, answer_text)
        print(f"Saved your answer for question #{entry['question_id']} at {entry['answered_at']}.")

    elif args.interview_command == "review":
        answers = get_review(args.file, category=args.category, question_id=args.question_id)
        if not answers:
            print("No saved answers found.")
        else:
            for i, entry in enumerate(answers, start=1):
                print(f"--- Answer {i} of {len(answers)} ---")
                print(f"[{entry['answered_at']}] #{entry['question_id']} ({entry['category']}) {entry['question_text']}")
                print(textwrap.indent(entry["answer"], "  "))
                print()

    return 0


def _run_checklist(args: argparse.Namespace) -> int:
    if args.checklist_command == "list":
        print("Auto-checkable items (run `checklist scan <path>` to verify these for real):")
        for item in auto_items():
            print(f"  [ ] {item['label']}")
        print()
        print("Manual self-assessment items (use your own honest judgment):")
        for item in manual_items():
            print(f"  [ ] {item['label']}")

    elif args.checklist_command == "scan":
        results = scan_directory(args.path)
        print(f"Scanning {args.path} ...")
        print()
        print("Auto-checked (verified against real files on disk):")
        for item in auto_items():
            passed = results.get(item["key"], False)
            mark = "x" if passed else " "
            print(f"  [{mark}] {item['label']}")
        print()
        print("Manual self-assessment (not scannable -- be honest with yourself):")
        for item in manual_items():
            print(f"  [ ] {item['label']}")

    return 0


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    configure_logging(args.verbose)

    try:
        if args.command == "interview":
            return _run_interview(args)
        elif args.command == "checklist":
            return _run_checklist(args)
    except (InterviewError, ChecklistError) as exc:
        logger.error(str(exc))
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
