"""
Chapter 3 Project: Permission-Flags Calculator — reference solution.
"""

READ = 4
WRITE = 2
EXECUTE = 1

# TODO 1: Combine READ and WRITE into a single permissions value using
# the bitwise OR operator (|). Store it in a variable called `permissions`.
permissions = READ | WRITE

# TODO 2: Using bitwise AND (&) and bool(), check whether `permissions`
# includes READ, WRITE, and EXECUTE. Print all three results clearly,
# e.g. "Can read: True".
can_read = bool(permissions & READ)
can_write = bool(permissions & WRITE)
can_execute = bool(permissions & EXECUTE)

# TODO 3: Print the `permissions` value in binary using bin().
print("=== Permission Report ===")
print("Permissions value:", permissions)
print("Binary:", bin(permissions))
print("Can read:", can_read)
print("Can write:", can_write)
print("Can execute:", can_execute)
