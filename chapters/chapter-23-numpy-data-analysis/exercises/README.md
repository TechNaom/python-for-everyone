# Chapter 23 Exercises: NumPy for Data Analysis

These exercises use what Chapter 23 covered: creating NumPy arrays,
boolean masking, vectorized arithmetic, and the `axis=` parameter on
aggregate functions like `.mean()`. Every task here uses real NumPy --
make sure it's installed first: `pip install numpy`.

## How to run

Run this **from inside this `exercises/` folder**:

```bash
cd exercises
python3 starter.py
```

## Task 1 — Building a grade array

Find `# TODO 1`. Write `make_grade_array(grades)` — given a plain
Python list of numbers, return it as a NumPy array.

## Task 2 — Summarizing an array

Find `# TODO 2`. Write `array_summary(arr)` — return a dict with keys
`"sum"`, `"mean"`, `"min"`, `"max"` holding the array's sum, mean, min,
and max.

## Task 3 — Filtering with a boolean mask

Find `# TODO 3`. Write `passing_scores(scores, passing=60)` — given a
NumPy array of scores, return only the scores `>= passing`, using
boolean masking (no loop).

## Task 4 — Vectorized addition

Find `# TODO 4`. Write `add_bonus_points(scores, bonus)` — return a
**new** array with `bonus` added to every element.

## Task 5 — Per-subject average

Find `# TODO 5`. Write `per_subject_average(grades_grid)` — given a 2D
array where each row is a student and each column is a subject, return
the average for each subject (one value per column), using the correct
`axis=`.

## Task 6 — Per-student average

Find `# TODO 6`. Write `per_student_average(grades_grid)` — given the
same 2D array, return the average for each student (one value per
row), using the correct `axis=`.

## Task 7 — Reshaping

Find `# TODO 7`. Write `reshape_to_grid(flat_array, rows, cols)` —
return `flat_array` reshaped to `(rows, cols)`.

## Task 8 — Combining arrays

Find `# TODO 8`. Write `combine_arrays(arr1, arr2)` — return `arr1` and
`arr2` joined end-to-end into one longer 1D array.

## Task 9 — Debug the Code

Find `# TODO 9`. This is supposed to return the average of every
subject (one value per column) in a 2D grid, but it has the `axis`
backwards. Find and fix it.

## Checking your work

Compare your output against `solution.py`. Every task's output is
exactly reproducible, every time.
