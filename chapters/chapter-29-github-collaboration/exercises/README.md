# Chapter 29 Exercises: GitHub & Collaboration

These exercises use what Chapter 29 covered: remotes, `origin`,
`fetch` vs. `pull`, tracking branches, and diagnosing a rejected push.
Unlike most chapters, there's no Python function to write here -- the
"code" you're practicing is real `git` commands, run by hand in your
own terminal, against a real scratch scenario this folder builds for
you on disk. Every task uses only `git` (already on your system) plus
Python's standard library to build the scenario -- no installs needed.

## How to run

Run this **from inside this `exercises/` folder**:

```bash
cd exercises
python3 starter.py
```

This builds a `scenario/` folder containing:

- `scenario/upstream-remote.git` -- a real **bare repository**
  (`git init --bare`), standing in for "the project on GitHub." It has
  no working directory, and only accepts pushes / serves fetches --
  exactly like a real GitHub remote.
- `scenario/my-local-work/` -- your working clone, with `origin`
  already pointing at `upstream-remote.git`. It starts out **one
  commit behind** `origin/main`, because the script simulates a
  teammate pushing a change before you look at it -- the exact
  situation Tasks 1-3 ask you to diagnose and resolve.

`scenario/` is gitignored -- it's a disposable scratch environment.
Delete it and re-run `python3 starter.py` any time to reset it to a
clean starting state.

## Task 1 — Confirm your remote

`cd` into `scenario/my-local-work` and run:

```bash
git remote -v
```

Confirm `origin` points at `../upstream-remote.git` for both fetch and
push.

## Task 2 — Fetch, and prove it doesn't touch your branch

Run:

```bash
git fetch origin
git log --oneline              # local main -- should be UNCHANGED
git log --oneline origin/main  # what fetch downloaded -- one commit ahead
```

Confirm your local `main` didn't move, even though `origin/main` now
shows a new commit ("Teammate pushes a change").

## Task 3 — Pull, and watch your branch actually update

Run:

```bash
git pull origin main
git log --oneline
```

This time local `main` **does** move -- a fast-forward, since your
local branch had no commits of its own beyond what `origin` already
had.

## Task 4 — Debug the Code: a rejected push

This is the `.debug-card` task -- see `index.html` for the full
scenario. In short: after Task 3, someone else pushes *another* change
to `upstream-remote.git` while you make your own local commit without
fetching first. Your push gets rejected:

```text
 ! [rejected]        main -> main (fetch first)
error: failed to push some refs to '../upstream-remote.git'
hint: Updates were rejected because the remote contains work that you do not
hint: have locally. ...
```

**Diagnose it, then fix it for real:**

1. Run `git fetch origin` and look at `git log --oneline --graph --all`
   to see exactly how history has diverged.
2. Run `git rebase origin/main` to replay your commit on top of the
   teammate's. If both changes touched the same lines, you'll hit a
   real merge conflict -- resolve it the same way Chapter 28 taught
   (edit the file, remove the `<<<<<<<`/`=======`/`>>>>>>>` markers,
   `git add` the file, then `git rebase --continue`).
3. Push again -- it now succeeds.

## Checking your work

`solution.py` runs this entire scenario end to end automatically,
including reproducing the rejected push and resolving the conflict,
and prints the real output of every command as it runs:

```bash
python3 solution.py
```

Compare its output against what you saw running the same commands
yourself. Exact commit hashes will differ every time (they're
content-addressed and include a timestamp) -- that's expected. The
*pattern* (fetch doesn't move your branch, pull does, a push against
stale history gets rejected until you fetch+rebase) is what matters,
not matching hashes exactly.
