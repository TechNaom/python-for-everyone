# Chapter 28 Project: Git Workflow Practice

A guided, hands-on git workflow on a real scratch repository — not a
Python script to write. You'll branch, diverge, hit a genuine merge
conflict, resolve it, merge, and rebase a second branch onto the
result, using real `git` commands in your own terminal.

## What you'll do

`starter.py` is a one-time setup script (it runs real `git` commands
under the hood via `subprocess`) that builds a scratch repository
called `recipe-box/` and pre-loads it with a scenario:

1. An initial commit on `main` — a shared chili recipe.
2. A `feature/double-recipe` branch that diverges from `main` with two
   of its own commits (doubling the recipe, then adding a secret
   ingredient).
3. A follow-up commit on `main` that edits the **same line**
   `feature/double-recipe` already changed — so the two branches now
   conflict on purpose.

Nothing is merged yet. That part is your job, done by hand in the
terminal — this README's numbered steps walk you through it.
`solution.py` is a **verifier**, not a second copy of the answer: run
it after you're done and it inspects your actual repo's git state
(branch existence, commit count, whether the conflict was really
resolved, whether the rebase was clean) and reports pass/fail per
check.

## How to run

```bash
cd chapters/chapter-28-git-fundamentals/project
python3 starter.py
cd recipe-box
```

Everything from here happens with real `git` commands, inside
`recipe-box/`.

## The workflow, step by step

### 1. Look around first

```bash
git log --oneline --graph --all
git status
git branch
```

You should see `main` and `feature/double-recipe` diverging from the
same initial commit, each with their own commits after that.

### 2. Attempt the merge

```bash
git checkout main
git merge feature/double-recipe
```

This **will** fail with a conflict — that's the point. `main` and
`feature/double-recipe` both changed the last line of `recipe.txt`,
so git can't automatically decide which version is correct. You'll
see:

```text
Auto-merging recipe.txt
CONFLICT (content): Merge conflict in recipe.txt
Automatic merge failed; fix conflicts and then commit the result.
```

### 3. Inspect the conflict markers

```bash
git status
cat recipe.txt
```

Notice the ingredient lines merged automatically with no conflict —
only the lines both branches genuinely disagree about get marked.
`recipe.txt` now contains:

```text
<<<<<<< HEAD
Serves: 4-6 depending on appetite
=======
Serves: 8 (doubled)
- pinch of cinnamon
>>>>>>> feature/double-recipe
```

- Everything between `<<<<<<< HEAD` and `=======` is **your current
  branch's** version (`main`).
- Everything between `=======` and `>>>>>>> feature/double-recipe` is
  the **incoming branch's** version.

### 4. Resolve the conflict

Open `recipe.txt` in an editor and decide what the final content
should actually be. A reasonable resolution keeps both ideas — the
doubled quantities and the cinnamon note — and drops the markers
entirely:

```text
Grandma's Chili
================
Ingredients:
- 2 lb ground beef
- 2 cans beans
- 2 cans tomatoes

Serves: 8 (doubled)
- pinch of cinnamon
```

Delete all three marker lines (`<<<<<<<`, `=======`, `>>>>>>>`) — they
must not survive into the final file.

### 5. Stage and commit the resolution

```bash
git add recipe.txt
git commit
```

Git pre-fills a merge commit message for you (`Merge branch
'feature/double-recipe'`) — accept it or edit it, then save and close.
Check the result:

```bash
git log --oneline --graph --all
```

You now have a real three-way merge commit with two parents, tying
both branches' histories together.

### 6. Create a second branch and let main move on

```bash
git checkout -b feature/add-notes
echo "Note: can substitute kidney beans for black beans." >> recipe.txt
git add recipe.txt
git commit -m "Add substitution note"

git checkout main
echo "" >> README.md
echo "Contributions welcome!" >> README.md
git add README.md
git commit -m "Update README with contribution note"
```

Now `main` has moved on *again* since `feature/add-notes` branched off
it — a very common situation on a real team.

### 7. Rebase your feature branch onto the updated main

```bash
git checkout feature/add-notes
git rebase main
```

