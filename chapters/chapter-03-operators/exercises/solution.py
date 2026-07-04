"""
Chapter 3 Exercises: Operators — reference solution.
"""

# TODO 1: Given a = 17 and b = 5, print the result of every arithmetic
# operator: +, -, *, /, //, %, **
a = 17
b = 5
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)


# TODO 2: Given age = 25, check (and print) whether age is between 18 and
# 65 (inclusive) using a single expression with 'and'.
age = 25
print(age >= 18 and age <= 65)


# TODO 3: Given x = 12 (binary 1100) and y = 10 (binary 1010), print the
# result of x & y, x | y, and x ^ y.
x = 12
y = 10
print(x & y)
print(x | y)
print(x ^ y)


# TODO 4 (Debug the Code): this is supposed to print the exact average of
# 7 and 2 (which is 3.5), but it always prints 3. Find and fix the bug.
total = 7
count = 2
average = total / count
print("Average:", average)
