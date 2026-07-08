"""
Chapter 23 Practice Bank: NumPy for Data Analysis -- reference solution.
Run this from inside the practice/ folder: python3 solution.py
"""

import numpy as np

# ============================================================
# Topic 1: What NumPy Is & Why It Exists
# ============================================================

# TODO 1.1
def loop_sum(values):
    total = 0
    for v in values:
        total += v
    return total


print(loop_sum([1, 2, 3, 4, 5]))


# TODO 1.2
def array_sum(values):
    return np.array(values).sum()


print(array_sum([1, 2, 3, 4, 5]))


# TODO 1.3 (Debug the Code)
# Bug: claimed NumPy is faster due to memory usage -- the real reason is
# a fixed dtype (skipping per-element type checks) plus vectorized
# operations running in optimized compiled code, not memory size per se.
def describe_numpy_speed():
    return (
        "NumPy arrays are faster because every element shares one fixed "
        "data type (skipping per-element type-checking) and operations run "
        "as vectorized, compiled code instead of a Python-level loop."
    )


print(describe_numpy_speed())


# TODO 1.A (Scenario -- Comparing Two Approaches)
def should_use_numpy(dataset_size, operation_count):
    return dataset_size > 1000 or operation_count > 10


print(should_use_numpy(50, 3))
print(should_use_numpy(5000, 3))
print(should_use_numpy(50, 20))


# TODO 1.B (Scenario -- Interview Prep)
def explain_why_numpy_is_foundational():
    return (
        "NumPy's ndarray, shape conventions, and broadcasting rules are "
        "reused directly by pandas, scikit-learn, and other data libraries "
        "-- building on one shared, fast array representation instead of "
        "each library reinventing its own."
    )


print(explain_why_numpy_is_foundational())


# ============================================================
# Topic 2: Creating Arrays
# ============================================================

# TODO 2.1
def build_range_array(start, stop, step):
    return np.arange(start, stop, step)


print(build_range_array(0, 10, 2))


# TODO 2.2
def describe_array(arr):
    return {"shape": arr.shape, "dtype": str(arr.dtype), "ndim": arr.ndim}


print(describe_array(np.array([[1, 2], [3, 4]])))


# TODO 2.3 (Debug the Code)
# Bug: used np.arange(0, 1, 5) (a step-based range, which produces just
# [0]) instead of np.linspace(0, 1, 5) (5 evenly spaced values from 0 to
# 1 inclusive).
def make_evenly_spaced():
    return np.linspace(0, 1, 5)


print(make_evenly_spaced())


# TODO 2.A (Scenario -- Sensor Baseline Array)
def build_baseline_readings(count):
    return np.zeros(count)


print(build_baseline_readings(4))


# TODO 2.B (Scenario -- Interview Prep)
def explain_shape_vs_dtype_vs_ndim():
    return (
        "shape is a tuple giving the size of each dimension; dtype is the "
        "single data type every element shares; ndim is how many "
        "dimensions the array has -- 1 for a flat array, 2 for a grid."
    )


print(explain_shape_vs_dtype_vs_ndim())


# ============================================================
# Topic 3: Indexing, Slicing & Boolean Masking
# ============================================================

# TODO 3.1
def get_column(grid, col_index):
    return grid[:, col_index]


print(get_column(np.array([[1, 2, 3], [4, 5, 6]]), 1))


# TODO 3.2
def above_threshold(arr, threshold):
    return arr[arr > threshold]


print(above_threshold(np.array([3, 8, 1, 9, 4]), 5))


# TODO 3.3 (Debug the Code)
# Bug: read grid[:, 1] (column 1) when the task asked for ROW index 1.
def get_second_row(grid):
    return grid[1]


sample_grid = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(get_second_row(sample_grid))


# TODO 3.A (Scenario -- Flagging Failing Grades)
def flag_failing_grades(scores, passing=60):
    return scores[scores < passing]


print(flag_failing_grades(np.array([45, 72, 88, 55, 60])))


# TODO 3.B (Scenario -- Interview Prep)
def explain_boolean_masking():
    return (
        "A boolean mask is an array of True/False values produced by a "
        "comparison like arr > 5; indexing with that mask (arr[arr > 5]) "
        "returns only the elements where it's True, with no explicit loop "
        "-- the single most common NumPy idiom for filtering real data."
    )


