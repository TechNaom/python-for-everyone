"""
Chapter 29 Practice Bank: GitHub & Collaboration -- REFERENCE SOLUTION
See README.md in this folder for full instructions.
Run this from inside the practice/ folder: python3 solution.py

Standard library only -- no installs needed.
"""

# ============================================================
# Topic 1: Remotes (origin, push/pull/fetch, tracking branches)
# ============================================================

# TODO 1.1
def remote_url_for(remotes, name):
    return remotes.get(name)


# TODO 1.2
def is_fast_forward_pull(local_only_commits, remote_only_commits):
    return local_only_commits == 0


# TODO 1.3
def explain_fetch_vs_pull():
    return (
        "git fetch only downloads new commits and updates remote-tracking "
        "refs like origin/main -- it never touches your working directory "
        "or your current branch. git pull is fetch followed by a merge (or "
        "rebase) into your current branch, which is what actually changes "
        "your working directory files."
    )


print(explain_fetch_vs_pull())


# TODO 1.4
def has_tracking_branch(branch_info):
    return branch_info.get("upstream") is not None


# TODO 1.A
def needs_dash_u_explanation(used_dash_u_on_first_push):
    if used_dash_u_on_first_push:
        return "git push would work fine -- the branch already has an upstream set."
    return (
        "The plain 'git push' fails because the first push never set an "
        "upstream (tracking) branch. 'git push origin feature-x' without -u "
        "creates the branch on the remote but doesn't link it to your local "
        "branch, so git doesn't know where a bare 'git push' should go next "
        "time. Fix it with 'git push -u origin feature-x' once, or add "
        "-u/--set-upstream on that push."
    )


# TODO 1.B
def explain_fetch_then_pull_workflow():
    return (
        "git fetch is non-destructive -- it just updates origin/main "
        "without touching your branch, so you can safely inspect what "
        "changed (e.g. git log main..origin/main or git diff) before "
        "deciding how to bring those changes in. Pulling blindly can "
        "surprise you with a merge commit or a conflict you weren't "
        "expecting; fetch-then-inspect gives you a chance to review first."
    )


# ============================================================
# Topic 2: Forking vs. Cloning
# ============================================================

# TODO 2.1
def correct_workflow_for(has_write_access):
    return "clone" if has_write_access else "fork"


# TODO 2.2
def remote_setup_after_fork():
    return ["origin", "upstream"]


# TODO 2.3
def explain_fork_relationship():
    return (
        "A fork is a snapshot copy taken at the moment you fork it -- it "
        "does NOT automatically stay in sync with the original repository. "
        "To get new commits made to the original after that point, you "
        "must explicitly fetch/merge from an 'upstream' remote pointing at "
        "the original repo, or use GitHub's 'Sync fork' button."
    )


print(explain_fork_relationship())


# TODO 2.A
def first_contribution_steps(has_write_access):
    if has_write_access:
        return ["clone", "create a branch", "push to origin", "open a pull request"]
    return ["fork", "clone your fork", "create a branch", "push to your fork", "open a pull request"]


# TODO 2.B
def explain_fork_vs_clone():
    return (
        "Forking creates a brand-new repository -- a copy under your own "
        "GitHub account or organization -- that exists independently on "
        "GitHub's servers. Cloning just downloads an existing repository "
        "(any repository, including your own fork) to your local machine; "
        "it doesn't create anything new on GitHub. The typical outside-"
        "contributor flow is fork (on GitHub) then clone (your fork, to "
        "your machine)."
    )


# ============================================================
# Topic 3: Pull Requests (workflow, descriptions, draft PRs)
# ============================================================

# TODO 3.1
def is_ready_for_review(is_draft, has_description, tests_passing):
    return (not is_draft) and has_description and tests_passing


# TODO 3.2
def pr_title_quality(title):
    if not title:
        return "needs work"
    if len(title) > 72:
        return "needs work"
    stripped_lower = title.strip().lower()
    if stripped_lower in ("fix", "update"):
        return "needs work"
    return "good"


# TODO 3.3
def should_open_draft_pr(work_is_finished):
    return not work_is_finished


print("should_open_draft_pr(False):", should_open_draft_pr(False))


