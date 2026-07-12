# Chapter 33 Project: careerprep — a Mock-Interview Drill Tool + Portfolio Checklist Scanner

A real, multi-file, pip-installable command-line tool with two genuinely
useful features for wrapping up this course: a mock-interview drill that
saves your typed answers with a timestamp so you can watch them improve
over multiple practice sessions, and a portfolio-readiness scanner that
actually points at one of your own project folders and checks real files
on disk — not a static list you tick by hand.

## Project layout

```text
project/
├── starter/            <- you work here
│   └── careerprep/
│       ├── __init__.py
│       ├── interview.py  (TODOs 1-10 — question bank + answer storage)
│       ├── checklist.py  (TODOs 11-12 — the directory scanner)
│       └── cli.py        (TODOs 11-25 — the argparse wiring)
├── solution/            <- complete, working reference
│   ├── careerprep/
│   │   ├── __init__.py
│   │   ├── interview.py
│   │   ├── checklist.py
│   │   └── cli.py
│   ├── pyproject.toml
│   ├── requirements.txt
│   └── README.md
```

Both `starter/` and `solution/` are real installable packages. The
starter's `pyproject.toml` and `requirements.txt` are identical to the
solution's (packaging is not part of the TODOs; the logic in
`interview.py`/`checklist.py`/`cli.py` is). Copy them in from `solution/`
once you're ready to test `pip install -e .`, or just run the starter
directly with `python3 -m careerprep.cli` while you work through the
TODOs — no install needed for that.

## What you're building

**Feature 1 — mock-interview drill (`careerprep interview ...`)**

- **`careerprep interview list [--category behavioral|technical]`** —
  list all 25 questions in the built-in question bank (10 behavioral
  STAR-method questions, 15 technical-concept questions spanning Python
  fundamentals, OOP, testing, git, APIs, databases, memory, and
  concurrency — pulled from topics across this course).
- **`careerprep interview random [--category behavioral|technical]`** —
  pick one random question, print it, read a typed/pasted multi-line
  answer from the terminal, and save it to a local JSON file with a
  timestamp.
- **`careerprep interview review [--category ...] [--question-id N]`** —
  show previously saved answers, optionally filtered, so you can watch
  how your answers to the same question evolve across practice sessions.
  Every practice session **appends** to the answers file — nothing is
  ever silently overwritten.

**Feature 2 — portfolio checklist scanner (`careerprep checklist ...`)**

- **`careerprep checklist list`** — print the full 9-item checklist: 4
  auto-checkable items and 5 manual self-assessment items.
- **`careerprep checklist scan <path>`** — point it at a real directory
  (e.g. one of your own capstone project folders) and it actually checks
  4 items for real: does a non-trivial `README.md` exist, does a
  `requirements.txt`/`pyproject.toml` exist, does a test file exist
  (`tests/` folder or `test_*.py`/`*_test.py`), does a `.gitignore`
  exist. The other 5 items (README explains WHY not just WHAT, no
  hardcoded secrets, an honest limitations section, tests exercise real
  logic, meaningful commit history) are printed as manual checkboxes —
  a script can't honestly judge those, so it doesn't pretend to.

A top-level **`--file <path>`** flag points interview commands at which
JSON answers file to read/write (defaults to `~/.careerprep/answers.json`).
A top-level **`-v/--verbose`** flag raises the tool's own log level from
INFO to DEBUG, scoped to `careerprep`'s own logger only.

## Why two modules, not one script

`interview.py` and `checklist.py` hold the actual logic — reading/writing
JSON, filtering questions, scanning a directory's real files. Neither
imports `argparse`, touches `sys.argv`, or calls `print()`. `cli.py` holds
the argparse parser, the `input()` calls that collect a typed answer, and
is the only place that talks to the terminal. This is the same
"separate the engine from the dashboard" split Chapter 31's `taskbox`
project used — `interview.py`/`checklist.py` could be reused by a future
web UI or test suite with zero changes.

## How to run it while building (starter, no install needed)

