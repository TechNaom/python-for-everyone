# Chapter 9 Project: Data-Cleaning One-Liners Kit

A menu-driven mini-app that takes a small list of messy, inconsistent
records and turns it into a clean, sorted, summarized dataset &mdash;
built around this chapter's core tools: **comprehensions, lambda,
`map()`/`filter()`/`sorted()`**. Every record lives in one running list
of dicts, `raw_records` (the messy input) and `cleaned_records` (the
result of running it through this chapter's one-liners), the same
shape a real data-cleaning script works with.

## What you'll build

A script with a `while True` menu loop offering seven options:

1. Show raw sample data
2. Clean whitespace & casing
3. Filter out invalid records
4. Sort cleaned data by a field
5. Generate a summary report
6. Export final cleaned dataset
7. Quit

The sample data (`raw_records`) is eight dicts with realistic mess
baked in: leading/trailing whitespace on names and emails, mixed-case
names and emails, a blank name, a blank email, a non-numeric age, and a
negative age. Cleaning (option 2) uses a **list comprehension** to
build a brand-new `cleaned_records` list, one dict per record, with
`.strip()` and `.title()`/`.lower()` applied to each field &mdash; the
idiomatic replacement for a for-loop with `.append()`. Filtering
(option 3) uses **`filter()` with a `lambda`** to drop any record with
a blank name, a blank email, or an age that isn't a positive whole
number, wrapped in `list(...)` and reassigned back to
`cleaned_records`. Sorting (option 4) uses **`sorted(key=lambda ...)`**
to reorder `cleaned_records` by name, email, or age (age sorts
numerically by converting it with `int()` inside the lambda).
Summarizing (option 5) uses comprehensions to collect ages and compute
an average, then buckets records into age groups and counts records
per email domain. Exporting (option 6) prints the final cleaned
dataset aligned into columns with f-strings.

Example run:

```
=== Data-Cleaning One-Liners Kit ===

1. Show raw sample data
2. Clean whitespace & casing
3. Filter out invalid records
4. Sort cleaned data by a field
5. Generate a summary report
6. Export final cleaned dataset
7. Quit
Choose an option (1-7): 2

Cleaned 8 record(s) -- whitespace stripped, names title-cased, emails lowercased.

1. Show raw sample data
2. Clean whitespace & casing
3. Filter out invalid records
4. Sort cleaned data by a field
5. Generate a summary report
6. Export final cleaned dataset
7. Quit
Choose an option (1-7): 3

Removed 4 invalid record(s) -- 4 record(s) remain.

1. Show raw sample data
2. Clean whitespace & casing
3. Filter out invalid records
4. Sort cleaned data by a field
5. Generate a summary report
6. Export final cleaned dataset
7. Quit
Choose an option (1-7): 4

Sort by: 1) name  2) email  3) age
Choose a field (1-3): 3
Sorted by age.

{'name': 'Elena Ferreira', 'email': 'elena@example.com', 'age': '27'}
{'name': 'Ana Silva', 'email': 'ana@example.com', 'age': '29'}
{'name': 'Gabriela Nunes', 'email': 'gabriela@example.com', 'age': '31'}
{'name': 'Bruno Costa', 'email': 'bruno@example.com', 'age': '34'}

1. Show raw sample data
2. Clean whitespace & casing
3. Filter out invalid records
4. Sort cleaned data by a field
5. Generate a summary report
6. Export final cleaned dataset
7. Quit
Choose an option (1-7): 5

--- Summary Report ---
Total cleaned records: 4
Average age: 30.2
Age groups: {'under 30': 2, '30-39': 2, '40 and up': 0}
Records per email domain: {'example.com': 4}

1. Show raw sample data
2. Clean whitespace & casing
3. Filter out invalid records
4. Sort cleaned data by a field
5. Generate a summary report
6. Export final cleaned dataset
7. Quit
Choose an option (1-7): 7

Session summary: 4 cleaned record(s) ready for export.
Goodbye!
```

## How to run it

```bash
python3 starter.py
```

Fill in the numbered `# TODO` sections in `starter.py`. Want to see one
finished version first? Run `python3 solution.py`.

## Ideas to make it your own (optional stretch goals)

- Add a "reset to raw data" option that clears `cleaned_records` back
  to empty so you can re-run the whole pipeline from scratch.
- Track and print which record had the largest number of whitespace
  characters trimmed off during cleaning.
- Add a fourth sort option that sorts by *email domain* using
  `sorted(key=lambda r: r["email"].split("@")[-1])`.

## Why this project matters

Almost every real dataset arrives messy &mdash; a CSV export from a
spreadsheet, a form submission, a scraped web page &mdash; with
inconsistent whitespace, casing, and the occasional invalid or missing
field. Data engineers and analysts write exactly this kind of
cleaning pipeline constantly: normalize every record with a
comprehension, drop the invalid ones with `filter()`, order the result
with `sorted(key=lambda ...)`, and roll it up into summary counts with
a dict comprehension. Those four one-liners, chained together, are the
backbone of real-world ETL (extract-transform-load) scripts, and
they're far more Pythonic and readable than the equivalent hand-written
for-loops once you're comfortable with them.

## More project ideas (build one of these instead, or after)

From Chapter 7 onward, you get a genuine choice of what to build. The
Data-Cleaning One-Liners Kit above is fully built out with a starter
and reference solution &mdash; the four ideas below are not. Each is a
real, grounded use case solvable with only what's been taught through
Chapter 9 (variables, operators, `if`/`elif`/`else`, loops, strings,
lists, dictionaries, sets, comprehensions, lambda, and
`map()`/`filter()`/`sorted()`). No starter or solution files are
provided on purpose &mdash; building one of these unassisted, menu loop
and all, is the point.

### 1. CSV-Row Data Validator

**Problem:** Before any spreadsheet export gets loaded into a real
system, someone has to check every row for missing or malformed
fields &mdash; the same gatekeeping step every data-import pipeline
needs.

**What it should do:** Keep a list of dicts representing rows (e.g.
`{"id": "101", "email": "x@y.com", "amount": "49.99"}`), some
deliberately broken (missing `@` in the email, a non-numeric amount,
a blank id). Menu options: show all rows, validate rows with
`filter()` + `lambda` (keeping only rows where the email contains
`"@"`, the amount is numeric, and the id isn't blank), show which rows
failed validation and why, and show a pass/fail count summary.

**Suggested approach:** Write one lambda per rule (e.g.
`lambda r: "@" in r["email"]`) and combine them with `and` inside a
single `filter()` predicate, or chain multiple `filter()` calls back to
back. For "show which rows failed and why," loop over the rows and
check each rule individually with `if`/`elif` so you can report the
*specific* reason a row was rejected, rather than just a blanket
pass/fail.

### 2. Leaderboard Ranking Tool

**Problem:** A game, a sales contest, or a fitness app needs to turn a
list of raw scores into a ranked leaderboard, sorted the right
direction, on demand.

**What it should do:** Keep a list of dicts like
`{"player": "Ana", "score": 4200}`. Menu options: add a new
score entry, view the leaderboard sorted highest-to-lowest with
`sorted(key=lambda ..., reverse=True)`, view the bottom N players the
same way, and compute the average score across everyone with a
comprehension.

**Suggested approach:** `sorted(scores, key=lambda p: p["score"],
reverse=True)` handles the ranking in one line &mdash; assign the rank
number while printing by using `enumerate()`-free counting (a running
counter variable) since `enumerate()` isn't required here, just a loop
variable you increment yourself. The average is
`sum(p["score"] for p in scores) / len(scores)` using a generator
expression, the same idea as a list comprehension without the
brackets.

### 3. Text-Normalization Batch Tool

**Problem:** A batch of user-submitted text (comments, product
descriptions, form fields) needs consistent formatting before it's
displayed or stored &mdash; extra spaces collapsed, casing normalized,
empty entries dropped.

**What it should do:** Keep a list of raw strings with inconsistent
spacing and casing (e.g. `"  Hello   World  "`, `"ALL CAPS TEXT"`, an
empty string). Menu options: show the raw list, normalize every entry
with a comprehension (`.strip()`, `.lower()` or `.title()`,
`" ".join(s.split())` to collapse repeated internal spaces), filter
out any entry that's empty after normalizing, and show before/after
character-count totals.

**Suggested approach:** `" ".join(text.split())` is the standard trick
for collapsing multiple spaces into one, since `.split()` with no
argument already treats any run of whitespace as one separator. Build
the whole normalized list in one comprehension, then a second
`filter()` + `lambda` pass to drop anything that normalized down to an
empty string.

### 4. Duplicate Record Finder

**Problem:** A mailing list, a contact import, or a signup form often
ends up with the same person entered more than once, sometimes with
slightly different casing or spacing &mdash; finding those duplicates
by eye doesn't scale.

**What it should do:** Keep a list of dicts like
`{"name": "Ana Silva", "email": "ana@x.com"}`, with a few intentional
duplicates (identical or same-after-cleaning). Menu options: show all
records, show only the unique emails using a **set comprehension**,
show which specific records are duplicates (appeared more than once),
and show a final deduplicated list (one record per unique email).

**Suggested approach:** `{r["email"].strip().lower() for r in records}`
is a one-line set comprehension that collapses every email down to its
unique, normalized form. To find *which* records are duplicates, loop
over the records while building a "seen so far" set; any record whose
normalized email is already in that set is a duplicate &mdash; add it
to a separate "duplicates" list as you go.
