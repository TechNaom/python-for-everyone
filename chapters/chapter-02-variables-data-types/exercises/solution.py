"""
Chapter 2 Exercises: Variables & Data Types — reference solution.
"""

# TODO 1: Create three variables: favorite_number (int), pi_estimate (float),
# and is_raining (bool). Print each value along with its type using type().
favorite_number = 7
pi_estimate = 3.14
is_raining = False
print(favorite_number, type(favorite_number))
print(pi_estimate, type(pi_estimate))
print(is_raining, type(is_raining))


# TODO 2: Set a = 5 and b = 5. Print whether id(a) == id(b), and print a
# short sentence explaining why, based on what Chapter 2 taught.
a = 5
b = 5
print(id(a) == id(b))
print("Small immutable ints like 5 are reused by Python, so a and b share the same object.")


# TODO 3: Ask the user for their birth year with input(), convert it to an
# int, then calculate and print their approximate age (assume current year
# is 2026).
birth_year = int(input("What year were you born? "))
age = 2026 - birth_year
print("You are approximately " + str(age) + " years old.")


# TODO 4 (Debug the Code): this code crashes with a TypeError. Find and fix
# the bug using what you learned about type conversion.
total = 150
print("Total: " + str(total))
