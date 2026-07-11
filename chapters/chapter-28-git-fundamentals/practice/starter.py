"""
Chapter 28 Practice Bank: Git Fundamentals
See README.md in this folder for full instructions.
Run this from inside the practice/ folder: python3 starter.py

Standard library only -- no installs needed. These problems teach git by
having you write Python functions that SIMULATE or REASON ABOUT git
concepts using plain data (lists, dicts, strings) standing in for a repo's
history -- the same way the chapter's challenges.html works. Every
behavior described here was checked against real git in a scratch repo
before being written into this file.
"""

# ============================================================
# Topic 1: Why Version Control Matters
# ============================================================

# TODO 1.1: Write count_versions_without_git(filenames). Given a list of
# filenames like ["report.docx", "report_final.docx",
# "report_final_v2.docx"], return how many of them contain the substring
# "final" (case-insensitive) -- a stand-in for "how many manual backup
# copies did this workflow produce because there was no real version
# control."


# TODO 1.2: Write can_two_people_edit_safely(uses_git). Return True if
# uses_git is True (git tracks independent changes and merges them),
# else False (without it, simultaneous edits silently overwrite).


# TODO 1.3 (Debug the Code): explain_what_git_tracks() below wrongly
# claims git only tracks the CURRENT state of files, like a shared
# folder. Fix its return value to describe what git actually tracks.
def explain_what_git_tracks():
    return "Git only keeps the current version of each file, the same as a shared drive folder."


print(explain_what_git_tracks())


# TODO 1.A (Scenario -- Comparing Two Approaches): write
# safer_collaboration_choice(team_size, needs_history). Return "git" if
# team_size > 1 or needs_history is True, else "either is fine" (a
# single person with no need to look back can technically get by
# without it, though git is still recommended in practice).


# TODO 1.B (Scenario -- Interview Prep): write
# explain_why_version_control_matters() describing, in your own words,
# what problem version control solves for a team (not just "it saves
# versions" -- mention collaboration and history).


# ============================================================
# Topic 2: The Core Git Workflow (init, add, commit, status,
# diff, log, staging area)
# ============================================================

# TODO 2.1: Write files_in_staging_area(added_files, committed_files).
# Given two lists, return the list of filenames that have been `git
# add`-ed but not yet committed (present in added_files but not in
# committed_files), preserving added_files's order.


# TODO 2.2: Write is_working_tree_clean(staged, unstaged). Return True
# only if both staged and unstaged (lists of filenames) are empty --
# this is what `git status` reports as "nothing to commit, working tree
# clean."


# TODO 2.3 (Debug the Code): describe_staging_area() below wrongly
# claims `git add` immediately creates a permanent commit. Fix its
# return value to describe the staging area correctly.
def describe_staging_area():
    return "Running 'git add' on a file immediately and permanently commits it to the project history."


print(describe_staging_area())


# TODO 2.A (Scenario -- Comparing Two Approaches): write
# should_run_status_first(has_uncommitted_changes). A teammate is about
# to run `git commit` but isn't sure what will be included. Return True
# (recommend running `git status` first) if has_uncommitted_changes is
# True, else False (nothing pending, no need).


# TODO 2.B (Scenario -- Interview Prep): write
# explain_add_then_commit() describing why git splits "stage" (git add)
# and "commit" into two separate steps instead of committing the whole
# working directory in one command.


# ============================================================
# Topic 3: Branching (create/switch/delete, branch-as-pointer)
# ============================================================

# TODO 3.1: Write new_branch_points_to(current_commit). When you create
# a new branch with `git branch <name>` (or `git checkout -b <name>`),
# it starts out pointing at the SAME commit as the branch you branched
# from. Return current_commit unchanged -- this models that starting
# point.


# TODO 3.2: Write commits_on_branch_after(history, branch_start_commit,
# new_commits). Given a starting commit id and a list of new commit ids
# added after switching to that branch, return branch_start_commit
# followed by all of new_commits, in order -- this models how a
# branch's pointer advances one commit at a time as you commit on it.


# TODO 3.3 (Debug the Code): explain_branch_deletion() below wrongly
# claims deleting a branch deletes its commits from the repository
# forever, immediately. Fix its return value -- deleting a branch just
# removes the pointer/label; the commits are still reachable (e.g. via
# reflog or another branch/tag) until git's garbage collector eventually
# cleans up genuinely unreachable ones.
def explain_branch_deletion():
    return "Deleting a branch with 'git branch -d' instantly and permanently erases every commit that was ever made on it."


print(explain_branch_deletion())


# TODO 3.A (Scenario -- Comparing Two Approaches): write
# should_delete_branch(is_merged, still_needed). A teammate finished a
# feature branch and merged it. Return True (safe to delete) only if
# is_merged is True and still_needed is False.


# TODO 3.B (Scenario -- Interview Prep): write
# explain_branch_as_pointer() describing the "branch is just a movable
# pointer to a commit" mental model, and how that's different from
# thinking of a branch as its own copy of every file.


# ============================================================
# Topic 4: Merging (fast-forward vs. three-way, merge commits,
# resolving conflicts)
# ============================================================

