"""
careerprep.interview -- the mock-interview question bank and drill logic.

Deliberately kept separate from cli.py: this module knows nothing about
argparse, sys.argv, or terminal I/O beyond the input() calls needed to
capture a learner's typed answer. It reads/writes a JSON answers file and
raises plain Python exceptions on bad input -- the same "engine vs.
dashboard" split chapter 31's taskbox project used.
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


# 25 real questions spanning behavioral/STAR-method prompts and technical
# concepts drawn from across this course: Python fundamentals, OOP,
# testing, git, APIs, databases, debugging, memory, concurrency.
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
    if category is not None and category not in VALID_CATEGORIES:
        raise CareerPrepError(
            f"Invalid category {category!r}. Choose from: {', '.join(sorted(VALID_CATEGORIES))}."
        )
    questions = QUESTION_BANK
    if category is not None:
        questions = [q for q in questions if q["category"] == category]
    logger.debug("Returning %d question(s) (category=%s)", len(questions), category)
    return questions


def get_question_by_id(question_id: int) -> dict:
    for q in QUESTION_BANK:
        if q["id"] == question_id:
            return q
    raise CareerPrepError(f"No question with id {question_id}.")


def pick_random_question(category: str | None = None) -> dict:
    """Pick one random question, optionally restricted to a category."""
    questions = get_questions(category)
    if not questions:
        raise CareerPrepError(f"No questions available for category {category!r}.")
    question = random.choice(questions)
    logger.debug("Picked random question #%d (category=%s)", question["id"], question["category"])
    return question


def load_answers(answers_file: Path) -> list[dict]:
    """Load saved answers from disk. Returns [] if the file doesn't exist yet."""
    if not answers_file.exists():
        logger.debug("Answers file %s does not exist yet -- starting empty", answers_file)
        return []

    logger.debug("Loading answers from %s", answers_file)
    try:
        raw = answers_file.read_text(encoding="utf-8")
    except OSError as exc:
        raise CareerPrepError(f"Could not read answers file {answers_file}: {exc}") from exc

    if not raw.strip():
        return []

    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise CareerPrepError(
            f"Answers file {answers_file} is not valid JSON (corrupted?): {exc}"
        ) from exc

    if not isinstance(data, list):
        raise CareerPrepError(f"Answers file {answers_file} does not contain a JSON list.")

    return data


def save_answers(answers_file: Path, answers: list[dict]) -> None:
    """Write the full answers list back to disk, creating the parent folder if needed."""
    logger.debug("Saving %d answer(s) to %s", len(answers), answers_file)
    answers_file.parent.mkdir(parents=True, exist_ok=True)
    try:
        answers_file.write_text(json.dumps(answers, indent=2) + "\n", encoding="utf-8")
    except OSError as exc:
        raise CareerPrepError(f"Could not write answers file {answers_file}: {exc}") from exc


def record_answer(answers_file: Path, question: dict, answer_text: str) -> dict:
    """
    Append a new answer to the answers file (never overwrite past ones --
    each practice session should add to the learner's history, not erase
    it, so they can see how their answers evolve over time).
    """
    answer_text = answer_text.strip()
    if not answer_text:
        raise CareerPrepError("Answer cannot be empty.")

    answers = load_answers(answers_file)
    entry = {
        "question_id": question["id"],
        "category": question["category"],
        "question_text": question["text"],
        "answer": answer_text,
        "answered_at": _now_iso(),
    }
    answers.append(entry)
    save_answers(answers_file, answers)
    logger.info("Saved answer for question #%d (%s)", question["id"], question["category"])
    return entry


def get_review(
    answers_file: Path,
    category: str | None = None,
    question_id: int | None = None,
) -> list[dict]:
    """Return saved answers, optionally filtered by category and/or question id."""
    if category is not None and category not in VALID_CATEGORIES:
        raise CareerPrepError(
            f"Invalid category {category!r}. Choose from: {', '.join(sorted(VALID_CATEGORIES))}."
        )
    answers = load_answers(answers_file)
    if category is not None:
        answers = [a for a in answers if a["category"] == category]
    if question_id is not None:
        answers = [a for a in answers if a["question_id"] == question_id]
    logger.debug(
        "Returning %d saved answer(s) (category=%s, question_id=%s)",
        len(answers), category, question_id,
    )
    return answers
