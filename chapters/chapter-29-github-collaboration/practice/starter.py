"""
Chapter 29 Practice Bank: GitHub & Collaboration
See README.md in this folder for full instructions.
Run this from inside the practice/ folder: python3 starter.py

Standard library only -- no installs needed. This chapter builds on
Chapter 28 (local git: commits, branches, merge, rebase, conflicts,
undo) and covers the remote/collaboration layer on top of it: remotes,
forking vs. cloning, pull requests, code review, issues, and an
end-to-end collaboration workflow. Since a browser/grader can't run
real git commands, every task here reasons about or simulates GitHub
collaboration concepts as plain Python data and functions -- but every
piece of git/GitHub behavior described was checked against a real
local bare-repo simulation before being written down here.
"""

# ============================================================
# Topic 1: Remotes (origin, push/pull/fetch, tracking branches)
# ============================================================

# TODO 1.1: Write remote_url_for(remotes, name). Given a dict like
# {"origin": "https://github.com/me/repo.git"}, return the URL for
# the given remote name, or None if it doesn't exist.


# TODO 1.2: Write is_fast_forward_pull(local_only_commits, remote_only_commits).
# Given how many commits exist only on the local branch and only on
# the remote-tracking branch since their common ancestor, return True
# if a `git pull` would fast-forward cleanly (no local-only commits,
# at least the branches aren't identical -- remote_only_commits can be
# 0 or more) and False if it would need a merge/rebase (local_only_commits > 0
# and remote_only_commits > 0, i.e. the histories have diverged).


# TODO 1.3 (Debug the Code): explain_fetch_vs_pull() below wrongly
# claims `git fetch` changes your working directory files. Fix its
# return value -- fetch only updates remote-tracking refs (like
# origin/main); it never touches your working tree or current branch.
def explain_fetch_vs_pull():
    return "git fetch immediately updates the files in your working directory to match the remote."


print(explain_fetch_vs_pull())


# TODO 1.4: Write has_tracking_branch(branch_info). Given a dict like
# {"name": "newbranch", "upstream": "origin/newbranch"} or
# {"name": "newbranch2", "upstream": None}, return True if the branch
# has an upstream (tracking) branch set, else False.


# TODO 1.A (Scenario -- Silent Push Confusion): A teammate ran
# `git push origin feature-x` (no -u flag) for the first time on a
# brand-new local branch. The push succeeded and the branch now exists
# on GitHub, but next time they just type `git push` with no
# arguments, git complains it doesn't know where to push. Write
# needs_dash_u_explanation(used_dash_u_on_first_push). Return a short
# string explaining why the second push failed when
# used_dash_u_on_first_push is False, or a string confirming it would
# have worked fine when it is True.


# TODO 1.B (Scenario -- Interview Prep): write
# explain_fetch_then_pull_workflow() describing why experienced
# developers often run `git fetch` followed by inspecting the changes
# (e.g. `git log main..origin/main`) before running `git pull` or
# `git merge`, instead of pulling blindly.


# ============================================================
# Topic 2: Forking vs. Cloning
# ============================================================

# TODO 2.1: Write correct_workflow_for(has_write_access). Given
# whether a contributor has write (push) access to the target
# repository, return "clone" if has_write_access is True (they can
# clone the repo directly and push branches), or "fork" if False (they
# need their own fork to push to, then open a PR back to the original).


# TODO 2.2: Write remote_setup_after_fork(). Return a list of two
# remote names, in the order they'd typically be added, that an
# external contributor sets up after forking and cloning their fork:
# the remote pointing at their own fork (conventionally "origin") and
# the remote pointing at the original repo they forked from
# (conventionally "upstream"). Return ["origin", "upstream"].


# TODO 2.3 (Debug the Code): explain_fork_relationship() below wrongly
# claims a fork automatically stays in sync with the original repo
# forever. Fix its return value -- a fork is a snapshot copy at fork
# time; it only gets new commits from the original when you explicitly
# fetch/merge (or use GitHub's "Sync fork" button).
def explain_fork_relationship():
    return "A fork automatically updates itself whenever the original repository changes, with no action needed."


print(explain_fork_relationship())


