"""
Chapter 1 Practice Bank: Your First Python Program
See README.md in this folder for full instructions.

Only uses what Chapter 1 covered: print(), variables, basic types
(string/int/float), input(), string concatenation with + and str().
"""

# ============================================================
# Topic 1: print()
# ============================================================

# TODO 1.1: Print "Hello, World!" on one line, then print your own name
# on the next line — two separate print() calls.


# TODO 1.2: Print a 3-line shipping label — name, street address, and
# city + zip — one print() call per line.


# TODO 1.3: Print a decorative header for a program: a line of dashes,
# then a title, then another line of dashes — three print() calls.


# TODO 1.4: Print the word "Loading..." three times, each in its own
# print() call. Add a comment underneath explaining why the three
# words appear on three separate lines instead of running together.


# TODO 1.5: Print a 2-line "Welcome" banner using symbols of your choice
# in the quoted text (e.g. "*** Welcome! ***").


# TODO 1.A (Scenario — Internal Tool): Your team's internal CLI script
# needs a startup banner. Print two lines: a title line for the tool,
# and a second line that says "Type --help for options".


# TODO 1.B (Scenario — Interview Prep): An interviewer asks whether
# print() automatically starts a new line after each call. Prove it —
# write two separate print() calls, and add a comment above them
# explaining what you expect to see on screen and why.


# ============================================================
# Topic 2: Variables
# ============================================================

# TODO 2.1: Store your name, age, and height in three variables
# (string, int, float) and print each one on its own line.


# TODO 2.2: Create a variable score = 10 and print it. Then reassign
# score to 20 and print it again, to show a variable's value can
# change over time.


# TODO 2.3: Create two variables, a and b, holding two different
# values. Print b first, then a — to show a variable is just a label,
# not tied to the order it was created in.


# TODO 2.4: Create a variable balance starting at 100. Reassign it
# three times in a row (like a running total after purchases:
# 100 -> 80 -> 95 -> 60), printing it after each reassignment.


# TODO 2.5: Store your favorite color in a variable called
# favorite_color. Create a second variable, favorite_color_backup,
# and assign it the value of favorite_color. Print both to show they
# currently match.


# TODO 2.A (Scenario — Click Counter): You're simulating a button-click
# counter with no loops yet. Start click_count = 0, print it, then
# reassign it to 1, 2, and 3 in turn (as if simulating 3 clicks),
# printing the count after each one.


# TODO 2.B (Scenario — Debug the Code — Interview Prep): The snippet
# below is supposed to print a bank balance AFTER a deposit of 50 is
# added, but it prints the balance from BEFORE the deposit. Find the
# bug and fix it (hint: check the order of the lines).
balance = 200
print("Balance after deposit:", balance)
balance = balance + 50


# ============================================================
# Topic 3: Basic Types (string / int / float)
# ============================================================

# TODO 3.1: Create one variable of each type studied — a string
# (product name), an int (quantity), and a float (price) — and print
# each with a label sentence, using + and str() to join them.


# TODO 3.2: Create a variable item_count = 12 (an int). Print a
# sentence "Total items: " joined with str(item_count).


# TODO 3.3 (Debug the Code): This line tries to join a string directly
# with an int and will crash with a TypeError. Fix it using str().
total_price = 45
print("Total price: $" + total_price)


# TODO 3.4: Build a one-line "ID card" sentence that joins a person's
# name (string), age (int), and GPA (float) into a single sentence,
# converting the int and float with str() before joining.


# TODO 3.5: Store the same numeric value two ways — once as an int
# (e.g. 5) and once as a float (e.g. 5.0) — in two variables, and
# print both to see how Python displays them differently.


# TODO 3.A (Scenario — Till Receipt): Store an item name (string) and
# a price (float) in variables, then print one receipt line like
# "Coffee - $4.50" by joining them with + and str().


# TODO 3.B (Scenario — Interview Prep): An interviewer asks why
# "Age: " + 30 crashes but "Age: " + str(30) works. Below, write the
# FIXED version only (don't leave a line that actually crashes the
# file), and add a one-line comment explaining the difference in your
# own words.


# ============================================================
# Topic 4: input()
# ============================================================

# TODO 4.1: Ask the user for their name with input() and print a
# personalized greeting using their answer.


# TODO 4.2: Ask the user for two separate pieces of information (their
# name, and their favorite hobby) using two input() calls, then print
# both combined in one sentence.


# TODO 4.3: Ask the user for their age (as text, via input()) and
# build a sentence combining it with other text using +.


# TODO 4.4 (Debug the Code): This code asks for the user's name, then
# tries to build a welcome sentence by joining it directly with an int
# (age) using +, which crashes with a TypeError. Fix it using str().
age = 30
user_name = input("What's your name? ")
print("Hello " + user_name + ", did you know our app is " + age + " years old?")


# TODO 4.5: Ask the user two questions via input() (favorite food,
# favorite season), then print a single sentence combining both
# answers with fixed text around them.


# TODO 4.A (Scenario — Mini Mad Libs): Ask the user for a noun and an
# adjective using two input() calls, then print a silly sentence that
# combines both answers with fixed text around them.


# TODO 4.B (Scenario — Interview Prep): An interviewer asks what data
# type input() always returns, no matter what the user types. Prove
# your answer: ask the user to type a number with input(), then
# directly join that answer with another string using + (no str()
# needed here!). Add a comment explaining why this works without
# str(), unlike TODO 4.4 above where age needed str() first.
