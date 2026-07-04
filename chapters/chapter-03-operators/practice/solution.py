"""
Chapter 3 Practice Bank: Operators — reference solution.
"""

# ============================================================
# Topic 1: Arithmetic & assignment
# ============================================================

# TODO 1.1
a = 17
b = 5
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a // b =", a // b)
print("a % b =", a % b)
print("a ** b =", a ** b)


# TODO 1.2
score = 50
score += 10
print(score)
score -= 5
print(score)
score *= 2
print(score)
score //= 3
print(score)
score %= 7
print(score)
score **= 2
print(score)


# TODO 1.3
celsius = 25
fahrenheit = celsius * 9 / 5 + 32
print("Fahrenheit:", fahrenheit)


# TODO 1.4 (Debug the Code)
# Bug: "-number ** 2" is parsed as "-(number ** 2)" because ** binds
# tighter than unary minus, so it computed -(3 ** 2) = -9 instead of
# (-3) ** 2 = 9. Wrapping the negation in parentheses fixes it.
number = 3
squared = (-number) ** 2
print("Square of -3:", squared)


# TODO 1.5
length = 8
width = 3
area = length * width
perimeter = 2 * (length + width)
print("Area:", area)
print("Perimeter:", perimeter)


# TODO 1.A (Scenario — Grocery Bill Split)
total_cents = 1875
friends = 4
share_cents = total_cents // friends
leftover_cents = total_cents % friends
print("Each friend pays (cents):", share_cents)
print("Leftover cents:", leftover_cents)


# TODO 1.B (Scenario — Interview Prep)
# "/" is true division in Python and always returns a float, even when
# the division comes out even — 10 / 2 is 5.0 (a float), not 5 (an
# int). Only "//" (floor division) can return an int here.
print(10 / 2)


# ============================================================
# Topic 2: Relational & logical
# ============================================================

# TODO 2.1
x = 8
y = 3
print(x == y)
print(x != y)
print(x < y)
print(x > y)
print(x <= y)
print(x >= y)


# TODO 2.2
age = 25
print(age >= 18 and age <= 65)


# TODO 2.3
temperature = 95
print(temperature > 90 or temperature < 32)


# TODO 2.4
is_raining = False
print(not is_raining)


# TODO 2.5
credit_score = 720
has_income = True
print(credit_score >= 700 and has_income)


# TODO 2.A (Scenario — Login Gatekeeper)
is_active_account = True
correct_password = True
print(is_active_account and correct_password)


# TODO 2.B (Scenario — Interview Prep)
# This does not crash because "and" short-circuits: Python checks
# "x != 0" first, finds it False, and already knows the whole
# expression must be False — so it never evaluates "10 / x", which
# would otherwise raise a ZeroDivisionError.
x = 0
print(x != 0 and 10 / x > 1)


# ============================================================
# Topic 3: Bitwise
# ============================================================

# TODO 3.1
a = 5
b = 6
print(a & b)
print(a | b)
print(a ^ b)


# TODO 3.2
print(a << 1)
print(a >> 1)


# TODO 3.3
# Bitwise NOT flips every bit of the number, which for signed integers
# is the same as computing -(n + 1); ~5 is -6.
print(~a)


# TODO 3.4
read = 4
write = 2
execute = 1
permissions = read | write
print(permissions)


# TODO 3.5
print(permissions & write)


# TODO 3.A (Scenario — Unix File Permissions)
read = 4
write = 2
execute = 1
full_permissions = read | write | execute
print(full_permissions)


# TODO 3.B (Scenario — Interview Prep)
# Powers of 2 (1, 2, 4, 8, ...) each occupy exactly one unique bit, so
# any combination of them produces a distinct pattern that can be
# split back apart with & — plain sequential numbers like 1, 2, 3
# would overlap in their bits and couldn't be combined/checked
# independently.
read = 4
execute = 1
combined = read | execute
has_execute = combined & execute
print(combined)
print(has_execute)


# ============================================================
# Topic 4: Special: is / in
# ============================================================

# TODO 4.1
a = 10
b = 10
print(a is b)
print(a == b)


# TODO 4.2
name = "Ada"
name_alias = name
print(name is name_alias)


# TODO 4.3
word = "python"
print("th" in word)


# TODO 4.4
print("z" not in word)


# TODO 4.5
pin = "4821"
digit = "8"
print(digit in pin)


# TODO 4.A (Scenario — Access Code Validator)
allowed_chars = "ABCDEF0123456789"
entered_char = "F"
print(entered_char in allowed_chars)


# TODO 4.B (Scenario — Interview Prep)
# "==" checks value equality and is always the reliable choice here:
# x == y is True. "is" checks identity (same object in memory), and
# Python only guarantees caching (and therefore "is" being True) for
# small integers, roughly -5 to 256 — 300 is outside that range, so
# "x is y" is not guaranteed to be True even though the values match.
x = 300
y = 300
print(x == y)
print(x is y)
