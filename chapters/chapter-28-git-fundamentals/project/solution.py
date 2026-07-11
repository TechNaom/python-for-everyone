"""
Chapter 28 Project: Git Workflow Practice -- Verifier Script
See README.md in this folder for full instructions.

This is a VERIFIER, not a second copy to fill in. Run it AFTER you've
worked through README.md's numbered steps inside `recipe-box/` (the
repo `starter.py` created) -- it inspects your actual repo's real git
state via subprocess calls to `git` and reports which milestones you
completed, instead of showing you a "correct" answer to copy.

Standard library only -- no installs needed. Requires `git` itself to
be installed and on your PATH.

Run this from inside the project/ folder, AFTER completing the
workflow in recipe-box/:
    python3 solution.py
"""

import subprocess
import sys
from pathlib import Path

REPO_NAME = "recipe-box"


def run_git(repo_dir, *args, check=True):
    """Run a git command inside repo_dir, returning stdout (or None on failure)."""
    result = subprocess.run(
        ["git", *args],
        cwd=repo_dir,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        if check:
            return None
        return result.stdout
    return result.stdout.strip()


def check(label, passed, detail=""):
    mark = "PASS" if passed else "FAIL"
    line = f"  [{mark}] {label}"
    if detail:
        line += f" -- {detail}"
    print(line)
    return passed


def verify():
    project_dir = Path(__file__).resolve().parent
    repo_dir = project_dir / REPO_NAME

    if not repo_dir.exists():
        print(f"No '{REPO_NAME}/' folder found next to this script.")
        print("Run `python3 starter.py` first, then work through README.md.")
        sys.exit(1)

    if run_git(repo_dir, "rev-parse", "--is-inside-work-tree") != "true":
        print(f"'{REPO_NAME}/' exists but isn't a git repository.")
        sys.exit(1)

    print(f"Checking {repo_dir} ...\n")
    results = []

    # 1. feature/double-recipe branch exists (or was merged and can
    #    still be found in history -- either counts).
    branches = run_git(repo_dir, "branch", "--list") or ""
    all_refs = run_git(repo_dir, "log", "--all", "--format=%D") or ""
    had_feature_branch = "feature/double-recipe" in branches or "feature/double-recipe" in all_refs
    results.append(check(
        "feature/double-recipe branch was created",
        had_feature_branch,
    ))

    # 2. main has a merge commit (2 parents) merging feature/double-recipe.
    merge_commits = run_git(repo_dir, "log", "main", "--merges", "--format=%H %P") or ""
    has_merge_commit = len(merge_commits.strip()) > 0
    results.append(check(
        "main has a merge commit (the conflict was resolved and committed)",
        has_merge_commit,
    ))

    # 3. No leftover conflict markers anywhere in tracked files on main.
    run_git(repo_dir, "checkout", "main", "-q", check=False)
    ls_files = run_git(repo_dir, "ls-files") or ""
    markers_found = False
    for filename in ls_files.splitlines():
        file_path = repo_dir / filename
        if file_path.is_file():
            lines = file_path.read_text(encoding="utf-8", errors="ignore").splitlines()
            if any(l.startswith("<<<<<<<") or l.startswith(">>>>>>>") for l in lines):
                markers_found = True
    results.append(check(
        "no leftover conflict markers in tracked files on main",
        not markers_found,
    ))

    # 4. recipe.txt contains evidence both sides' changes survived
    #    the resolution (doubled ingredients AND the cinnamon line).
    recipe_path = repo_dir / "recipe.txt"
    recipe_text = recipe_path.read_text(encoding="utf-8") if recipe_path.exists() else ""
    results.append(check(
        "recipe.txt reflects a real resolution (doubled ingredients kept)",
        "2 lb ground beef" in recipe_text or "2 cans beans" in recipe_text,
    ))

    # 5. main has more than the original 1 commit (i.e. history moved).
    main_commit_count = run_git(repo_dir, "rev-list", "--count", "main") or "0"
    results.append(check(
        "main has more than one commit",
        main_commit_count.isdigit() and int(main_commit_count) > 1,
        detail=f"{main_commit_count} commits on main",
    ))

    # 6. A second branch exists and was rebased onto the updated main
    #    (linear history: its merge-base with main IS main's tip, but
    #    the branch itself has no merge commits of its own).
    other_branches = [
        b.strip().lstrip("* ").strip()
        for b in branches.splitlines()
        if b.strip() and "double-recipe" not in b and "main" not in b
    ]
    rebased_ok = False
    rebase_detail = "no second branch found"
    if other_branches:
        second_branch = other_branches[0]
        main_tip = run_git(repo_dir, "rev-parse", "main")
        merge_base = run_git(repo_dir, "merge-base", second_branch, "main")
        # Only look at merge commits UNIQUE to this branch (i.e. commits
        # added since main) -- merge commits that are already part of
        # main's own history (like the earlier feature/double-recipe
        # merge) don't count against a clean rebase.
        branch_merges = run_git(repo_dir, "log", f"main..{second_branch}", "--merges", "--format=%H") or ""
        rebased_ok = (merge_base == main_tip) and (branch_merges.strip() == "")
        rebase_detail = f"branch '{second_branch}': merge-base == main tip and no merge commits"
    results.append(check(
        "a second branch was created and rebased cleanly onto the updated main",
        rebased_ok,
        detail=rebase_detail,
    ))

    # 7. reflog has more than the minimum entries, implying real work
    #    (branching/merging/rebasing/committing) happened, not just init.
    reflog = run_git(repo_dir, "reflog") or ""
    reflog_lines = [l for l in reflog.splitlines() if l.strip()]
    results.append(check(
        "reflog shows a real sequence of git operations",
        len(reflog_lines) >= 8,
        detail=f"{len(reflog_lines)} reflog entries",
    ))

    print()
    passed_count = sum(1 for r in results if r)
    total = len(results)
    print(f"{passed_count}/{total} checks passed.")
    if passed_count == total:
        print("Workflow verified -- branch, diverge, conflict, resolve, merge, and rebase all confirmed.")
    else:
        print("Some milestones aren't showing up yet -- revisit README.md's numbered steps for the ones marked FAIL above.")


if __name__ == "__main__":
    verify()
