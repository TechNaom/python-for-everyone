# Chapter 13 Project: Log-File Analyzer

A menu-driven log-file analyzer built **around file handling and the `csv`
module** as its core organizing principle -- every operation reads a real
log file with `with open(...)`, processes it using plain Python (dicts,
loops, string methods) from earlier chapters, and the export option writes a
real CSV report using `csv.writer`. A `try`/`except FileNotFoundError` guards
the very first read so a missing log file fails gracefully with a helpful
message instead of crashing, exactly like Chapter 12's exception-handling
pattern. Each operation lives in its own small function, matching Chapter
10's function-library pattern.

## What you'll build

A function library covering this chapter's core tools -- **`open()`/`with`,
file modes, and the `csv` module** -- plus a menu loop offering five options:

1. Show counts by log level
2. Search for a keyword
3. Show the most common error message
4. Export summary to CSV
5. Quit

The library itself is built from these pieces:

- `load_log_lines(log_filename)` -- opens the log file with `with open(...)`
  and returns a list of its stripped, non-blank lines. Lets
  `FileNotFoundError` propagate up to the caller instead of catching it
  itself, so the one place that decides how to respond to a missing file is
  the top-level session code.
- `count_by_level(lines)` -- returns a dict of `{"INFO": count, "WARNING":
  count, "ERROR": count}` by checking each line for `" LEVEL "`.
- `search_lines(lines, keyword)` -- returns every line containing `keyword`,
  case-insensitively.
- `most_common_error(lines)` -- splits every `ERROR` line on the word
  `ERROR` to isolate the message, counts how often each distinct message
  occurs, and returns the most frequent one as `(message, count)`.
- `export_summary(lines, report_filename)` -- writes a CSV report combining
  level counts and error-message counts using `csv.writer`, always opening
  the output file with `newline=""`.
- `print_level_counts(level_counts)` -- prints level counts as a small
  aligned table.

The log file itself (`server.log`) is loaded once when the program starts,
guarded by `try`/`except FileNotFoundError` -- if it's missing, the program
prints a helpful message and exits the menu loop instead of crashing.

Example run:

```
=== Log-File Analyzer ===
Loaded 30 line(s) from 'server.log'.

1. Show counts by log level
2. Search for a keyword
3. Show the most common error message
4. Export summary to CSV
5. Quit
Choose an option (1-5): 1

Counts by level:
  INFO     14
  WARNING  5
  ERROR    11

1. Show counts by log level
2. Search for a keyword
3. Show the most common error message
4. Export summary to CSV
5. Quit
Choose an option (1-5): 3

Most common error: 'Database connection timeout' (5 occurrence(s))

1. Show counts by log level
2. Search for a keyword
3. Show the most common error message
4. Export summary to CSV
5. Quit
Choose an option (1-5): 4

Report filename to write (e.g. summary.csv): summary.csv
Summary written to 'summary.csv'.

1. Show counts by log level
2. Search for a keyword
3. Show the most common error message
4. Export summary to CSV
5. Quit
Choose an option (1-5): 5

Goodbye!
```

`summary.csv` ends up looking like this:

```
category,label,count
level,INFO,14
level,WARNING,5
level,ERROR,11
error_message,Database connection timeout,5
error_message,Invalid API key,4
error_message,Payment gateway unreachable,2
```

Notice how much of this chapter shows up in one small program: a `with`
block reading the log line by line, a `try`/`except FileNotFoundError`
guarding the initial open, plain-Python counting logic from earlier
chapters, and `csv.writer` producing a clean report at the end. That's the
entire point of this project -- file handling isn't just "read a string,"
it's the foundation real programs use to remember data and turn raw text
into a structured report someone else's tool (a spreadsheet, another
script) can pick up directly.

## How to run it

This project reads `server.log` using a plain relative path, so you must run
it from **inside this `project/` folder**:

```bash
cd chapters/chapter-13-file-handling-csv/project
python3 starter.py
```

Fill in the numbered `# TODO` sections in `starter.py`. Want to see one
finished version first? Run `python3 solution.py` (also from inside this
folder).

## Ideas to make it your own (optional stretch goals)

- Add a "filter by log level" option that only shows lines matching a
  chosen level (INFO/WARNING/ERROR), reusing the same `" LEVEL "` check
  `count_by_level` already does.
- Add a "busiest time window" option that groups lines by the hour in their
  timestamp (the first part of each line, before the log level) and reports
  which hour had the most log entries overall.
- Add a second CSV export option that writes one row per matching line from
  a keyword search (option 2), using `csv.writer`, so a specific search's
  results can be shared as their own report.

## Why this project matters

