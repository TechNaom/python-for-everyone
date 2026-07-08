"""
Chapter 23 Practice Bank: NumPy for Data Analysis
See README.md in this folder for full instructions.
Run this from inside the practice/ folder: python3 starter.py

Real NumPy is used throughout -- install it first: pip install numpy
"""

import numpy as np

# ============================================================
# Topic 1: What NumPy Is & Why It Exists
# ============================================================

# TODO 1.1: Write loop_sum(values). Given a plain Python list of
# numbers, return their sum using a manual for-loop accumulator (no
# built-in sum() or NumPy) -- this is the "before" side of the
# loop-vs-vectorized comparison.


# TODO 1.2: Write array_sum(values). Given a plain Python list of
# numbers, convert it to a NumPy array and return its .sum() -- the
# "after" side of the same comparison.


# TODO 1.3 (Debug the Code): describe_numpy_speed() below wrongly
# claims NumPy is faster because it uses less memory than a list. Fix
# its return value to correctly explain the real reason (fixed dtype +
# vectorized operations in compiled code).
def describe_numpy_speed():
    return "NumPy arrays are faster than lists because they use less memory."


print(describe_numpy_speed())


# TODO 1.A (Scenario -- Comparing Two Approaches): write
# should_use_numpy(dataset_size, operation_count). Return True if
# dataset_size > 1000 or operation_count > 10 (numeric work at that
# scale benefits from vectorization), otherwise False.


# TODO 1.B (Scenario -- Interview Prep): write
# explain_why_numpy_is_foundational() describing why so many other
# Python data libraries (pandas, scikit-learn, etc.) are built on top
# of NumPy specifically.


# ============================================================
# Topic 2: Creating Arrays
# ============================================================

# TODO 2.1: Write build_range_array(start, stop, step). Return
# np.arange(start, stop, step).


# TODO 2.2: Write describe_array(arr). Return a dict with keys
# "shape", "dtype", "ndim" holding arr.shape, str(arr.dtype), arr.ndim.


# TODO 2.3 (Debug the Code): make_evenly_spaced() below is supposed to
# return 5 evenly spaced values between 0 and 1 (inclusive), but it
# uses np.arange() instead of np.linspace(), so the count and endpoint
# behavior are both wrong. Fix it.
def make_evenly_spaced():
    return np.arange(0, 1, 5)


print(make_evenly_spaced())


# TODO 2.A (Scenario -- Sensor Baseline Array): write
# build_baseline_readings(count). Return a NumPy array of `count`
# zeros representing a sensor log that hasn't recorded anything yet.


# TODO 2.B (Scenario -- Interview Prep): write
# explain_shape_vs_dtype_vs_ndim() describing what each of the three
# attributes tells you about an array.


# ============================================================
# Topic 3: Indexing, Slicing & Boolean Masking
# ============================================================

# TODO 3.1: Write get_column(grid, col_index). Return column
# `col_index` of a 2D NumPy array `grid`.


# TODO 3.2: Write above_threshold(arr, threshold). Return only the
# elements of arr strictly greater than threshold, using boolean
# masking (no loop).


# TODO 3.3 (Debug the Code): get_second_row() below is supposed to
# return row index 1 of a 2D grid, but it uses list-style chained
# indexing (grid[1][:]) mixed incorrectly -- actually the real bug is
# it reads grid[:, 1] (a COLUMN) when a ROW was asked for. Fix it.
def get_second_row(grid):
    return grid[:, 1]


sample_grid = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(get_second_row(sample_grid))


# TODO 3.A (Scenario -- Flagging Failing Grades): write
# flag_failing_grades(scores, passing=60). Return only the scores
# strictly below `passing`, using boolean masking.


# TODO 3.B (Scenario -- Interview Prep): write
# explain_boolean_masking() describing what a boolean mask is and why
# it's considered NumPy's most important idiom.


# ============================================================
# Topic 4: Vectorized Math & Broadcasting
# ============================================================

# TODO 4.1: Write scale_array(arr, factor). Return a NEW array with
# every element multiplied by factor.


# TODO 4.2: Write add_row_offset(grid, offsets). Return grid + offsets,
# relying on broadcasting to add offsets (a 1D array) to every row of
# grid (a 2D array).


# TODO 4.3 (Debug the Code): try_add_mismatched() below is supposed to
# demonstrate a broadcasting error by adding two incompatible-shaped
# arrays, but it accidentally uses two COMPATIBLE shapes instead (so no
# error occurs, and the demonstration fails to show anything). Fix it
# so it actually raises the intended ValueError by using genuinely
# incompatible shapes, e.g. a length-3 array and a length-2 array.
def try_add_mismatched():
    a = np.array([1, 2, 3])
    b = np.array([1, 2, 3])
    return a + b


print(try_add_mismatched())


# TODO 4.A (Scenario -- Applying a Uniform Price Increase): write
# apply_price_increase(prices, percent). Return prices scaled up by
# percent (e.g. percent=10 means multiply every price by 1.10).


# TODO 4.B (Scenario -- Interview Prep): write
# explain_broadcasting_rule() describing, in plain language, when two
# differently-shaped arrays CAN be combined and when they can't.


# ============================================================
# Topic 5: Aggregate Functions & axis=
# ============================================================

# TODO 5.1: Write grid_total(grid). Return the single grand total of
# every element in a 2D grid (no axis=).


# TODO 5.2: Write column_totals(grid). Return one total per column
# (the correct axis= for "collapse down the rows").


# TODO 5.3 (Debug the Code): row_totals() below is supposed to return
# one total per ROW, but it uses the wrong axis. Fix it.
def row_totals(grid):
    return grid.sum(axis=0)


print(row_totals(np.array([[1, 2], [3, 4]])))


# TODO 5.A (Scenario -- Class Performance Report): write
# subject_and_student_averages(grades_grid). Given a 2D array (rows =
# students, columns = subjects), return a tuple
# (per_subject_averages, per_student_averages) using the correct axis=
# for each.


# TODO 5.B (Scenario -- Interview Prep): write
# explain_axis_parameter() describing, in plain language, what axis=0
# and axis=1 each collapse on a 2D array.


# ============================================================
# Topic 6: Reshaping & Stacking
# ============================================================

# TODO 6.1: Write flat_to_grid(flat_array, rows, cols). Return
# flat_array reshaped to (rows, cols).


# TODO 6.2: Write grid_to_flat(grid). Return grid flattened to 1D.


# TODO 6.3 (Debug the Code): stack_as_rows() below is supposed to
# stack two 1D arrays as two rows of a new 2D grid, but it uses
# np.hstack() (side by side) instead of np.vstack() (as rows). Fix it.
def stack_as_rows(arr1, arr2):
    return np.hstack([arr1, arr2])


print(stack_as_rows(np.array([1, 2]), np.array([3, 4])))


# TODO 6.A (Scenario -- Reshaping a Week of Sensor Data): write
# daily_averages(hourly_readings). Given a flat 1D array of 168 hourly
# readings (7 days x 24 hours), reshape it to (7, 24) and return the
# average reading for each day (one value per day, using the correct
# axis=).


# TODO 6.B (Scenario -- Interview Prep): write
# explain_reshape_vs_stack() describing the difference between
# reshaping a single array and stacking multiple separate arrays
# together.
