"""
careerprep.interview -- the mock-interview question bank and drill logic.

TODO chapter 33: fill in the functions below. Keep this module free of
argparse/sys.argv/print() beyond what's already here -- it should only
know how to read/write the JSON answers file and raise CareerPrepError on
bad input. cli.py (the other file) is where terminal-facing concerns like
printing and input() belong.

Run `python3 -m careerprep.cli --help` from this folder as you go to test
each piece as you finish it.
"""

import json
import logging
import random
from datetime import datetime, timezone
from pathlib import Path

logger = logging.getLogger(__name__)

DEFAULT_ANSWERS_FILE = Path.home() / ".careerprep" / "answers.json"

VALID_CATEGORIES = {"behavioral", "technical"}


class CareerPrepError(Exception):
    """Raised for any user-facing error (bad category, bad id, corrupt file, etc.)."""


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


# The question bank is provided for you -- at least 20 real questions
# spanning behavioral/STAR-method prompts and technical concepts from
# across this course. You don't need to edit this list; the TODOs below
# are about the functions that read and filter it.
QUESTION_BANK = [
    {"id": 1, "category": "behavioral", "text": "Tell me about a time you had to debug a difficult production issue. What was the situation, and how did you resolve it?"},
    {"id": 2, "category": "behavioral", "text": "Describe a time you disagreed with a teammate's code review feedback. How did you handle it?"},
    {"id": 3, "category": "behavioral", "text": "Tell me about a project where the requirements changed midway through. How did you adapt?"},
    {"id": 4, "category": "behavioral", "text": "Describe a time you had to learn a new technology quickly to finish a task."},
    {"id": 5, "category": "behavioral", "text": "Tell me about a time you made a mistake that reached production. What happened, and what did you do about it?"},
    {"id": 6, "category": "behavioral", "text": "Describe a time you had to explain a technical concept to a non-technical stakeholder."},
    {"id": 7, "category": "behavioral", "text": "Tell me about a time you had to prioritize between multiple competing deadlines."},
    {"id": 8, "category": "behavioral", "text": "Describe a time you received critical feedback on your code. How did you respond, and what changed afterward?"},
    {"id": 9, "category": "behavioral", "text": "Tell me about a time you hit a merge conflict working with Git on a team project. How did you resolve it?"},
    {"id": 10, "category": "behavioral", "text": "Describe a time you had to push back on a request or decision you disagreed with. How did you handle the conversation?"},
    {"id": 11, "category": "technical", "text": "What's the difference between a list and a tuple in Python, and when would you choose one over the other?"},
    {"id": 12, "category": "technical", "text": "Explain the difference between `==` and `is` in Python."},
    {"id": 13, "category": "technical", "text": "What is a Python decorator, and can you describe a real use case for one?"},
    {"id": 14, "category": "technical", "text": "Explain the difference between instance methods, class methods, and static methods in OOP."},
    {"id": 15, "category": "technical", "text": "What is method resolution order (MRO), and why does it matter for multiple inheritance?"},
    {"id": 16, "category": "technical", "text": "What's the difference between a unit test and an integration test, and when should you write each?"},
    {"id": 17, "category": "technical", "text": "What does `git rebase` do differently from `git merge`, and when would you reach for one over the other?"},
    {"id": 18, "category": "technical", "text": "Explain what a race condition is and how you'd avoid one in a multi-threaded Python program."},
    {"id": 19, "category": "technical", "text": "What's the difference between a REST API's GET and POST methods, and why does idempotency matter?"},
    {"id": 20, "category": "technical", "text": "How would you prevent SQL injection when building a database query from user input?"},
    {"id": 21, "category": "technical", "text": "What is a memory leak in Python, and how can reference cycles contribute to one despite garbage collection?"},
    {"id": 22, "category": "technical", "text": "Explain the difference between a shallow copy and a deep copy, and give an example where the distinction matters."},
    {"id": 23, "category": "technical", "text": "What's the purpose of a virtual environment, and what problem does it solve?"},
    {"id": 24, "category": "technical", "text": "How does Python's Global Interpreter Lock (GIL) affect multi-threaded CPU-bound code?"},
    {"id": 25, "category": "technical", "text": "What's the difference between a `@staticmethod` and a plain module-level function?"},
]