A DevOps engineer scanning last night's server logs for the first sign of
trouble, a support team pulling every log line that mentions a specific
customer's account, a monitoring script that emails a daily summary of
what went wrong -- all of these are, underneath, the exact same shape as
this project: read a real file defensively, count and search through it
with plain logic, and turn the result into something durable and shareable.
That's the real skill this project practices -- treating a raw text file as
a genuine source of truth, and `csv` as the universal hand-off format
between your script and every spreadsheet, database, or dashboard tool that
comes after it.

## More project ideas (build one of these instead, or after)

From Chapter 7 onward, you get a genuine choice of what to build. The
Log-File Analyzer above is fully built out with a starter and reference
solution -- the four ideas below are not. Each is a real, grounded use case
solvable with only what's been taught through Chapter 13 (everything
through Chapter 12's exception-handling material, plus `open()`/`with` file
I/O and `import csv`). No starter or solution files are provided on purpose
-- building one of these unassisted is the point.

### 1. CSV Contact List Manager

**Problem:** A phone's contacts app, a small business's client list, a
club's membership roster -- all need to persist between runs, so the data
a user enters today is still there the next time the program starts, not
wiped out the moment it closes.

**What it should do:** Store contacts (name, phone, email) in a CSV file
using `csv.DictReader`/`csv.DictWriter`, loading the whole file into a list
of dicts when the program starts and rewriting the whole file any time a
contact is added, updated, or removed. Menu options: list all contacts, add
a new contact, search by name, remove a contact by name, and quit (saving
before exit). Guard the initial load with `try`/`except FileNotFoundError`
so a brand-new contact list (no file yet) starts empty instead of crashing.

**Suggested approach:** Keep the full contact list as a list of dicts in
memory during the session (the same running-state pattern earlier
projects use), and write a `save_contacts(contacts, filename)` function
using `csv.DictWriter` with `fieldnames=["name", "phone", "email"]` that
gets called after every change, so the file on disk always matches what's
in memory.

### 2. Persistent To-Do List

**Problem:** A to-do list that forgets every task the moment the program
closes isn't useful for planning anything longer than a single sitting --
real to-do apps need tasks to still be there tomorrow.

**What it should do:** Store tasks as plain lines in a text file (one task
per line, perhaps with a `done`/`pending` marker at the start of the
line), loading them into a list when the program starts and rewriting the
whole file whenever a task is added, completed, or removed. Menu options:
list tasks (showing done vs. pending clearly), add a task, mark a task
done by number, remove a task by number, and quit.

**Suggested approach:** A simple line format like `"[ ] Buy milk\n"` or
`"[x] Buy milk\n"` makes both reading and rewriting straightforward with
plain string methods (`.startswith("[x]")`, slicing off the marker) --
`csv` isn't required here since each line only needs one piece of
structured information (done or not) alongside free text.

### 3. CSV Grade-Report Generator

**Problem:** A teacher tracking a class's scores across several
assignments needs an easy way to turn raw scores into a summary report --
each student's average, and who's above or below a passing threshold --
without doing the arithmetic by hand every time a new score comes in.

**What it should do:** Read a CSV file of student scores (one row per
student, one column per assignment) using `csv.DictReader`. Compute each
student's average score, flag anyone below a passing threshold (e.g. 60),
and export a summary CSV with columns for student name, average, and
pass/fail status using `csv.DictWriter`. Guard the input file's read with
`try`/`except FileNotFoundError`, printing a clear message if the input
file isn't found yet.

**Suggested approach:** Loop over each row from `csv.DictReader`, pull out
every column except the name (the assignment scores), convert each to
`float`, and average them with `sum(...) / len(...)` -- exactly the kind
of running-total logic from Chapter 9's math material, just fed by CSV
rows instead of typed input.

### 4. Word-Frequency Counter

**Problem:** A writer wanting to know which words they overuse, a search
engine ranking how relevant a document is to a query, a spam filter
looking for suspicious word patterns -- all rely on the same basic tool:
counting how often each word appears in a body of text.

**What it should do:** Read a plain text file, split its contents into
individual words (lowercased, with basic punctuation stripped), count how
many times each distinct word appears, and export the results as a CSV
report (columns: word, count) sorted from most to least frequent, using
`csv.writer`. Menu options: load a text file, show the top N most common
words, look up how many times one specific word appears, and export the
full report to CSV.

**Suggested approach:** `.lower().split()` on the file's full text gets a
rough word list; stripping simple punctuation off each word (e.g. with a
loop that removes any of `.,!?"';:` from both ends of the word) cleans it
up enough for this chapter's tools. A dict built with
`counts[word] = counts.get(word, 0) + 1` tracks frequency, the same
counting pattern this project's own `most_common_error` uses.
