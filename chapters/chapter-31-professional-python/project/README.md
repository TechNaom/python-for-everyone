# Chapter 31 Project: taskbox — a Packaged CLI Tool

A real, multi-file, pip-installable command-line task manager — not a
single-file script. `taskbox` has four subcommands (`add`, `list`,
`done`, `delete`), persists tasks to a JSON file, uses real `logging`
instead of `print()` for its diagnostic output, and ships with a
correct `pyproject.toml` so it can be installed with
`pip install -e .` and run as a plain `taskbox` command from anywhere.

## Project layout

```text
project/
├── starter/            <- you work here
│   └── taskbox/
│       ├── __init__.py
│       ├── core.py      (TODOs 1-14 — the task logic)
│       └── cli.py       (TODOs 15-26 — the argparse wiring)
├── solution/            <- complete, working reference
│   ├── taskbox/
│   │   ├── __init__.py
│   │   ├── core.py
│   │   └── cli.py
│   ├── pyproject.toml
│   ├── requirements.txt
│   └── README.md
```

Both `starter/` and `solution/` are real installable packages — each
has its own `taskbox/` package directory. The starter's `pyproject.toml`
and `requirements.txt` are identical to the solution's (packaging is
not part of the TODOs; the logic in `core.py`/`cli.py` is). Copy them
in from `solution/` once you're ready to test `pip install -e .`, or
just run the starter directly with `python3 -m taskbox.cli` while you
work through the TODOs — no install needed for that.

## What you're building

- **`taskbox add "<title>" [--priority low|normal|high]`** — add a task.
- **`taskbox list [--all] [--priority ...]`** — list tasks (pending
  only by default; `--all` includes completed ones).
- **`taskbox done <id>`** — mark a task complete.
- **`taskbox delete <id>`** — delete a task.
- A top-level **`--file <path>`** flag on every subcommand, pointing at
  which JSON file to read/write (defaults to `~/.taskbox/tasks.json`).
- A top-level **`-v/--verbose`** flag that raises the tool's own log
  level from INFO to DEBUG — without flooding the terminal with debug
  noise from any library the tool might import.

## Why two files, not one script

`core.py` holds the actual task logic — loading/saving the JSON file,
adding/listing/completing/deleting tasks. It never imports `argparse`,
never touches `sys.argv`, and never calls `print()`. `cli.py` holds the
argparse parser and is the only place that talks to the terminal.

This split is the same "separate the engine from the dashboard" idea
you've seen in earlier projects — `core.py` could be reused by a future
web API or test suite with zero changes, because it doesn't know a
terminal exists.

## How to run it while building (starter, no install needed)

```bash
cd chapters/chapter-31-professional-python/project/starter
python3 -m taskbox.cli --help
```

Running it this way (`python3 -m taskbox.cli ...`) works because
Python adds the current directory to `sys.path`, so `taskbox/` is
importable as a package without installing anything. Use `--file` to
point at a scratch file so you don't need `~/.taskbox/` to exist yet:

```bash
python3 -m taskbox.cli --file /tmp/my_tasks.json add "Learn packaging"
python3 -m taskbox.cli --file /tmp/my_tasks.json list
```

Every TODO in `starter/taskbox/core.py` and `starter/taskbox/cli.py`
raises `NotImplementedError` until you fill it in — that's on purpose,
so `--help` and argument parsing partially work even before you've
written the logic, and you get a clear "not done yet" signal (not a
silent wrong answer) for pieces you haven't reached.

## How to run it as a real installed tool (solution)

This is the part that makes it a genuinely "packaged" CLI tool, not
just a script — installing it with `pip` so `taskbox` becomes a normal
command on your `PATH`, runnable from any directory.

```bash
cd chapters/chapter-31-professional-python/project/solution
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -e .
```

`-e` (editable) installs the package in a way that still reads from
this source folder — so changes to `taskbox/*.py` take effect
immediately, without reinstalling. This is real output from actually
running that install:

```text
$ pip install -e .
Obtaining file:///.../chapter-31-professional-python/project/solution
  Installing build dependencies: started
  Installing build dependencies: finished with status 'done'
  ...
Building wheels for collected packages: taskbox
  Building editable for taskbox (pyproject.toml): finished with status 'done'
  Created wheel for taskbox: filename=taskbox-1.0.0-0.editable-py3-none-any.whl ...
Successfully built taskbox
Installing collected packages: taskbox
Successfully installed taskbox-1.0.0
```

Now `taskbox` is a real command:

```text
$ taskbox --file /tmp/demo_tasks.json add "Ship chapter 31"
INFO: Added task #1: Ship chapter 31
Added task #1: Ship chapter 31

$ taskbox --file /tmp/demo_tasks.json add "Review PR" --priority high
INFO: Added task #2: Review PR
Added task #2: Review PR

$ taskbox --file /tmp/demo_tasks.json list
[ ] #1 (normal) Ship chapter 31
[ ] #2 (high) Review PR

$ taskbox --file /tmp/demo_tasks.json done 1
INFO: Marked task #1 done: Ship chapter 31
Marked done: #1 Ship chapter 31

$ taskbox --file /tmp/demo_tasks.json list
[ ] #2 (high) Review PR

$ taskbox --file /tmp/demo_tasks.json list --all
[x] #1 (normal) Ship chapter 31
[ ] #2 (high) Review PR
```

