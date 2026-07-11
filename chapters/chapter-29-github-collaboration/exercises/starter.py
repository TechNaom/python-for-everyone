"""
Chapter 29 Exercises: GitHub & Collaboration
See README.md in this folder for full instructions.
Run this from inside the exercises/ folder: python3 starter.py

This script does NOT use git itself -- it only builds a real scratch
scenario on disk using subprocess calls to the real `git` command, so
you can then practice the actual git remote/push/pull/fetch commands
from your own terminal, for real, against real local repositories.

Every task here uses only the standard library (subprocess, pathlib,
shutil) plus the `git` command already on your system -- no installs
needed.
"""

import subprocess
import shutil
from pathlib import Path

SCENARIO_DIR = Path(__file__).parent / "scenario"

ENV_AUTHOR = {
    "GIT_AUTHOR_NAME": "Ada Learner",
    "GIT_AUTHOR_EMAIL": "ada@example.com",
    "GIT_COMMITTER_NAME": "Ada Learner",
    "GIT_COMMITTER_EMAIL": "ada@example.com",
}


def run(cmd, cwd):
    """Run a git command for real, raise if it fails."""
    import os

    env = os.environ.copy()
    env.update(ENV_AUTHOR)
    result = subprocess.run(
        cmd, cwd=cwd, env=env, capture_output=True, text=True
    )
    if result.returncode != 0:
        raise RuntimeError(
            f"Command failed: {' '.join(cmd)}\n{result.stdout}\n{result.stderr}"
        )
    return result.stdout


def build_scenario():
    """
    Builds a real scratch scenario on disk:

      scenario/upstream-remote.git   -- a bare repo standing in for
                                         "the project on GitHub"
      scenario/my-local-work/        -- your working clone, with
                                         `origin` already pointing at
                                         upstream-remote.git

    This mirrors Sub-topic 1 of the lesson: git init --bare simulates
    a GitHub remote realistically, since it has no working directory
    and only accepts pushes / serves fetches, exactly like GitHub does.
    """
    if SCENARIO_DIR.exists():
        shutil.rmtree(SCENARIO_DIR)
    SCENARIO_DIR.mkdir(parents=True)

    bare = SCENARIO_DIR / "upstream-remote.git"
    run(["git", "init", "--bare", "-q", str(bare)], cwd=SCENARIO_DIR)

    work = SCENARIO_DIR / "my-local-work"
    run(["git", "init", "-q", str(work)], cwd=SCENARIO_DIR)
    run(["git", "checkout", "-q", "-b", "main"], cwd=work)

    (work / "README.md").write_text("# Recipe Box\n\nA tiny shared project.\n")
    (work / "app.py").write_text("print('hello from recipe box')\n")
    run(["git", "add", "README.md", "app.py"], cwd=work)
    run(["git", "commit", "-q", "-m", "Initial commit"], cwd=work)

    run(["git", "remote", "add", "origin", "../upstream-remote.git"], cwd=work)
    run(["git", "push", "-u", "-q", "origin", "main"], cwd=work)

    # Simulate a teammate pushing a change directly to the "remote" via a
    # second clone, so your local main starts out one commit BEHIND
    # origin/main -- exactly the situation TODO 1-4 below ask you to
    # diagnose and resolve using real fetch/pull.
    teammate = SCENARIO_DIR / "_teammate-clone"
    run(["git", "clone", "-q", "upstream-remote.git", "_teammate-clone"], cwd=SCENARIO_DIR)
    run(["git", "checkout", "-q", "main"], cwd=teammate)
    with open(teammate / "app.py", "a") as f:
        f.write("print('a teammate added this line')\n")
    run(["git", "add", "app.py"], cwd=teammate)
    run(["git", "commit", "-q", "-m", "Teammate pushes a change"], cwd=teammate)
    run(["git", "push", "-q", "origin", "main"], cwd=teammate)
    shutil.rmtree(teammate)

    print(f"Scenario built at: {SCENARIO_DIR}")
    print()
    print("You now have:")
    print(f"  {bare}   (a real bare repo -- your stand-in GitHub remote)")
    print(f"  {work}   (your local clone -- ONE COMMIT BEHIND origin/main)")
    print()
    print("cd into scenario/my-local-work and work through README.md's")
    print("tasks using real git commands in your own terminal.")


# TODO 1: In your terminal, cd into scenario/my-local-work and run
# `git remote -v`. Confirm `origin` points at ../upstream-remote.git
# for both fetch and push.

# TODO 2: Run `git fetch origin`. Notice your local `main` branch does
# NOT change -- only origin/main (a remote-tracking branch) updates.
# Prove it: run `git log --oneline` (local main) and then
# `git log --oneline origin/main` (what fetch downloaded) and compare.

# TODO 3: Now run `git pull origin main`. This time your local main
# DOES update -- it's a fast-forward, since your local branch had no
# commits of its own beyond what origin already had.

# TODO 4 (Debug the Code): see DEBUG_TASK.md in this folder -- your
# next push gets rejected because upstream has a change you don't have
# locally. Diagnose why, then fix it for real using fetch + rebase (or
# merge) followed by a successful push.

if __name__ == "__main__":
    build_scenario()
