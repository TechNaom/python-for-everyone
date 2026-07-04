"""
Chapter 3 Project: Permission-Flags Calculator
See README.md in this folder for the full brief and an example run.

This mirrors how real Unix file permissions work: read=4, write=2,
execute=1. Combining flags with | and checking them with & is the same
trick used by chmod, file systems, and countless real permission systems.
"""

READ = 4
WRITE = 2
EXECUTE = 1

# TODO 1: Combine READ and WRITE into a single permissions value using
# the bitwise OR operator (|). Store it in a variable called `permissions`.


# TODO 2: Using bitwise AND (&) and bool(), check whether `permissions`
# includes READ, WRITE, and EXECUTE. Print all three results clearly,
# e.g. "Can read: True".


# TODO 3: Print the `permissions` value in binary using bin().


print("=== Permission Report ===")
