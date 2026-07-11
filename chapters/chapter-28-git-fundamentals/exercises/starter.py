"""
Chapter 28 Exercises: Git Fundamentals -- scenario setup script.

This chapter has no Python functions to write or grade. Instead, this
script BUILDS a real git repository on disk (in ./git-playground/)
with a specific commit history -- including a real merge conflict
waiting to happen and a commit that's about to get "lost" -- so you
can practice actual git commands against it in your own terminal.

Run this once, from inside this exercises/ folder:
    python3 starter.py

Then:
    cd git-playground
    git log --oneline --graph --all
    git status

...and work through Tasks 1-9 in README.md (or index.html), running
real git commands yourself as you go. Nothing here is auto-graded --
git's own output is the feedback. Compare what you did against
solution.py, which documents the exact command sequence for every
task as comments (there's no Python logic to run for this chapter).
"""

import os
import shutil
import subprocess

PLAYGROUND = "git-playground"


def run(*args, cwd=PLAYGROUND, check=True):
    return subprocess.run(
        ["git", *args], cwd=cwd, check=check,
        capture_output=True, text=True,
    )


def write(path, content, cwd=PLAYGROUND):
    with open(os.path.join(cwd, path), "w") as f:
        f.write(content)


def append(path, content, cwd=PLAYGROUND):
    with open(os.path.join(cwd, path), "a") as f:
        f.write(content)


def read(path, cwd=PLAYGROUND):
    with open(os.path.join(cwd, path)) as f:
        return f.read()


def build_playground():
    if os.path.exists(PLAYGROUND):
        shutil.rmtree(PLAYGROUND)
    os.makedirs(PLAYGROUND)

    subprocess.run(["git", "init", "-b", "main"], cwd=PLAYGROUND, check=True, capture_output=True)
    subprocess.run(["git", "config", "user.email", "learner@example.com"], cwd=PLAYGROUND, check=True)
    subprocess.run(["git", "config", "user.name", "Learner"], cwd=PLAYGROUND, check=True)

    # --- Commits 1-2: the core workflow (Tasks 1-2) ---
    write("tasks.py", (
        'def add_task(tasks, description):\n'
        '    tasks.append({"description": description, "done": False})\n'
        '    return tasks\n\n\n'
        'def list_tasks(tasks):\n'
        '    for i, task in enumerate(tasks, start=1):\n'
        '        mark = "x" if task["done"] else " "\n'
        '        print(f"[{mark}] {i}. {task[\'description\']}")\n'
    ))
    run("add", "tasks.py")
    run("commit", "-m", "Add basic task add/list functions")

    append("tasks.py", (
        '\n\ndef complete_task(tasks, index):\n'
        '    tasks[index - 1]["done"] = True\n'
        '    return tasks\n'
    ))
    run("add", "tasks.py")
    run("commit", "-m", "Add complete_task function")

    # --- Fast-forward merge setup (Task 3) ---
    run("switch", "-c", "feature/delete-task")
    append("tasks.py", (
        '\n\ndef delete_task(tasks, index):\n'
        '    tasks.pop(index - 1)\n'
        '    return tasks\n'
    ))
    run("add", "tasks.py")
    run("commit", "-m", "Add delete_task function")
    run("switch", "main")
    run("merge", "feature/delete-task")
    run("branch", "-d", "feature/delete-task")

    # --- Diverging branches, left UNMERGED on purpose: a real conflict
    #     is waiting for you to trigger yourself in Task 5 ---
    run("switch", "-c", "feature/priority")
    content = read("tasks.py")
    content = content.replace(
        'def add_task(tasks, description):\n'
        '    tasks.append({"description": description, "done": False})\n'
        '    return tasks',
        'def add_task(tasks, description, priority="normal"):\n'
        '    tasks.append({"description": description, "done": False, "priority": priority})\n'
        '    return tasks',
    )
    write("tasks.py", content)
    run("add", "tasks.py")
    run("commit", "-m", "Add priority field to add_task")

    run("switch", "main")
    content = read("tasks.py")
    content = content.replace(
        'def add_task(tasks, description):\n'
        '    tasks.append({"description": description, "done": False})\n'
        '    return tasks',
        'def add_task(tasks, description):\n'
        '    if not description.strip():\n'
        '        raise ValueError("description cannot be empty")\n'
        '    tasks.append({"description": description, "done": False})\n'
        '    return tasks',
    )
    write("tasks.py", content)
    run("add", "tasks.py")
    run("commit", "-m", "Validate description is not empty in add_task")
    # main is left right here on purpose -- Task 5 asks you to run
    # `git merge feature/priority` yourself and resolve the conflict.

    # --- A commit that's about to become "lost" (Task 8: reflog) ---
    append("tasks.py", "\n\ndef task_count(tasks):\n    return len(tasks)\n")
    run("add", "tasks.py")
    run("commit", "-m", "Add task_count helper")
    run("reset", "--hard", "HEAD~1")
    # The commit above still exists -- it's just unreachable from any
    # branch right now. Task 8 asks you to find it again with
    # `git reflog` and bring it back, without being told its hash.

    # --- A dirty, uncommitted change left in the working tree
    #     (Task 6: restore/reset practice) ---
    append("tasks.py", "\n\n# scratch note: not ready to commit this yet\nDEBUG = True\n")

    print("git-playground/ is ready. Current state:")
    print()
    print(run("log", "--oneline", "--all", "--graph").stdout)
    print(run("status").stdout)
    print("cd into git-playground/ and start with Task 1 in README.md.")


if __name__ == "__main__":
    build_playground()
