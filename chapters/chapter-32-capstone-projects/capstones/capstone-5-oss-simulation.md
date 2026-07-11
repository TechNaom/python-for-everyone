# Capstone 5: Open-Source Contribution Simulation

## 1. Overview

This capstone is different from the other four on purpose: **it is not about writing new code from scratch — it's about practicing the process of open-source collaboration end to end.** You will not build a new app. Instead, you'll take a project you already built (an earlier chapter project, or one of Capstones 1-4), simulate a real GitHub issue → fork → branch → PR → review → merge loop against it using the exact local-bare-repo-as-GitHub-stand-in technique Chapters 28 and 29 already taught and verified, and come out the other side having genuinely practiced the workflow — including the hardest part real contributors skip: reviewing your own work honestly before calling it done.

If Capstones 1-4 test "can you build something," Capstone 5 tests "can you ship a change the way a professional team actually ships changes" — atomic commits, a real PR description, a real self-review with real requested changes, and a clean merge. The deliverable is a documented workflow, not a new product.

## 2. Skills this combines

**From Chapter 28 (Git Fundamentals):**
- The core workflow (`init`, `add`, `commit`, `status`, `diff`, `log`) — used for every commit you make on the feature branch.
- Branching (`git switch -c`) — creating a feature branch off the project you're extending, exactly like Ch28's `feature/delete-task` and `feature/priority` branches.
- Atomic, well-scoped commits with messages that explain the "why," not just the "what" — Ch28's `genai-prompt-box` thought process on commit scoping applies directly here.
- Merging (`git merge`, including `--no-ff` for an explicit merge commit) — used when the "maintainer" merges the approved PR.
- Undoing safely (`git restore`/`reset`/`revert`) if a self-review catches something before it's shared — the "still local, not yet pushed" case from Ch28 Sub-topic 5/6 applies while you're still on the contributor side.