Notice task #1 disappears from the plain `list` once it's done —
that's the `show_done` filter — but reappears with `--all`.

### Error handling, for real

An error case, run for real, not invented for the docs:

```text
$ taskbox --file /tmp/demo_tasks.json done 999
ERROR: No task with id 999.
$ echo $?
1
```

A missing required argument, run for real:

```text
$ taskbox add
usage: taskbox add [-h] [--priority {low,normal,high}] title
taskbox add: error: the following arguments are required: title
$ echo $?
2
```

argparse handles that second case entirely on its own — no code in
`cli.py` had to catch it. That's the payoff of a real argument parser
over hand-rolling `sys.argv[1]` checks: bad input gets a clear message
and a non-zero exit code (which matters if `taskbox` is ever called
from a shell script that checks `$?`) for free.

### `--verbose`, for real

```text
$ taskbox --file /tmp/demo_tasks.json -v add "Debug this"
DEBUG: Loading tasks from /tmp/demo_tasks.json
DEBUG: Saving 3 task(s) to /tmp/demo_tasks.json
INFO: Added task #3: Debug this
Added task #3: Debug this
```

Without `-v`, only the `INFO:` line shows — the `DEBUG:` lines are
suppressed by the logger's level, not by removing print statements.
That's the actual difference between `logging` and scattering
`print()` calls everywhere: one flag controls verbosity for the whole
tool, and none of the diagnostic messages had to be deleted or
commented out to quiet them down.

## Why `requirements.txt` is (correctly) empty

`taskbox` only imports from the standard library: `argparse`,
`logging`, `json`, `pathlib`, `datetime`. There is nothing to pin. The
file is kept (not deleted) with a comment explaining that — an empty
`requirements.txt` that says "nothing needed" is a deliberate,
documented design choice; a *missing* `requirements.txt` just looks
like someone forgot to write one.

## Verify it yourself

```bash
cd chapters/chapter-31-professional-python/project/solution
python3 -m taskbox.cli --file /tmp/verify.json add "Sanity check"
python3 -m taskbox.cli --file /tmp/verify.json list
```

If both commands print output with no traceback, the package is wired
up correctly.

## Why this project matters

Every real Python tool you've used from a terminal — `pip`, `black`,
`pytest`, `git` itself — is exactly this shape: subcommands parsed by
something like `argparse`, logic separated from the argument-parsing
layer, `logging` instead of scattered `print()`s so verbosity is a
flag instead of a code edit, and a packaging file that makes `pip
install` turn a folder of `.py` files into a real command. This
project is a small, honest version of that shape — the same one you'd
scale up for a real internal tool at a job.

## More project ideas

No starter/solution files are provided for these on purpose — building
and verifying each one yourself is the point. Each is solvable with
only what this chapter (and earlier chapters) have taught.

### 1. Wrap an earlier project's logic in a proper CLI

**Scenario:** You already built a menu-driven tool in an earlier
chapter (e.g. the inventory tracker or a similar loop-based project)
that reads input with `input()` in a `while True:` loop.

**What to do:** Rewrite it as a package with subcommands instead —
`inventory add`, `inventory list`, `inventory remove`, etc. — using the
same `core.py`/`cli.py` split this project uses. The underlying logic
barely changes; only how a user reaches it does.

**Suggested approach:** Start by writing down what your old `while
True:` menu options were — each menu option usually maps to exactly
one subcommand.

### 2. Add a `--config` flag that reads defaults from a file

**Scenario:** Typing `--priority high` on every single `taskbox add`
call gets old if you mostly add high-priority tasks.

**What to do:** Add a `--config` flag pointing at a small JSON (or
`.ini`, using `configparser`) file with a `default_priority` key. Load
it (if present) before parsing args, and use its value as the
`--priority` default instead of the hardcoded `"normal"`.

**Suggested approach:** `argparse` lets you build the parser's defaults
dynamically before calling `add_argument` — read the config file first,
then pass its value as `default=` for that argument.

### 3. Add a `--dry-run` flag

**Scenario:** Before deleting a task (or running any destructive
command), it's useful to preview what *would* happen without actually
changing anything.

**What to do:** Add a top-level `--dry-run` flag. When set, `delete`
and `done` should print what they *would* do (`"Would delete: #2 Buy
groceries"`) without calling `save_tasks`.

**Suggested approach:** Thread the flag from `args.dry_run` down into
`core.py`'s functions as a parameter, and add an `if dry_run: return
...` early-exit right before the `save_tasks` call in each.

### 4. Publish it as a real installable package with a second entry point

**Scenario:** `taskbox` currently has one console script. Real CLI
tools sometimes ship a second, shorter alias.

**What to do:** Add a second entry under `[project.scripts]` in
`pyproject.toml` — e.g. `tb = "taskbox.cli:main"` — reinstall with
`pip install -e .`, and confirm both `taskbox` and `tb` work identically.
Then try `pip uninstall taskbox` and confirm both commands disappear.

**Suggested approach:** `[project.scripts]` is just a mapping of
command-name → `module:function` — add as many keys as you want, they
all point at the same `main()`.