```bash
cd chapters/chapter-33-interview-career-prep/project/starter
python3 -m careerprep.cli --help
```

Running it this way works because Python adds the current directory to
`sys.path`, so `careerprep/` is importable as a package without
installing anything. Use `--file` to point at a scratch file so you don't
need `~/.careerprep/` to exist yet:

```bash
python3 -m careerprep.cli --file /tmp/my_answers.json interview list --category behavioral
```

Every TODO in `starter/careerprep/*.py` raises `NotImplementedError`
until you fill it in — that's on purpose, so `--help` partially works
even before you've written the logic, and you get a clear "not done yet"
signal (not a silent wrong answer) for pieces you haven't reached.

## How to run it as a real installed tool (solution)

```bash
cd chapters/chapter-33-interview-career-prep/project/solution
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -e .
```

Real output from actually running that install:

```text
$ pip install -e .
Obtaining file:///.../chapter-33-interview-career-prep/project/solution
  Installing build dependencies: started
  Installing build dependencies: finished with status 'done'
  ...
Building wheels for collected packages: careerprep
  Building editable for careerprep (pyproject.toml): finished with status 'done'
  Created wheel for careerprep: filename=careerprep-1.0.0-0.editable-py3-none-any.whl ...
Successfully built careerprep
Installing collected packages: careerprep
Successfully installed careerprep-1.0.0
```

### Feature 1, for real — mock-interview drill

```text
$ careerprep --file /tmp/demo_answers.json interview random --category behavioral
============================================================
#2 [behavioral] Describe a time you disagreed with a teammate's code review feedback. How did you handle it?
============================================================
(Type or paste your answer. Press Enter on a blank line when you're done.)
Situation: our checkout API started 500ing under load.
Task: I needed to find root cause before the weekend traffic spike.
Action: I added structured logging around the payment call and traced it to a connection pool exhaustion bug.
Result: fixed the pool size and added an alert so we caught it early next time.

INFO: Saved answer for question #2 (behavioral)
Saved your answer for question #2 at 2026-07-12T05:42:02+00:00.
```

A second practice session on a different (random) question, then
`review` showing both — proving the answers file **appends**, it never
overwrites past sessions:

```text
$ careerprep --file /tmp/demo_answers.json interview random --category technical
============================================================
#17 [technical] What does `git rebase` do differently from `git merge`, and when would you reach for one over the other?
============================================================
(Type or paste your answer. Press Enter on a blank line when you're done.)
A decorator wraps a function to add behavior without changing its source, e.g. logging execution time.
Real use case: a @require_auth decorator on Flask view functions.

INFO: Saved answer for question #17 (technical)
Saved your answer for question #17 at 2026-07-12T05:42:14+00:00.

$ careerprep --file /tmp/demo_answers.json interview review
--- Answer 1 of 2 ---
[2026-07-12T05:42:02+00:00] #2 (behavioral) Describe a time you disagreed with a teammate's code review feedback. How did you handle it?
  Situation: our checkout API started 500ing under load.
  Task: I needed to find root cause before the weekend traffic spike.
  Action: I added structured logging around the payment call and traced it to a connection pool exhaustion bug.
  Result: fixed the pool size and added an alert so we caught it early next time.

--- Answer 2 of 2 ---
[2026-07-12T05:42:14+00:00] #17 (technical) What does `git rebase` do differently from `git merge`, and when would you reach for one over the other?
  A decorator wraps a function to add behavior without changing its source, e.g. logging execution time.
  Real use case: a @require_auth decorator on Flask view functions.
```

`--category technical` filters the review to just that one:

```text
$ careerprep --file /tmp/demo_answers.json interview review --category technical
--- Answer 1 of 1 ---
[2026-07-12T05:42:14+00:00] #17 (technical) What does `git rebase` do differently from `git merge`, and when would you reach for one over the other?
  A decorator wraps a function to add behavior without changing its source, e.g. logging execution time.
  Real use case: a @require_auth decorator on Flask view functions.
```

