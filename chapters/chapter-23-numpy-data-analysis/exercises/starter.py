"""
Chapter 23 Exercises: NumPy for Data Analysis
See README.md in this folder for full instructions.
Run this from inside the exercises/ folder: python3 starter.py

Every task here uses NumPy directly -- make sure it's installed first:
pip install numpy
"""

import numpy as np


# TODO 1: Write make_grade_array(grades). Given a plain Python list of
# numbers, return it as a NumPy array.


# TODO 2: Write array_summary(arr). Return a dict with keys "sum", "mean",
# "min", "max" holding arr's sum, mean, min, and max (each converted with
# float()/int() as appropriate isn't required here -- just return the
# raw NumPy values).


# TODO 3: Write passing_scores(scores, passing=60). Given a NumPy array
# of scores, return only the scores that are >= passing, using boolean
# masking (no loop).


# TODO 4: Write add_bonus_points(scores, bonus). Given a NumPy array and
# a number, return a NEW array with bonus added to every element
# (vectorized -- no loop).


# TODO 5: Write per_subject_average(grades_grid). Given a 2D NumPy array
# where each ROW is a student and each COLUMN is a subject, return the
# average for each SUBJECT (one value per column) using the correct
# axis=.


# TODO 6: Write per_student_average(grades_grid). Given the same 2D
# array, return the average for each STUDENT (one value per row) using
# the correct axis=.


# TODO 7: Write reshape_to_grid(flat_array, rows, cols). Return
# flat_array reshaped to (rows, cols).


# TODO 8: Write combine_arrays(arr1, arr2). Return arr1 and arr2 joined
# end-to-end into one longer 1D array (np.concatenate).


# TODO 9 (Debug the Code): this is supposed to return the average of
# every COLUMN (one value per subject) in a 2D grid, but it has the
# axis backwards -- it currently returns one value per row/student
# instead. Find and fix it.
def average_per_subject(grades_grid):
    return grades_grid.mean(axis=1)


demo_grid = np.array([[90, 80], [70, 60], [100, 95]])
print(average_per_subject(demo_grid))