**From Chapter 29 (GitHub & Collaboration):**
- The `git init --bare` local-repo-as-GitHub-stand-in technique — the entire architecture of this capstone (Section 4 below) is a direct reuse of Ch29's verified pattern, not a new invention.
- Remotes, forking vs. cloning, and the `origin`/`upstream` convention — your "contributor clone" plays the fork; your "maintainer clone" plays the original repo you don't have direct push access to.
- The real pull request workflow: branch → commit → push → PR description → review loop → merge → fork sync — this capstone runs that exact 6-sub-topic loop from Ch29 against your own project instead of the toy `recipes.py`/`ShoppingList` examples.
- Writing a genuine issue (what's the problem, repro/context, expected vs. actual or desired behavior) and a genuine PR description (what changed, why, how to verify) using Ch29's real templates.
- Code review as a first-class skill — Ch29 Sub-topic 4's "Comment / Approve / Request changes" verdicts and the "name the issue, explain why, suggest a fix" comment shape are what your self-review in Phase 5 must actually produce, not skip.

## 3. Prerequisites

- **[Chapter 28: Git Fundamentals](../../chapter-28-git-fundamentals/lesson.html)** completed — you should be comfortable with `init`/`add`/`commit`/`status`/`diff`/`log`, branching and switching, merging (including resolving a real conflict), and at least one undo command (`restore`, `reset`, or `revert`).
- **[Chapter 29: GitHub & Collaboration](../../chapter-29-github-collaboration/lesson.html)** completed — you should understand remotes, `origin` vs. `upstream`, fork vs. clone, what a pull request actually is, what a reviewer checks for, and how issues link to PRs via `Closes #N`.
- **At least one earlier project or capstone to extend.** You pick which — good candidates:
  - A chapter project with clear room for a new feature (e.g. the Chapter 22 Task API gaining a new endpoint or filter option).
  - Capstone 1, 2, 3, or 4 — pick one small, well-scoped gap in it (a missing validation, an unhandled edge case, a genuinely useful new command/option).
  - Even an earlier chapter's exercises/practice project, if it's substantial enough to meaningfully extend.
- The project you extend must already exist as a real git repository (or be turned into one with `git init` first) — this capstone assumes you're extending tracked code, not writing something from a blank folder.

## 4. Architecture

This reuses Chapter 29's exact verified pattern — a local bare repository standing in for "GitHub," with two working clones playing the two roles you'll switch between:

```text
                    +---------------------------+
                    |  upstream.git (bare)       |
                    |  git init --bare           |
                    |  stands in for "GitHub"     |
                    |  hosting the project you're |
                    |  extending                  |
                    +---------------------------+
                       ^                    |
                       | push (after         | clone (once, up front)
                       | maintainer merge)   |
                       |                    v
        +--------------------+      +------------------------+
        |  maintainer-clone/  |      |  contributor-clone/     |
        |  (you, playing      |      |  (you, playing           |
        |  "maintainer")      |      |  "contributor" -- this   |
        |                      |      |  is your "fork")         |
        |  origin -> upstream  |      |  origin  -> upstream     |
        |                      |      |            (simulates     |
        |  reviews + merges    |      |             your fork)    |
        |  the contributor's   |      |  branches, commits,      |
        |  branch              |      |  pushes feature work     |
        +--------------------+      +------------------------+
```

**Why two clones instead of Ch29's fork/upstream split:** Ch29's project used `origin` (your fork) and `upstream` (the original) as two remotes inside *one* working clone. For this capstone, the clearer simulation of "playing two people" is two **separate working directories**, both pointed at the same `upstream.git` bare repo as their `origin` — one directory is where you act as the contributor (push feature branches, open PRs), the other is where you act as the maintainer (fetch, review, merge, push back to `upstream.git`). This keeps the two roles physically separate on disk, which makes the role-switch in Phases 5-7 concrete instead of just "pretend I'm someone else in the same folder." Either clone can be named `origin` locally since each only ever talks to the one bare repo — there is no real fork divergence needed here since you're not simulating a permissions boundary, just the review/merge ceremony.

Concrete setup commands (directly modeled on Ch29 Sub-topic 1's verified sequence):

```bash
# 1. Turn your existing project into (or confirm it already is) a real repo
cd path/to/your-existing-project
git init -b main            # skip if already a git repo
git add .
git commit -m "Snapshot before capstone 5 workflow"

# 2. Create the bare repo standing in for "GitHub"
cd ..
git clone --bare your-existing-project upstream.git

# 3. Two working clones, one per role
git clone upstream.git maintainer-clone
git clone upstream.git contributor-clone
```

From here, `contributor-clone/` is where Phases 2-4 and 6 happen; `maintainer-clone/` is where Phases 1, 5, and 7 happen. Switching "roles" is just `cd`-ing into the other clone and running `git fetch origin` to see what the other role pushed.

## 5. Step-by-step roadmap

**Phase 1 — Maintainer: file the issue (15-20 min).**
In `maintainer-clone/`, pick the project to extend and write a real GitHub-style issue as a Markdown file (`ISSUE.md` or similar, since there's no live GitHub issue tracker to file it in). Follow Ch29 Sub-topic 5's shape exactly: a clear title, what's happening / what's wanted, expected vs. actual (for a bug) or the concrete feature request (for an enhancement), and why it matters. Commit this file on `main` in the maintainer clone, or just draft it — either way, write it as if a real user filed it, not as a to-do note to yourself.

**Phase 2 — Contributor: fork/clone and branch (10-15 min).**
Switch to `contributor-clone/` (your "fork" per Section 4). Run `git fetch origin` to pick up the issue file if it was pushed. Create a feature branch named after the fix/feature, exactly like Ch28/Ch29's convention: `git switch -c fix-<short-description>` or `feature/<short-description>`.

**Phase 3 — Contributor: implement with atomic commits (30-60 min, depending on feature size).**
Implement the change. This is the phase most learners get wrong (see Common Pitfalls) — practice **atomic commits**: each commit should be one coherent, reviewable step (e.g. "Add input validation for empty description," then separately "Add test for empty description case"), not one giant commit at the end. Use `git status`/`git diff` before each commit, exactly as Ch28 Sub-topic 2 taught, to confirm what's actually being staged.

**Phase 4 — Contributor: push and open the "PR" (15-20 min).**
Push the branch to the bare repo: `git push -u origin <branch-name>`. Since there's no real github.com to click "Create pull request" on, write the PR description as a real Markdown file (`PR.md`) inside the branch, following Ch29 Sub-topic 3's exact three-part structure: **What changed** (plain summary), **Why** (motivation, with `Closes #N` referencing your Phase 1 issue if you numbered it), **How to test it**. A description that just says "fixed it" defeats the purpose — write it as if a stranger reviewer has to act on it with zero other context.

**Phase 5 — Maintainer: genuine self-review (20-30 min).**
Switch to `maintainer-clone/`, `git fetch origin`, and check out the contributor's branch read-only (`git switch --detach origin/<branch-name>`) to review it as the maintainer would. This is the step it's tempting to skip — don't. Read the actual diff (`git diff main origin/<branch-name>`) line by line and leave **real, written review comments** referencing specific lines or commits (a `REVIEW.md` file or inline comments as a text block is fine — there's no GitHub UI to attach them to a diff here). Use Ch29 Sub-topic 4's reviewer checklist: correctness, tests, readability, consistency, scope. Give a genuine verdict — **Comment, Approve, or Request changes** — and if the code is good enough to approve immediately without a single real note, you likely didn't look hard enough; aim to find at least one legitimate thing to request a change on.

**Phase 6 — Contributor: address the feedback (15-30 min).**
Switch back to `contributor-clone/`, still on the feature branch. Make the requested change as a **new commit** (not an amend/rewrite — the branch may already be "shared" with the maintainer clone, so treat it like pushed history per Ch28 Sub-topic 5's rebase-safety rule). Push again: `git push origin <branch-name>`. This mirrors Ch29 Sub-topic 3's "PR updates automatically, no new PR needed" loop.

**Phase 7 — Maintainer: merge and clean up (15-20 min).**
Back in `maintainer-clone/`: `git switch main`, `git fetch origin`, then merge the branch with an explicit merge commit (`git merge --no-ff origin/<branch-name> -m "Merge pull request: <title>"`), matching Ch29's project reference solution's Step 7 pattern. Push the merge to the bare repo: `git push origin main`. Then, still playing contributor, switch to `contributor-clone/` and sync: `git fetch origin && git merge origin/main` (or `git pull`), then delete the now-merged branch both locally (`git branch -d <branch-name>`) and on the remote (`git push origin --delete <branch-name>`) — the exact fork-sync-and-cleanup sequence from Ch29 Sub-topic 6, step 8.

**Total time-box:** roughly 2-3 hours for the MVP scope (a small, real feature), spread across the 7 phases above.

## 6. MVP vs. stretch goals

**MVP:** the full 7-phase loop completed once, for one genuinely small feature or fix — issue written, branch created, 2+ atomic commits, a real PR description, a real self-review with at least one requested change, that change addressed, and a clean merge with fork sync and branch cleanup.

**Stretch goals (pick one or more):**
- Do the entire loop a second time with a **genuinely larger feature** (something that took real design thought, not just a one-line fix) to prove the workflow holds up under more complexity.
- **Deliberately create a merge conflict** as part of the exercise: while the contributor branch is open, make an unrelated change directly on `main` in the maintainer clone that touches the same lines, then resolve the real conflict during the Phase 7 merge, using Ch28 Sub-topic 4's conflict-marker process.
- Add a **second reviewer role** — a third clone (`second-reviewer-clone/`) that also fetches and reviews the branch independently before the maintainer merges, practicing reconciling two sets of feedback (a very common real-world situation when a PR needs more than one approval).
- Try a **squash merge** (`git merge --squash`) instead of `--no-ff` for the second pass, and compare the resulting `git log --oneline --graph` shape against the merge-commit version — directly extending the "ideas to make it your own" suggestion from Ch29's own project.

## 7. What a strong README for this capstone looks like

There is no new "product" here, so this capstone's `README.md` is **not** a features/setup doc — it should be structured as two things:

1. **An updated README for the project you extended**, documenting the new feature/fix as if it shipped for real (what it does, how to use it, any new flags/endpoints/behavior) — updated in place in that project's own repo, not duplicated here.
2. **A short retrospective/log of the workflow itself**, living in this capstone's own folder, written as a real account of what happened, not a generic template filled with placeholders. Concretely, it should include:
   - **The issue** — link to (or paste) the `ISSUE.md` you wrote in Phase 1, and one sentence on why you picked this particular gap to fill.
   - **The PR** — link to (or paste) the `PR.md` from Phase 4.
   - **The review** — what feedback actually came up in Phase 5's self-review, quoted or summarized, and whether it was a real issue you'd genuinely missed or something you added deliberately to practice the loop.
   - **What changed as a result** — the diff between the first push (Phase 4) and the final push (Phase 6), described in a sentence or two.
   - **A short reflection** — 3-5 sentences on what felt different about reviewing your own work critically versus just merging it, and one thing you'd do differently on a real team PR next time.

This retrospective is the actual evidence this capstone was completed with the process taken seriously, not just the git mechanics run through on autopilot.

## 8. Common pitfalls

- **Writing one giant commit instead of practicing atomic commits.** If Phase 3 produces a single "implement feature" commit, the atomic-commit practice this capstone is partly testing didn't happen — go back and think in terms of the smallest reviewable steps.
- **Skipping the genuine self-review and just merging immediately.** This is the single most common way to hollow out this capstone — if Phase 5 doesn't produce at least one real, specific requested change, the most valuable skill in the whole exercise (catching your own mistakes before someone else has to) never got practiced.
- **Writing a PR description that just says "fixed it" or restates the diff.** Per Ch29 Sub-topic 3, a good description answers what changed, why, and how to verify — a description a stranger reviewer couldn't act on without asking follow-up questions isn't done yet.
- **Forgetting to sync the "fork" after merge.** If `contributor-clone/`'s `main` never gets `git fetch`/`merge`'d after the maintainer's Phase 7 merge, the two clones silently diverge — exactly the drift Ch29 Sub-topic 2 warns forks fall into without deliberate syncing.
- **Amending or rebasing the feature branch after it's already been fetched by the maintainer clone.** Once `maintainer-clone/` has fetched the branch in Phase 5, treat it as shared history — address feedback with new commits (Phase 6), not `commit --amend` or an interactive rebase, per Ch28 Sub-topic 5's "never rebase shared history" rule.

## 9. Self-assessment checklist

**Git mechanics:**
- [ ] `upstream.git` bare repo created and both `maintainer-clone/`/`contributor-clone/` correctly point to it as `origin`.
- [ ] Feature branch created with a clear, descriptive name (not `fix` or `patch`).
- [ ] At least 2-3 atomic commits on the branch, each with a clear scope — not one dump commit.
- [ ] Commit messages explain **why**, not just what — someone reading `git log` alone should understand the reasoning, not just the mechanical change.
- [ ] Branch pushed to the bare repo (`git push -u origin <branch>`), and the push actually visible via `git log --oneline --graph --all` from either clone.
- [ ] Feedback addressed with new commits, not history rewrites, once the branch was "shared" with the maintainer clone.
- [ ] Merge performed explicitly and correctly (`--no-ff` or a deliberate squash), pushed back to `upstream.git`.
- [ ] Fork (contributor clone) synced after merge, and the merged branch deleted both locally and on the remote.

**Process and communication quality:**
- [ ] The issue (`ISSUE.md`) reads like something a real user or maintainer would file — specific, with context — not a one-line placeholder.
- [ ] The PR description (`PR.md`) covers what changed, why, and how to verify, per Ch29's template.
- [ ] The self-review in Phase 5 produced at least one genuine, specific, actionable comment — not a rubber-stamp approval.
- [ ] The review comment(s) name the issue, explain why it matters, and suggest a concrete fix — the same shape Ch29 Sub-topic 4 taught for real review feedback.
- [ ] The extended project's own README was updated to document the new feature/fix, separately from this capstone's retrospective.
- [ ] The retrospective log honestly reflects what happened (including anything that didn't go smoothly), not a cleaned-up narrative that skips the messy parts.
