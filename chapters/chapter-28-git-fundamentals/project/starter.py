"""
Chapter 28 Project: Git Workflow Practice -- Setup Script
See README.md in this folder for full instructions.

This is NOT a script you fill in TODOs for. Run it once to build a
scratch practice repository, then close this file and do the rest of
the project in your TERMINAL using real `git` commands, guided by
README.md / index.html's numbered steps.

Standard library only -- no installs needed. Requires `git` itself to
be installed and on your PATH.

Run this from inside the project/ folder:
    python3 starter.py

It creates a new folder called `recipe-box/` right next to this
script (NOT inside your course clone's own git repo -- it's a fully
separate, throwaway git repository) and pre-loads it with:

  1. An initial commit on `main` (a recipe file + README).
  2. A `feature/double-recipe` branch that diverges from main with
     two of its own commits, editing the SAME lines main is about to
     edit next.
  3. A follow-up commit on `main` that edits those same lines
     differently -- so main and feature/double-recipe now conflict
     on purpose.

Nothing is merged yet. That's your job, in the terminal, using the
steps in README.md.
"""

import subprocess
import sys
from pathlib import Path

REPO_NAME = "recipe-box"


def run_git(repo_dir, *args):
    """Run a git command inside repo_dir, raising if it fails."""
    result = subprocess.run(
        ["git", *args],
        cwd=repo_dir,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(f"git {' '.join(args)} failed:")
        print(result.stdout)
        print(result.stderr)
        sys.exit(1)
    return result.stdout


def write_file(path, content):
    path.write_text(content, encoding="utf-8")


def build_scratch_repo():
    project_dir = Path(__file__).resolve().parent
    repo_dir = project_dir / REPO_NAME

    if repo_dir.exists():
        print(f"'{REPO_NAME}/' already exists at {repo_dir}")
        print("Delete it first if you want a fresh start:")
        print(f"  rm -rf {repo_dir}")
        sys.exit(1)

    repo_dir.mkdir()
    print(f"Created {repo_dir}")

    # --- init + local identity (scoped to this repo only) -------------
    run_git(repo_dir, "init", "-q")
    run_git(repo_dir, "config", "user.email", "learner@example.com")
    run_git(repo_dir, "config", "user.name", "Learner")
    run_git(repo_dir, "branch", "-m", "main")

    # --- initial commit on main ----------------------------------------
    write_file(
        repo_dir / "recipe.txt",
        "Grandma's Chili\n"
        "================\n"
        "Ingredients:\n"
        "- 1 lb ground beef\n"
        "- 1 can beans\n"
        "- 1 can tomatoes\n"
        "\n"
        "Serves: 4\n",
    )
    write_file(
        repo_dir / "README.md",
        "# Recipe Box\n"
        "A shared collection of family recipes.\n",
    )
    run_git(repo_dir, "add", "recipe.txt", "README.md")
    run_git(repo_dir, "commit", "-q", "-m", "Initial commit: add recipe box with chili recipe")
    print("Committed: Initial commit (main)")

    # --- feature branch that diverges with its own commits ------------
    run_git(repo_dir, "checkout", "-b", "feature/double-recipe", "-q")
    write_file(
        repo_dir / "recipe.txt",
        "Grandma's Chili\n"
        "================\n"
        "Ingredients:\n"
        "- 2 lb ground beef\n"
        "- 2 cans beans\n"
        "- 2 cans tomatoes\n"
        "\n"
        "Serves: 8 (doubled)\n",
    )
    run_git(repo_dir, "add", "recipe.txt")
    run_git(repo_dir, "commit", "-q", "-m", "Double the chili recipe for a bigger crowd")
    print("Committed: Double the chili recipe (feature/double-recipe)")

    write_file(
        repo_dir / "recipe.txt",
        "Grandma's Chili\n"
        "================\n"
        "Ingredients:\n"
        "- 2 lb ground beef\n"
        "- 2 cans beans\n"
        "- 2 cans tomatoes\n"
        "\n"
        "Serves: 8 (doubled)\n"
        "- pinch of cinnamon\n",
    )
    run_git(repo_dir, "add", "recipe.txt")
    run_git(repo_dir, "commit", "-q", "-m", "Add secret ingredient: cinnamon")
    print("Committed: Add secret ingredient (feature/double-recipe)")

    # --- main moves on and edits the SAME line, on purpose -------------
    run_git(repo_dir, "checkout", "main", "-q")
    write_file(
        repo_dir / "recipe.txt",
        "Grandma's Chili\n"
        "================\n"
        "Ingredients:\n"
        "- 1 lb ground beef\n"
        "- 1 can beans\n"
        "- 1 can tomatoes\n"
        "\n"
        "Serves: 4-6 depending on appetite\n",
    )
    run_git(repo_dir, "add", "recipe.txt")
    run_git(repo_dir, "commit", "-q", "-m", "Clarify serving size on main")
    print("Committed: Clarify serving size (main)")

    print()
    print("=" * 60)
    print(f"Scratch repo ready at: {repo_dir}")
    print("=" * 60)
    print(run_git(repo_dir, "log", "--oneline", "--graph", "--all"))
    print(
        "Both `main` and `feature/double-recipe` edited the last line\n"
        "of recipe.txt differently -- merging them WILL conflict.\n"
        "\n"
        "Next step: `cd project/recipe-box` and follow README.md's\n"
        "numbered workflow starting with branching and merging.\n"
    )


if __name__ == "__main__":
    build_scratch_repo()
