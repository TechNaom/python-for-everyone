"""
Chapter 23 Project: Grade & Statistics Analyzer
See README.md in this folder for full instructions.
Run this from inside the project/ folder: python3 starter.py

Install NumPy first if you haven't: pip install numpy

This is a menu-driven mini-app, like Chapter 21's project, but built on
top of a 2D NumPy array of grades instead of a database connection:
each ROW is a student, each COLUMN is a subject.
"""

import numpy as np

STUDENT_NAMES = ["Ana", "Ben", "Chidi", "Dana", "Eli"]
SUBJECT_NAMES = ["Math", "Science", "English"]

# TODO 1: Build GRADES as a 2D NumPy array, 5 rows (students) x 3
# columns (subjects). Use these sample scores, one row per student in
# the same order as STUDENT_NAMES:
#   Ana:   [88, 92, 79]
#   Ben:   [72, 65, 81]
#   Chidi: [95, 91, 89]
#   Dana:  [60, 58, 70]
#   Eli:   [84, 88, 92]


# TODO 2: Write overall_stats(grades). Return a dict with keys "mean",
# "median", "std", "min", "max" summarizing EVERY grade in the whole
# grid (no axis=). Use np.median() for the median. Round each value to
# 2 decimal places with round(float(value), 2).


# TODO 3: Write per_subject_stats(grades, subject_names). Return a list
# of dicts, one per subject, each with keys "subject", "mean", "min",
# "max" -- using the correct axis= to get one result per SUBJECT
# (column). Round mean to 2 decimal places.


# TODO 4: Write per_student_stats(grades, student_names). Return a list
# of dicts, one per student, each with keys "student", "mean", "min",
# "max" -- using the correct axis= to get one result per STUDENT (row).
# Round mean to 2 decimal places.


# TODO 5: Write above_average_students(grades, student_names). Compute
# each student's average (axis=1), then the class-wide average of
# those per-student averages. Return a list of student names whose
# average is STRICTLY ABOVE the class-wide average, using boolean
# masking (no loop over students by index -- use the mask to select
# from a NumPy array of names).


# TODO 6: Write below_average_students(grades, student_names). Same as
# above_average_students, but for students STRICTLY BELOW the
# class-wide average.


# TODO 7: Write format_report(grades, student_names, subject_names).
# Build and return one multi-line string report combining:
#   - "=== Overall Statistics ===" followed by overall_stats()'s values
#   - "=== Per-Subject Statistics ===" followed by one line per subject
#     from per_subject_stats()
#   - "=== Per-Student Statistics ===" followed by one line per student
#     from per_student_stats()
#   - "=== Above-Average Students ===" followed by names from
#     above_average_students() (comma-separated, or "(none)" if empty)
#   - "=== Below-Average Students ===" followed by names from
#     below_average_students() (comma-separated, or "(none)" if empty)


def run():
    print("=== Grade & Statistics Analyzer ===")
    print()
    print(format_report(GRADES, STUDENT_NAMES, SUBJECT_NAMES))


if __name__ == "__main__":
    run()
