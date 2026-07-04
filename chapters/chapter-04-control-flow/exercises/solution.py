"""
Chapter 4 Exercises: Control Flow — reference solution.
"""

# TODO 1: Given a = 45 and b = 78, print whichever is greater using if-else.
a = 45
b = 78
if a > b:
    print(a, "is greater")
else:
    print(b, "is greater")


# TODO 2: Given number = 17, print whether it's even or odd using if-else
# and the % operator from Chapter 3.
number = 17
if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")


# TODO 3: Given year = 2024, print whether it's a leap year. A year is a
# leap year if it's divisible by 4 AND (not divisible by 100 OR divisible
# by 400).
year = 2024
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")


# TODO 4 (Debug the Code): this is supposed to grade 90 as "A", but it
# always prints "D". Find and fix the ordering bug.
score = 90
if score >= 75:
    grade = "A"
elif score >= 60:
    grade = "B"
elif score >= 50:
    grade = "C"
elif score >= 40:
    grade = "D"
else:
    grade = "Fail"
print("Grade:", grade)
