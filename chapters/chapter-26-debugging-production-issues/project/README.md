# Chapter 26 Project (Category 1): Production Incident Runbook

A small, standalone **incident runbook** (one Python file, standard
library only) that takes a plain-language description of a symptom —
the kind of thing you'd type into a bug report or say out loud during
an incident — and classifies it against the Category 1 catalog,
returning the likely root cause(s) and fix(es) instead of leaving you
to search the lesson page manually.

## What you'll build

A `CATALOG` of the 10 issues from Category 1: Crashes & Exceptions,
each with a set of keywords a symptom description might contain. A
classifier matches a free-text description against that catalog and
formats a short runbook entry for every match:

1. **`classify_symptom(description)`** — finds every catalog entry
   whose keywords appear in the description.
2. **`format_runbook_entry(entry)`** — formats one match as a readable
   block: the exception, the root cause, and the fix.
3. **`diagnose(description)`** — ties it together, handling the "no
   match found" case gracefully instead of crashing or returning
   nothing.

## Example run

```text
SYMPTOM: Service crashes on startup with a KeyError for a missing config key
Issue #1: KeyError
  Root cause: A dict was accessed with [] on a key that isn't present -- often a config/env var missing in this environment.
  Fix: Use .get(key, default) for optional keys, or validate all required keys explicitly at startup and fail with a clear message.

SYMPTOM: Everything is fine, no crash at all
No matching catalog entry for this symptom yet -- check Category 1 in the lesson for the closest pattern.
```

## How to run

```bash
cd chapters/chapter-26-debugging-production-issues/project
python3 starter.py
```

Fill in the numbered `# TODO` sections. Want to see a finished version?
Run `python3 solution.py`.

## The pieces

- **`CATALOG`** — the 10 Category 1 issues, each with an exception
  name, matching keywords, a root cause, and a fix, mirroring the
  lesson's issue cards exactly.
- **`classify_symptom(description)`** — the matching logic: lowercase
  the description, check each catalog entry's keywords against it.
- **`format_runbook_entry(entry)`** — turns one matched catalog entry
  into a readable block.
- **`diagnose(description)`** — the public entry point most code would
  actually call.

## Ideas to make it your own

- Add a `confidence` field to each catalog entry based on how many
  keywords matched, and sort results by confidence instead of catalog
  order.
- Feed it real error messages/tracebacks from your own earlier chapter
  projects and see how well the keyword matching holds up.
- Extend `CATALOG` with your own entries for bugs you've personally
  hit, using the same symptom/root_cause/fix shape.

## Why this project matters

Real incident response almost always starts with someone describing a
symptom in plain language, not a stack trace — "the checkout page is
crashing for some users" comes before anyone finds the actual
`KeyError`. A tool that maps loose, human descriptions to known
patterns and their fixes is exactly the kind of internal tooling real
engineering teams build once they've hit the same handful of bugs
enough times to notice the pattern.

## More project ideas (build one of these instead, or after)

From Chapter 7 onward, you get a genuine choice of what to build. The
Production Incident Runbook above is fully built out with a starter
and reference solution — the four ideas below are not. Each is a real,
grounded use case solvable with only what Category 1 has taught so
far. No starter or solution files are provided on purpose — building
one of these unassisted is the point.

### 1. A Traceback-to-Exception-Type Extractor

**Problem:** Given a full, multi-line Python traceback as a string
(the kind you'd paste from a log file), extract just the exception
type and message from the last line — the part someone actually needs
to search for.

**What it should do:** Take a raw traceback string and return a tuple
`(exception_type, message)`, e.g. `("KeyError", "'DATABASE_URL'")`
from a real traceback's last line.

**Suggested approach:** The last non-empty line of a traceback always
has the shape `ExceptionType: message` — split on the first `: `.

### 2. A "Would This Crash?" Static Checker

**Problem:** Given a small snippet of code as a string, flag common
crash-prone patterns without actually running it — a lightweight
linter for exactly the bugs this chapter covers.

**What it should do:** Check a code string for patterns like a bare
`except:`, `except Exception:` catching too broadly, or `range(` used
without an obvious length check nearby, and report which patterns it
found.

**Suggested approach:** Simple substring/regex checks (Chapter 18) on
the code text — this isn't meant to be a real AST-based linter, just a
pattern-spotter using what's been taught.

### 3. A Symptom-to-Fix Quiz Generator

**Problem:** Turn the Category 1 catalog into a self-quiz: show a
random symptom, let the user guess the exception type, then reveal the
root cause and fix.

**What it should do:** Pick a random `CATALOG` entry, print its
root_cause as a clue, prompt the user (via `input()`) for their guess
at the exception name, and report whether they were right.

**Suggested approach:** `random.choice(CATALOG)` plus a simple
case-insensitive string comparison against the guess.

### 4. A Multi-Symptom Incident Report

**Problem:** A single incident often has more than one symptom
reported at once (e.g. "crashes AND wrong data") — the runbook should
handle a list of symptom descriptions, not just one.

**What it should do:** Take a list of symptom strings, run `diagnose()`
(or `classify_symptom()`) on each, and produce one combined report
with a section per symptom, plus a summary counting how many distinct
catalog issues were involved in total.

**Suggested approach:** Loop over the list, reuse this project's
`classify_symptom()`, and track a running set of matched issue IDs
across all symptoms for the summary count.
