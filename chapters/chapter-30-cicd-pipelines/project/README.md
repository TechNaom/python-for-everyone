# Chapter 30 Project: Lint + Test + Ship

A real, multi-piece CI/CD setup — not a single calculator.py with a
one-job workflow bolted on. You'll work with an actual installable
Python package (`expense_tracker`, three modules plus a real pytest
suite of 22 tests), find and fix one genuine lint violation in it, and
read through a real multi-job, matrix-strategy GitHub Actions workflow
that lints and tests that package across two Python versions.

## What's here

```text
project/
├── starter.py            → run this first: confirms your tools, shows you
│                            the lint violation and the passing test suite,
│                            as shipped
├── solution.py            → run this after you fix the violation: a
│                            verifier that runs ruff + pytest for real and
│                            parses ci.yml with yaml.safe_load() to confirm
│                            it's still structurally correct
└── sample_project/        → the real package this whole project is about
    ├── expense_tracker/
    │   ├── __init__.py
    │   ├── models.py       → the Expense dataclass
    │   ├── tracker.py      → ExpenseTracker: add/total/filter/budget logic
    │   └── report.py       → summary_lines()/print_summary() -- HAS the
    │                          one intentional lint violation (an unused
    │                          `import sys`)
    ├── tests/
    │   ├── test_models.py
    │   ├── test_tracker.py
    │   └── test_report.py  → 22 real pytest tests total, happy paths + edge cases
    ├── .github/workflows/
    │   └── ci.yml          → the real multi-job workflow: lint job + a
    │                          matrix test job (Python 3.11 and 3.12), pip
    │                          caching, triggers on both push and pull_request
    ├── pyproject.toml
    ├── requirements-dev.txt
    └── README.md
```

## Important: no live GitHub Actions run happens here

This site/course has no way to actually push to GitHub or trigger a
real Actions run from this environment. What you're building and
verifying instead is **everything a live run would actually do**,
run for real, locally:

- `ruff check .` — the exact command the workflow's lint job runs.
- `pytest` — the exact command the workflow's test job runs (the
  workflow just runs it twice, once per matrix Python version).
- `yaml.safe_load()` on `ci.yml` — confirms the workflow file itself
  is valid, parseable YAML with the jobs, triggers, matrix, and
  caching it's supposed to have.

If you pushed this `sample_project/` folder to a real GitHub repo with
Actions enabled, `ci.yml` would run exactly these same commands on
GitHub's own runners — that's the entire point of a CI workflow: the
commands it runs are not special, they're the same commands you can
and should run yourself.

## How to run

```bash
cd chapters/chapter-30-cicd-pipelines/project
python3 starter.py
```

This installs `pytest` and `ruff` if you don't have them, then runs
both against `sample_project/` as shipped — you'll see ruff catch
exactly one violation (the unused import) and pytest pass all 22
tests.

## Your job

### 1. Fix the lint violation

Open `sample_project/expense_tracker/report.py`. Near the top:

```python
import sys  # unused import -- intentionally left in for the lint job to catch
```

`sys` is never actually used anywhere in the file. Delete that import
line, then re-run `ruff check .` from inside `sample_project/` and
confirm it reports zero violations.

```bash
cd sample_project
ruff check .
```

### 2. Read through ci.yml

Open `sample_project/.github/workflows/ci.yml`. It has two jobs:

- **`lint`** — checks out the code, sets up Python 3.12 with pip
  caching, installs `requirements-dev.txt`, and runs `ruff check .`.
- **`test`** — same setup, but under a `strategy: matrix:` with
  `python-version: ["3.11", "3.12"]`, so the whole job (checkout,
  setup, install, `pytest -v`) runs twice, once per version, in
  parallel.

Both jobs trigger `on: push` and `on: pull_request` targeting `main`.
Neither job depends on the other (no `needs:` key), so in a real run
they'd start and run at the same time on separate runners.

### 3. Re-run everything and verify

```bash
cd sample_project
ruff check .
pytest -v
cd ..
python3 solution.py
```

