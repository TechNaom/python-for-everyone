# Chapter 29 Practice Bank: GitHub & Collaboration

A deeper set of practice problems, organized by topic, on top of the
main `exercises/` folder — including scenario-based problems written
in the same style you'll see in real interviews. Every task here uses
only the standard library — no installs needed.

This chapter builds on Chapter 28 (local git: commits, branches,
merge, rebase, conflicts, undo) and covers the remote/collaboration
layer on top of it. Since a browser/grader can't run real git
commands, every task here reasons about or simulates a GitHub
collaboration concept as plain Python data and functions — but every
piece of git/GitHub behavior described was checked against a real
local bare-repo simulation before being written into these problems
(fast-forward vs. divergent-history pulls, `fetch` vs. `pull`, tracking
branches after `push -u`, and the fork-behind-upstream update flow were
all reproduced with real `git init --bare` repos first).

## How to run

```bash
cd practice
python3 starter.py
```

## Topic 1: Remotes (origin, push/pull/fetch, tracking branches)

1. Look up a remote's URL from a dict of remotes.
2. Decide whether a pull would fast-forward or need a merge.
3. **Debug the Code:** fix a wrong claim that `git fetch` changes your working directory.
4. Check whether a branch has an upstream (tracking) branch set.
5. **Scenario — Silent Push Confusion:** write `needs_dash_u_explanation()`.
6. **Scenario — Interview Prep:** explain the fetch-then-pull workflow.

## Topic 2: Forking vs. Cloning

1. Decide whether to fork or clone based on write access.
2. Return the two remotes set up after forking (`origin`, `upstream`).
3. **Debug the Code:** fix a wrong claim that forks auto-sync forever.
4. **Scenario — Open Source First Contribution:** write `first_contribution_steps()`.
5. **Scenario — Interview Prep:** explain forking vs. cloning.

## Topic 3: Pull Requests (workflow, descriptions, draft PRs)

1. Decide if a PR is ready for review.
2. Judge a PR title's quality.
3. **Debug the Code:** fix backwards draft-PR logic.
4. **Scenario — Merge Conflict Blocking a PR:** write `safe_way_to_update_stale_pr()`.
5. **Scenario — Interview Prep:** explain what makes a good PR description.

## Topic 4: Code Review (what reviewers look for, giving/receiving feedback)

1. Map a review type to a merge verdict.
2. Count how many reviews are blocking (`request_changes`).
3. **Debug the Code:** fix a check that ignored a follow-up-request flag.
4. **Scenario — "LGTM but can you add a test?":** write `interpret_lgtm_with_ask()`.
5. **Scenario — Interview Prep:** explain what makes review feedback constructive.

## Topic 5: Issues & Project Workflow (good issues, labels, linking to PRs)

1. Check whether an issue meets a minimum quality bar.
2. Build the right label list for an issue.
3. **Debug the Code:** fix a case-sensitive check for closing keywords.
4. **Scenario — Triaging a Vague Bug Report:** write `triage_action()`.
5. **Scenario — Interview Prep:** explain a good issue vs. a bad one.

## Topic 6: Real-World End-to-End Collaboration Scenario

1. Return the next step in a fixed contribution workflow.
2. Decide whether a PR is safe to merge.
3. **Debug the Code:** fix a workflow check that only looked at the first step.
4. **Scenario — End-to-End Contribution:** write `plan_contribution()`.
5. **Scenario — Interview Prep:** explain the full issue-to-merge loop.

## Checking your work

Compare your output against `solution.py`. Your exact wording doesn't
need to match on the explanation-style tasks — the goal is that your
program runs without errors and does what each TODO asks. Every
non-explanation task's output is exactly reproducible; run
`python3 solution.py` to see every self-check pass.
