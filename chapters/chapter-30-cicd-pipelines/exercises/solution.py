"""
Chapter 30 Exercises: CI/CD Pipelines -- REFERENCE SOLUTION
See README.md in this folder for full instructions.
Run this from inside the exercises/ folder: python3 solution.py

This builds the same scenario/ folder as starter.py, then runs a real
YAML-validation pass against both the valid and the broken workflow
file, printing exactly what a maintainer reviewing these files by hand
(or a stricter CI linter) would catch.

Uses only the standard library plus `pyyaml`.
"""

import shutil
from pathlib import Path

import yaml

EXERCISE_DIR = Path(__file__).parent
SCENARIO_DIR = EXERCISE_DIR / "scenario"


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

# Intentional bug: `steps` is a sibling of the job name instead of being
# nested under it correctly, AND `runs-on` is missing entirely -- a real
# GitHub Actions workflow requires every job to declare runs-on, and
# without it GitHub rejects the workflow before it ever runs.
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
    return project, workflows


REQUIRED_JOB_KEYS = {"runs-on", "steps"}


def load_workflow(path):
    with open(path) as f:
        return yaml.safe_load(f)


def validate_workflow_structure(workflow):
    """Return a list of problem strings; empty list means valid."""
    problems = []

    if not isinstance(workflow, dict):
        return ["workflow root is not a mapping (dict) at all"]

    # PyYAML's YAML 1.1 loader reads the bare key `on:` as the boolean
    # True rather than the string "on" -- GitHub's own parser handles
    # `on` correctly as a real key, but a validator using plain PyYAML
    # has to check for both forms to avoid a false negative here.
    has_on = "on" in workflow or True in workflow
    if not has_on:
        problems.append("missing required top-level key: on")

    jobs = workflow.get("jobs")
    if not jobs or not isinstance(jobs, dict):
        problems.append("missing or empty required top-level key: jobs")
        return problems  # nothing more to check without jobs

    for job_name, job in jobs.items():
        if not isinstance(job, dict):
            problems.append(f"job '{job_name}' is not a mapping (dict)")
            continue

        missing = REQUIRED_JOB_KEYS - job.keys()
        for key in sorted(missing):
            problems.append(f"job '{job_name}' is missing required key: {key}")

        steps = job.get("steps")
        if "steps" in job and (not isinstance(steps, list) or len(steps) == 0):
            problems.append(f"job '{job_name}' has a 'steps' key but it isn't a non-empty list")

    return problems


def validate_workflow_file(path):
    """Return (is_valid: bool, problems: list[str])."""
    try:
        workflow = load_workflow(path)
    except yaml.YAMLError as exc:
        return False, [f"not valid YAML: {exc}"]

    problems = validate_workflow_structure(workflow)
    return (len(problems) == 0, problems)


def section(title):
    print()
    print("=" * 70)
    print(title)
    print("=" * 70)


if __name__ == "__main__":
    section("Building the scenario (same as starter.py)")
    project, workflows = build_scenario()
    print(f"Scenario built at: {SCENARIO_DIR}")

    section("TASK 1-3 -- validating ci.yml (should be VALID)")
    ok, problems = validate_workflow_file(workflows / "ci.yml")
    print(f"valid: {ok}")
    for p in problems:
        print(f"  - {p}")
    assert ok, "ci.yml should validate cleanly -- something's wrong with the checker"

    section("TASK 4 (Debug the Code) -- validating ci-broken.yml (should be INVALID)")
    ok, problems = validate_workflow_file(workflows / "ci-broken.yml")
    print(f"valid: {ok}")
    for p in problems:
        print(f"  - {p}")
    assert not ok, "ci-broken.yml should NOT validate -- it's missing runs-on"
    assert any("runs-on" in p for p in problems), "the reported problem should name the missing runs-on key"

    section("Done -- ci.yml passed, ci-broken.yml correctly failed on 'runs-on'.")
    print("This is exactly the kind of structural check worth running on any")
    print("workflow file before trusting it -- a missing runs-on is a real")
    print("mistake GitHub Actions itself would reject before ever running a job.")