# TODO 4.1: Write is_fast_forward_possible(target_branch_commits,
# source_branch_commits). Both arguments are lists of commit ids
# representing each branch's full history from the root, in order (so
# the last element is each branch's tip). A fast-forward merge of
# source_branch_commits INTO target_branch_commits is possible only if
# every commit in target_branch_commits also appears, in the same
# order, as a prefix of source_branch_commits (i.e. target's tip commit
# is somewhere in source's history and target hasn't diverged). Return
# True/False.


# TODO 4.2: Write merge_creates_commit(is_fast_forward). A three-way
# merge always creates a new merge commit; a fast-forward merge does
# not (the target branch's pointer just moves). Return True if
# is_fast_forward is False, else False.


# TODO 4.3 (Debug the Code): conflict_marker_order() below has the
# HEAD/incoming order backwards. In a real conflict, git shows the
# CURRENT branch's (HEAD's) version first, then a "=======" divider,
# then the branch being merged in, then a ">>>>>>> branchname" marker.
# Fix the order below.
def conflict_marker_order():
    return ["<<<<<<< HEAD", "incoming branch content", "=======", "current branch content", ">>>>>>> other-branch"]


print(conflict_marker_order())


# TODO 4.A (Scenario -- Comparing Two Approaches): write
# predict_merge_type(target_has_new_commits). A teammate wants to merge
# their feature branch into main. Return "three-way" if
# target_has_new_commits is True (main moved on since the branch point),
# else "fast-forward".


# TODO 4.B (Scenario -- Interview Prep): write
# explain_resolving_a_conflict() describing, step by step in plain
# language, what a developer actually does when git reports a merge
# conflict (open the file, look for the markers, decide what the final
# content should be, remove the markers, stage the file, then commit).


# ============================================================
# Topic 5: Rebase (vs. merge, interactive rebase basics, don't
# rebase shared history)
# ============================================================

# TODO 5.1: Write rebase_result_is_linear(). A rebase replays your
# branch's commits one by one on top of the target branch's tip, so the
# resulting history has no merge commit and no diverging paths -- it's
# a single straight line. Return True.


# TODO 5.2: Write commit_hashes_change_after_rebase(original_hashes).
# Rebase rewrites every replayed commit (new parent means a new commit
# object, so a new hash), even though the content/message stays the
# same. Given a list of original commit hashes/ids, return a NEW list
# of the same length where every element is a different value than the
# original at that position (e.g. append "'" to each) -- this models
# "same commits, new identities."


# TODO 5.3 (Debug the Code): should_rebase_shared_branch() below always
# says it's safe to rebase. Fix it: rebasing a branch that other people
# have already pulled and built work on top of is NOT safe -- it
# rewrites history they already have, causing painful divergence for
# everyone else. Only rebase when is_shared_with_others is False.
def should_rebase_shared_branch(is_shared_with_others):
    return True


print(should_rebase_shared_branch(True))


# TODO 5.A (Scenario -- Comparing Two Approaches): write
# choose_merge_or_rebase(branch_is_shared, wants_linear_history). Return
# "merge" if branch_is_shared is True (never rewrite shared history),
# else return "rebase" if wants_linear_history is True, else "merge".


# TODO 5.B (Scenario -- Interview Prep): write
# explain_why_not_rebase_shared_history() describing what breaks for
# collaborators when someone force-pushes a rebased branch that others
# already pulled.


# ============================================================
# Topic 6: Undoing Things Safely (checkout/restore vs. reset vs.
# revert, stashing, reflog)
# ============================================================

# TODO 6.1: Write revert_keeps_history_length(original_commit_count).
# `git revert` adds a new commit that undoes an earlier one -- it never
# removes commits. Return original_commit_count + 1.


# TODO 6.2: Write reset_hard_removes_from_log(original_commit_count,
# commits_reset_away). `git reset --hard` moves the branch pointer
# backward, so `git log` no longer shows the reset-away commits (even
# though they're still recoverable via reflog until garbage collected).
# Return original_commit_count - commits_reset_away.


# TODO 6.3 (Debug the Code): safe_undo_for_pushed_commit() below always
# recommends "reset". For a commit that has ALREADY been pushed and
# pulled by others, reset --hard rewrites shared history (same danger
# as Topic 5's rebase problem) -- revert is the safe choice because it
# adds a new commit instead of erasing old ones. Fix it: return "revert"
# if already_shared is True, else "reset" is fine for local-only work.
def safe_undo_for_pushed_commit(already_shared):
    return "reset"


print(safe_undo_for_pushed_commit(True))


# TODO 6.A (Scenario -- Recovering "Lost" Work): write
# can_recover_after_hard_reset(reflog_still_has_entry). A teammate
# panics after `git reset --hard` wiped commits from `git log`. Return
# True if reflog_still_has_entry is True (git hasn't garbage collected
# it yet, so `git reset --hard <reflog-hash>` can bring it back), else
# False.


# TODO 6.B (Scenario -- Interview Prep): write
# explain_reset_vs_revert() describing the core difference: reset moves
# the branch pointer and can discard history (dangerous on shared
# branches), while revert adds a brand-new commit that undoes changes
# without erasing anything (safe on shared branches).
