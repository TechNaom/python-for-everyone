# Capstone 3: Ops Toolkit

## Overview

Three tools you already built separately — the Chapter 13 Log-File
Analyzer, the Chapter 18 Resume Keyword Scanner, and the Chapter 19
Weather & Quote-of-the-Day Fetcher — get unified into **one installable,
multi-subcommand CLI package** called `ops`. Instead of three
`python3 starter.py` scripts with three different menu loops, you ship one
real command with a consistent interface: `ops logs analyze server.log`,
`ops scan resume resume.txt --keywords Python,SQL,Docker`,
`ops fetch weather Austin`. This capstone isn't about writing new logic —
it's about proving you can take working-but-separate code and turn it into
one coherent, professional tool.

## Skills this combines

- **Chapter 13 (File Handling & CSV)** — the log-analysis engine:
  `open()`/`with`, reading a log file line by line, counting by log
  level, keyword search, and a `csv.writer` export, all lifted from the
  Log-File Analyzer's function library (`load_log_lines`,
  `count_by_level`, `search_lines`, `most_common_error`,
  `export_summary`).
- **Chapter 18 (Regular Expressions)** — the resume-scanning engine:
  the `ResumeScanner` class's compiled patterns (`EMAIL_PATTERN`,
  `PHONE_PATTERN`), word-boundary-anchored keyword matching
  (`r"\b" + re.escape(keyword) + r"\b"` with `re.IGNORECASE`), and the
  found/missing/match-percentage report shape from `match_report()`.
- **Chapter 19 (APIs & JSON)** — the fetch engine: the
  `fetch → parse → format` pipeline, mocked JSON "API" responses (no real
  network calls, same as the original project), and the
  `status`-checking defensive-parsing pattern from `parse_weather()`/
  `parse_quote()`.
- **Chapter 31 (Professional Python)** — the packaging shape: a real
  `pyproject.toml` so `pip install -e .` makes `ops` a command on your
  `PATH`, `argparse` **subparsers** (one level deeper than taskbox's flat
  subcommands, since `ops` needs a subcommand-of-a-subcommand:
  `ops logs analyze`, not just `ops analyze`), `logging` instead of
  `print()` for diagnostics, and the `core.py`/`cli.py`-style split
  between logic and terminal-facing code.

## Prerequisites

Complete these chapters first:

- [Chapter 13: File Handling & CSV](../../chapter-13-file-handling-csv/lesson.html)
- [Chapter 18: Regular Expressions](../../chapter-18-regular-expressions/lesson.html)
- [Chapter 19: APIs & JSON](../../chapter-19-apis-json/lesson.html)
- [Chapter 31: Professional Python](../../chapter-31-professional-python/lesson.html)

You should have already built (or at least read) all three source
projects — [Log-File Analyzer](../../chapter-13-file-handling-csv/project/README.md),
[Resume Keyword Scanner](../../chapter-18-regular-expressions/project/README.md),
[Weather & Quote-of-the-Day Fetcher](../../chapter-19-apis-json/project/README.md)
— and the [taskbox](../../chapter-31-professional-python/project/README.md)
packaging pattern, since this capstone reuses its `core.py`/`cli.py` split
directly.

## Architecture

```text
ops/                              <- installable package root
├── pyproject.toml                <- [project.scripts] ops = "ops.cli:main"
├── requirements.txt              <- stdlib only: empty, with a comment (see taskbox)
├── ops/
│   ├── __init__.py
│   ├── cli.py                    <- ONLY file that touches argparse/sys.argv/print()
│   ├── logs.py                   <- Ch13 engine: load_log_lines, count_by_level,
│   │                                search_lines, most_common_error, export_summary
│   ├── scan.py                   <- Ch18 engine: ResumeScanner class, EMAIL_PATTERN,
│   │                                PHONE_PATTERN, find_keyword_matches, match_report
│   ├── fetch.py                  <- Ch19 engine: fetch_weather/parse_weather/
│   │                                format_weather, fetch_quote/parse_quote/format_quote
│   └── formatting.py             <- shared output helpers used by all three subcommands
│                                     (see "shared conventions" below)
└── tests/                        <- optional but recommended; see Chapter 27 patterns
```

**Subcommand tree** (`argparse` subparsers-of-subparsers, one parent
subparser per domain, each with its own child subparsers):

```text
ops
├── logs
│   ├── analyze <file>              [--level] [--keyword] [--export FILE]
├── scan
│   ├── resume <file> --keywords a,b,c
│   ├── contacts <file>              (email/phone extraction)
└── fetch
    ├── weather <city> [--simulate-error]
    └── quote [--index N]
```

**Why one package, not three scripts glued together with `if` checks:**
each domain (`logs`, `scan`, `fetch`) is its own module with its own pure
functions — none of them import `argparse` or call `print()`, exactly
like `core.py` in taskbox. `cli.py` is the *only* place that parses
arguments, formats output, and decides what exit code to return. That
means the log-analysis engine, the resume scanner, and the fetch pipeline
could each be imported and reused by a future script or test suite with
zero changes — the same "engine vs. dashboard" separation taskbox
established.

