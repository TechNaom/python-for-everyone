# Chapter 23 Practice Bank: NumPy for Data Analysis

A deeper set of practice problems, organized by topic, on top of the
main `exercises/` folder — including scenario-based problems written in
the same style you'll see in real interviews. Every task here uses real
NumPy directly — install it first: `pip install numpy`.

## How to run

```bash
cd practice
python3 starter.py
```

## Topic 1: What NumPy Is & Why It Exists

1. Sum a list with a manual loop (the "before").
2. Sum the same list with a NumPy array (the "after").
3. **Debug the Code:** fix a wrong explanation of why NumPy is faster.
4. **Scenario — Comparing Two Approaches:** write `should_use_numpy()`.
5. **Scenario — Interview Prep:** explain why NumPy underlies so many other Python data libraries.

## Topic 2: Creating Arrays

1. Build a range array with `np.arange()`.
2. Describe an array's shape, dtype, and ndim as a dict.
3. **Debug the Code:** fix code that used `np.arange()` where `np.linspace()` was needed.
4. **Scenario — Sensor Baseline Array:** write `build_baseline_readings()`.
5. **Scenario — Interview Prep:** explain what shape, dtype, and ndim each tell you.

## Topic 3: Indexing, Slicing & Boolean Masking

1. Read a specific column from a 2D grid.
2. Filter an array to values above a threshold with a boolean mask.
3. **Debug the Code:** fix code that read a column when a row was asked for.
4. **Scenario — Flagging Failing Grades:** write `flag_failing_grades()`.
5. **Scenario — Interview Prep:** explain what a boolean mask is and why it matters.

## Topic 4: Vectorized Math & Broadcasting

1. Scale every element of an array by a factor.
2. Add a 1D offset array to every row of a 2D grid via broadcasting.
3. **Debug the Code:** fix a broadcasting-error demo that accidentally used compatible shapes.
4. **Scenario — Applying a Uniform Price Increase:** write `apply_price_increase()`.
5. **Scenario — Interview Prep:** explain the general broadcasting compatibility rule.

## Topic 5: Aggregate Functions & axis=

1. Compute a grid's grand total (no axis=).
2. Compute one total per column (axis=0).
3. **Debug the Code:** fix code that used the wrong axis for per-row totals.
4. **Scenario — Class Performance Report:** write `subject_and_student_averages()`.
5. **Scenario — Interview Prep:** explain what axis=0 and axis=1 each collapse.

## Topic 6: Reshaping & Stacking

1. Reshape a flat array into a grid.
2. Flatten a grid back to 1D.
3. **Debug the Code:** fix code that used `np.hstack()` where `np.vstack()` was needed.
4. **Scenario — Reshaping a Week of Sensor Data:** write `daily_averages()`.
5. **Scenario — Interview Prep:** explain the difference between reshaping and stacking.

## Checking your work

Compare your output against `solution.py`. Your exact wording doesn't
need to match on the explanation-style tasks — the goal is that your
program runs without errors and does what each TODO asks. Every
numeric task's output is exactly reproducible, every time.