This replays `feature/add-notes`'s one commit on top of `main`'s new
tip, producing a straight, linear history with no extra merge commit:

```bash
git log --oneline --graph --all
```

### 8. Practice one undo command

Pick at least one of these and actually run it (see the "More project
ideas" section below for a deeper version of each):

```bash
# stash a change, then bring it back
echo "temp idea" >> recipe.txt
git stash push -m "WIP idea"
git status
git stash pop

# see the full history of where HEAD has pointed
git reflog
```

### 9. Verify your work

From the `project/` folder (one level up from `recipe-box/`):

```bash
cd ..
python3 solution.py
```

It checks: the feature branch existed, the merge commit exists, no
conflict markers were left behind, the resolved content reflects both
sides, and the second branch was cleanly rebased. Fix anything marked
`FAIL` by revisiting the matching step above.

## Want to start over?

```bash
rm -rf recipe-box
python3 starter.py
```

## Why this project matters

Merge conflicts and rebases are not edge cases — they're what
actually happens on any team where more than one person touches the
same file. Reading conflict markers calmly, resolving them
deliberately instead of panicking and picking a side at random, and
knowing when to reach for merge vs. rebase is a day-one skill on every
real engineering team, not a one-time interview topic.

## More project ideas (do one of these instead, or after)

No starter/solution files are provided for these on purpose — building
and verifying each one yourself, entirely with real `git` commands, is
the point. Each is solvable with only what this chapter and the main
project above have taught.

### 1. Simulate a hotfix workflow

**Scenario:** Production is broken and needs a fix *right now*, but
you also have a half-finished feature branch that isn't ready yet.

**What to do:** From `main`, create `hotfix/urgent-bug`, make and
commit a one-line fix, merge it straight back into `main`, then switch
to your still-open feature branch and rebase it onto the now-updated
`main` so it picks up the fix too.

**Suggested approach:** This is steps 6–7 above, just framed as a
hotfix instead of a notes branch — practice explaining out loud *why*
the feature branch needs rebasing (or merging) after the hotfix lands,
not just running the commands.

### 2. Recover a commit you "accidentally" `reset --hard`

**Scenario:** You just ran `git reset --hard HEAD~1` and realized the
commit you threw away actually had work you needed.

**What to do:** On a throwaway branch, make a commit, note its
message, then deliberately run `git reset --hard HEAD~1` to "lose" it.
Use `git reflog` to find the lost commit's hash, then
`git reset --hard <that-hash>` to bring it back. Confirm with
`git log` that the commit is really there again.

**Suggested approach:** `git reflog` lists every place HEAD has
pointed, most recent first — the commit you "lost" is still in there
even though `git log` no longer shows it, because it hasn't been
garbage-collected yet.

### 3. Squash three messy commits into one clean commit

**Scenario:** A feature branch has three sloppy, in-progress commits
("wip", "fix typo", "actually fix it") that should become one clean
commit before anyone else looks at the history.

**What to do:** On a throwaway branch, make three small commits with
exactly that kind of messy message. Run `git rebase -i HEAD~3`, mark
the last two as `squash` (or `fixup`), and write one clean combined
commit message. Confirm with `git log --oneline` that the branch now
has one commit instead of three.

**Suggested approach:** In the interactive rebase editor, only the
word at the start of each line needs to change from `pick` to
`squash`/`fixup` — everything else about the commit list stays as-is.

### 4. Resolve a conflict where one branch deletes a file and the other modifies it

**Scenario:** One branch removes a file entirely; another branch, not
knowing that, keeps editing it. Merging them is a different *kind* of
conflict than an edit/edit conflict.

**What to do:** From `main`, create two branches. On one, delete
`README.md` and commit. On the other, edit `README.md` and commit.
Merge both into `main` one at a time and see how git reports a
"deleted by us" / "deleted by them" conflict differently from a normal
content conflict — then decide (and act on) whether the file should
stay deleted or be kept with the edit.

**Suggested approach:** `git status` during this kind of conflict
shows the file as "deleted by them" or "modified by us" rather than
"both modified" — read that language carefully, since the resolution
commands differ (`git rm` to confirm a deletion, or `git add` to keep
a modified version).
