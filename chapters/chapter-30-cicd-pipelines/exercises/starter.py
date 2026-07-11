"""
Chapter 30 Exercises: CI/CD Pipelines
See README.md in this folder for full instructions.
Run this from inside the exercises/ folder: python3 starter.py

This script builds a real scratch scenario on disk -- a tiny sample
project with its own .github/workflows/ folder -- and then walks
through the same kind of checks a real CI workflow performs, using
Python's `yaml` module (pyyaml) to parse and validate workflow YAML,
exactly like a maintainer reviewing a workflow file by hand would.

It does NOT actually run the workflow on GitHub (that needs a real
repo and a real push) -- instead it validates the YAML the same way
you'd sanity-check it locally before ever pushing: does it parse? does
it have the required top-level keys? does every job have runs-on and
steps? This is the exact kind of check worth doing before trusting a
workflow file at all.

Uses only the standard library plus `pyyaml` (`pip install pyyaml` if
you don't already have it -- it's a very common, lightweight package).
"""

import shutil
from pathlib import Path

import yaml

EXERCISE_DIR = Path(__file__).parent
SCENARIO_DIR = EXERCISE_DIR / "scenario"


# ---------------------------------------------------------------------------
# Part 1: build a small sample project with a real, VALID workflow file.
# ---------------------------------------------------------------------------

VALID_WORKFLOW = """\
name: Lint and Test

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  lint-and-test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ["3.10", "3.11", "3.12"]
    steps:
      - name: Check out the repository
        uses: actions/checkout@v4

      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}
          cache: "pip"

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
          pip install ruff pytest

      - name: Lint with ruff
        run: ruff check .

      - name: Run tests with pytest
        run: pytest
"""

# This one LOOKS similar but has a real, intentional bug: `steps` is
# indented as a sibling of `runs-on` instead of nested under the job,
# and the job is missing `runs-on` entirely -- a workflow GitHub would
# reject at parse/schema time. This is Task 4's Debug the Code file.
BROKEN_WORKFLOW = """\
name: Lint and Test (broken)

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  lint-and-test:
    steps:
      - name: Check out the repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
          pip install ruff pytest

      - name: Lint with ruff
        run: ruff check .

      - name: Run tests with pytest
        run: pytest
"""


def build_scenario():
    """
    Builds a real scratch scenario on disk:

      scenario/sample_project/
        requirements.txt
        app.py
        test_app.py
        .github/workflows/ci.yml           <- VALID_WORKFLOW
        .github/workflows/ci-broken.yml    <- BROKEN_WORKFLOW (Task 4)

    Nothing here is pushed to GitHub -- this is a local stand-in so you
    can practice reading and validating workflow YAML for real, the
    same way you'd sanity-check a file before committing it.
    """
    if SCENARIO_DIR.exists():
        shutil.rmtree(SCENARIO_DIR)
    project = SCENARIO_DIR / "sample_project"
    workflows = project / ".github" / "workflows"
    workflows.mkdir(parents=True)

    (project / "requirements.txt").write_text("requests==2.31.0\n")
    (project / "app.py").write_text(
        "def add(a, b):\n"
        "    return a + b\n\n\n"
        "def divide(a, b):\n"
        "    return a / b\n"
    )
    (project / "test_app.py").write_text(
        "from app import add, divide\n\n\n"
        "def test_add():\n"
        "    assert add(2, 3) == 5\n\n\n"
        "def test_divide():\n"
        "    assert divide(10, 2) == 5\n"
    )

    (workflows / "ci.yml").write_text(VALID_WORKFLOW)
    (workflows / "ci-broken.yml").write_text(BROKEN_WORKFLOW)

    print(f"Scenario built at: {SCENARIO_DIR}")
    print()
    print("You now have:")
    print(f"  {project}")
    print("    requirements.txt, app.py, test_app.py")
    print("    .github/workflows/ci.yml         <- a real, valid workflow")
    print("    .github/workflows/ci-broken.yml  <- Task 4's broken workflow")
    print()
    print("Work through README.md's tasks using the functions below.")


# ---------------------------------------------------------------------------
# Part 2: validation helpers -- fill these in (or study them if you're
# using this file mainly to check your own answers against solution.py).
# ---------------------------------------------------------------------------

REQUIRED_JOB_KEYS = {"runs-on", "steps"}


def load_workflow(path):
    """
    Parse a workflow YAML file with yaml.safe_load() and return the
    resulting dict. Raises yaml.YAMLError if the file isn't valid YAML
    at all (a syntax error, bad indentation, etc.).
    """
    with open(path) as f:
        return yaml.safe_load(f)


def validate_workflow_structure(workflow):
    """
    TODO 1: Given a parsed workflow dict (from load_workflow), check
    that it has the required top-level structure a real GitHub Actions
    workflow needs, and return a list of problem strings (empty list =
    valid). Check for:

      - a truthy "on" key present (note: PyYAML's YAML 1.1 parser reads
        the bare key `on:` as the boolean True, not the string "on" --
        so check for either "on" OR True as a key)
      - a "jobs" key present, and it must be a non-empty dict
      - every job in "jobs" must itself be a dict containing BOTH
        "runs-on" and "steps" (use REQUIRED_JOB_KEYS above)
      - every job's "steps" must be a non-empty list

    Return the list of problems found, e.g.:
      ["job 'lint-and-test' is missing required key: runs-on"]
    An empty list means the workflow structure is valid.
    """
    problems = []
    # your code here
    return problems


def validate_workflow_file(path):
    """
    TODO 2: Combine load_workflow() and validate_workflow_structure()
    into one convenience function. Return a tuple:
      (is_valid: bool, problems: list[str])

    If the file isn't even valid YAML (yaml.safe_load raises), catch
    the exception and return (False, ["not valid YAML: <error>"])
    instead of letting the exception crash the script.
    """
    # your code here
    pass


# ---------------------------------------------------------------------------
# TODO 3: Run validate_workflow_file() against BOTH workflow files in
# scenario/sample_project/.github/workflows/ and print the result for
# each -- ci.yml should come back valid, ci-broken.yml should not.
# ---------------------------------------------------------------------------

# TODO 4 (Debug the Code): open scenario/sample_project/.github/workflows/
# ci-broken.yml directly and read it carefully against Sub-topic 2 of the
# lesson (workflow structure: on / jobs / each job needs runs-on + steps).
# Find the structural bug BEFORE running your validator against it, then
# confirm your validate_workflow_file() catches it and explains why.
# See DEBUG_TASK in README.md / index.html for the full walkthrough.


if __name__ == "__main__":
    build_scenario()