**Shared conventions that make this feel like one tool, not three stapled
together:**

- One `--file`-style pattern: every subcommand takes its target
  (log file, resume file, city name) as a positional argument, not
  inconsistent flags.
- One error-handling convention: every domain module raises a plain
  Python exception (`FileNotFoundError` for missing files, a custom
  `OpsError` for "not found"/"bad input" cases) and lets it propagate;
  `cli.py` has exactly one `try`/`except` wrapper per subcommand handler
  that catches, logs an `ERROR:`-prefixed message via `logging`, and
  returns exit code `1` — never three different ad hoc error-printing
  styles.
- One output convention: a shared `formatting.py` helper (e.g.
  `print_table(rows, headers)` or `print_kv(pairs)`) used by all three
  domains for their tabular/list output, so `ops logs analyze` and
  `ops scan resume` don't each invent their own alignment/spacing rules.
- One `--verbose`/`-v` top-level flag (taskbox's pattern) that raises log
  level from INFO to DEBUG across *all* subcommands, not just one.
- One `--help` system: `ops --help` lists the three domains; `ops logs
  --help` lists `analyze`; `ops logs analyze --help` shows that command's
  specific flags — all generated by argparse for free once the subparser
  tree is wired up correctly.

## Step-by-step roadmap

**Phase 1: Extract the three engines (~2 hours).** Copy the pure-logic
functions out of each original project's `solution.py` into
`ops/logs.py`, `ops/scan.py`, `ops/fetch.py`. Strip out every `print()`
and every `input()` call — these become plain functions that take
arguments and return values (or raise exceptions), exactly like
taskbox's `core.py`. Run each module's functions from a plain Python
REPL or a scratch script to confirm the logic still works before touching
argparse at all.

**Phase 2: Design the subparser tree (~1.5 hours).** In `cli.py`, build
the top-level parser with `subparsers = parser.add_subparsers(dest="domain")`,
then for each domain (`logs`, `scan`, `fetch`) add its own subparser that
*itself* adds subparsers for its specific actions (`analyze`; `resume`,
`contacts`; `weather`, `quote`). Wire a top-level `--file`/positional
argument, plus `-v/--verbose` and any per-command flags (`--keywords`,
`--export`, `--simulate-error`). Confirm `ops --help`, `ops logs --help`,
and `ops logs analyze --help` all render sensibly before writing any
handler logic.

**Phase 3: Wire handlers and shared formatting (~2 hours).** Write one
handler function per leaf subcommand (`handle_logs_analyze`,
`handle_scan_resume`, etc.) in `cli.py`, each calling into the
corresponding engine module and passing results through
`formatting.py`'s shared helpers. Set up `logging` once (matching
taskbox's INFO/DEBUG split) instead of scattering `print()` for
diagnostics — reserve `print()` for the actual user-facing result.

**Phase 4: Error handling and exit codes (~1 hour).** Make every domain
module raise real exceptions instead of returning `None`/error strings.
In `cli.py`, wrap each handler call in one `try`/`except`, log the error,
and `sys.exit(1)`. Test the failure paths for real: a missing log file,
a resume file that doesn't exist, an unsupported city.

**Phase 5: Packaging and install (~1 hour).** Write `pyproject.toml`
(model it directly on taskbox's — `[project.scripts] ops =
"ops.cli:main"`), an empty-but-documented `requirements.txt` (this
capstone is stdlib-only, same as taskbox: `argparse`, `logging`, `re`,
`csv`, `json`, `os`), then `pip install -e .` in a fresh venv and confirm
`ops` runs as a bare command from any directory.

**Phase 6: README and verification (~1.5 hours).** Write `project/README.md`
following the guidance below. Run every subcommand for real, capture
actual terminal output (not invented), and paste it into the README —
same standard taskbox's README holds itself to ("run for real, not
invented for the docs").

## MVP vs. stretch goals

**MVP (required to call this capstone done):**

- All three domains (`logs`, `scan`, `fetch`) reachable through one
  installed `ops` command with a working subparser tree.
- Each domain's *core* original feature works: log level counts +
  keyword search + CSV export; resume keyword matching + contact
  extraction; mocked weather fetch + quote fetch (including the
  simulated-error path).
- One shared error-handling convention and one shared output-formatting
  convention used by all three domains — not three different styles.
- A working `pyproject.toml`; `pip install -e .` succeeds and `ops
  --help` / every subcommand's `--help` renders correctly.
- `-v/--verbose` works globally.

**Stretch goals:**

- A `--json` global flag that makes every subcommand print structured
  JSON instead of formatted text (useful for piping `ops` output into
  another tool) — reuses Chapter 19's `json` module.
- A `--config` file (JSON or `.ini` via `configparser`, per taskbox's
  own stretch-goal #2) storing defaults like a preferred city for
  `ops fetch weather` or a default keyword list for `ops scan resume`.
- A `ops logs analyze --watch` mode that re-reads the log file every N
  seconds and prints only new anomalies (builds on Chapter 20's
  threading/timing ideas if you've covered it).
- A second console-script entry point (e.g. a shorter `o` alias),
  matching taskbox's own stretch goal #4.
- Batch mode: `ops scan resume *.txt` scanning every matching file in
  one call and printing a per-file summary table.

## What a strong README for this capstone looks like

- **Open with the "why unify three tools" pitch** in 2-3 sentences —
  not "here's what each subcommand does" as the first thing a reader
  sees, but why one coherent tool beats three loose scripts (discovery
  via one `--help`, one install step, one consistent error style).
- **A subcommand tree diagram** (like the one in this doc) near the top,
  so a reader can see the whole shape of the tool at a glance before
  reading prose.
- **Real, copy-pasted terminal output** for at least one command from
  each domain — actually run `ops logs analyze`, `ops scan resume`, and
  `ops fetch weather`, and paste the real output, including one genuine
  error case (a missing file) showing the error message and exit code,
  the same standard taskbox's README holds ("run for real, not invented
  for the docs").
- **An install section** showing the full `python3 -m venv` → `pip
  install -e .` → `ops --help` sequence, copied from a real terminal run,
  not written from memory.
- **A short "what came from which chapter" table or list** — this is a
  capstone about combining prior work, so name the chapters explicitly
  (this doc's "Skills this combines" section is a good template).
- **A "why `requirements.txt` is empty" note** if you keep this
  stdlib-only, following taskbox's own precedent — a documented empty
  file, not a missing one.

## Common pitfalls

- **Three different error-handling styles bolted together.** The most
  likely failure mode: the log module still uses the original project's
  bare `try/except FileNotFoundError: print(...)`, the scan module raises
  a custom exception, and the fetch module returns `None` on failure —
  and `cli.py` has three different `if`/`except` shapes to cope with all
  three. This is exactly the "feels stapled together, not designed as
  one tool" failure this capstone is testing for. Pick one convention
  (this doc recommends: engine modules raise, `cli.py` catches once per
  handler) and apply it to *all three* domains, even where the original
  project did it differently.
- **Argparse subparser depth confusion.** Forgetting that `ops logs
  analyze` needs *two* levels of subparsers (a `logs` subparser that
  itself has an `analyze` sub-subparser), not one flat subparser named
  `"logs analyze"` — this silently breaks `--help` discovery and
  argument routing. Test the exact command shape (`ops logs analyze
  file.log`) early, not just that argparse "accepts something."
  reference here.
- **Leaking `print()`/`input()` into the engine modules.** If
  `ops/logs.py` still has `print()` calls left over from the original
  menu-driven `solution.py`, output ends up duplicated or
  wrongly-ordered once `cli.py` also tries to format results — same
  "engine talks to the terminal" bug taskbox's README calls out
  explicitly for `core.py`.
- **Losing the regex correctness details from Chapter 18 during the
  port.** It's easy to accidentally drop the word-boundary anchoring
  (`\b`) or `re.escape()` around user-supplied keywords while moving
  `ResumeScanner` into `ops/scan.py` — verify `--keywords SQL` still
  doesn't false-positive-match `"MySQL"` after the port, exactly the bug
  the original project's README calls out.
- **Mocked fetch data accidentally becoming "real" in spirit.** Keep
  `ops/fetch.py`'s weather/quote data hardcoded JSON strings, exactly
  like the original project — don't reach for `requests` or a live API
  just because this is "the professional version"; the whole point of
  the original mocked pipeline (deterministic, no network dependency)
  still applies here.

## Self-assessment checklist

- [ ] `pip install -e .` succeeds from a clean virtual environment with
      no errors.
- [ ] `ops --help` lists all three domains; each domain's `--help` lists
      its actions; each action's `--help` lists its specific flags.
- [ ] `ops logs analyze <file>` reproduces the Chapter 13 project's level
      counts, keyword search, and CSV export.
- [ ] `ops scan resume <file> --keywords ...` reproduces the Chapter 18
      project's found/missing/percentage report, including correct
      word-boundary matching (`SQL` doesn't match `MySQL`).
- [ ] `ops scan contacts <file>` reproduces the Chapter 18 project's
      email/phone extraction.
- [ ] `ops fetch weather <city>` and `ops fetch quote` reproduce the
      Chapter 19 project's mocked fetch → parse → format pipeline,
      including the simulated-error path.
- [ ] All three domains use the *same* error-handling convention (one
      exception style, one catch point in `cli.py`) and the *same*
      output-formatting helpers.
- [ ] `-v/--verbose` raises log level to DEBUG across every subcommand,
      not just one.
- [ ] At least one genuine error case (missing file, bad city) was run
      for real and its actual output/exit code is pasted into the README.
- [ ] No `print()` or `input()` calls exist inside `logs.py`, `scan.py`,
      or `fetch.py` — only in `cli.py`.
- [ ] `requirements.txt` is present and either lists real third-party
      deps or is a documented-empty stdlib-only file.
