"""
Chapter 5 Exercises: Loops — reference solution.
"""

# TODO 1: Use a while loop to calculate and print the sum of numbers from
# 1 to 20 (inclusive).
total = 0
i = 1
while i <= 20:
    total += i
    i += 1
print("Sum 1-20:", total)


# TODO 2: Use a for loop to print the multiplication table of 7, from
# 7 x 1 up to 7 x 10.
for i in range(1, 11):
    print("7 x", i, "=", 7 * i)


# TODO 3: Given n = 1234, reverse its digits using % and // in a while
# loop (result should be 4321). Print the reversed number.
n = 1234
reversed_number = 0
while n > 0:
    last_digit = n % 10
    reversed_number = reversed_number * 10 + last_digit
    n = n // 10
print("Reversed:", reversed_number)


# TODO 4 (Debug the Code): this is supposed to print the numbers 1
# through 10 (inclusive), but it stops at 9. Find and fix the bug.
for i in range(1, 11):
    print(i)
