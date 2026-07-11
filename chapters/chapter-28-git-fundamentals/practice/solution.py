"""
Chapter 28 Practice Bank: Git Fundamentals -- reference solution.
Run this from inside the practice/ folder: python3 solution.py
"""

# ============================================================
# Topic 1: Why Version Control Matters
# ============================================================

# TODO 1.1
def count_versions_without_git(filenames):
    return sum(1 for name in filenames if "final" in name.lower())


print(count_versions_without_git(["report.docx", "report_final.docx", "report_final_v2.docx"]))


# TODO 1.2
def can_two_people_edit_safely(uses_git):
    return uses_git is True


print(can_two_people_edit_safely(True))
print(can_two_people_edit_safely(False))


# TODO 1.3 (Debug the Code)
# Bug: claimed git only tracks the current state, like a shared folder.
# In fact git stores a full history of committed snapshots, with a
# complete log of who changed what and when.
def explain_what_git_tracks():
    return (
        "Git tracks a full history of committed snapshots over time, not "
        "just the current state -- every commit records who changed what "
        "and when, and any earlier version can be inspected or restored."
    )


print(explain_what_git_tracks())


# TODO 1.A (Scenario -- Comparing Two Approaches)
def safer_collaboration_choice(team_size, needs_history):
    if team_size > 1 or needs_history:
        return "git"
    return "either is fine"


print(safer_collaboration_choice(3, False))
print(safer_collaboration_choice(1, False))


# TODO 1.B (Scenario -- Interview Prep)
def explain_why_version_control_matters():
    return (
        "Version control lets multiple people change the same codebase "
        "without overwriting each other's work, since every change is "
        "tracked as its own commit and can be merged rather than blindly "
        "replaced. It also gives the whole project a searchable history "
        "-- who changed what, when, and why -- so you can find when a bug "
        "was introduced or safely undo a bad change."
    )


print(explain_why_version_control_matters())


# ============================================================
# Topic 2: The Core Git Workflow (init, add, commit, status,
# diff, log, staging area)
# ============================================================

# TODO 2.1
def files_in_staging_area(added_files, committed_files):
    return [f for f in added_files if f not in committed_files]


print(files_in_staging_area(["a.py", "b.py"], ["a.py"]))


# TODO 2.2
def is_working_tree_clean(staged, unstaged):
    return len(staged) == 0 and len(unstaged) == 0


print(is_working_tree_clean([], []))
print(is_working_tree_clean(["a.py"], []))


# TODO 2.3 (Debug the Code)
# Bug: claimed 'git add' immediately and permanently commits a file. In
# fact 'git add' only moves it into the staging area -- it's not part
# of project history until a following 'git commit'.
def describe_staging_area():
    return (
        "Running 'git add' on a file only moves it into the staging "
        "area, marking it ready to be included in the NEXT commit -- "
        "the file isn't part of the project's committed history until "
        "'git commit' actually runs."
    )


print(describe_staging_area())


# TODO 2.A (Scenario -- Comparing Two Approaches)
def should_run_status_first(has_uncommitted_changes):
    return has_uncommitted_changes is True


print(should_run_status_first(True))
print(should_run_status_first(False))


# TODO 2.B (Scenario -- Interview Prep)
def explain_add_then_commit():
    return (
        "Splitting 'add' and 'commit' into two steps lets you build a "
        "commit deliberately -- you can stage only some of the files (or "
        "even part of a file with 'git add -p') you changed, review "
        "exactly what's staged with 'git status'/'git diff --staged', "
        "and leave unrelated in-progress changes out of that commit "
        "entirely, instead of every edit in the working directory being "
        "forced into one commit."
    )


print(explain_add_then_commit())


# ============================================================
# Topic 3: Branching (create/switch/delete, branch-as-pointer)
# ============================================================

# TODO 3.1
def new_branch_points_to(current_commit):
    return current_commit


print(new_branch_points_to("c1"))


# TODO 3.2
def commits_on_branch_after(history, branch_start_commit, new_commits):
    return [branch_start_commit] + list(new_commits)


print(commits_on_branch_after([], "c1", ["c2", "c3"]))


# TODO 3.3 (Debug the Code)
# Bug: claimed deleting a branch instantly erases its commits forever.
# In fact deleting a branch just removes the pointer/label -- the
# commits stay reachable (e.g. via reflog, another branch, or a tag)
# until git's garbage collector eventually cleans up truly unreachable
# ones.
def explain_branch_deletion():
    return (
        "Deleting a branch with 'git branch -d' only removes that "
        "pointer/label -- the commits it pointed to are not erased "
        "immediately. They stay reachable (via the reflog, another "
        "branch, or a tag) until git's garbage collector eventually "
        "cleans up commits that are truly unreachable from anywhere."
    )


print(explain_branch_deletion())


# TODO 3.A (Scenario -- Comparing Two Approaches)
def should_delete_branch(is_merged, still_needed):
    return is_merged is True and still_needed is False


print(should_delete_branch(True, False))
print(should_delete_branch(False, False))


# TODO 3.B (Scenario -- Interview Prep)
def explain_branch_as_pointer():
    return (
        "A branch is just a movable label pointing at one commit -- not "
        "a separate copy of every file. Creating a branch is cheap "
        "(just writing a new pointer), and committing on a branch simply "
        "moves that pointer to the new commit. This is different from "
        "thinking of a branch as its own full copy of the project, which "
        "would be slow to create and expensive to store."
    )


print(explain_branch_as_pointer())


# ============================================================
# Topic 4: Merging (fast-forward vs. three-way, merge commits,
# resolving conflicts)
# ============================================================

