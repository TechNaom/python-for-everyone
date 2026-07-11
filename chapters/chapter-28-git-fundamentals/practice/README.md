# Chapter 28 Practice Bank: Git Fundamentals

A deeper set of practice problems, organized by topic, on top of the
main `exercises/` folder — including scenario-based problems written
in the same style you'll see in real interviews.

This chapter teaches git itself, not just Python syntax — so instead of
running real git commands, every problem here is a Python function that
**simulates or reasons about** a git concept using plain data (lists,
dicts, strings) standing in for a repo's history. Every behavior
described in these problems was checked against real git in a scratch
repository before being written down here — the git semantics are
genuinely correct, not just internally consistent. Standard library
only, no installs needed.

## How to run

```bash
cd practice
python3 starter.py
```

## Topic 1: Why Version Control Matters

1. Count how many manually-named "backup" files a no-version-control workflow produced.
2. Decide whether two people can edit safely at the same time.
3. **Debug the Code:** fix a wrong claim that git only tracks the current file state, like a shared folder.
4. **Scenario — Comparing Two Approaches:** write `safer_collaboration_choice()`.
5. **Scenario — Interview Prep:** explain why version control matters for a team.

## Topic 2: The Core Git Workflow (init, add, commit, status, diff, log, staging area)

1. Find which files are staged but not yet committed.
2. Decide whether the working tree is clean.
3. **Debug the Code:** fix a wrong claim that `git add` immediately commits a file.
4. **Scenario — Comparing Two Approaches:** write `should_run_status_first()`.
5. **Scenario — Interview Prep:** explain why git splits staging from committing.

## Topic 3: Branching (create/switch/delete, branch-as-pointer)

1. Model what commit a brand-new branch starts pointing at.
2. Model how a branch's pointer advances as you commit on it.
3. **Debug the Code:** fix a wrong claim that deleting a branch instantly erases its commits.
4. **Scenario — Comparing Two Approaches:** write `should_delete_branch()`.
5. **Scenario — Interview Prep:** explain the "branch is a movable pointer" model.

## Topic 4: Merging (fast-forward vs. three-way, merge commits, resolving conflicts)

1. Determine whether a fast-forward merge is possible from two branch histories.
2. Determine whether a merge creates a new commit.
3. **Debug the Code:** fix a conflict marker example with the HEAD/incoming order backwards.
4. **Scenario — Comparing Two Approaches:** write `predict_merge_type()`.
5. **Scenario — Interview Prep:** explain the steps to resolve a real merge conflict.

## Topic 5: Rebase (vs. merge, interactive rebase basics, don't rebase shared history)

1. Confirm a rebase produces a linear history.
2. Model that rebased commits get new hashes even with identical content.
3. **Debug the Code:** fix code that always said it's safe to rebase a shared branch.
4. **Scenario — Comparing Two Approaches:** write `choose_merge_or_rebase()`.
5. **Scenario — Interview Prep:** explain what breaks when someone force-pushes rebased shared history.

## Topic 6: Undoing Things Safely (checkout/restore vs. reset vs. revert, stashing, reflog)

1. Model how `git revert` always adds one commit, never removes any.
2. Model how `git reset --hard` shortens what `git log` shows.
3. **Debug the Code:** fix code that always recommended `reset` even for already-shared commits.
4. **Scenario — Recovering "Lost" Work:** write `can_recover_after_hard_reset()`.
5. **Scenario — Interview Prep:** explain the core difference between `reset` and `revert`.

## Checking your work

Compare your output against `solution.py`. Your exact wording doesn't
need to match on the explanation-style tasks — the goal is that your
program runs without errors and does what each TODO asks. Every
data-driven task's output is exactly reproducible.