### Feature 2, for real — checklist scan pointed at a real directory in this repo

This is `careerprep checklist scan` pointed at
`chapters/chapter-31-professional-python/project/solution/` — a real
chapter folder in this very repo. At the time of this scan, that folder
has a 140-character `README.md` (below the 200-character "substantial"
threshold), a `pyproject.toml`, no `tests/` folder or `test_*.py` files,
and no `.gitignore`:

```text
$ careerprep checklist scan ../../chapter-31-professional-python/project/solution
INFO: Scanned ../../chapter-31-professional-python/project/solution: 1/4 auto-checkable items passed
Scanning ../../chapter-31-professional-python/project/solution ...

Auto-checked (verified against real files on disk):
  [ ] README.md exists and is a non-trivial length (not a one-line placeholder)
  [x] requirements.txt or pyproject.toml declares dependencies
  [ ] At least one test file exists (tests/ folder or test_*.py / *_test.py)
  [ ] .gitignore exists

Manual self-assessment (not scannable -- be honest with yourself):
  [ ] README explains WHY the project exists, not just WHAT it does
  [ ] No hardcoded secrets or API keys anywhere in the codebase
  [ ] An honest 'Limitations' or 'Known Issues' section exists somewhere
  [ ] Tests actually exercise real logic, not just placeholder asserts
  [ ] Commit history shows incremental progress, not one giant commit
```

That result matches the real files on disk exactly — `pyproject.toml`
passes, the short `README.md` correctly fails the length check, and there
really is no `tests/` folder or `.gitignore` in that chapter's solution
folder. As a contrast, scanning a folder that actually has all four (a
substantial README, a `requirements.txt`, a `tests/` folder with a real
test file, and a `.gitignore`) reports a clean 4/4:

```text
$ careerprep checklist scan /tmp/portfolio_demo
INFO: Scanned /tmp/portfolio_demo: 4/4 auto-checkable items passed
Scanning /tmp/portfolio_demo ...

Auto-checked (verified against real files on disk):
  [x] README.md exists and is a non-trivial length (not a one-line placeholder)
  [x] requirements.txt or pyproject.toml declares dependencies
  [x] At least one test file exists (tests/ folder or test_*.py / *_test.py)
  [x] .gitignore exists

Manual self-assessment (not scannable -- be honest with yourself):
  [ ] README explains WHY the project exists, not just WHAT it does
  [ ] No hardcoded secrets or API keys anywhere in the codebase
  [ ] An honest 'Limitations' or 'Known Issues' section exists somewhere
  [ ] Tests actually exercise real logic, not just placeholder asserts
  [ ] Commit history shows incremental progress, not one giant commit
```

### Error handling, for real

```text
$ careerprep checklist scan /tmp/does_not_exist_xyz
ERROR: No such directory: /tmp/does_not_exist_xyz
$ echo $?
1

$ careerprep interview list --category nope
usage: careerprep interview list [-h] [--category {behavioral,technical}]
careerprep interview list: error: argument --category: invalid choice: 'nope' (choose from behavioral, technical)
$ echo $?
2
```

### `--verbose`, for real

```text
$ careerprep --file /tmp/demo_answers.json -v interview random --category behavioral
DEBUG: Returning 10 question(s) (category=behavioral)
DEBUG: Picked random question #7 (category=behavioral)
============================================================
#7 [behavioral] Tell me about a time you had to prioritize between multiple competing deadlines.
============================================================
(Type or paste your answer. Press Enter on a blank line when you're done.)
Answer text here.

DEBUG: Loading answers from /tmp/demo_answers.json
DEBUG: Saving 3 answer(s) to /tmp/demo_answers.json
INFO: Saved answer for question #7 (behavioral)
Saved your answer for question #7 at 2026-07-12T05:42:46+00:00.
```

Without `-v`, only the `INFO:` line shows.

## Why `requirements.txt` is (correctly) empty

`careerprep` only imports from the standard library: `argparse`,
`logging`, `json`, `pathlib`, `datetime`, `random`, `textwrap`. There is
nothing to pin. The file is kept (not deleted) with a comment explaining
that.

