"""
Chapter 11 Exercises: Modules & Packages — reference solution.
"""

import math
import datetime
import random

# TODO 1: Import the math module. Write a function hypotenuse(a, b) that
# returns the length of a right triangle's hypotenuse, using
# math.sqrt(a ** 2 + b ** 2). Call it with 3 and 4 and print the result.
def hypotenuse(a, b):
    return math.sqrt(a ** 2 + b ** 2)

print(hypotenuse(3, 4))


# TODO 2: Using "from math import ceil, floor", write a function
# billing_and_stock(actual_weight, egg_count) that returns a tuple of
# (ceil(actual_weight), floor(egg_count / 12)). Call it with 3.2 and 50
# and print the result.
from math import ceil, floor

def billing_and_stock(actual_weight, egg_count):
    return (ceil(actual_weight), floor(egg_count / 12))

print(billing_and_stock(3.2, 50))


# TODO 3: Write a function circle_area(radius) that returns
# math.pi * radius ** 2, rounded to 2 decimals. Call it with 5 and print
# the result.
def circle_area(radius):
    return round(math.pi * radius ** 2, 2)

print(circle_area(5))


# TODO 4: Using the datetime module, write a function
# days_until(target_date, from_date) that returns
# (target_date - from_date).days. Call it with datetime.date(2026, 12, 25)
# as the target and datetime.date(2026, 7, 5) as the "from" date, and
# print the result.
def days_until(target_date, from_date):
    return (target_date - from_date).days

print(days_until(datetime.date(2026, 12, 25), datetime.date(2026, 7, 5)))


# TODO 5: Write a function format_nicely(a_date) that returns
# a_date.strftime("%B %d, %Y"). Call it with datetime.date(2026, 3, 15)
# and print the result.
def format_nicely(a_date):
    return a_date.strftime("%B %d, %Y")

print(format_nicely(datetime.date(2026, 3, 15)))


# TODO 6: Write a function roll_dice(sides=6) that returns
# random.randint(1, sides). Then write a function pick_winner(names)
# that returns random.choice(names). Call roll_dice() once and
# pick_winner(["Priya", "Amir", "Zoe"]) once, and print both results
# (your output will be different every run — that's expected).
def roll_dice(sides=6):
    return random.randint(1, sides)

def pick_winner(names):
    return random.choice(names)

print(roll_dice())
print(pick_winner(["Priya", "Amir", "Zoe"]))


# TODO 7 (Debug the Code): this code tries to use sqrt directly without
# importing it correctly, and raises a NameError. Find and fix the bug.
# Bug: "import math" only defines math.sqrt, not a bare sqrt name.
# Fix: either call math.sqrt(25), or import sqrt directly from math.
print(math.sqrt(25))


# TODO 8: Write a function build_confirmation(item, price, order_date)
# that: rounds price up to a whole number with math.ceil, computes a
# delivery date 5 days after order_date using datetime.timedelta(days=5),
# and returns a string like "Desk Lamp confirmed at $25 — arriving by
# July 10, 2026" (use strftime("%B %d, %Y") for the delivery date). Call
# it with "Desk Lamp", 24.10, and datetime.date(2026, 7, 5), and print
# the result.
def build_confirmation(item, price, order_date):
    rounded_price = math.ceil(price)
    delivery_date = order_date + datetime.timedelta(days=5)
    return (
        item
        + " confirmed at $"
        + str(rounded_price)
        + " — arriving by "
        + delivery_date.strftime("%B %d, %Y")
    )

print(build_confirmation("Desk Lamp", 24.10, datetime.date(2026, 7, 5)))
