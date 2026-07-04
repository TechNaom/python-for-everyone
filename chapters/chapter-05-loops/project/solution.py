"""
Chapter 5 Project: Number Pattern Generator — reference solution.
"""

# TODO 1: Print this increasing-digit triangle using nested for loops:
# 1
# 12
# 123
# 1234
# 12345
print("--- Pattern 1: Increasing triangle ---")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()


# TODO 2: Print this star pyramid using nested for loops:
# *
# **
# ***
# ****
# *****
print("--- Pattern 2: Star pyramid ---")
for i in range(1, 6):
    print("*" * i)


# TODO 3: Print this decreasing-width triangle using nested for loops:
# 54321
# 5432
# 543
# 54
# 5
print("--- Pattern 3: Decreasing triangle ---")
for i in range(1, 6):
    count = 6 - i
    for num in range(5, 5 - count, -1):
        print(num, end="")
    print()
