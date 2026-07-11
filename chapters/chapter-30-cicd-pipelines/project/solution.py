"""
Chapter 30 Project: Lint + Test + Ship -- Verifier Script
See README.md in this folder for full instructions.

This is a VERIFIER, not a second copy to fill in. Run it AFTER you've
worked through README.md's numbered steps inside `sample_project/` --
it actually runs `ruff check .` and `pytest` as real subprocesses
against your edited copy of the package, and parses
`.github/workflows/ci.yml` with `yaml.safe_load()` to confirm the
workflow itself is still structurally correct, instead of showing you
a "correct" copy to compare against.

Requires `pytest`, `ruff`, and `pyyaml` to be installed (starter.py
installs pytest + ruff for you; pyyaml is needed only for this
verifier -- installed automatically below if missing).

Run this from inside the project/ folder, AFTER completing the
workflow in sample_project/:
    python3 solution.py
"""

import subprocess
import sys
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent
SAMPLE_DIR = PROJECT_DIR / "sample_project"
WORKFLOW_PATH = SAMPLE_DIR / ".github" / "workflows" / "ci.yml"


def ensure_yaml():
    try:
        import yaml  # noqa: F401
        return
    except ImportError:
        print("pyyaml not found -- installing (needed only to verify the workflow file)...")
        subprocess.run([sys.executable, "-m", "pip", "install", "pyyaml"], check=True)


def check(label, passed, detail=""):
    mark = "PASS" if passed else "FAIL"
    line = f"  [{mark}] {label}"
    if detail:
        line += f" -- {detail}"
    print(line)
    return passed


def run(cmd, cwd):
    result = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    return result.returncode, result.stdout, result.stderr


def verify():
    if not SAMPLE_DIR.exists():
        print(f"No 'sample_project/' folder found next to this script.")
        print("Run `python3 starter.py` first, then work through README.md.")
        sys.exit(1)

    ensure_yaml()
    import yaml

    print(f"Checking {SAMPLE_DIR} ...\n")
    results = []

    # 1. ruff reports zero violations -- the unused import should be fixed.
    rc, out, err = run(["ruff", "check", "."], cwd=SAMPLE_DIR)
    results.append(check(
        "ruff check . reports zero violations (unused import fixed)",
        rc == 0,
        detail="ruff still found issues -- see output below" if rc != 0 else "",
    ))
    if rc != 0:
        print(out or err)

    # 2. pytest passes on the full suite.
    rc, out, err = run(["pytest", "-q"], cwd=SAMPLE_DIR)
    results.append(check(
        "pytest passes on the full test suite",
        rc == 0,
        detail="pytest reported failures -- see output below" if rc != 0 else "",
    ))
    if rc != 0:
        print(out or err)

    # 3. ci.yml exists and parses as valid YAML.
    workflow_data = None
    if not WORKFLOW_PATH.exists():
        results.append(check("ci.yml exists at .github/workflows/ci.yml", False))
    else:
        try:
            workflow_data = yaml.safe_load(WORKFLOW_PATH.read_text(encoding="utf-8"))
            results.append(check("ci.yml is valid YAML (yaml.safe_load succeeds)", True))
        except yaml.YAMLError as e:
            results.append(check("ci.yml is valid YAML (yaml.safe_load succeeds)", False, detail=str(e)))

    if workflow_data:
        # 4. Triggers on both push and pull_request.
        # PyYAML's default (non-1.2) resolver treats the bare key `on:` as
        # the boolean True -- check both spellings defensively.
        triggers = workflow_data.get("on", workflow_data.get(True, {})) or {}
        results.append(check(
            "workflow triggers on both push and pull_request",
            "push" in triggers and "pull_request" in triggers,
            detail=f"found triggers: {list(triggers.keys())}",
        ))

        # 5. Both a lint job and a test job exist.
        jobs = workflow_data.get("jobs", {})
        results.append(check(
            "workflow has a lint job and a test job",
            "lint" in jobs and "test" in jobs,
            detail=f"found jobs: {list(jobs.keys())}",
        ))

        # 6. The test job uses a matrix strategy with 2+ Python versions.
        test_job = jobs.get("test", {})
        matrix_versions = (
            test_job.get("strategy", {}).get("matrix", {}).get("python-version", [])
        )
        results.append(check(
            "test job uses a matrix strategy with 2+ Python versions",
            isinstance(matrix_versions, list) and len(matrix_versions) >= 2,
            detail=f"matrix python-version: {matrix_versions}",
        ))

        # 7. pip caching is configured somewhere in the workflow.
        workflow_text = WORKFLOW_PATH.read_text(encoding="utf-8")
        results.append(check(
            "pip dependency caching is configured (cache: \"pip\")",
            'cache: "pip"' in workflow_text or "cache: 'pip'" in workflow_text,
        ))

    print()
    passed_count = sum(1 for r in results if r)
    total = len(results)
    print(f"{passed_count}/{total} checks passed.")
    if passed_count == total:
        print("Verified: package is lint-clean, tests pass, and ci.yml is a valid")
        print("multi-job, matrix-strategy, cached, push+PR-triggered workflow.")
        print("(No live GitHub Actions run happened -- this environment can't")
        print("trigger one -- but every command the workflow runs was just run")
        print("for real, right here, against your actual code.)")
    else:
        print("Some checks aren't passing yet -- revisit README.md's numbered steps for the ones marked FAIL above.")


if __name__ == "__main__":
    verify()