print(explain_boolean_masking())


# ============================================================
# Topic 4: Vectorized Math & Broadcasting
# ============================================================

# TODO 4.1
def scale_array(arr, factor):
    return arr * factor


print(scale_array(np.array([1, 2, 3]), 10))


# TODO 4.2
def add_row_offset(grid, offsets):
    return grid + offsets


print(add_row_offset(np.array([[1, 2], [3, 4]]), np.array([10, 100])))


# TODO 4.3 (Debug the Code)
# Bug: used two compatible (equal) shapes, so no broadcasting error ever
# occurs -- fixed by using genuinely incompatible shapes (length 3 vs 2).
def try_add_mismatched():
    a = np.array([1, 2, 3])
    b = np.array([1, 2])
    return a + b


try:
    print(try_add_mismatched())
except ValueError as e:
    print("ValueError:", e)


# TODO 4.A (Scenario -- Applying a Uniform Price Increase)
def apply_price_increase(prices, percent):
    return prices * (1 + percent / 100)


print(apply_price_increase(np.array([100, 200, 50]), 10))


# TODO 4.B (Scenario -- Interview Prep)
def explain_broadcasting_rule():
    return (
        "Two array shapes can broadcast together if, comparing from the "
        "rightmost dimension inward, every pair of dimensions is either "
        "equal or one of them is 1 (which gets stretched to match); if "
        "neither condition holds for some dimension, NumPy raises a "
        "ValueError instead of guessing."
    )


print(explain_broadcasting_rule())


# ============================================================
# Topic 5: Aggregate Functions & axis=
# ============================================================

# TODO 5.1
def grid_total(grid):
    return grid.sum()


print(grid_total(np.array([[1, 2], [3, 4]])))


# TODO 5.2
def column_totals(grid):
    return grid.sum(axis=0)


print(column_totals(np.array([[1, 2], [3, 4]])))


# TODO 5.3 (Debug the Code)
# Bug: used axis=0 (per-column) when the task asked for per-ROW totals,
# which is axis=1.
def row_totals(grid):
    return grid.sum(axis=1)


print(row_totals(np.array([[1, 2], [3, 4]])))


# TODO 5.A (Scenario -- Class Performance Report)
def subject_and_student_averages(grades_grid):
    return grades_grid.mean(axis=0), grades_grid.mean(axis=1)


demo = np.array([[90, 85, 92], [70, 75, 80], [88, 91, 95]])
print(subject_and_student_averages(demo))


# TODO 5.B (Scenario -- Interview Prep)
def explain_axis_parameter():
    return (
        "axis=0 collapses down the rows, producing one result per column; "
        "axis=1 collapses across the columns, producing one result per "
        "row. Checking result.shape after an axis= call confirms which "
        "direction actually collapsed."
    )


print(explain_axis_parameter())


# ============================================================
# Topic 6: Reshaping & Stacking
# ============================================================

# TODO 6.1
def flat_to_grid(flat_array, rows, cols):
    return flat_array.reshape(rows, cols)


print(flat_to_grid(np.arange(6), 2, 3))


# TODO 6.2
def grid_to_flat(grid):
    return grid.flatten()


print(grid_to_flat(np.array([[1, 2], [3, 4]])))


# TODO 6.3 (Debug the Code)
# Bug: used np.hstack() (side by side, one long row) when the task asked
# for stacking as two separate ROWS, which is np.vstack().
def stack_as_rows(arr1, arr2):
    return np.vstack([arr1, arr2])


print(stack_as_rows(np.array([1, 2]), np.array([3, 4])))


# TODO 6.A (Scenario -- Reshaping a Week of Sensor Data)
def daily_averages(hourly_readings):
    return hourly_readings.reshape(7, 24).mean(axis=1)


week = np.arange(168)
print(daily_averages(week))


# TODO 6.B (Scenario -- Interview Prep)
def explain_reshape_vs_stack():
    return (
        "Reshaping regroups the SAME array's existing data into a new "
        "shape without changing any values; stacking (concatenate/vstack/"
        "hstack) combines two or more SEPARATE arrays into one, either "
        "end-to-end, as new rows, or side by side."
    )


print(explain_reshape_vs_stack())
