"""
Chapter 23 Project: Grade & Statistics Analyzer -- reference solution.
Run this from inside the project/ folder: python3 solution.py
"""

import numpy as np

STUDENT_NAMES = ["Ana", "Ben", "Chidi", "Dana", "Eli"]
SUBJECT_NAMES = ["Math", "Science", "English"]

# TODO 1
GRADES = np.array([
    [88, 92, 79],   # Ana
    [72, 65, 81],   # Ben
    [95, 91, 89],   # Chidi
    [60, 58, 70],   # Dana
    [84, 88, 92],   # Eli
])


# TODO 2
def overall_stats(grades):
    return {
        "mean": round(float(grades.mean()), 2),
        "median": round(float(np.median(grades)), 2),
        "std": round(float(grades.std()), 2),
        "min": round(float(grades.min()), 2),
        "max": round(float(grades.max()), 2),
    }


# TODO 3
def per_subject_stats(grades, subject_names):
    means = grades.mean(axis=0)
    mins = grades.min(axis=0)
    maxes = grades.max(axis=0)
    return [
        {
            "subject": subject_names[i],
            "mean": round(float(means[i]), 2),
            "min": int(mins[i]),
            "max": int(maxes[i]),
        }
        for i in range(len(subject_names))
    ]


# TODO 4
def per_student_stats(grades, student_names):
    means = grades.mean(axis=1)
    mins = grades.min(axis=1)
    maxes = grades.max(axis=1)
    return [
        {
            "student": student_names[i],
            "mean": round(float(means[i]), 2),
            "min": int(mins[i]),
            "max": int(maxes[i]),
        }
        for i in range(len(student_names))
    ]


# TODO 5
def above_average_students(grades, student_names):
    student_averages = grades.mean(axis=1)
    class_average = student_averages.mean()
    names_arr = np.array(student_names)
    return list(names_arr[student_averages > class_average])


# TODO 6
def below_average_students(grades, student_names):
    student_averages = grades.mean(axis=1)
    class_average = student_averages.mean()
    names_arr = np.array(student_names)
    return list(names_arr[student_averages < class_average])


# TODO 7
def format_report(grades, student_names, subject_names):
    lines = []

    lines.append("=== Overall Statistics ===")
    stats = overall_stats(grades)
    lines.append(f"Mean: {stats['mean']}  Median: {stats['median']}  Std: {stats['std']}  Min: {stats['min']}  Max: {stats['max']}")
    lines.append("")

    lines.append("=== Per-Subject Statistics ===")
    for s in per_subject_stats(grades, subject_names):
        lines.append(f"{s['subject']}: mean={s['mean']}  min={s['min']}  max={s['max']}")
    lines.append("")

    lines.append("=== Per-Student Statistics ===")
    for s in per_student_stats(grades, student_names):
        lines.append(f"{s['student']}: mean={s['mean']}  min={s['min']}  max={s['max']}")
    lines.append("")

    lines.append("=== Above-Average Students ===")
    above = above_average_students(grades, student_names)
    lines.append(", ".join(above) if above else "(none)")
    lines.append("")

    lines.append("=== Below-Average Students ===")
    below = below_average_students(grades, student_names)
    lines.append(", ".join(below) if below else "(none)")

    return "\n".join(lines)


def run():
    print("=== Grade & Statistics Analyzer ===")
    print()
    print(format_report(GRADES, STUDENT_NAMES, SUBJECT_NAMES))


if __name__ == "__main__":
    run()
