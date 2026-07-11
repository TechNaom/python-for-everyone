"""
Chapter 29 Exercises: GitHub & Collaboration -- REFERENCE SOLUTION
See README.md in this folder for full instructions.
Run this from inside the exercises/ folder: python3 solution.py

Unlike most chapters' solution.py, this chapter's tasks are git
commands run BY HAND in your terminal against the scenario/ folder
that starter.py builds -- there's no Python function to "call" that
checks your answer. This file instead runs the entire scenario AND
every correct command sequence end to end, for real, and prints the
actual output at each step, so you can compare it against what you
saw running the same commands yourself.

Every command shown below was verified by actually running it while
writing this course -- the output printed is real git output, not
invented.
"""

import subprocess
import shutil
import os
from pathlib import Path

SCENARIO_DIR = Path(__file__).parent / "scenario"

ENV_AUTHOR = {
    "GIT_AUTHOR_NAME": "Ada Learner",
    "GIT_AUTHOR_EMAIL": "ada@example.com",
    "GIT_COMMITTER_NAME": "Ada Learner",
    "GIT_COMMITTER_EMAIL": "ada@example.com",
}


def run(cmd, cwd, show=True, allow_fail=False):
    """Run a real git command, print it and its output, return stdout."""
    env = os.environ.copy()
    env.update(ENV_AUTHOR)
    if show:
        print(f"$ {' '.join(cmd)}")
    result = subprocess.run(cmd, cwd=cwd, env=env, capture_output=True, text=True)
    output = (result.stdout + result.stderr).strip()
    if show and output:
        print(output)
    if result.returncode != 0 and not allow_fail:
        raise RuntimeError(f"Command failed: {' '.join(cmd)}\n{output}")
    return result


def section(title):
    print()
    print("=" * 70)
    print(title)
    print("=" * 70)


def build_scenario():
    if SCENARIO_DIR.exists():
        shutil.rmtree(SCENARIO_DIR)
    SCENARIO_DIR.mkdir(parents=True)

    bare = SCENARIO_DIR / "upstream-remote.git"
    run(["git", "init", "--bare", "-q", "upstream-remote.git"], cwd=SCENARIO_DIR, show=False)

    work = SCENARIO_DIR / "my-local-work"
    run(["git", "init", "-q", "my-local-work"], cwd=SCENARIO_DIR, show=False)
    run(["git", "checkout", "-q", "-b", "main"], cwd=work, show=False)

    (work / "README.md").write_text("# Recipe Box\n\nA tiny shared project.\n")
    (work / "app.py").write_text("print('hello from recipe box')\n")
    run(["git", "add", "README.md", "app.py"], cwd=work, show=False)
    run(["git", "commit", "-q", "-m", "Initial commit"], cwd=work, show=False)
    run(["git", "remote", "add", "origin", "../upstream-remote.git"], cwd=work, show=False)
    run(["git", "push", "-u", "-q", "origin", "main"], cwd=work, show=False)

    teammate = SCENARIO_DIR / "_teammate-clone"
    run(["git", "clone", "-q", "upstream-remote.git", "_teammate-clone"], cwd=SCENARIO_DIR, show=False)
    run(["git", "checkout", "-q", "main"], cwd=teammate, show=False)
    with open(teammate / "app.py", "a") as f:
        f.write("print('a teammate added this line')\n")
    run(["git", "add", "app.py"], cwd=teammate, show=False)
    run(["git", "commit", "-q", "-m", "Teammate pushes a change"], cwd=teammate, show=False)
    run(["git", "push", "-q", "origin", "main"], cwd=teammate, show=False)
    shutil.rmtree(teammate)

    return bare, work


def task_1_2_3(work):
    section("TASK 1 -- confirm origin's URLs")
    run(["git", "remote", "-v"], cwd=work)

    section("TASK 2 -- fetch, then prove local main is untouched")
    run(["git", "fetch", "origin"], cwd=work)
    print("\nlocal main:")
    run(["git", "log", "--oneline"], cwd=work)
    print("\norigin/main (what fetch downloaded):")
    run(["git", "log", "--oneline", "origin/main"], cwd=work)

    section("TASK 3 -- pull, which DOES update local main (fast-forward)")
    run(["git", "pull", "origin", "main"], cwd=work)
    print("\nlocal main after pull:")
    run(["git", "log", "--oneline"], cwd=work)


def task_4_debug(work):
    section("TASK 4 (Debug the Code) -- reproduce the rejected push")

    # A second teammate pushes directly to upstream while you're not looking
    teammate2 = SCENARIO_DIR / "_teammate2"
    run(["git", "clone", "-q", "upstream-remote.git", "_teammate2"], cwd=SCENARIO_DIR, show=False)
    run(["git", "checkout", "-q", "main"], cwd=teammate2, show=False)
    with open(teammate2 / "app.py", "a") as f:
        f.write("print('second teammate change')\n")
    run(["git", "add", "app.py"], cwd=teammate2, show=False)
    run(["git", "commit", "-q", "-m", "Second teammate change"], cwd=teammate2, show=False)
    run(["git", "push", "-q", "origin", "main"], cwd=teammate2, show=False)
    shutil.rmtree(teammate2)

    # Meanwhile, you make your OWN local commit without fetching first
    with open(work / "app.py", "a") as f:
        f.write("print('my own feature')\n")
    run(["git", "add", "app.py"], cwd=work, show=False)
    run(["git", "commit", "-q", "-m", "My local feature"], cwd=work, show=False)

    print("\nAttempting to push -- this is the bug scenario:")
    result = run(["git", "push", "origin", "main"], cwd=work, allow_fail=True)
    assert "[rejected]" in (result.stdout + result.stderr)
    print("\n^ Rejected, exactly as the debug task describes. DIAGNOSIS:")
    print("  Upstream has a commit (the second teammate's) that this local")
    print("  branch never fetched, so git refuses a push that would silently")
    print("  discard history the remote already has.")

    section("TASK 4 -- the fix: fetch, then rebase (or merge), then push")
    run(["git", "fetch", "origin"], cwd=work)
    print("\nDivergent history, visualized:")
    run(["git", "log", "--oneline", "--graph", "--all"], cwd=work)

    print("\nRebasing local commit onto the fetched origin/main:")
    result = run(["git", "rebase", "origin/main"], cwd=work, allow_fail=True)

    if "CONFLICT" in (result.stdout + result.stderr):
        print("\n^ A real conflict, since both changes appended to the same")
        print("  region of app.py -- resolve it by editing the file directly:")
        conflicted = (work / "app.py").read_text()
        print(conflicted)
        resolved = (
            "print('hello from recipe box')\n"
            "print('a teammate added this line')\n"
            "print('second teammate change')\n"
            "print('my own feature')\n"
        )
        (work / "app.py").write_text(resolved)
        run(["git", "add", "app.py"], cwd=work)
        run(["git", "rebase", "--continue"], cwd=work)

    print("\nPush again -- now succeeds:")
    run(["git", "push", "origin", "main"], cwd=work)
    print("\nFinal history:")
    run(["git", "log", "--oneline"], cwd=work)


if __name__ == "__main__":
    section("Building the scenario (same as starter.py)")
    bare, work = build_scenario()
    print(f"Scenario built at: {SCENARIO_DIR}")

    task_1_2_3(work)
    task_4_debug(work)

    section("Done -- every command above ran for real against real repos.")
    print("Compare this output against what you saw running the same")
    print("commands yourself in scenario/my-local-work.")
