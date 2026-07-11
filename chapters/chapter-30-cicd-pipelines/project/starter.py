"""
Chapter 30 Project: Lint + Test + Ship -- Setup Script
See README.md in this folder for full instructions.

This is NOT a script you fill in TODOs for -- CI/CD is not something you
practice by editing one Python file. Run this once to confirm your local
tools are ready, then close this file and do the rest of the project in
your TERMINAL, working inside `sample_project/`, guided by README.md /
index.html's numbered steps.

Requires: python3, pip, and (ideally) `git`. Installs pytest + ruff into
whatever Python environment you run this with, if they aren't already
present.

Run this from inside the project/ folder:
    python3 starter.py

What it does:
  1. Checks that `sample_project/` exists next to this script (it does --
     it ships with the course, already containing a real installable
     package called `expense_tracker`, a pytest suite, and a GitHub
     Actions workflow at `sample_project/.github/workflows/ci.yml`).
  2. Installs `pytest` and `ruff` if they're missing.
  3. Runs `ruff check .` inside sample_project/ so you can see, before
     touching anything, that ONE real lint violation is waiting for you
     to find and fix (an unused import in expense_tracker/report.py).
  4. Runs `pytest` inside sample_project/ so you can see the full test
     suite passing on the code as shipped.

Your job (in the terminal, in sample_project/) is to:
  - Read the ruff output and fix the unused-import violation yourself.
  - Read ci.yml and understand every job, step, and trigger in it --
    the README's numbered steps walk through each piece.
  - Re-run ruff + pytest locally to confirm both are clean, the same way
    the lint and test jobs in ci.yml would if this were pushed to GitHub.

Nothing here pushes to GitHub or calls the GitHub Actions API -- this
environment can't literally trigger a workflow run. The whole point of
building it this way is that the SAME commands the workflow runs
(`ruff check .`, `pytest`) are commands you can -- and should -- run
yourself, locally, before ever trusting a green checkmark on GitHub.
"""

import subprocess
import sys
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent
SAMPLE_DIR = PROJECT_DIR / "sample_project"


def run(cmd, cwd=None, check=False):
    print(f"$ {' '.join(cmd)}")
    result = subprocess.run(cmd, cwd=cwd, text=True)
    if check and result.returncode != 0:
        sys.exit(result.returncode)
    return result.returncode


def ensure_tool(module_name, pip_name):
    check = subprocess.run(
        [sys.executable, "-m", module_name, "--version"],
        capture_output=True,
        text=True,
    )
    if check.returncode != 0:
        print(f"{pip_name} not found -- installing...")
        run([sys.executable, "-m", "pip", "install", pip_name], check=True)
    else:
        print(f"{pip_name} already available: {check.stdout.strip() or check.stderr.strip()}")


def main():
    if not SAMPLE_DIR.exists():
        print(f"ERROR: expected to find {SAMPLE_DIR}, but it's missing.")
        print("Re-clone or restore the course repo and try again.")
        sys.exit(1)

    print("=== Step 1: checking tools ===")
    ensure_tool("pytest", "pytest")
    ensure_tool("ruff", "ruff")

    print("\n=== Step 2: running ruff against sample_project/ (as shipped) ===")
    print("(Expect exactly ONE violation -- an unused import. That's intentional.)")
    run(["ruff", "check", "."], cwd=SAMPLE_DIR)

    print("\n=== Step 3: running pytest against sample_project/ (as shipped) ===")
    run(["pytest", "-v"], cwd=SAMPLE_DIR)

    print("\n=== Done ===")
    print("Now go work in the terminal, inside sample_project/, following")
    print("README.md's numbered steps: fix the lint violation, read through")
    print(".github/workflows/ci.yml, and re-run both commands until they're clean.")
    print("When you're done, run: python3 solution.py  (from this project/ folder)")
    print("to verify your work.")


if __name__ == "__main__":
    main()
