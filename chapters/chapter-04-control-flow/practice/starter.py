"""
Chapter 4 Practice Bank: Control Flow (if / elif / else)
See README.md in this folder for full instructions.

Only uses what Chapters 1-4 covered: print(), variables, input(), the
conversion functions, arithmetic/relational/logical/bitwise operators,
is/in, and if / if-else / elif chains / nested if. No loops, functions,
lists, dicts, or f-strings yet.
"""

# ============================================================
# Topic 1: Simple if
# ============================================================

# TODO 1.1: Create a variable temperature = 35. If temperature is above
# 32, print "Above freezing." Then add one more print() call right
# after the if block that always runs, no matter what temperature is,
# to show the program keeps going either way.


# TODO 1.2: Create a variable email holding an email-looking string
# (e.g. "name@example.com"). Using the `in` operator, print a message
# only if "@" is found inside email.


# TODO 1.3: Create a variable number = 17. Using the bitwise `&`
# operator (number & 1 == 1 is True only for odd numbers), print a
# message saying the number is odd, only if that check is True.


# TODO 1.4: Create a variable logged_in = True. Using `is` (not ==),
# check whether logged_in is True, and print a welcome message only if
# it is.


# TODO 1.5: Use input() to ask the user to type a password. If it
# exactly matches a password you choose in the code, print
# "Access granted." (Nothing should print if it doesn't match.)


# TODO 1.A (Scenario — Free Shipping Threshold): Create cart_total =
# 82.50. If cart_total is 75 or more, print a message telling the
# shopper they qualify for free shipping.


# TODO 1.B (Scenario — Interview Prep): An interviewer asks whether
# code placed right after an if block runs even when the condition is
# False. Prove it: write an if whose condition is False, then a
# print() right after it (same indent level as the if) that always
# runs. Add a comment explaining what you expect to see and why.


# ============================================================
# Topic 2: if-else
# ============================================================

# TODO 2.1: Create price_a = 42.00 and price_b = 37.50. Print which one
# is more expensive using if-else (treat equal prices as "price_b is
# more expensive or equal" in the else branch).


# TODO 2.2: Create completion_percent = 104. Using if-else and the
# `and` operator (or a chained comparison like 0 <= x <= 100), print
# "Valid percentage" if it's between 0 and 100 inclusive, otherwise
# print "Invalid percentage".


# TODO 2.3: Create letter = "e" and vowels = "aeiouAEIOU". Using
# if-else and the `in` operator, print whether letter is a vowel or a
# consonant.


# TODO 2.4: Create value = 24. Using if-else and the bitwise `&`
# operator, print whether value is odd or even (same technique as
# TODO 1.3, but now with an else branch instead of a bare if).


# TODO 2.5: Use input() to ask "Subscribe to our newsletter? (yes/no): ".
# If the answer is exactly "yes", print a confirmation message,
# otherwise print a friendly decline message.


# TODO 2.A (Scenario — Age-Based Ticket Pricing): Create visitor_age =
# 15. Using if-else, print "Child ticket: $8" if visitor_age is under
# 18, otherwise print "Adult ticket: $15".


# TODO 2.B (Scenario — Login Permission Check — Interview Prep): Create
# stored_username, stored_password, entered_username, and
# entered_password variables. Using if-else and `and`, print
# "Access granted." only if both entered values match both stored
# values, otherwise print "Access denied."


# ============================================================
# Topic 3: elif chains
# ============================================================

# TODO 3.1: Create signal_color = "yellow". Using an if/elif/elif/else
# chain, print "Stop" for "red", "Slow down" for "yellow", "Go" for
# "green", and "Unknown signal" for anything else.


# TODO 3.2: Create number = -6. Using if/elif/else, print whether
# number is positive, negative, or zero.


# TODO 3.3 (Debug the Code): This is meant to classify a temperature
# into exactly ONE category, but it uses three separate `if`
# statements instead of an elif chain. Because each `if` is checked
# independently, a hot temperature (95) also matches the "warm" check
# below it, so category gets overwritten and the final print shows the
# wrong result. Find the bug and fix it by turning the extra `if`s
# into `elif`s so only the first matching branch runs.
temperature = 95
category = "cold"
if temperature >= 90:
    category = "hot"
if temperature >= 60:
    category = "warm"
if temperature < 60:
    category = "cold"
print("Category:", category)


# TODO 3.4: Create n = 45. Using an if/elif/elif/else chain, print
# "FizzBuzz" if n is divisible by 15, "Fizz" if divisible by 3 (but not
# 15), "Buzz" if divisible by 5 (but not 15), otherwise print n itself.
# (Check divisible-by-15 first, or the more specific case never gets a
# chance to run — same lesson as the elif-ordering rule above.)


# TODO 3.5: Use input() to ask "Enter a day number (1-7): ", convert it
# to an int, then use an elif chain (one branch per day, 1 through 7)
# to print the matching weekday name. Print "Not a valid day number"
# for anything else.


# TODO 3.A (Scenario — Discount Tier by Purchase Amount): Create
# purchase_amount = 650. Using an elif chain, print "Tier: Platinum"
# for 1000+, "Tier: Gold" for 500+, "Tier: Silver" for 100+, and
# "No discount tier" otherwise. (Order matters here too — highest
# threshold first.)


# TODO 3.B (Scenario — Interview Prep): Create score = 82. Using an
# elif chain ordered highest-threshold-first (>=90 "A", >=80 "B",
# >=70 "C", else "F"), print the correct grade. Add a comment
# explaining, in your own words, why checking the highest threshold
# first is required for the chain to work correctly.


# ============================================================
# Topic 4: Nested if
# ============================================================

# TODO 4.1: Create number = 14. Using a nested if (an outer if checking
# whether number is positive, and an inner if-else checking even/odd),
# print one of: "is positive and even", "is positive and odd", or
# "is not positive".


# TODO 4.2: Create stored_username, stored_password, entered_username,
# and entered_password variables (make entered_password wrong on
# purpose so you can see the inner branch run). Using a nested if
# (outer checks the username, inner checks the password), print
# "Login successful.", "Incorrect password.", or "Username not found."


# TODO 4.3: Create exam_score = 62 and attendance_percent = 80. Using a
# nested if (outer checks exam_score >= 50, inner checks
# attendance_percent >= 75), print a message for each of the three
# possible outcomes: pass, "not eligible" (passed but low attendance),
# or fail.


# TODO 4.4: Create value = 250. Using a nested if (outer checks
# value > 0, inner checks value > 100), print "Large positive number.",
# "Small positive number.", or "Not a positive number."


# TODO 4.5: Use input() to ask "Enter your age: " and convert it to an
# int. If age is 18 or over, use a nested if that then asks
# "Do you have a valid ID? (yes/no): " with another input() — print
# "Entry allowed." or "ID required for entry." based on the answer. If
# age is under 18, print a message saying they must be 18 or older
# (no need to ask about ID in that case).


# TODO 4.A (Scenario — Bank Withdrawal): Create balance = 500 and
# withdrawal_amount = 200. Using a nested if (outer checks
# balance >= withdrawal_amount, inner checks withdrawal_amount > 0),
# print a success message with the new balance, an "invalid amount"
# message, or an "insufficient funds" message.


# TODO 4.B (Scenario — Interview Prep): Create a = 10, b = 5, c = 4.
# Write the nested version (if a > b: if a > c: print(...)) AND the
# single-condition version (if a > b and a > c: print(...)) back to
# back, so both print the same result. Add a comment explaining when
# nesting is genuinely required instead of just a style choice (hint:
# think about what happens once the inner check needs its own,
# different else).
