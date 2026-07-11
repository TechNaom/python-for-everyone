# Chapter 29 Project: Open-Source-Style Collaboration Workflow

A guided, hands-on simulation of a real GitHub contribution: fork,
feature branch, push, pull request, code review, merge, and syncing
your fork afterward. Every remote/branch/commit/merge command below is
a **real git command that actually runs** against a **real local Git
repository** — not a description of GitHub's UI. The parts that
genuinely can't be scripted (opening a PR, a reviewer leaving
comments, clicking "Approve," clicking "Merge pull request") are
called out explicitly below as **documented-only** steps, because they
happen inside github.com's web UI, which this offline project has no
way to reach.

## Why a local bare repo stands in for GitHub

This site is static (GitHub Pages, no backend, no server you can push
to from a learner's machine). So instead of describing fictional
GitHub commands, this project builds a real stand-in for "GitHub"
using `git init --bare` — a genuine Git repository with no working
directory, structurally identical to what GitHub hosts on its own
servers for every repo. Cloning it, pushing to it, and fetching from
it are the exact same git operations you'd run against a real
github.com URL — only the URL is a local folder path instead of
`https://github.com/...`.

## What you'll build

`starter.py` sets up the scenario for you (`setup_scenario()`, already
written) and then hands you 7 TODOs that drive the full workflow with
real git commands, executed via Python's `subprocess` module:

1. **Clone your fork** (not the original repo) into a working
   directory — *(real, executed)*
2. **Add `upstream` as a second remote**, alongside `origin` (your
   fork) — *(real, executed)*
3. **Create a feature branch and commit real work** to it — *(real,
   executed)*
4. **Push the feature branch to your fork** — *(real, executed)*
5. **Open a pull request on github.com** comparing your fork's branch
   against upstream's `main` — ***documented-only***, see below
6. **A reviewer reviews the PR and approves it on github.com** —
   ***documented-only***, see below
7. **The maintainer clicks "Merge pull request"** — the *underlying
   mechanics* of this are simulated with real git commands (a second
   clone fetches your branch and performs a real `git merge --no-ff`,
   then pushes the result) — *(real, executed)* — but the actual
   button-click and merge-strategy picker live on github.com and are
   ***documented-only*** here
8. **Sync your fork** now that upstream has moved ahead of it (fetch,
   merge, push) — *(real, executed)*
9. **Delete the merged feature branch**, locally and on your fork —
   *(real, executed)*

## Example run

```text
=== Chapter 29 Project: GitHub Collaboration Workflow ===

Scenario ready.
  upstream (stands in for the real GitHub repo you don't own): .../scenario/upstream.git
  my-fork  (stands in for YOUR fork of it on GitHub):          .../scenario/my-fork.git

--- Step 1: clone your fork (not upstream) ---
$ git clone .../my-fork.git scenario/workdir
...
--- Step 5: simulate the maintainer merging the approved PR ---
$ git merge --no-ff pr-1-add-pancake-servings -m "Merge pull request #1 ..."
Merge made by the 'ort' strategy.
 recipes.py | 7 +++++++

Upstream history after the merge:
*   e11dccf Merge pull request #1 from learner/add-pancake-servings
|\
| * a34b3a4 Add servings_for() to scale a recipe by number of people
|/
* 0a69be7 Initial commit: recipe box skeleton

=== Done. Your fork's main branch now matches upstream's main, ... ===
```

(Your own commit hashes will differ — the *shape* of the history is
what matters.)

## How to run

```bash
cd chapters/chapter-29-github-collaboration/project
python3 starter.py
```

Fill in the 7 numbered `# TODO` sections with real git commands run
through the provided `run_git()` helper. Want to see a finished
version? Run `python3 solution.py`. Everything runs inside a
`scenario/` subfolder that's safe to delete and re-create any time
(re-running the script wipes and rebuilds it automatically).

## The pieces

- **`run_git(args, cwd)`** — runs a real git command via `subprocess`,
  printing exactly what executed and its output, so you can see every
  step as it happens (not a log statement claiming something happened).
- **`setup_scenario()`** — builds the two bare repos (`upstream.git`,
  `my-fork.git`) and seeds upstream with one starter commit. Provided
  for you — your work is everything that happens *after* this.
- **TODOs 1-7** — the actual collaboration workflow: clone the fork,
  add the upstream remote, branch, commit, push, simulate the
  maintainer's merge, sync the fork, clean up the branch.

## Steps 5-6, written up for real (since they happen on github.com)

These are the steps this script cannot execute, because they require
a real github.com account and browser session. Here's exactly what
you'd do on the real site, in order, right after Step 4's push:

1. **Open a pull request.** Go to your fork on github.com. GitHub
   detects the recently-pushed branch and shows a "Compare & pull
   request" banner — click it. You'll land on a compare view showing
   `base: upstream/main ← compare: your-fork/add-pancake-servings`.
2. **Write a PR description.** Give it a clear title ("Add
   servings_for() to scale a recipe by number of people") and a body
   explaining *what* changed and *why* — see this chapter's interview
   questions for what makes a PR description actually useful to a
   reviewer.
3. **Click "Create pull request."** This opens PR #1 against the
   upstream repo. GitHub now shows a "Files changed" diff view and a
   comment thread.
4. **A reviewer reviews it.** On github.com, a reviewer opens "Files
   changed," reads the diff, and either leaves inline comments,
   requests changes, approves, or just comments — see this chapter's
   interview questions for the difference between those three review
   actions.
5. **The reviewer approves.** Once satisfied, they submit a review
   with "Approve" selected.
6. **The maintainer merges.** With an approval in hand, the "Merge
   pull request" button becomes available (assuming no branch
   protection rule blocks it). They pick a merge strategy (merge
   commit, squash-and-merge, or rebase-and-merge — see interview
   questions for the tradeoffs) and click through.

Step 7 in the script above reproduces the **mechanical result** of
that merge — a real merge commit built from real git commands — so you
can see exactly what git itself did underneath GitHub's button, even
though the button itself isn't something a script can click.

## Ideas to make it your own

- Change the merge in Step 7 to a **squash merge** instead
  (`git merge --squash pr-1-... && git commit -m "..."`) and compare
  the resulting `git log` shape against the `--no-ff` merge commit
  version — this is exactly the difference GitHub's three merge-button
  options produce.
- Add a **second contributor**: clone another fork from the same
  upstream, make a conflicting change to the same line of `recipes.py`,
  and work through resolving the merge conflict for real.
- After the sync in Step 8, try opening a **second** feature branch
  from the now-updated `main` and repeat the whole cycle — this is
  the actual weekly rhythm of contributing to a real open-source repo.

## Why this project matters

Fork/clone, remotes, PRs, and code review are the daily mechanics of
essentially every professional software job that uses Git — not just
open source. The GitHub UI parts (opening a PR, reviewing, clicking
merge) are easy to read about and hard to internalize without
practice; the git mechanics underneath them (what a fork actually is,
what `git fetch` really does, what a merge commit actually looks like)
are the part a script *can* make completely real, so that's exactly
what this project does.

## More project ideas (build one of these instead, or after)

From Chapter 7 onward, you get a genuine choice of what to build. The
Collaboration Workflow above is fully built out with a starter and
reference solution — the four ideas below are not. Each is a real,
grounded use case solvable with only what's been taught through
Chapter 29. No starter or solution files are provided on purpose —
building one of these unassisted is the point.

### 1. Sync a Fork That's Fallen Badly Behind

**Problem:** A fork hasn't been synced in a long time — upstream has
several new commits on `main`, and the fork's `main` is now many
commits behind.

**What it should do:** Using the same `git init --bare` technique from
this project, build a bare "upstream" repo with 4-5 sequential commits
on `main`, a "fork" bare repo cloned from an *early* point in that
history (so it's genuinely behind), and a working clone of the fork.
Practice the real sync sequence — `git fetch upstream`, `git merge
upstream/main`, `git push origin main` — and print the before/after
`git log --oneline --graph` to show the fork catching up.

**Suggested approach:** Reuse this project's `run_git()`/
`setup_scenario()` pattern, but seed upstream with multiple commits
*after* cloning the fork instead of before, so there's a real gap to
close.

### 2. Write a PR Description From a Bug Report

**Problem:** A bug report says: "The `servings_for()` function crashes
with a `ZeroDivisionError` if `people` is 0, instead of returning a
sensible message." You've fixed it — now you need a PR description a
reviewer would actually find useful.

**What it should do:** Write the actual code fix (a real Python
function with a guard clause for `people <= 0`), then write a real PR
description using this template: **What changed**, **Why**, **How to
test it**, **Anything a reviewer should pay special attention to**.
No starter file — write both the fix and the description from
scratch, in a plain text or Markdown file.

**Suggested approach:** Base the description on this chapter's
interview-question answer about what makes a PR description genuinely
useful to a reviewer, not just a summary of the diff.

### 3. Write Three Kinds of Review Comments for One Diff

**Problem:** The same small, buggy diff needs three *different* kinds
of code review comments — a real reviewer doesn't write every comment
the same way.

**What it should do:** Take this diff (a function with a real bug —
mutating a default mutable argument, straight from Chapter 8's
lesson):
```python
def add_topping(topping, toppings=[]):
    toppings.append(topping)
    return toppings
```
Write three separate comments a reviewer might leave on it: **one
nitpick** (something small and non-blocking, like a naming or
docstring suggestion), **one blocking comment** (the actual mutable
default argument bug — specific enough that the author knows exactly
what to change), and **one piece of praise** (something genuinely
good about the code, stated specifically rather than generically).

**Suggested approach:** Use this chapter's interview-question answer
on "what reviewers look for" and "approve vs. request-changes vs.
comment" to calibrate tone and specificity for each of the three.

### 4. Simulate a Full Issue-to-PR Workflow

**Problem:** A real open-source contribution usually starts with an
issue, not a PR — someone reports a bug, a contributor claims it,
fixes it, and links the fix back to the original report.

**What it should do:** Using the same bare-repo technique as this
project, write up (in a Markdown file) a realistic issue report for a
bug in `recipes.py` (choose your own — e.g. `list_recipes()` doesn't
handle an empty `RECIPES` dict cleanly), then actually build the fix
as a real feature branch + commit against a bare-repo scenario you set
up yourself, with a commit message and PR description that includes a
**closing keyword** (e.g. `Fixes #12`) linking back to the issue
number.

**Suggested approach:** Reuse this project's `setup_scenario()`/
`run_git()` pattern for the real git mechanics; write the issue and PR
description as plain Markdown files since GitHub issues themselves
can't be created without a real repo.