# TODO 2.A (Scenario -- Open Source First Contribution): write
# first_contribution_steps(has_write_access). This stands in for
# planning a first contribution to a public open-source project the
# contributor does NOT have write access to. Return a list of strings
# in order: if has_write_access is False, return
# ["fork", "clone your fork", "create a branch", "push to your fork", "open a pull request"].
# If has_write_access is True, return
# ["clone", "create a branch", "push to origin", "open a pull request"].


# TODO 2.B (Scenario -- Interview Prep): write
# explain_fork_vs_clone() describing the actual difference between
# forking and cloning -- forking creates a new repository (a copy)
# under your own GitHub account/organization, while cloning just
# downloads an existing repository (any repository, including your own
# fork) to your local machine. You clone your fork after forking it.


# ============================================================
# Topic 3: Pull Requests (workflow, descriptions, draft PRs)
# ============================================================

# TODO 3.1: Write is_ready_for_review(is_draft, has_description, tests_passing).
# Return True only if is_draft is False AND has_description is True AND
# tests_passing is True -- otherwise False.


# TODO 3.2: Write pr_title_quality(title). Return "good" if title is a
# non-empty string, is at most 72 characters, and does NOT start with a
# lowercase "fix" or "update" alone with no other context (i.e. the
# title is not exactly "fix" or exactly "update", case-insensitive,
# after stripping whitespace). Otherwise return "needs work".


# TODO 3.3 (Debug the Code): should_open_draft_pr() below has its
# condition backwards -- it returns True (open as draft) when the work
# IS finished, and False when it ISN'T. Fix it: a draft PR is for work
# that is still in progress (not yet finished), used to get early
# feedback or show progress, not for finished work ready for review.
def should_open_draft_pr(work_is_finished):
    return work_is_finished


print("should_open_draft_pr(False):", should_open_draft_pr(False))


# TODO 3.A (Scenario -- Merge Conflict Blocking a PR): write
# safe_way_to_update_stale_pr(commits_behind_upstream, has_open_pr).
# Your fork's feature branch (with an open pull request) has fallen
# `commits_behind_upstream` commits behind the upstream default
# branch. Return the string "fetch upstream, then rebase (or merge)
# your feature branch onto upstream's default branch, then push"
# if commits_behind_upstream > 0 and has_open_pr is True. Return
# "nothing to do, already up to date" if commits_behind_upstream == 0.
# (This mirrors the real fork-behind-upstream situation verified
# against a live bare-repo simulation: fetching upstream and rebasing
# the feature branch keeps your PR's commits intact instead of
# discarding them.)


# TODO 3.B (Scenario -- Interview Prep): write
# explain_good_pr_description() describing what a strong pull request
# description includes: what changed and why, how to test/verify it,
# and links to any related issue (e.g. "Closes #42").


# ============================================================
# Topic 4: Code Review (what reviewers look for, giving/receiving feedback)
# ============================================================

# TODO 4.1: Write review_verdict(comment_type). Given a string that is
# one of "approve", "request_changes", or "comment", return "merge
# allowed" if comment_type == "approve", "blocked" if comment_type ==
# "request_changes", and "informational only" if comment_type ==
# "comment".


# TODO 4.2: Write count_blocking_reviews(review_types). Given a list of
# strings each one of "approve", "request_changes", "comment", return
# how many of them are "request_changes" (the count of reviews that
# block merging until addressed).


# TODO 4.3 (Debug the Code): is_approval_with_followup() below is
# supposed to detect the common ambiguous case where a reviewer
# approves but also leaves a follow-up ask (e.g. "LGTM but can you add
# a test?") -- it should return True only when review_type is
# "approve" AND has_followup_request is True, but it currently ignores
# has_followup_request entirely.
def is_approval_with_followup(review_type, has_followup_request):
    return review_type == "approve"


print("is_approval_with_followup('approve', True):", is_approval_with_followup("approve", True))


# TODO 4.A (Scenario -- "LGTM but can you add a test?"): write
# interpret_lgtm_with_ask(review_type, has_followup_request). A
# reviewer left an "approve" review whose comment text was "LGTM but
# can you add a test?" Return the string "technically approved to
# merge, but you should still add the test as a courtesy before
# merging" when review_type == "approve" and has_followup_request is
# True. Return "blocked -- address the requested changes first" when
# review_type == "request_changes". Otherwise return "no action
# required yet".


