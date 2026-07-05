# Chapter 11 Project: Expense Tracker

A menu-driven expense tracker built **around the `math` and `datetime`
modules** as its core organizing principle -- every date calculation
goes through `datetime`, every rounding/aggregation calculation goes
through `math` or plain arithmetic, and each operation lives in its own
small function, exactly like Chapter 10's function-library pattern. The
`while True` menu loop at the bottom does nothing but call into those
functions and print results.

## What you'll build

A function library covering this chapter's core tools -- **`import`,
the `math` module, and the `datetime` module** -- plus a menu loop
offering seven options:

1. Add an expense
2. Show all expenses
3. Show totals & average
4. Show monthly summary
5. Show category breakdown
6. Days since last expense / days until a target date
7. Quit

The library itself is built from these functions:

- `parse_date(raw, today)` -- turns a typed `'YYYY-MM-DD'` string into a
  real `datetime.date`, or falls back to `today` if the input was left
  blank. Splits the raw string on `-` and builds the date with
  `datetime.date(year, month, day)`.
- `add_expense(expenses, amount, category, note, expense_date)` --
  builds one expense as a dict (amount rounded to 2 decimals) and
  appends it to the running `expenses` list.
- `total_spent(expenses)` -- sums every expense's `amount`, rounded to
  2 decimals.
- `average_expense(expenses)` -- the running average per expense, or
  `0` if nothing's been recorded yet.
- `round_up_to_nearest(amount, nearest=1)` -- uses `math.ceil` to round
  a total up to the nearest multiple of `nearest`, e.g. up to the
  nearest $10.
- `days_since(expense_date, today)` / `days_until(target_date, today)`
  -- both subtract two `datetime.date` objects and read `.days` off the
  resulting `timedelta`.
- `month_key(expense_date)` -- turns a date into a `'YYYY-MM'` grouping
  key using the date's `.year` and `.month` attributes.
- `summarize_by_month(expenses)` / `summarize_by_category(expenses)` --
  group expenses into a `{key: total}` dict by month or by category.
- `print_expense(expense, index)` -- prints one numbered, aligned
  expense line.
- `read_float(prompt, default)` -- handles "press Enter to accept the
  default" input parsing so the menu loop's `input()` calls stay short.

Every expense added during the session is appended to a running
`expenses` list, so options 2-6 can report on the full history -- the
same running-state pattern earlier chapters' projects have used, just
now organized as a small function library on top of `math` and
`datetime` instead of one flat block of logic.

Example run:

```
=== Expense Tracker ===
Today's date: 2026-07-05

1. Add an expense
2. Show all expenses
3. Show totals & average
4. Show monthly summary
5. Show category breakdown
6. Days since last expense / days until a target date
7. Quit
Choose an option (1-7): 1
Amount: $50
Category (e.g. food, rent, transport): food
Note (optional): lunch
Date (YYYY-MM-DD, blank = today):

Added: $50.00 in food on 2026-07-05.

1. Add an expense
2. Show all expenses
3. Show totals & average
4. Show monthly summary
5. Show category breakdown
6. Days since last expense / days until a target date
7. Quit
Choose an option (1-7): 1
Amount: $30
Category (e.g. food, rent, transport): rent
Note (optional):
Date (YYYY-MM-DD, blank = today): 2026-06-01

Added: $30.00 in rent on 2026-06-01.

1. Add an expense
2. Show all expenses
3. Show totals & average
4. Show monthly summary
5. Show category breakdown
6. Days since last expense / days until a target date
7. Quit
Choose an option (1-7): 1
Amount: $20
Category (e.g. food, rent, transport): transport
Note (optional): bus
Date (YYYY-MM-DD, blank = today): 2026-07-01

Added: $20.00 in transport on 2026-07-01.

1. Add an expense
2. Show all expenses
3. Show totals & average
4. Show monthly summary
5. Show category breakdown
6. Days since last expense / days until a target date
7. Quit
Choose an option (1-7): 2

1. [2026-07-05] food         $50.00  lunch
2. [2026-06-01] rent         $30.00
3. [2026-07-01] transport    $20.00  bus

1. Add an expense
2. Show all expenses
3. Show totals & average
4. Show monthly summary
5. Show category breakdown
6. Days since last expense / days until a target date
7. Quit
Choose an option (1-7): 3

Total spent: $100.00
Average per expense: $33.33
Suggested round-number budget to set aside: $100.00

1. Add an expense
2. Show all expenses
3. Show totals & average
4. Show monthly summary
5. Show category breakdown
6. Days since last expense / days until a target date
7. Quit
Choose an option (1-7): 4

2026-06: $30.00
2026-07: $70.00

1. Add an expense
2. Show all expenses
3. Show totals & average
4. Show monthly summary
5. Show category breakdown
6. Days since last expense / days until a target date
7. Quit
Choose an option (1-7): 5

food         $50.00
rent         $30.00
transport    $20.00

1. Add an expense
2. Show all expenses
3. Show totals & average
4. Show monthly summary
5. Show category breakdown
6. Days since last expense / days until a target date
7. Quit
Choose an option (1-7): 6

Days since last expense (2026-07-01): 4
Enter a target date (YYYY-MM-DD) to count down to (blank to skip): 2026-12-25
Days until 2026-12-25: 173

1. Add an expense
2. Show all expenses
3. Show totals & average
4. Show monthly summary
5. Show category breakdown
6. Days since last expense / days until a target date
7. Quit
Choose an option (1-7): 7

Session summary: 3 expense(s) recorded, $100.00 total.
Goodbye!
```

