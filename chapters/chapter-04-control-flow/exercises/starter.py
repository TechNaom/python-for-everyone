"""
Chapter 4 Exercises: Control Flow
See README.md in this folder for full instructions.
"""

# TODO 1: Given a = 45 and b = 78, print whichever is greater using if-else.


# TODO 2: Given number = 17, print whether it's even or odd using if-else
# and the % operator from Chapter 3.


# TODO 3: Given year = 2024, print whether it's a leap year. A year is a
# leap year if it's divisible by 4 AND (not divisible by 100 OR divisible
# by 400).


# TODO 4 (Debug the Code): this is supposed to grade 90 as "A", but it
# always prints "D". Find and fix the ordering bug.
score = 90
if score >= 40:
    grade = "D"
elif score >= 50:
    grade = "C"
elif score >= 60:
    grade = "B"
elif score >= 75:
    grade = "A"
else:
    grade = "Fail"
print("Grade:", grade)