`solution.py` runs `ruff check .` and `pytest` for real against your
edited copy, and re-parses `ci.yml` with `yaml.safe_load()` to confirm
the workflow itself is still structurally sound: valid YAML, both
triggers present, both jobs present, the matrix has 2+ Python
versions, and pip caching is configured. All 7 checks should pass once
you've fixed the lint violation.

## Why this project matters

A workflow YAML file is worthless if the commands inside it don't
actually behave the way you think they do — the single most common
real-world CI mistake is a workflow that looks correct but was never
actually run locally first, so a typo in a script name or a missing
dependency only surfaces after a push, wasting a full round trip. This
project forces the habit the rest of your CI/CD career depends on: run
the exact commands your workflow runs, locally, before you ever trust
what GitHub reports back.

## More project ideas

No starter/solution files are provided for these on purpose — each
one is meant to be built and verified by editing `ci.yml` (and
re-running the underlying commands) yourself.

### 1. Add a third Python version to the matrix, and think through the tradeoff

**Scenario:** Your team wants to officially support Python 3.10 in
addition to 3.11 and 3.12.

**What to do:** Add `"3.10"` to the `python-version` matrix list in
`ci.yml`. Actually run `pytest` locally under a Python 3.10
interpreter if you have one available (or reason through the code —
does `expense_tracker` use any syntax newer than 3.10?) to confirm it
would actually pass.

**Suggested approach:** Every extra matrix version is a real tradeoff:
more confidence the package works everywhere it claims to, at the
direct cost of more total CI runtime and more runner-minutes consumed
on every single push. Write down, in your own words, how you'd decide
where to draw the line for a real team's project.

### 2. Only run the expensive test job on pull_request, not every push

**Scenario:** The lint job is fast and cheap, but imagine the test job
were much slower (a large integration suite hitting a real database) —
running it on every single push to every branch would be wasteful.

**What to do:** Change the `test` job's trigger so it only runs `on:
pull_request`, while `lint` still runs on both `push` and
`pull_request`. (Hint: a job-level `on` doesn't exist — the trigger
lives at the workflow level, so this actually requires either two
separate workflow files, or an `if:` condition on the job checking
`github.event_name`.)

**Suggested approach:** Look up GitHub Actions' `github.event_name`
context variable and add `if: github.event_name == 'pull_request'` to
the `test` job, then validate the resulting YAML with
`yaml.safe_load()` the same way `solution.py` does.

### 3. Add a status badge to the README showing CI pass/fail

**Scenario:** Anyone visiting the repo on GitHub should be able to see
at a glance whether the latest commit on `main` is passing CI, without
clicking into the Actions tab.

**What to do:** GitHub generates a badge URL for any workflow:
`https://github.com/<owner>/<repo>/actions/workflows/ci.yml/badge.svg`.
Add that as a Markdown image at the top of `sample_project/README.md`:
`![CI](https://github.com/<owner>/<repo>/actions/workflows/ci.yml/badge.svg)`.

**Suggested approach:** Since this workflow was never actually pushed
to a real GitHub repo, the badge URL won't resolve to real data here —
write the correct badge Markdown anyway and explain, in a comment,
exactly what `<owner>/<repo>` would need to be replaced with for it to
work for real.

### 4. Add a job that builds a distributable package artifact

**Scenario:** Beyond lint and test, a real Python package's pipeline
usually also builds the actual installable artifact (a wheel) so it
can be published or deployed without rebuilding from source again.

**What to do:** Add a third job, `build`, that checks out the code,
sets up Python, installs the `build` package (`pip install build`),
runs `python -m build` inside `sample_project/` to produce a `.whl`
and `.tar.gz` in `dist/`, then uses `actions/upload-artifact@v4` to
save them. Actually run `python -m build` locally yourself to confirm
it produces real files in `dist/`.

**Suggested approach:** Since `pyproject.toml` already declares
`[build-system]` and `[tool.setuptools.packages.find]`, `python -m
build` should work as-is once the `build` package is installed —
inspect the resulting `dist/*.whl` filename and explain what each part
of it encodes (package name, version, Python tag).