# TODO 4.1
def is_fast_forward_possible(target_branch_commits, source_branch_commits):
    n = len(target_branch_commits)
    if n > len(source_branch_commits):
        return False
    return list(source_branch_commits[:n]) == list(target_branch_commits)


print(is_fast_forward_possible(["c1"], ["c1", "c2"]))
print(is_fast_forward_possible(["c1", "c3"], ["c1", "c2"]))


# TODO 4.2
def merge_creates_commit(is_fast_forward):
    return is_fast_forward is False


print(merge_creates_commit(False))
print(merge_creates_commit(True))


# TODO 4.3 (Debug the Code)
# Bug: had HEAD/incoming order reversed. Verified against real git: the
# CURRENT branch (HEAD) content is shown first, then "=======", then
# the branch being merged in, then the ">>>>>>> branchname" marker.
def conflict_marker_order():
    return ["<<<<<<< HEAD", "current branch content", "=======", "incoming branch content", ">>>>>>> other-branch"]


print(conflict_marker_order())


# TODO 4.A (Scenario -- Comparing Two Approaches)
def predict_merge_type(target_has_new_commits):
    return "three-way" if target_has_new_commits else "fast-forward"


print(predict_merge_type(True))
print(predict_merge_type(False))


# TODO 4.B (Scenario -- Interview Prep)
def explain_resolving_a_conflict():
    return (
        "Open the file git flagged as conflicted and find the "
        "<<<<<<< HEAD / ======= / >>>>>>> markers. The section above "
        "the ======= is your current branch's version, the section "
        "below is the incoming branch's version. Decide what the final "
        "content should actually be -- keep one side, the other, or a "
        "combination -- then delete the marker lines entirely, save the "
        "file, 'git add' it to mark the conflict resolved, and commit."
    )


print(explain_resolving_a_conflict())


# ============================================================
# Topic 5: Rebase (vs. merge, interactive rebase basics, don't
# rebase shared history)
# ============================================================

# TODO 5.1
def rebase_result_is_linear():
    return True


print(rebase_result_is_linear())


# TODO 5.2
def commit_hashes_change_after_rebase(original_hashes):
    return [h + "'" for h in original_hashes]


print(commit_hashes_change_after_rebase(["c2", "c3"]))


# TODO 5.3 (Debug the Code)
# Bug: always returned True. Rebasing a branch other people already
# pulled and built on top of rewrites history they have locally,
# causing painful divergence -- only safe when nobody else depends on
# the current commits.
def should_rebase_shared_branch(is_shared_with_others):
    return is_shared_with_others is False


print(should_rebase_shared_branch(True))
print(should_rebase_shared_branch(False))


# TODO 5.A (Scenario -- Comparing Two Approaches)
def choose_merge_or_rebase(branch_is_shared, wants_linear_history):
    if branch_is_shared:
        return "merge"
    return "rebase" if wants_linear_history else "merge"


print(choose_merge_or_rebase(True, True))
print(choose_merge_or_rebase(False, True))
print(choose_merge_or_rebase(False, False))


# TODO 5.B (Scenario -- Interview Prep)
def explain_why_not_rebase_shared_history():
    return (
        "Rebasing replays commits as brand-new commit objects with new "
        "hashes, even though the content looks the same. If someone "
        "already pulled the old commits and force-pushing replaces them "
        "on the remote, everyone else's local branch now points at "
        "commits that no longer exist upstream -- their next pull either "
        "creates a confusing duplicate history or fails outright, and "
        "they have to manually reconcile diverged branches."
    )


print(explain_why_not_rebase_shared_history())


# ============================================================
# Topic 6: Undoing Things Safely (checkout/restore vs. reset vs.
# revert, stashing, reflog)
# ============================================================

# TODO 6.1
def revert_keeps_history_length(original_commit_count):
    return original_commit_count + 1


print(revert_keeps_history_length(5))


# TODO 6.2
def reset_hard_removes_from_log(original_commit_count, commits_reset_away):
    return original_commit_count - commits_reset_away


print(reset_hard_removes_from_log(5, 2))


# TODO 6.3 (Debug the Code)
# Bug: always recommended "reset". For a commit that's already been
# pushed and pulled by others, 'git reset --hard' rewrites shared
# history (the same danger as rebasing shared history in Topic 5) --
# 'git revert' is the safe choice there because it adds a new commit
# instead of erasing old ones. Reset is fine for local-only work.
def safe_undo_for_pushed_commit(already_shared):
    return "revert" if already_shared else "reset"


print(safe_undo_for_pushed_commit(True))
print(safe_undo_for_pushed_commit(False))


# TODO 6.A (Scenario -- Recovering "Lost" Work)
def can_recover_after_hard_reset(reflog_still_has_entry):
    return reflog_still_has_entry is True


print(can_recover_after_hard_reset(True))
print(can_recover_after_hard_reset(False))


# TODO 6.B (Scenario -- Interview Prep)
def explain_reset_vs_revert():
    return (
        "'git reset' moves the current branch's pointer to an earlier "
        "commit -- with --hard it also rewrites the working directory to "
        "match, and any commits after that point stop showing up in "
        "'git log' (though they're still recoverable via the reflog for "
        "a while). 'git revert' never moves the pointer backward or "
        "deletes anything -- it adds a brand-new commit that applies the "
        "opposite change. Because revert only adds history instead of "
        "erasing it, it's the safe choice once a commit has been shared "
        "with others; reset --hard on a shared commit rewrites history "
        "they already have."
    )


print(explain_reset_vs_revert())