## Verify it yourself

```bash
cd chapters/chapter-33-interview-career-prep/project/solution
python3 -m careerprep.cli --file /tmp/verify.json interview list
python3 -m careerprep.cli checklist scan .
```

If both commands print output with no traceback, the package is wired
up correctly.

## Why this project matters

Every real interview loop combines exactly these two things: practicing
how you talk about your work out loud (or in writing, for a take-home),
and having a portfolio that actually holds up when someone opens the
folder. A checklist you never run against real files is just a list you
feel good about; a mock-interview tool that doesn't save your answers
gives you no way to notice you're getting better. This project is a
small, honest version of both — the same shape you'd want for real job
prep, built with the same subcommands-plus-package pattern you used for
`taskbox` back in Chapter 31.

## More project ideas

No starter/solution files are provided for these on purpose — building
and verifying each one yourself is the point. Each is solvable with only
what this chapter (and earlier chapters) have taught.

### 1. Add a `--timer` flag that times how long you take to answer each question

**Scenario:** Real interviews are timed, even if informally — a behavioral
answer that takes eight minutes to get to the point is a real problem,
and you won't notice unless you measure it.

**What to do:** Add a `--timer` flag to `interview random`. When set,
start a timer (`time.monotonic()`) right after the question is printed,
and stop it right after `read_multiline_answer()` returns. Print the
elapsed time, and save it alongside the answer in the JSON entry (a new
`elapsed_seconds` key).

**Suggested approach:** `time.monotonic()` before and after, subtract,
`round(..., 1)` for a clean display — don't use `time.time()`, which can
jump backward if the system clock adjusts mid-interview.

### 2. Add a 1-5 confidence self-rating after each answer

**Scenario:** Raw answer text doesn't tell you which questions you
actually feel shaky on — a self-rating, tracked over time, does.

**What to do:** After saving an answer in `interview random`, prompt
`"How confident do you feel about that answer? (1-5): "`, validate it's
an int 1-5 (re-prompt on bad input), and save it in the JSON entry
alongside the answer as a `confidence` key. Add a way to see your average
confidence per question when reviewing (e.g. group `interview review`
entries by `question_id` and print the average).

**Suggested approach:** A small `while True:` input-validation loop, the
same pattern you used in earlier chapters' menu-driven projects.

### 3. Extend the checklist scanner to check for a LICENSE file and a CI workflow

**Scenario:** Two more genuinely checkable portfolio signals: does the
repo have an open-source license, and does it have any automated CI at
all.

**What to do:** Add two more auto-checkable items to `CHECKLIST_ITEMS` in
`checklist.py`: `license_exists` (a `LICENSE`, `LICENSE.md`, or
`LICENSE.txt` file at the project root) and `ci_workflow_exists` (a
`.github/workflows/` folder containing at least one `.yml`/`.yaml` file).
Wire both into `scan_directory()`'s results dict the same way the
existing four items work.

**Suggested approach:** Reuse the `_find_file()` helper pattern for
`LICENSE*`; for the CI check, `(target / ".github" / "workflows").is_dir()
and any((target / ".github" / "workflows").glob("*.y*ml"))`.

### 4. Add an export-to-markdown feature that turns saved answers into a study guide

**Scenario:** A JSON file of past answers isn't something you'd actually
review the night before an interview — a readable document is.

**What to do:** Add a new `careerprep interview export <output.md>`
subcommand. It should load all saved answers (optionally filtered by
`--category`), group them by question, and write a Markdown file with
one `## Question text` heading per question followed by each of your
saved answers to it in chronological order (so you can literally watch
your own answer improve across attempts, read top to bottom).

**Suggested approach:** Build a `dict[int, list[dict]]` keyed by
`question_id` from the loaded answers (a dict of lists, same pattern used
elsewhere in this course for grouping), then iterate it to build the
Markdown string before writing it with `Path(output).write_text(...)`.
