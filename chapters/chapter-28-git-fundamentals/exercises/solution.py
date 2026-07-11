"""
Chapter 28 Exercises: Git Fundamentals -- reference solution.

There's no Python logic to run for this chapter -- git itself is what
you're practicing. This file documents the exact, verified command
sequence for every task in README.md / index.html, as comments, so
you can check your own terminal work against it.

Every command below was actually run against the repo starter.py
builds (in ./git-playground/) before being written here -- this is
real, checked git behavior, not invented output.

Run `python3 starter.py` first if you haven't already, then `cd
git-playground` and try each task yourself BEFORE reading the answer
below -- that's the actual exercise.
"""

# --- Task 1: Read the history --------------------------------------
#
# $ git log --oneline --all --graph
#
# You should see 5 commits on main plus one diverging commit on
# feature/priority (main and feature/priority split after "Add
# delete_task function"). Answer: main is 2 commits ahead of the
# point where feature/priority branched off, and feature/priority has
# 1 commit main doesn't have -- this is exactly the "diverged" shape
# from the lesson's rebase section.


# --- Task 2: Check status and diff before touching anything --------
#
# $ git status
#
# tasks.py should show as "Changes not staged for commit" -- this is
# the dirty DEBUG = True line starter.py deliberately left uncommitted.
#
# $ git diff
#
# Shows exactly that one addition, in diff format (+ lines only, since
# nothing was removed).


# --- Task 3: Discard the uncommitted change ------------------------
#
# $ git restore tasks.py
# $ git status
#
# Expected: "nothing to commit, working tree clean" -- the DEBUG line
# is gone. This is the safe, correct tool here specifically because
# the change was never committed; restore only touches uncommitted
# work.


# --- Task 4: Trigger and resolve a real merge conflict --------------
#
# $ git merge feature/priority
#
# Expected: a real CONFLICT (content): Merge conflict in tasks.py.
# Both main and feature/priority edited add_task()'s signature and
# body differently -- main added validation, feature/priority added a
# priority parameter.
#
# Open tasks.py, find the <<<<<<< HEAD / ======= / >>>>>>> markers,
# and hand-edit to a single correct version keeping BOTH changes:
#
#     def add_task(tasks, description, priority="normal"):
#         if not description.strip():
#             raise ValueError("description cannot be empty")
#         tasks.append({"description": description, "done": False, "priority": priority})
#         return tasks
#
# Then:
#
# $ git add tasks.py
# $ git commit -m "Merge feature/priority into main"
# $ git log --oneline --graph --all
#
# Expected: a merge commit with two parents, visible as a |\ / |/
# shape in the graph -- exactly like Sub-topic 4 of the lesson.


# --- Task 5: Verify the resolved code actually works ----------------
#
# After Task 4, confirm your resolution is correct Python, not just
# conflict-marker-free text:
#
# $ python3 -c "
# import tasks
# t = []
# tasks.add_task(t, 'write docs', priority='high')
# tasks.list_tasks(t)
# try:
#     tasks.add_task(t, '   ')
# except ValueError as e:
#     print('correctly raised:', e)
# "
#
# Expected output:
#     [ ] 1. write docs
#     correctly raised: description cannot be empty
#
# If this raises an unrelated error (like a duplicate "return tasks"
# line, a common conflict-resolution mistake), your merge resolution
# has a bug -- go back and fix tasks.py directly.


# --- Task 6: Recover the "lost" commit with reflog -------------------
#
# starter.py committed "Add task_count helper" and then immediately
# ran `git reset --hard HEAD~1`, so it doesn't show in `git log`
# anymore -- but it isn't gone.
#
# $ git log --oneline
#
# (task_count helper is NOT visible here -- this is expected)
#
# $ git reflog
#
# Look for a line like:
#     abc1234 HEAD@{1}: commit: Add task_count helper
#
# Recover it either by resetting straight to that hash (safe here,
# since it's simply moving forward again on the same line of history):
#
# $ git reset --hard abc1234
#
# ...or, since after Task 4's merge commit main has moved on, the more
# broadly correct tool is actually cherry-pick (replay just that one
# commit's change onto wherever you currently are, without discarding
# anything since):
#
# $ git cherry-pick abc1234
#
# Both were tested against this exact scenario and work. Use whichever
# the lesson's Sub-topic 6 reflog explanation makes clearer to you --
# the teaching point is the same either way: reflog remembers commits
# git log doesn't show anymore.


# --- Task 7: Stash a change, then bring it back ----------------------
#
# $ echo "\n\ndef pending_count(tasks):\n    return len([t for t in tasks if not t['done']])" >> tasks.py
# $ git status
# (shows tasks.py modified, unstaged)
#
# $ git stash
# $ git status
# (working tree clean again -- but the change isn't gone)
#
# $ git stash list
# (shows stash@{0}: WIP on main: ...)
#
# $ git stash pop
# $ git status
# (tasks.py is modified again, exactly as before -- and the stash
# entry is now gone from `git stash list`)


# --- Task 8 (Debug the Code) -----------------------------------------
#
# Scenario: a teammate says "I ran git reset --hard on the wrong
# branch and now my last three commits are just gone from git log --
# is my work actually lost?"
#
# Bug in their reasoning: `git reset --hard` moves the branch pointer
# and updates the working tree, but it does NOT delete the commit
# objects themselves -- they become unreachable from any branch, not
# deleted, and git's reflog (a separate, local record of everywhere
# HEAD has pointed) still has them for about 90 days by default.
#
# Fix (the actual recovery procedure):
#
# $ git reflog
# (find the commit hash from right before the reset ran)
# $ git reset --hard <that-hash>
#
# This is recoverable specifically because reflog is local -- it would
# NOT help if the mistake happened only on a remote/shared repository
# nobody has a local reflog for.


# --- Task 9 (scenario / interview-style): the hotfix question -------
#
# Scenario: you're two days into a messy, half-broken feature branch
# when a production bug needs an urgent fix based on the CURRENT
# stable code, not your in-progress feature. What do you do?
#
# Answer: switch back to main (your feature branch's changes stay
# completely untouched, since they only exist on that branch's own
# commits), branch off main's current tip for the hotfix, fix and
# commit there, merge/ship the hotfix independently, then return to
# the feature branch exactly as you left it:
#
# $ git switch main
# $ git switch -c hotfix/urgent-fix
# # ... make the fix, commit it ...
# $ git switch main
# $ git merge hotfix/urgent-fix
# # ... ship main ...
# $ git switch feature/my-in-progress-work
# # your half-finished work is exactly as you left it
#
# This is the exact scenario from the lesson's hook, and branching
# (Sub-topic 3) is precisely the mechanism that makes it routine
# instead of a crisis.
