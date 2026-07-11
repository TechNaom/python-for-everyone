# Chapter 28 Exercises: Git Fundamentals

This chapter is different from every other chapter's exercises: there
are no Python functions to write. Instead, `starter.py` **builds a
real git repository** in a folder called `git-playground/`, with a
specific commit history already in place -- including a real merge
conflict waiting to happen and a commit that's about to become
"lost." You practice actual git commands, in your own terminal,
against that repository.

## How to run this

From inside this `exercises/` folder:

```bash
python3 starter.py
cd git-playground
git log --oneline --graph --all
git status
```

Then work through Tasks 1-9 below, running real git commands as you
go. There's no auto-grading here -- git's own output (`git status`,
`git log`, `git diff`) is the feedback. Compare what you did against
`solution.py`, which documents the exact, verified command sequence
for every task as comments.

When you're done, delete the practice repo (it's disposable, and
regenerating it with `python3 starter.py` always gives you the same
starting point again):

```bash
cd ..
rm -rf git-playground
```

## Task 1 — Read the history

Run `git log --oneline --all --graph` inside `git-playground/`. You
should see 5 commits on `main` and one additional commit on a branch
called `feature/priority` that hasn't been merged in yet. Answer for
yourself: at what commit did `main` and `feature/priority` diverge?

## Task 2 — Check status and diff before touching anything

`starter.py` deliberately left an uncommitted change sitting in
`tasks.py`. Run `git status`, then `git diff`, and read exactly what
changed before doing anything else — this is always the right first
move.

## Task 3 — Discard the uncommitted change

Use the correct command to throw away that uncommitted change
entirely, restoring `tasks.py` to its last committed state. (Hint:
this is Sub-topic 6's `restore`, not `reset` — the change was never
committed.)

## Task 4 — Trigger and resolve a real merge conflict

Run `git merge feature/priority` from `main`. It will conflict — both
branches changed `add_task()`'s signature and body differently. Open
`tasks.py`, read the `<<<<<<<`/`=======`/`>>>>>>>` markers, and
hand-resolve it into one correct function that keeps **both** changes
(the validation check from `main`, and the `priority` parameter from
`feature/priority`). Then `git add` and `git commit` to finish the
merge.

## Task 5 — Verify your resolution actually works

A conflict resolution that "looks right" isn't the same as one that
**is** right. Run the small Python check in `solution.py`'s Task 5
comment against your resolved `tasks.py` and confirm the output
matches. If it doesn't, your merge resolution has a bug — a common
one is an accidental duplicate line left over from the conflict
markers.

## Task 6 — Recover the "lost" commit with reflog

`starter.py` committed a function called `task_count()` and then
immediately ran `git reset --hard HEAD~1` on it — so it won't show up
in `git log` anymore. Use `git reflog` to find its hash, and bring it
back (either with `git reset --hard <hash>` or `git cherry-pick
<hash>` — both work here, see `solution.py` for why).

## Task 7 — Stash a change, then bring it back

Add a small new function to `tasks.py` but don't commit it. Use `git
stash` to shelve it, confirm with `git status` that the working tree
is clean, confirm with `git stash list` that your change is still
tracked, then use `git stash pop` to bring it back exactly as it was.

## Task 8 — Debug the Situation

A teammate says: *"I ran `git reset --hard` on the wrong branch and
now my last three commits are just gone from `git log` — is my work
actually lost?"*

Their mistake is assuming `git reset --hard` deletes commits. Explain
(to yourself, or write it down) what actually happened to those three
commits, and give the exact command sequence that recovers them —
this is the same underlying mechanism as Task 6.

## Task 9 — Scenario: the production hotfix

You're two days into a messy, half-broken feature branch when a
production bug needs an urgent fix based on the **current stable**
code, not your in-progress feature. Walk through, command by command,
exactly what you'd run to fix and ship the hotfix without touching or
losing any of your feature branch's in-progress work. (This is the
exact scenario from the lesson's opening hook — see `solution.py`'s
Task 9 for the verified command sequence.)

## Checking your work

There's no single "correct" final state to diff against, since this
chapter is about the git commands themselves, not a specific output.
Instead:

- After Task 4, your merged `tasks.py` should behave exactly as shown
  in Task 5's check.
- After Task 6, `git log --oneline` should show the recovered
  `task_count` commit again.
- After Task 7, `git stash list` should be empty again.
- Every command's exact output was verified against this course's own
  build system before being written into `solution.py` — if your
  output differs meaningfully (not just commit hashes, which are
  always unique), re-read the relevant lesson sub-topic.