(Your own `Today's date:` line will show whatever the actual current
date is when you run it -- everything above is a real, verified run
from a machine where today happened to be July 5, 2026.)

## How to run it

```bash
python3 starter.py
```

Fill in the numbered `# TODO` sections in `starter.py`. Want to see one
finished version first? Run `python3 solution.py`.

## Ideas to make it your own (optional stretch goals)

- Add an "edit or delete the last expense" option that pops the most
  recent entry off `expenses` and lets you re-add it with corrected
  values, reusing `add_expense(...)` rather than writing new logic.
- Add a `most_expensive_category(expenses)` function that reuses
  `summarize_by_category(...)` and returns whichever category has the
  highest total, for a quick "where is most of my money going" answer.
- Add a "recurring expense" option that uses `datetime.timedelta` to
  automatically log the same expense on the same day for the next N
  months, reusing `add_expense(...)` in a loop.

## Why this project matters

Tracking expenses sounds like a spreadsheet's job, but the real skill
this project practices is building a small program **around a standard
library module's strengths**: every date-related decision (how many
days since, which month something falls in, how far away a target date
is) goes through `datetime` instead of hand-rolled string parsing, and
every rounding/aggregation decision goes through `math` or plain
arithmetic instead of guesswork. That's exactly the shape of real
production finance and budgeting tools -- a subscription billing
system grouping charges by month, a personal-finance app's "days until
your next bill" reminder, or an expense-report tool summarizing a
trip's spending by category -- all of them lean on the same
`math`/`datetime` foundation this project practices.

## More project ideas (build one of these instead, or after)

From Chapter 7 onward, you get a genuine choice of what to build. The
Expense Tracker above is fully built out with a starter and reference
solution -- the four ideas below are not. Each is a real, grounded use
case solvable with only what's been taught through Chapter 11
(everything through Chapter 10's functions material, plus `import` of
only `math`, `datetime`, and `random`). No starter or solution files
are provided on purpose -- building one of these unassisted, menu loop
and all, is the point.

### 1. Countdown-to-Event Date Calculator

**Problem:** Event planners, students tracking deadlines, and anyone
counting down to a big day (a wedding, a launch date, an exam) need a
quick, reliable way to see exactly how many days are left -- and how
that compares to other upcoming events.

**What it should do:** Let a user add named events with a target date
(`datetime.date(year, month, day)`, parsed from a typed
`'YYYY-MM-DD'` string the same way this project's `parse_date` does),
store them in a running list, and show days remaining until each one
using `datetime` subtraction. Menu options: add an event, list all
events sorted by how soon they happen, show the single soonest
upcoming event, and remove an event that's already passed.

**Suggested approach:** Reuse this project's `parse_date` and
`days_until` pattern directly -- a `days_until(target_date, today)`
function that returns `(target_date - today).days` is the whole
engine. "Sort by soonest" is a `sorted(...)` call using each event's
computed days-remaining value as the sort key.

### 2. Geometry Toolkit

**Problem:** Anyone working with shapes -- a woodworking hobbyist, a
student checking homework, a small business estimating material for
circular or triangular signage -- needs quick, correct area and
perimeter formulas without re-deriving them by hand each time.

**What it should do:** Build functions like
`circle_area(radius)` and `circle_circumference(radius)` (using
`math.pi`), `rectangle_area(length, width)`,
`triangle_area(base, height)`, and `right_triangle_hypotenuse(a, b)`
(using `math.sqrt`). Menu options: pick a shape, enter its
measurements, and print its area (and perimeter/circumference where it
applies), plus an option to compare the area of two different shapes.

**Suggested approach:** Each formula is its own one-line function with
a clear docstring, exactly like `round_up_to_nearest` in this
project -- `math.pi` and `math.sqrt` are the only two `math` tools
needed for the whole toolkit. A `describe_shape(shape_name, **measurements)`
function is a natural place to dispatch to the right formula function
based on `shape_name`.

### 3. Random Quiz-Question Picker & Shuffler

**Problem:** Teachers building practice quizzes, and study apps
quizzing users from a question bank, need to serve questions in a
random, non-repeating order each time -- not the exact same order
every single run.

**What it should do:** Store a list of question/answer dicts, then use
`random.shuffle` to reorder them at the start of a session and
`random.choice` to pull a single random question for a "quick quiz me"
option. Menu options: start a full shuffled quiz (asks every question
once, in random order), get one random single question, and add a new
question to the bank.

**Suggested approach:** `random.shuffle(questions)` reorders the whole
list in place before looping over it to ask each one exactly
once -- this guarantees no repeats within one shuffled run, unlike
repeatedly calling `random.choice`, which could pick the same question
twice. Track a running score across the session the same way this
project tracks a running `expenses` list.

### 4. Age & Tenure Calculator

**Problem:** HR systems computing an employee's tenure, membership
apps showing "member since," and eligibility checks that depend on
someone's exact age (in years, not just birth year) all need accurate
date-based age math, not a naive year-subtraction that ignores whether
a birthday has happened yet this year.

**What it should do:** Given a birth date (or start date) and today's
date, compute a precise age or tenure in full years -- correctly
handling the case where this year's birthday/anniversary hasn't
happened yet. Menu options: enter a birth date and get an exact age,
enter a start date and get tenure in years and days, and show days
remaining until the next birthday/anniversary.

**Suggested approach:** A naive `today.year - birth_date.year`
overcounts by one until the birthday actually happens this year --
the fix is checking whether `(today.month, today.day)` is still
earlier than `(birth_date.month, birth_date.day)`, and subtracting one
more year if so. `days_until` from this project's own pattern (via a
date built with this year's or next year's anniversary) handles the
"days until next birthday" option.