# TODO 3.A
def safe_way_to_update_stale_pr(commits_behind_upstream, has_open_pr):
    if commits_behind_upstream == 0:
        return "nothing to do, already up to date"
    if has_open_pr:
        return (
            "fetch upstream, then rebase (or merge) your feature branch "
            "onto upstream's default branch, then push"
        )
    return (
        "fetch upstream, then rebase (or merge) your feature branch "
        "onto upstream's default branch, then push"
    )


# TODO 3.B
def explain_good_pr_description():
    return (
        "A strong PR description explains WHAT changed and WHY (not just "
        "a restatement of the diff), HOW to test or verify it (steps, "
        "screenshots, or a demo for UI changes), and links any related "
        "issue with a closing keyword like 'Closes #42' so merging the PR "
        "automatically closes the issue."
    )


# ============================================================
# Topic 4: Code Review (what reviewers look for, giving/receiving feedback)
# ============================================================

# TODO 4.1
def review_verdict(comment_type):
    if comment_type == "approve":
        return "merge allowed"
    if comment_type == "request_changes":
        return "blocked"
    return "informational only"


# TODO 4.2
def count_blocking_reviews(review_types):
    return sum(1 for r in review_types if r == "request_changes")


# TODO 4.3
def is_approval_with_followup(review_type, has_followup_request):
    return review_type == "approve" and has_followup_request


print("is_approval_with_followup('approve', True):", is_approval_with_followup("approve", True))


# TODO 4.A
def interpret_lgtm_with_ask(review_type, has_followup_request):
    if review_type == "approve" and has_followup_request:
        return "technically approved to merge, but you should still add the test as a courtesy before merging"
    if review_type == "request_changes":
        return "blocked -- address the requested changes first"
    return "no action required yet"


# TODO 4.B
def explain_good_code_review_feedback():
    return (
        "Good review feedback is specific and actionable -- it points at "
        "a line and explains the reasoning, not just 'this is wrong'. It "
        "clearly distinguishes must-fix issues (bugs, security, broken "
        "tests) from optional nitpicks (style preference), so the author "
        "knows what's actually blocking. And it assumes good intent -- "
        "asking questions ('what happens if X?') rather than making "
        "accusations."
    )


# ============================================================
# Topic 5: Issues & Project Workflow (good issues, labels, linking to PRs)
# ============================================================

# TODO 5.1
def has_minimum_issue_quality(title, has_repro_steps, has_expected_behavior):
    return bool(title) and has_repro_steps and has_expected_behavior


# TODO 5.2
def issue_labels_for(is_bug, is_feature_request, blocks_release):
    labels = []
    if is_bug:
        labels.append("bug")
    if is_feature_request:
        labels.append("enhancement")
    if blocks_release:
        labels.append("priority:high")
    return labels


# TODO 5.3
def closes_issue_on_merge(pr_description):
    lowered = pr_description.lower()
    return "closes #" in lowered or "fixes #" in lowered or "resolves #" in lowered


print("closes_issue_on_merge('closes #12'):", closes_issue_on_merge("closes #12"))


# TODO 5.A
def triage_action(has_repro_steps, has_expected_behavior):
    if not has_repro_steps and not has_expected_behavior:
        return "ask for reproduction steps and expected behavior before triaging further"
    if has_repro_steps and has_expected_behavior:
        return "ready to triage"
    return "ask for the missing details"


# TODO 5.B
def explain_good_issue_vs_bad_issue():
    return (
        "A well-written issue has a clear, specific title; numbered steps "
        "to reproduce the problem; what you expected to happen vs. what "
        "actually happened; and environment details (OS, version) when "
        "relevant. A vague issue like 'it doesn't work' gives a maintainer "
        "nothing to act on -- they can't reproduce it, don't know what "
        "'working' looks like, and have to spend a round-trip just asking "
        "for the details a good issue would have included up front."
    )


# ============================================================
# Topic 6: Real-World End-to-End Collaboration Scenario
# ============================================================

_WORKFLOW_ORDER = [
    "forked", "cloned", "branched", "committed", "pushed",
    "opened_pr", "reviewed", "approved", "merged",
]


# TODO 6.1
def next_step_in_workflow(step):
    idx = _WORKFLOW_ORDER.index(step)
    return _WORKFLOW_ORDER[idx + 1]


# TODO 6.2
def is_safe_to_merge(approved, ci_passing, has_conflicts):
    return approved and ci_passing and (not has_conflicts)


# TODO 6.3
def full_workflow_valid(steps):
    required = ["forked", "branched", "pushed", "opened_pr"]
    return all(step in steps for step in required)


