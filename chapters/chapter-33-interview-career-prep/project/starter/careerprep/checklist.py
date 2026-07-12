"""
careerprep.checklist -- portfolio-readiness checklist and directory scanner.

TODO chapter 33: fill in scan_directory() below. Some checklist items are
objectively checkable by looking at real files on disk (does a README
exist and is it non-trivial, is there a dependencies file, do tests exist,
is there a .gitignore). Others are judgment calls a script can't verify
honestly (does the README explain WHY, not just WHAT; are there no
hardcoded secrets) -- those stay manual self-assessment items this module
tracks and prints, but never marks pass/fail on its own.
"""

import logging
from pathlib import Path

logger = logging.getLogger(__name__)

MIN_README_CHARS = 200

DEPENDENCY_FILENAMES = ("requirements.txt", "pyproject.toml")
README_FILENAMES = ("README.md", "readme.md", "Readme.md", "README.MD")

# Each item: key (used to look up an auto-scan result), label (shown to
# the learner), auto (True = scan_directory can check this for real,
# False = the learner must self-assess it honestly). Provided for you --
# no TODOs on this list itself.
CHECKLIST_ITEMS = [
    {"key": "readme_substantial", "label": "README.md exists and is a non-trivial length (not a one-line placeholder)", "auto": True},
    {"key": "dependencies_declared", "label": "requirements.txt or pyproject.toml declares dependencies", "auto": True},
    {"key": "tests_exist", "label": "At least one test file exists (tests/ folder or test_*.py / *_test.py)", "auto": True},
    {"key": "gitignore_exists", "label": ".gitignore exists", "auto": True},
    {"key": "readme_explains_why", "label": "README explains WHY the project exists, not just WHAT it does", "auto": False},
    {"key": "no_hardcoded_secrets", "label": "No hardcoded secrets or API keys anywhere in the codebase", "auto": False},
    {"key": "limitations_section", "label": "An honest 'Limitations' or 'Known Issues' section exists somewhere", "auto": False},
    {"key": "tests_exercise_real_logic", "label": "Tests actually exercise real logic, not just placeholder asserts", "auto": False},
    {"key": "meaningful_commits", "label": "Commit history shows incremental progress, not one giant commit", "auto": False},
]


class CareerPrepError(Exception):
    """Raised for any user-facing checklist error (bad path, etc.)."""


def _find_file(directory: Path, filenames: tuple[str, ...]) -> Path | None:
    for name in filenames:
        candidate = directory / name
        if candidate.is_file():
            return candidate
    return None


def _is_substantial(file_path: Path) -> bool:
    try:
        text = file_path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return False
    return len(text.strip()) >= MIN_README_CHARS


def _has_tests(directory: Path) -> bool:
    tests_dir = directory / "tests"
    if tests_dir.is_dir() and any(tests_dir.rglob("*.py")):
        return True
    for pattern in ("test_*.py", "*_test.py"):
        if any(directory.rglob(pattern)):
            return True
    return False


def scan_directory(target: Path) -> dict[str, bool]:
    """
    Run the objectively-checkable "auto" items against a real directory.

    Returns a dict of {key: True/False} for every item marked auto=True
    in CHECKLIST_ITEMS. Manual items are not included here -- see
    manual_items() for those.
    """
    # TODO 11: if `target` doesn't exist, raise CareerPrepError
    #   ("No such directory: ..."). If it exists but isn't a directory,
    #   raise CareerPrepError ("Not a directory: ...").

    # TODO 12: find the README with _find_file(target, README_FILENAMES)
    #   (already written for you above). Build and return a results
    #   dict with these four keys, each computed for real against
    #   `target`:
    #     "readme_substantial"    -> README found AND _is_substantial(it)
    #     "dependencies_declared" -> any file in DEPENDENCY_FILENAMES
    #                                 exists directly under target
    #     "tests_exist"           -> _has_tests(target)
    #     "gitignore_exists"      -> target / ".gitignore" is a file
    #   Log an info message summarizing how many of the 4 passed before
    #   returning.

    raise NotImplementedError("scan_directory: fill in TODOs 11-12")


def auto_items() -> list[dict]:
    return [item for item in CHECKLIST_ITEMS if item["auto"]]


def manual_items() -> list[dict]:
    return [item for item in CHECKLIST_ITEMS if not item["auto"]]
