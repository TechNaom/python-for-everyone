"""
Chapter 23 Exercises: NumPy for Data Analysis -- reference solution.
Run this from inside the exercises/ folder: python3 solution.py
"""

import numpy as np


# TODO 1
def make_grade_array(grades):
    return np.array(grades)


print(make_grade_array([88, 92, 79]))


# TODO 2
def array_summary(arr):
    return {
        "sum": arr.sum(),
        "mean": arr.mean(),
        "min": arr.min(),
        "max": arr.max(),
    }


print(array_summary(np.array([88, 92, 79, 95, 84])))


# TODO 3
def passing_scores(scores, passing=60):
    return scores[scores >= passing]


print(passing_scores(np.array([45, 72, 88, 55, 60])))


# TODO 4
def add_bonus_points(scores, bonus):
    return scores + bonus


print(add_bonus_points(np.array([70, 80, 90]), 5))


# TODO 5
def per_subject_average(grades_grid):
    return grades_grid.mean(axis=0)


# TODO 6
def per_student_average(grades_grid):
    return grades_grid.mean(axis=1)


grid = np.array([[90, 80], [70, 60], [100, 95]])
print(per_subject_average(grid))
print(per_student_average(grid))


# TODO 7
def reshape_to_grid(flat_array, rows, cols):
    return flat_array.reshape(rows, cols)


print(reshape_to_grid(np.arange(6), 2, 3))


# TODO 8
def combine_arrays(arr1, arr2):
    return np.concatenate([arr1, arr2])


print(combine_arrays(np.array([1, 2]), np.array([3, 4])))


# TODO 9 (Debug the Code)
# Bug: used axis=1 (per-row/per-student) when the task asked for
# per-column/per-subject averages, which is axis=0.
def average_per_subject(grades_grid):
    return grades_grid.mean(axis=0)


demo_grid = np.array([[90, 80], [70, 60], [100, 95]])
print(average_per_subject(demo_grid))