# TODO 4.B (Scenario -- Interview Prep): write
# explain_good_code_review_feedback() describing what makes review
# feedback constructive: specific and actionable (points at a line/
# reason, not just "this is wrong"), distinguishes must-fix issues from
# optional nitpicks, and assumes good intent from the author.


# ============================================================
# Topic 5: Issues & Project Workflow (good issues, labels, linking to PRs)
# ============================================================

# TODO 5.1: Write has_minimum_issue_quality(title, has_repro_steps, has_expected_behavior).
# Return True only if title is a non-empty string AND has_repro_steps
# is True AND has_expected_behavior is True.


# TODO 5.2: Write issue_labels_for(is_bug, is_feature_request, blocks_release).
# Build and return a list of label strings: include "bug" if is_bug,
# include "enhancement" if is_feature_request, include "priority:high"
# if blocks_release. Return them in that order (only the ones that
# apply).


# TODO 5.3 (Debug the Code): closes_issue_on_merge() below checks for
# the literal word "closes" only in uppercase, so it misses the
# common lowercase usage. Fix it to be case-insensitive when checking
# whether a PR description contains a closing keyword ("closes",
# "fixes", or "resolves") followed by an issue reference.
def closes_issue_on_merge(pr_description):
    return "Closes #" in pr_description or "Fixes #" in pr_description or "Resolves #" in pr_description


print("closes_issue_on_merge('closes #12'):", closes_issue_on_merge("closes #12"))


# TODO 5.A (Scenario -- Triaging a Vague Bug Report): write
# triage_action(has_repro_steps, has_expected_behavior). An incoming
# issue just says "the app is broken, please fix." Return "ask for
# reproduction steps and expected behavior before triaging further" if
# both has_repro_steps and has_expected_behavior are False. Return
# "ready to triage" if both are True. Return "ask for the missing
# details" if only one is True.


# TODO 5.B (Scenario -- Interview Prep): write
# explain_good_issue_vs_bad_issue() describing the difference between
# a well-written issue (clear title, steps to reproduce, expected vs.
# actual behavior, environment details) and a vague one ("it doesn't
# work") that a maintainer can't act on.


# ============================================================
# Topic 6: Real-World End-to-End Collaboration Scenario
# ============================================================

# TODO 6.1: Write next_step_in_workflow(step). Given the current step
# as one of "forked", "cloned", "branched", "committed", "pushed",
# "opened_pr", "reviewed", "approved", return the next step in this
# fixed order: forked -> cloned -> branched -> committed -> pushed ->
# opened_pr -> reviewed -> approved -> "merged". Return the correct
# next-step string for the given current step.


# TODO 6.2: Write is_safe_to_merge(approved, ci_passing, has_conflicts).
# Return True only if approved is True AND ci_passing is True AND
# has_conflicts is False.


# TODO 6.3 (Debug the Code): full_workflow_valid() below is supposed
# to check that every required step ("forked", "branched", "pushed",
# "opened_pr") appears somewhere in the given steps list, but it only
# checks the first element instead of checking membership across the
# whole list. Fix it.
def full_workflow_valid(steps):
    required = ["forked", "branched", "pushed", "opened_pr"]
    return steps[0] in required


print("full_workflow_valid(['forked','branched','pushed','opened_pr']):",
      full_workflow_valid(["forked", "branched", "pushed", "opened_pr"]))


# TODO 6.A (Scenario -- End-to-End Contribution): write
# plan_contribution(has_write_access, issue_number). Simulate planning
# a full contribution to a project given whether the contributor has
# write access and the issue number they're fixing (or None if not
# tied to an issue). Return a list of ordered step strings: start with
# "fork" if has_write_access is False, else "clone" if True; then
# always append "branch", "commit", "push", and finally "open PR
# referencing #<issue_number>" if issue_number is not None, else
# "open PR".


# TODO 6.B (Scenario -- Interview Prep): write
# explain_end_to_end_collaboration() describing, in your own words,
# the full loop a change goes through on a real team: an issue is
# filed, a contributor forks/clones and branches, commits and pushes,
# opens a pull request linked to the issue, a reviewer gives feedback,
# the author responds (more commits, or discussion), the PR is
# approved and CI passes, and it gets merged -- closing the issue.
