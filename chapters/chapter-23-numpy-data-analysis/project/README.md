# Chapter 23 Project: Grade & Statistics Analyzer

A **menu-driven mini-app** (one Python file, like Chapter 21's project)
that analyzes a class's grades using NumPy: overall statistics,
per-subject and per-student breakdowns via the `axis=` parameter, and
boolean-masking to identify above/below-average students.

## What you'll build

A grades grid: 5 students &times; 3 subjects, stored as a single 2D
NumPy array (rows = students, columns = subjects). The analyzer
computes and reports:

1. **Overall statistics** — mean, median, standard deviation, min, and
   max across every grade in the whole grid.
2. **Per-subject statistics** — mean/min/max for each subject
   (column), using `axis=0`.
3. **Per-student statistics** — mean/min/max for each student (row),
   using `axis=1`.
4. **Above/below-average students** — identified with boolean masking,
   comparing each student's average against the class-wide average.
5. **A formatted report** combining all four sections into one
   readable, multi-line string.

## Example run

```text
=== Grade & Statistics Analyzer ===

=== Overall Statistics ===
Mean: 80.27  Median: 84.0  Std: 11.92  Min: 58.0  Max: 95.0

=== Per-Subject Statistics ===
Math: mean=79.8  min=60  max=95
Science: mean=78.8  min=58  max=92
English: mean=82.2  min=70  max=92

=== Per-Student Statistics ===
Ana: mean=86.33  min=79  max=92
Ben: mean=72.67  min=65  max=81
Chidi: mean=91.67  min=89  max=95
Dana: mean=62.67  min=58  max=70
Eli: mean=88.0  min=84  max=92

=== Above-Average Students ===
Ana, Chidi, Eli

=== Below-Average Students ===
Ben, Dana
```

## How to run

```bash
cd chapters/chapter-23-numpy-data-analysis/project
pip install numpy   # if you haven't already
python3 starter.py
```

Fill in the numbered `# TODO` sections. Want to see a finished version?
Run `python3 solution.py`.

## The pieces

- **`GRADES`** — a 2D NumPy array built with `np.array([[...], [...], ...])`, one row per student.
- **`overall_stats()`** — `.mean()`/`.std()`/`.min()`/`.max()` with no `axis=`, plus `np.median()`, collapsing the whole grid to single numbers.
- **`per_subject_stats()`** / **`per_student_stats()`** — the same aggregate functions with `axis=0` (per column/subject) and `axis=1` (per row/student) respectively.
- **`above_average_students()`** / **`below_average_students()`** — boolean masking comparing each student's per-row average against the class-wide average of those averages.
- **`format_report()`** — combines every section into one readable report string.

## Ideas to make it your own

- Add a `.std()`-based "most consistent student" (lowest per-student standard deviation across subjects).
- Add a per-subject "hardest subject" callout (the subject with the lowest overall mean).
- Load grades from a hardcoded multi-line string instead of a literal array, parsing it with `.split()` (Chapter 6) before building the NumPy array.

## Why this project matters

Nearly every real "analyze this dataset" task &mdash; grades, sensor
readings, sales figures &mdash; follows this exact shape: load numeric
data into an array, compute summary statistics, break those statistics
down by group (subject, region, day), and flag outliers with a
condition. This project builds that entire pattern once, on data
concrete enough (grades) to reason about intuitively.

## More project ideas (build one of these instead, or after)

From Chapter 7 onward, you get a genuine choice of what to build. The
Grade & Statistics Analyzer above is fully built out with a starter and
reference solution — the four ideas below are not. Each is a real,
grounded use case solvable with only what's been taught through Chapter
23. No starter or solution files are provided on purpose — building one
of these unassisted is the point.

### 1. A Weather-Data Averager

**Problem:** Someone has a week of daily temperature readings for
several cities and wants quick summary statistics per city and per
day.

**What it should do:** Store readings as a 2D array (rows = cities,
columns = days), and report each city's weekly average
(`axis=1`) and each day's average across all cities (`axis=0`), plus
the single hottest and coldest reading overall.

**Suggested approach:** This is almost a direct re-skin of this
project's grid — swap "student" for "city" and "subject" for "day."

### 2. A Basic Image-Brightness Adjuster (conceptual)

**Problem:** A very simple stand-in for image processing — a small 2D
array of numbers represents pixel brightness values (0-255), and a
program should brighten or darken the whole "image" uniformly.

**What it should do:** Build a small 2D NumPy array of numbers standing
in for pixel brightness, then add or subtract a fixed amount from every
value (vectorized, using broadcasting), clipping results to stay within
0-255 with `np.clip()`. No real image file I/O is needed — the small
2D array itself is the "image."

**Suggested approach:** `np.clip(arr + amount, 0, 255)` is the whole
core operation; the rest is printing the before/after grids clearly.

### 3. A Sports Statistics Tracker

**Problem:** A coach wants to track several players' stats (points,
rebounds, assists) across a season and see who's over/under-performing
the team average.

**What it should do:** Store stats as a 2D array (rows = players,
columns = stat categories), report each player's average and each
category's team-wide average, and use boolean masking to flag players
above the team's average total.

**Suggested approach:** Directly reuses this chapter's project
structure — "player" instead of "student," "stat category" instead of
"subject."

### 4. A Simple Data Normalizer/Scaler

**Problem:** Raw numeric data (like grades on different scales, or
prices in different currencies) often needs to be rescaled to a
common 0-1 range before further analysis.

**What it should do:** Given a 1D or 2D array, write a
`normalize(arr)` function returning
`(arr - arr.min()) / (arr.max() - arr.min())`, mapping the lowest value
to 0.0 and the highest to 1.0. Handle the edge case where every value
is identical (avoiding a divide-by-zero).

**Suggested approach:** This is one vectorized expression, using
broadcasting throughout — the interesting work is handling the
all-identical-values edge case cleanly with an `if` check.
