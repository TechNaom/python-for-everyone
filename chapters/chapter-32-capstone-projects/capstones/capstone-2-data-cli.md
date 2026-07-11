# Capstone 2: Data Insights CLI

## Overview

You already built the analysis logic for this twice — once over a raw
NumPy grid in Chapter 23's Grade & Statistics Analyzer, and once over a
pandas DataFrame in Chapter 24's Sales-Data Dashboard. Both were
menu-driven scripts hardwired to one sample dataset. This capstone
repackages that analysis logic as a real, installable command-line tool
— following the exact `core`/`cli` package split and `pyproject.toml`
pattern Chapter 31's `taskbox` used — that works against **any** CSV a
user points it at, not just the one baked into the script. "I can turn a
messy real-world CSV into a report from the command line" is a
genuinely useful, demonstrable skill for a portfolio, and a packaged CLI
reads as more finished than a script a reviewer has to open and edit to
use.

## Skills this combines

- **Chapter 24 (Pandas)** — the actual analysis pipeline: `pd.read_csv()`,
  a computed column (like `revenue = units_sold * unit_price`),
  `.groupby()` + `.sum()`/`.mean()` + `.sort_values()` for top-N
  breakdowns, and boolean filtering (`df[df['col'] < threshold]`) for
  flagging outliers/underperformers. This is the core logic this
  capstone carries forward almost unchanged — what changes is how a user
  reaches it.
- **Chapter 23 (NumPy)** — optional but encouraged: any place your
  report computes cross-cutting statistics (mean, median, standard
  deviation, min/max) on a numeric column, you can reach for the same
  `axis=`-aware aggregate functions and boolean-masking technique
  Chapter 23's Grade Analyzer used, applied to a pandas Series' `.values`
  or directly via pandas' own (NumPy-backed) `.mean()`/`.std()`.
- **Chapter 31 (Professional Python / packaging)** — the whole shape of
  this capstone. `taskbox` split `core.py` (logic, never imports
  `argparse`, never calls `print()`) from `cli.py` (the argparse parser,
  the only place that talks to the terminal) — this capstone uses that
  same split for its analysis logic. It also reuses `taskbox`'s
  `pyproject.toml` + `[project.scripts]` console-entry-point pattern so
  `pip install -e .` turns your package into a real command, and its
  `logging`-over-`print()` habit for diagnostic output.

## Prerequisites