def get_questions(category: str | None = None) -> list[dict]:
    """Return the question bank, optionally filtered by category."""
    # TODO 1: if category is not None and not in VALID_CATEGORIES, raise
    #   CareerPrepError with a clear message listing the valid choices.

    # TODO 2: filter QUESTION_BANK to only questions matching `category`
    #   if one was given (otherwise return the whole bank). Log a debug
    #   message with the resulting count, then return the list.

    raise NotImplementedError("get_questions: fill in TODOs 1-2")


def get_question_by_id(question_id: int) -> dict:
    for q in QUESTION_BANK:
        if q["id"] == question_id:
            return q
    raise CareerPrepError(f"No question with id {question_id}.")


def pick_random_question(category: str | None = None) -> dict:
    """Pick one random question, optionally restricted to a category."""
    # TODO 3: call get_questions(category) to get the candidate list. If
    #   it's empty, raise CareerPrepError (no questions for that
    #   category). Otherwise use random.choice() to pick one, log a
    #   debug message with its id and category, and return it.

    raise NotImplementedError("pick_random_question: fill in TODO 3")


def load_answers(answers_file: Path) -> list[dict]:
    """Load saved answers from disk. Returns [] if the file doesn't exist yet."""
    # TODO 4: if answers_file doesn't exist, log a debug message
    #   ("Answers file ... does not exist yet -- starting empty") and
    #   return an empty list -- this is the normal "first run" case,
    #   not an error.

    # TODO 5: read the file's text. Wrap the read in try/except OSError
    #   and raise CareerPrepError with a clear message if it fails.

    # TODO 6: if the file is empty/blank, return [].

    # TODO 7: json.loads() the text. Wrap it in try/except
    #   json.JSONDecodeError and raise CareerPrepError with a clear
    #   "not valid JSON (corrupted?)" message -- don't let a raw
    #   JSONDecodeError traceback reach the user. Also raise
    #   CareerPrepError if the parsed data isn't a list.

    raise NotImplementedError("load_answers: fill in TODOs 4-7")


def save_answers(answers_file: Path, answers: list[dict]) -> None:
    """Write the full answers list back to disk, creating the parent folder if needed."""
    # TODO 8: log a debug message with how many answers are being
    #   saved and to which path. Create answers_file's parent folder if
    #   it doesn't exist yet (answers_file.parent.mkdir(parents=True,
    #   exist_ok=True)). Write the JSON (json.dumps(answers, indent=2))
    #   to answers_file. Wrap the write in try/except OSError and raise
    #   CareerPrepError on failure.

    raise NotImplementedError("save_answers: fill in TODO 8")


def record_answer(answers_file: Path, question: dict, answer_text: str) -> dict:
    """
    Append a new answer to the answers file (never overwrite past ones --
    each practice session should add to the learner's history, not erase
    it, so they can see how their answers evolve over time).
    """
    # TODO 9: strip() answer_text and raise CareerPrepError if it's
    #   empty after stripping. Load the existing answers with
    #   load_answers, build a new entry dict with keys: question_id,
    #   category, question_text (all pulled from `question`), answer
    #   (the stripped text), and answered_at (_now_iso()). APPEND the
    #   new entry to the loaded list -- do NOT replace or overwrite the
    #   existing answers, every past practice session must stay in the
    #   file. Save the full list with save_answers, log an info message,
    #   and return the new entry.

    raise NotImplementedError("record_answer: fill in TODO 9")


def get_review(
    answers_file: Path,
    category: str | None = None,
    question_id: int | None = None,
) -> list[dict]:
    """Return saved answers, optionally filtered by category and/or question id."""
    # TODO 10: if category is not None and not in VALID_CATEGORIES, raise
    #   CareerPrepError. Load the saved answers with load_answers. If
    #   category is not None, filter to answers matching it. If
    #   question_id is not None, filter to answers matching it. Log a
    #   debug message with the resulting count and filters, then return
    #   the filtered list.

    raise NotImplementedError("get_review: fill in TODO 10")
