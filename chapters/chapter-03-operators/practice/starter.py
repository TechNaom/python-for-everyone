"""
Chapter 3 Practice Bank: Operators
See README.md in this folder for full instructions.

Only uses what Chapters 1-3 covered: print(), variables, basic types,
input(), string concatenation with + and str(), type()/id(),
int()/float()/str()/bool()/complex(), all arithmetic and compound
assignment operators, relational and logical operators, bitwise
operators, and is / in. No if/elif/else, no loops, no functions, and no
list/dict literals (in is only demonstrated against strings here).
"""

# ============================================================
# Topic 1: Arithmetic & assignment
# ============================================================

# TODO 1.1: Given a = 17 and b = 5, print the result of all seven
# arithmetic operators (+, -, *, /, //, %, **) — one print() call per
# operator, each with a label.


# TODO 1.2: Start with score = 50. Apply each compound assignment
# shortcut in turn, printing the new value after each one:
# += 10, then -= 5, then *= 2, then //= 3, then %= 7, then **= 2.


# TODO 1.3: Given celsius = 25, convert it to Fahrenheit using
# fahrenheit = celsius * 9 / 5 + 32, and print the result labeled.


# TODO 1.4 (Debug the Code): This is supposed to print the square of
# -3, which is 9. It prints -9 instead. The bug is operator precedence:
# ** binds tighter than unary minus, so "-number ** 2" is actually
# "-(number ** 2)", not "(-number) ** 2". Fix it with parentheses.
number = 3
squared = -number ** 2
print("Square of -3:", squared)


# TODO 1.5: Given length = 8 and width = 3, compute and print the area
# (length * width) and the perimeter (2 * (length + width)), each with
# a label.


# TODO 1.A (Scenario — Grocery Bill Split): A group of friends is
# splitting a restaurant bill of total_cents = 1875 evenly among
# friends = 4 people. Use // to find each person's even share (in
# cents) and % to find the leftover cents that don't divide evenly,
# and print both with labels.


# TODO 1.B (Scenario — Interview Prep): An interviewer asks whether
# "/" in Python can ever return a whole number type when the division
# comes out even. Prove your answer: print the result of 10 / 2, and
# add a comment explaining what type it is and why.


# ============================================================
# Topic 2: Relational & logical
# ============================================================

# TODO 2.1: Given x = 8 and y = 3, print the result of all six
# relational operators (==, !=, <, >, <=, >=) — one print() call each.


# TODO 2.2: Given age = 25, print a single expression using "and" that
# checks whether age is between 18 and 65 (inclusive).


# TODO 2.3: Given temperature = 95, print a single expression using
# "or" that checks whether it's too hot (over 90) or too cold (under
# 32).


# TODO 2.4: Given is_raining = False, print "not is_raining" to show
# how "not" flips a boolean.


# TODO 2.5: Given credit_score = 720 and has_income = True, print a
# single expression using "and" that checks whether credit_score is at
# least 700 AND has_income is True.


# TODO 2.A (Scenario — Login Gatekeeper): A login system only lets a
# user in if is_active_account is True AND correct_password is True.
# Set both variables to True and print the combined "and" expression
# that decides whether login is allowed.


# TODO 2.B (Scenario — Interview Prep): An interviewer asks you to
# prove short-circuit evaluation is real. Given x = 0, print the
# expression "x != 0 and 10 / x > 1" and add a comment explaining why
# this does NOT crash even though 10 / 0 would normally raise an
# error.


# ============================================================
# Topic 3: Bitwise
# ============================================================

# TODO 3.1: Given a = 5 and b = 6, print a & b, a | b, and a ^ b.


# TODO 3.2: Using the same a = 5, print a << 1 and a >> 1.


# TODO 3.3: Using the same a = 5, print ~a, and add a comment
# explaining what bitwise NOT does to every bit (hint: ~n is the same
# as -(n + 1)).


# TODO 3.4: Given read = 4, write = 2, and execute = 1 (powers of 2),
# combine read and write into one number using | and print it.


# TODO 3.5: Using the permissions value from TODO 3.4, check whether
# the write flag is set by printing "permissions & write".


# TODO 3.A (Scenario — Unix File Permissions): Given read = 4,
# write = 2, and execute = 1, combine all three into one
# full_permissions value using | and print it (this is exactly how
# Unix file permissions like rwx work under the hood).


# TODO 3.B (Scenario — Interview Prep): An interviewer asks why bit
# flags are always assigned as powers of 2 (1, 2, 4, 8, ...) instead of
# plain sequential numbers (1, 2, 3, 4, ...). Given read = 4 and
# execute = 1, combine them with | into a variable called combined,
# then check whether execute is set with & and print both results. Add
# a comment explaining your answer.


# ============================================================
# Topic 4: Special: is / in
# ============================================================

# TODO 4.1: Given a = 10 and b = 10, print "a is b" and print "a == b"
# to compare identity vs. value equality for small integers.


# TODO 4.2: Given name = "Ada", create name_alias = name (copying the
# reference, not a new value), then print "name is name_alias".


# TODO 4.3: Given word = "python", print whether "th" is found inside
# it using in.


# TODO 4.4: Using the same word variable, print whether "z" is NOT
# found inside it using not in.


# TODO 4.5: Given pin = "4821" and digit = "8", print whether digit is
# found inside pin using in.


# TODO 4.A (Scenario — Access Code Validator): A keypad only accepts
# hex digits. Given allowed_chars = "ABCDEF0123456789" and
# entered_char = "F", print whether entered_char is in allowed_chars.


# TODO 4.B (Scenario — Interview Prep): An interviewer asks whether
# "is" is a safe way to check if two numbers are equal. Given x = 300
# and y = 300, print "x == y" and print "x is y", then add a comment
# explaining why "==" is the reliable choice here and "is" is not
# guaranteed to be True for integers this large (Python only
# guarantees caching for small integers, roughly -5 to 256).