Complete these chapters before starting (or at least skim their
lesson/project again if it's been a while):

- [Chapter 23: NumPy & Data Analysis](../../chapter-23-numpy-data-analysis/lesson.html)
- [Chapter 24: Pandas & Data Analysis](../../chapter-24-pandas-data-analysis/lesson.html)
- [Chapter 31: Professional Python](../../chapter-31-professional-python/lesson.html)

## Architecture

```text
                     $ datacli analyze sales.csv --group-by region
                     $ datacli report sales.csv --top 5
                     $ datacli export sales.csv --format json -o out.json
                                   |
                                   v
                cli.py  (argparse: subcommands + their flags)
        analyze / report / export subparsers, each mapping
        onto one function in core.py -- cli.py never touches
        pandas directly, only calls into core.py and prints
        what core.py hands back
                                   |
                                   v
                core.py  (the real logic, framework-agnostic)
        load_csv(path) -> DataFrame       (pd.read_csv, generalized --
                                            no hardcoded column names)
        compute_totals(df, group_by)      (Ch24's groupby+sum pattern)
        top_n(df, group_by, n)            (groupby+sum+sort_values)
        flag_outliers(df, column, threshold)  (Ch24's boolean filtering,
                                                optionally NumPy stats
                                                from Ch23 for mean/std)
        format_report(...)                (readable multi-section string)
                                   |
                                   v
                Any CSV file on disk the user points the tool at
        (NOT a hardcoded SALES_CSV string anymore -- the tool asks
         the user which columns matter via flags, e.g.
         --amount-column, --group-column, so it isn't locked to the
         sample dataset's exact column names)

                     packaged via pyproject.toml, same
                     [project.scripts] pattern as taskbox:
                     datacli = "datacli.cli:main"
                     -> `pip install -e .` makes `datacli` a
                        real command on PATH from any directory
```

The key architectural decision this capstone forces you to make and
defend: **how does the tool know which columns to analyze on a CSV it's
never seen before?** The sample dataset has known column names
(`product`, `region`, `units_sold`, `unit_price`), but a real CSV a
learner downloads might call the equivalent columns `Category`,
`Territory`, `Qty`, `Price`. Your CLI needs either flags letting the
user name their own columns (`--group-by`, `--value-column`) or a
documented convention for what it expects, and clear, honest error
messages when a required column is missing — not a raw pandas
`KeyError` traceback.

## Step-by-step roadmap

**Phase 1: Package structure (~1 hour)**
1. Create the package skeleton following `taskbox`'s layout:
   `datacli/__init__.py`, `datacli/core.py`, `datacli/cli.py`, plus a
   `pyproject.toml` at the project root.
2. Write `pyproject.toml` with your package metadata, a `pandas`
   dependency (and `numpy` if you're using it directly), and a
   `[project.scripts]` entry (`datacli = "datacli.cli:main"`).
3. `pip install -e .` immediately, even before any real logic exists,
   and confirm `datacli --help` runs (even if it just prints argparse's
   default usage) — catching packaging problems early beats debugging
   them after the logic is done.

**Phase 2: Generalize the analysis logic (~2-3 hours)**
4. Port Chapter 24's `load_sales()`, `total_revenue()`, `top_products()`/
   `top_regions()`, and `underperforming_sales()` into `core.py`,
   renamed to be dataset-agnostic (`load_csv()`, `compute_total()`,
   `top_n()`, `flag_outliers()`).
5. Remove every hardcoded column name (`'product'`, `'region'`,
   `'revenue'`) from `core.py`'s function bodies — every function that
   needs a column name should take it as a parameter instead, so the
   same function works on any CSV.
6. Add a validation step in `load_csv()` that checks whether the
   requested columns actually exist in the loaded DataFrame, raising a
   clear custom error (not a raw pandas `KeyError`) naming exactly which
   column was expected and which columns the file actually has.
7. Test `core.py`'s functions directly (a plain Python REPL or a scratch
   script is fine here) against both the original sales CSV and at
   least one CSV with different column names, to prove the
   generalization actually works before wiring up the CLI layer.

**Phase 3: Wire up argparse subcommands (~2 hours)**
8. Build `cli.py`'s parser with three subcommands, following `taskbox`'s
   `add`/`list`/`done`/`delete` subparser pattern:
   - `analyze <csv_path> --group-by COL --value-column COL` — prints
     total + per-group breakdown.
   - `report <csv_path> --group-by COL --value-column COL --top N` —
     prints the full formatted report (total, top-N groups, flagged
     outliers).
   - `export <csv_path> --format json|csv -o OUTPUT_PATH` — writes the
     computed summary to a file instead of just printing it.
9. Add a top-level `-v/--verbose` flag wired to Python's `logging`
   module (matching `taskbox`'s INFO/DEBUG pattern) instead of scattered
   `print()` calls for diagnostics.
10. Make sure every subcommand's required arguments produce argparse's
    normal clear error + non-zero exit code when missing — don't
    hand-roll your own argument validation where argparse already does
    it for free.

**Phase 4: Verify against a real, different CSV (~1 hour)**
11. Find (or hand-write) a small CSV that is NOT the sales sample and
    has different column names — expense tracking, weather readings,
    survey responses all work. Run `datacli analyze` /
    `datacli report` / `datacli export` against it for real and confirm
    the output makes sense.
12. Deliberately run the tool against a CSV missing a column you asked
    for, and confirm you get your clear custom error message, not a raw
    traceback.

**Phase 5: Polish and document (~1 hour)**
13. Write the README (see the section below), including real output
    from running all three subcommands.

## MVP vs. stretch goals

**MVP — must work to call this done:**
- `pip install -e .` produces a real `datacli` command runnable from any
  directory.
- All three subcommands (`analyze`, `report`, `export`) work against any
  CSV the user points them at, with column names passed as flags — not
  hardcoded to the sample sales dataset.
- A missing/misnamed column produces a clear, custom error message
  naming the problem, not a raw pandas traceback.
- `core.py` contains no `argparse` imports and no `print()` calls;
  `cli.py` is the only file that touches the terminal.
- A README with real example runs against at least two different CSVs.

**Stretch goals (optional, for learners who want to go further):**
- Add NumPy-backed summary statistics (mean, median, std, min, max) to
  the `report` output, reusing Chapter 23's `axis=`-aware pattern
  wherever the data is naturally 2D (e.g. multiple numeric columns).
- Add a `--config` flag (Chapter 31's stretch idea) pointing at a JSON
  file with default column names, so a user analyzing the same
  recurring CSV format doesn't have to retype flags every time.
- Support an additional input format (`.xlsx` via
  `pd.read_excel()`) alongside CSV, detected from the file extension.
- Add a second console-script alias (Chapter 31's stretch idea, e.g.
  `dcli` alongside `datacli`) pointing at the same `main()`.
- Add a `--chart` flag to `report` that saves a simple bar chart of the
  top-N groups as a `.png` using matplotlib.

## What a strong README for this capstone looks like

- **State the column-naming architecture decision explicitly** — did you
  go with required `--group-by`/`--value-column` flags, a documented
  default naming convention, or both (flags that fall back to sensible
  defaults)? Explain why, and show the exact command a user runs against
  a CSV with unusual column names.
- **Disclose real limitations honestly** — no support for extremely
  large files that don't fit in memory (pandas loads the whole CSV at
  once), no built-in handling of missing/NaN values beyond whatever
  pandas does by default (name what that default behavior actually is
  if you know it), single-file input only (no glob/batch mode) unless
  you built that as a stretch goal.
- **Show real output from at least two different CSVs** — the original
  sales-style dataset and one genuinely different one (different domain,
  different column names) — proving the "works on any CSV" claim isn't
  just asserted but demonstrated.
- **Document the install command and the exact subcommand syntax** for
  all three subcommands, the same way `taskbox`'s README shows real,
  copy-pasteable `taskbox add`/`list`/`done` examples with real output.

## Common pitfalls

- **Hardcoding a column name "just for now" and never coming back to
  generalize it.** It's easy to port Chapter 24's logic with
  `df['revenue']` still baked in, get it working against the sample CSV,
  and declare victory — the actual point of this capstone is that it
  works on a CSV it's never seen, so budget real time for Phase 4's
  different-CSV test, don't skip straight from "it works on the sample"
  to "done."
- **Letting a missing column crash with a raw pandas `KeyError`
  traceback.** A real CLI tool's users are not going to read a pandas
  stack trace to figure out they misspelled `--group-by Regoin`. Catch
  the missing-column case explicitly and print a clear message naming
  both what was requested and what columns actually exist in the file.
- **Forgetting `pyproject.toml` needs a real dependency list.**
  `taskbox` got away with an empty `requirements.txt` because it only
  used the standard library — this capstone genuinely depends on
  `pandas` (and maybe `numpy`), so `pyproject.toml`'s `dependencies =
  [...]` needs to list them, or a fresh `pip install -e .` on another
  machine will fail with an `ImportError` the first time `core.py` runs.
- **Mixing `print()` into `core.py` "just for a quick debug line."**
  Once one `print()` sneaks into the logic layer, `core.py` is no longer
  reusable by something else (a future web dashboard, a test suite)
  without dragging terminal output along with it — route every
  diagnostic message through `logging`, in `cli.py` only, the same
  discipline `taskbox` enforced.
- **Assuming numeric columns are always clean.** A real downloaded CSV
  might have a price column formatted as `"$1,234.56"` (a string, not a
  number) or contain blank cells in a numeric column. Decide explicitly
  how your tool handles this (reject with a clear error, or attempt a
  cleanup step) rather than letting pandas silently produce `NaN`s that
  quietly wreck your totals.

## Self-assessment checklist

- [ ] `pip install -e .` works from a clean clone and `datacli --help`
      shows all three subcommands.
- [ ] I ran `datacli analyze`, `datacli report`, and `datacli export`
      against the original sales-style CSV and against at least one
      genuinely different CSV (different domain, different column
      names) and both worked.
- [ ] Pointing the tool at a CSV missing a requested column produces my
      own clear error message, not a raw pandas traceback.
- [ ] `core.py` has zero `argparse` imports and zero `print()` calls —
      I grepped to confirm.
- [ ] `-v/--verbose` actually changes what's logged, and diagnostic
      output goes through `logging`, not scattered prints.
- [ ] `export` produces a real output file I opened and checked, in
      both formats I claim to support.
- [ ] My README shows real command output from at least two different
      CSVs, and states my column-naming design decision explicitly.
- [ ] My README honestly lists what this tool doesn't handle (large
      files, malformed numeric columns, etc.) unless I specifically
      built handling for it.
- [ ] A stranger with their own unrelated CSV could install this and
      get a useful report out of it using only the README.