print("full_workflow_valid(['forked','branched','pushed','opened_pr']):",
      full_workflow_valid(["forked", "branched", "pushed", "opened_pr"]))


# TODO 6.A
def plan_contribution(has_write_access, issue_number):
    steps = ["clone"] if has_write_access else ["fork"]
    steps += ["branch", "commit", "push"]
    if issue_number is not None:
        steps.append(f"open PR referencing #{issue_number}")
    else:
        steps.append("open PR")
    return steps


# TODO 6.B
def explain_end_to_end_collaboration():
    return (
        "An issue is filed describing a bug or feature. A contributor "
        "forks (or clones, if they have write access) the repo, creates a "
        "branch, makes commits, and pushes that branch. They open a pull "
        "request that references the issue (e.g. 'Closes #42'). A "
        "reviewer reads the diff and leaves feedback -- approve, request "
        "changes, or comments. The author responds, often with more "
        "commits addressing the feedback, and the conversation continues "
        "until the reviewer approves. Once the PR is approved and CI is "
        "passing with no conflicts, it gets merged into the default "
        "branch, which automatically closes the linked issue."
    )


if __name__ == "__main__":
    # Quick self-checks so `python3 solution.py` demonstrates everything runs.
    assert remote_url_for({"origin": "https://github.com/me/repo.git"}, "origin") == "https://github.com/me/repo.git"
    assert remote_url_for({}, "origin") is None
    assert is_fast_forward_pull(0, 3) is True
    assert is_fast_forward_pull(2, 3) is False
    assert has_tracking_branch({"name": "x", "upstream": "origin/x"}) is True
    assert has_tracking_branch({"name": "x", "upstream": None}) is False

    assert correct_workflow_for(True) == "clone"
    assert correct_workflow_for(False) == "fork"
    assert remote_setup_after_fork() == ["origin", "upstream"]
    assert first_contribution_steps(False)[0] == "fork"
    assert first_contribution_steps(True)[0] == "clone"

    assert is_ready_for_review(False, True, True) is True
    assert is_ready_for_review(True, True, True) is False
    assert pr_title_quality("Fix null pointer in checkout flow") == "good"
    assert pr_title_quality("fix") == "needs work"
    assert pr_title_quality("") == "needs work"
    assert should_open_draft_pr(False) is True
    assert should_open_draft_pr(True) is False
    assert safe_way_to_update_stale_pr(0, True) == "nothing to do, already up to date"
    assert "rebase" in safe_way_to_update_stale_pr(40, True)

    assert review_verdict("approve") == "merge allowed"
    assert review_verdict("request_changes") == "blocked"
    assert review_verdict("comment") == "informational only"
    assert count_blocking_reviews(["approve", "request_changes", "request_changes", "comment"]) == 2
    assert is_approval_with_followup("approve", True) is True
    assert is_approval_with_followup("approve", False) is False
    assert interpret_lgtm_with_ask("approve", True).startswith("technically approved")
    assert interpret_lgtm_with_ask("request_changes", False) == "blocked -- address the requested changes first"

    assert has_minimum_issue_quality("Login fails on Safari", True, True) is True
    assert has_minimum_issue_quality("", True, True) is False
    assert issue_labels_for(True, False, True) == ["bug", "priority:high"]
    assert issue_labels_for(False, True, False) == ["enhancement"]
    assert closes_issue_on_merge("closes #12") is True
    assert closes_issue_on_merge("Closes #12") is True
    assert closes_issue_on_merge("no keyword here") is False
    assert triage_action(False, False) == "ask for reproduction steps and expected behavior before triaging further"
    assert triage_action(True, True) == "ready to triage"

    assert next_step_in_workflow("forked") == "cloned"
    assert next_step_in_workflow("approved") == "merged"
    assert is_safe_to_merge(True, True, False) is True
    assert is_safe_to_merge(True, False, False) is False
    assert full_workflow_valid(["forked", "branched", "pushed", "opened_pr"]) is True
    assert full_workflow_valid(["branched", "pushed", "opened_pr"]) is False
    assert plan_contribution(False, 42) == ["fork", "branch", "commit", "push", "open PR referencing #42"]
    assert plan_contribution(True, None) == ["clone", "branch", "commit", "push", "open PR"]

    print("\nAll self-checks passed.")
