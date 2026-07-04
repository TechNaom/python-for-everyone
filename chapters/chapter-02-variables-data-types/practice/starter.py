"""
Chapter 2 Practice Bank: Variables & Data Types
See README.md in this folder for full instructions.

Only uses what Chapters 1-2 covered: print(), variables, input(),
string concatenation with + and str() (Chapter 1), plus valid/invalid
identifier naming, dynamic typing, type(), id(), and the conversion
functions int(), float(), str(), bool(), complex() (Chapter 2). No
arithmetic beyond simple +, no comparison/logical operators, no
if/else, no loops, no functions, no lists/dicts, no f-strings.
"""

# ============================================================
# Topic 1: Naming variables properly
# ============================================================

# TODO 1.1: Create three properly named (snake_case) variables for a
# person's first name, last name, and age. Print each on its own line.


# TODO 1.2: Someone named a shopping cart total "x" -- not descriptive.
# Create a properly named replacement variable (e.g. cart_total),
# assign it 49.99, and print it.


# TODO 1.3: Create three variables, total, Total, and TOTAL, each
# holding a different number. Print all three to prove Python treats
# them as three completely separate variables.


# TODO 1.4: Create a variable name that starts with an underscore for
# an internal-use value (e.g. _session_id), assign it a value, and
# print it.


# TODO 1.5: Below are three badly chosen identifier ideas, written as
# comments only (they are NOT valid Python and must stay commented):
#   2nd_place   -- starts with a digit
#   user name   -- has a space
#   api-key     -- has a hyphen
# Write three valid, corrected snake_case versions as real variables
# (e.g. second_place, user_name, api_key) with sample values, and
# print each one.


# TODO 1.A (Scenario -- Config Keys): You're naming variables for an
# app's config file: a maximum retry count, an API timeout in seconds,
# and whether debug mode is on. Create all three with proper snake_case
# names, assign sample values, and print each one.


# TODO 1.B (Scenario -- Interview Prep): An interviewer asks you to
# explain why total, Total, and TOTAL can all exist as separate
# variables in the same program. Re-create the three variables from
# TODO 1.3, print them again, and add a comment explaining why in your
# own words.


# ============================================================
# Topic 2: Python decides the type for you
# ============================================================

# TODO 2.1: Create four variables -- a username (str), a
# follower_count (int), a rating (float), and is_verified (bool) --
# and print all four in a single print() call, separated by commas.


# TODO 2.2: Create a variable signal = 10 and print it. Then reassign
# signal to the string "ten" and print it again, to see its type
# change after reassignment.


# TODO 2.3: Create a variable ready = True (a boolean) and print it.
# Then reassign ready to the string "yes" and print it again.


# TODO 2.4: Create a variable reading = 3 + 4j (a complex number) and
# print it directly.


# TODO 2.5: Create a variable temp = 98.6 (a float) and print it. Then
# reassign temp to the int 100 and print it again -- showing a
# variable can switch between numeric types too.


# TODO 2.A (Scenario -- Feature Flag): A feature flag starts as the
# boolean True. Create feature_enabled = True and print it. Then
# simulate a config reload that reassigns it to the string "enabled"
# and print it again. Add a comment noting this reassignment would be
# a compile error in a statically typed language like Java, but is
# completely legal in Python.


# TODO 2.B (Scenario -- Debug the Code -- Interview Prep): The snippet
# below is supposed to print a shopping cart summary line, but it
# crashes with a TypeError because the developer forgot item_count is
# a number, not text. Find the bug and fix it.
item_count = 3
print("Items in cart: " + item_count)


# ============================================================
# Topic 3: type() and id()
# ============================================================

# TODO 3.1: Create a variable price = 49.99 and print its type using
# type().


# TODO 3.2: Create two variables, a = 7 and b = 7. Print id(a) and
# id(b) on separate lines to see whether they match.


# TODO 3.3: Create a variable label = "hello". Print its type and its
# id, one per line.


# TODO 3.4: Create x = 500 and y = 500. Print id(x) and id(y), and add
# a comment noting whether the two ids matched, based on what the
# lesson said about small numbers vs. larger ones.


# TODO 3.5: Create a variable flag = True and print its type. Then
# reassign flag to 42 and print its type again -- showing that type()
# always reports the variable's CURRENT value, not its original one.


# TODO 3.A (Scenario -- QA Type Check): Your QA team wants proof that
# a config value loaded as user_id = 1001 is really an int before it's
# used in a billing system. Print type(user_id) as that proof.


# TODO 3.B (Scenario -- Interview Prep): An interviewer asks: "If
# x = 5 and y = 5, will id(x) and id(y) be the same?" Create both
# variables, print both ids, and add a comment answering the question
# and explaining why, based on what the lesson said about immutable
# small integers.


# ============================================================
# Topic 4: Converting between types
# ============================================================

# TODO 4.1: Ask the user for their age with input() (it comes back as
# text), convert it to an int with int(), and print the converted
# value along with its type using type().


# TODO 4.2: Create a variable pi_text = "3.14" and convert it to a
# float with float(). Print the converted value.


# TODO 4.3: Create a variable count = 42 (an int) and convert it to a
# string with str(). Print the converted value and its type.


# TODO 4.4: Create a variable switch = 0 and convert it to a bool with
# bool(); print the result. Then create switch2 = 1, convert that too,
# and print it -- to compare how 0 and 1 convert differently.


# TODO 4.5 (Debug the Code): This code is supposed to convert a typed
# quantity into a number, but it crashes with a ValueError because
# "three" isn't a numeral Python can parse. Find the bug and fix it.
food_quantity = "three"
quantity_number = int(food_quantity)
print("You have " + str(quantity_number) + " items.")


# TODO 4.A (Scenario -- Signup Form): Ask the user for their current
# age with input(), convert it to an int, then print a sentence
# stating their age next year (add 1 to the converted number using +).


# TODO 4.B (Scenario -- Interview Prep): An interviewer asks: "What
# does bool('False') return, and why does that surprise people?"
# Create a variable trick = bool("False"), print it, and add a comment
# explaining the empty-string rule in your own words.
