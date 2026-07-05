"""
Chapter 11 Practice Bank: Modules & Packages
See README.md in this folder for full instructions.

Only uses what Chapters 1-11 covered: print()/input(), variables, basic
types, operators, if/elif/else, while/for/range/break/continue, strings,
lists/tuples, dicts/sets, comprehensions, lambda, map()/filter()/sorted(),
def, *args/**kwargs, scope, recursion, closures, decorators, and this
chapter's own toolkit: import x / from x import y / import x as y /
from x import y as z, plus the math, datetime, and random modules. No
try/except, file I/O, classes, or any import beyond math/datetime/random.
"""

import math
import datetime
import random

# ============================================================
# Topic 1: What Is a Module?
# ============================================================

# TODO 1.1: Write a function pi_times_two() that returns math.pi
# multiplied by 2. Call it and print the result.


# TODO 1.2: Write a function describe_module(name, purpose) that returns
# f"The {name} module is useful for {purpose}.". Call it with
# ("math", "numeric calculations") and with
# ("random", "generating randomness"), printing both results.


# TODO 1.3: Write two functions: without_module_pi(), which returns the
# hand-typed literal 3.14159, and with_module_pi(), which returns
# math.pi. Call both and print their results to see the difference in
# precision.


# TODO 1.4: Write a function circle_circumference(radius) that returns
# 2 * math.pi * radius. Call it with 5 and with 1, printing both results.


# TODO 1.5 (Debug the Code): this function is supposed to compute a
# circle's area using math.pi, but it's missing the import statement for
# the math module entirely, so calling it raises a NameError. Fix it by
# adding "import math" at the top of the file (above Topic 1).
def circle_area(radius):
    return math.pi * radius * radius


print(circle_area(3))


# TODO 1.A (Scenario -- Why Real Projects Use Modules): write a function
# explain_module_reuse() that returns a string explaining that a module
# is a single .py file grouping related, tested code so it can be
# imported and reused across many programs instead of rewritten from
# scratch every time -- mention that math, random, and datetime are all
# modules that ship with Python itself. Call it and print the result.


# TODO 1.B (Scenario -- Interview Prep): an interviewer asks why you'd
# import math.pi instead of just typing 3.14159 in your code. Write a
# function why_not_reinvent_pi() that returns a string explaining that
# math.pi gives more decimal precision, is instantly recognizable to
# other Python developers, and can't be mistyped -- reaching for a
# well-tested standard library module beats reinventing something that
# already exists. Call it and print the result.


# ============================================================
# Topic 2: Import Variations
# ============================================================

# TODO 2.1: Using the plain "import math" already at the top of this
# file, write a function sqrt_via_plain_import(n) that returns
# math.sqrt(n). Call it with 16 and print the result.


# TODO 2.2: Add "from math import sqrt" here (above this function), then
# write a function sqrt_via_from_import(n) that returns sqrt(n) directly
# (no math. prefix, since it was imported by name). Call it with 25 and
# print the result.


# TODO 2.3: Add "import math as m" here (above this function), then
# write a function pi_via_aliased_import() that returns m.pi. Call it
# and print the result.


# TODO 2.4: Add "from random import randint as ri" here (above this
# function), then write a function dice_roll_via_aliased_from_import()
# that returns ri(1, 6). Call it, store the result, and print whether it
# falls between 1 and 6 inclusive (since it's random, don't assert an
# exact value).


# TODO 2.5 (Debug the Code): this function is supposed to round 4.1 up
# to 5 using math.ceil, but it calls math.round(n) instead, which doesn't
# exist on the math module (Python's built-in round() is a separate
# global function, not part of math), raising an AttributeError. Fix it
# by calling math.ceil(n) instead.
def ceil_via_plain_import(n):
    return math.round(n)


print(ceil_via_plain_import(4.1))


# TODO 2.A (Scenario -- Picking the Right Import Style): write a function
# compare_import_styles() that returns a string explaining when you'd
# reach for each import style: import math (clearest with many modules
# in a large file), from math import sqrt (shorter for a name used
# constantly), and import math as m / from math import sqrt as
# square_root (renaming for long names or to avoid clashing with an
# existing variable). Call it and print the result.


# TODO 2.B (Scenario -- Interview Prep): an interviewer asks you to
# explain the difference between import x and from x import y. Write a
# function explain_import_variations() that returns a string covering:
# import x loads the whole module so names are reached through x.name;
# from x import y pulls just y into the current namespace directly; and
# the "as" form in either style only renames what was imported, it
# doesn't change what the module contains. Call it and print the result.


# ============================================================
# Topic 3: The math Module
# ============================================================

# TODO 3.1: Write a function hypotenuse(a, b) that returns the length of
# the hypotenuse of a right triangle with legs a and b, using
# math.sqrt(a ** 2 + b ** 2). Call it with (3, 4) and print the result.


# TODO 3.2: Write a function round_down_and_up(n) that returns a tuple
# (math.floor(n), math.ceil(n)). Call it with 4.3 and with 4.7, printing
# both results.


# TODO 3.3: Write a function power_of(base, exponent) that returns
# math.pow(base, exponent). Call it with (2, 10) and print the result.


# TODO 3.4: Write a function circle_area(radius) that returns
# math.pi * radius ** 2. Call it with 2, round the result to 2 decimal
# places with round(), and print it.


# TODO 3.5 (Debug the Code): this function is supposed to calculate how
# many containers are needed to hold total_items at capacity items each,
# rounding *up* so leftover items still get their own container, but it
# uses math.floor instead of math.ceil, so it silently loses any leftover
# items. Fix it by switching to math.ceil.
def containers_needed(total_items, capacity):
    return math.floor(total_items / capacity)


print(containers_needed(23, 5))


# TODO 3.A (Scenario -- Shipping Box Calculator): write a function
# boxes_required(num_items, items_per_box) that returns
# math.ceil(num_items / items_per_box) -- a warehouse needs a whole
# number of boxes, rounding up for any partial box. Call it with
# (100, 12) and with (12, 12), printing both results.


# TODO 3.B (Scenario -- Interview Prep): an interviewer asks you to
# explain the difference between math.floor, math.ceil, and the built-in
# round(). Write a function explain_floor_vs_ceil_vs_round() that
# returns a string covering: floor always rounds down, ceil always
# rounds up, and round() rounds to the *nearest* value (so it can go
# either direction depending on the fractional part) -- illustrate with
# floor(4.1) == 4, ceil(4.1) == 5, round(4.1) == 4, round(4.6) == 5.
# Call it and print the result.


# ============================================================
# Topic 4: The datetime Module
# ============================================================

# TODO 4.1: Write a function make_date(year, month, day) that returns
# datetime.date(year, month, day). Call it with (2026, 7, 5), store it in
# launch_date, and print it.


# TODO 4.2: Write a function format_date_long(a_date) that returns
# a_date.strftime("%B %d, %Y") (a long human-readable format like
# "July 05, 2026"). Call it with datetime.date(2026, 7, 5) and print the
# result.


# TODO 4.3: Write a function days_between(date_a, date_b) that returns
# (date_b - date_a).days. Call it with
# (datetime.date(2026, 1, 1), datetime.date(2026, 7, 5)) and print the
# result.


# TODO 4.4: Write a function days_since_today() that gets today's date
# with datetime.date.today(), then returns (today - today).days (which
# will always be 0, proving the subtraction works). Call it and print
# the result.


# TODO 4.5 (Debug the Code): this function is supposed to return how
# many days remain until a deadline (a positive number for a future
# date), but it subtracts the deadline from today instead of today from
# the deadline, so a future deadline gives back a *negative* number
# instead of positive. Fix it by returning (deadline - today).days
# instead of (today - deadline).days.
def days_until_deadline(deadline):
    today = datetime.date.today()
    return (today - deadline).days


print(days_until_deadline(datetime.date(2027, 1, 1)) >= 0)


# TODO 4.A (Scenario -- Subscription Renewal Countdown): write a function
# days_until_renewal(signup_date, renewal_days=365) that returns
# (renewal_date - signup_date).days, where renewal_date is
# signup_date + datetime.timedelta(days=renewal_days). Call it with just
# a signup_date, then again passing renewal_days=30, printing both
# results.


# TODO 4.B (Scenario -- Interview Prep): an interviewer asks how date
# subtraction works in Python. Write a function explain_date_arithmetic()
# that returns a string explaining that subtracting one datetime.date
# from another gives back a timedelta object (not a plain number), and
# that timedelta's .days attribute is the whole number of days between
# them -- and that adding a timedelta (not a raw int) to a date shifts it
# forward or backward. Call it and print the result.


# ============================================================
# Topic 5: The random Module
# ============================================================

# TODO 5.1: Write a function roll_die() that returns
# random.randint(1, 6). Call it, store the result, and print whether it
# falls between 1 and 6 inclusive (since it's random, don't assert an
# exact value).


# TODO 5.2: Write a function pick_random_name(names) that returns
# random.choice(names). Call it with team = ["Asha", "Ravi", "Meera"],
# store the result, and print whether the picked name is in team.


# TODO 5.3: Write a function shuffled_copy(items) that makes a copy of
# items with items[:], shuffles the copy in place with random.shuffle(),
# and returns the shuffled copy (leaving the original list untouched).
# Call it with original = [1, 2, 3, 4, 5], then print whether
# sorted(shuffled) == sorted(original) (proving no elements were lost or
# added), and print original afterward to show it wasn't mutated.


# TODO 5.4: Write a function random_percentage() that returns
# random.randint(0, 100). Call it, store the result, and print whether
# it falls between 0 and 100 inclusive.


# TODO 5.5 (Debug the Code): this function is supposed to pick a random
# card from a list using random.choice(cards), but it calls
# random.choice() with no arguments at all, raising a TypeError. Fix it
# by passing cards into random.choice(cards).
def pick_a_card(cards):
    return random.choice()


deck = ["Ace", "King", "Queen", "Jack"]
card = pick_a_card(deck)
print(card in deck)


# TODO 5.A (Scenario -- Randomized A/B Test Assignment): write a function
# assign_ab_group() that returns random.choice(["A", "B"]) -- modeling
# how a real feature-flag system randomly assigns each user to a test
# group. Call it, store the result, and print whether it's "A" or "B".


# TODO 5.B (Scenario -- Interview Prep): an interviewer asks why you
# can't write a normal assert-exact-value test for code that calls
# random.randint or random.choice. Write a function
# explain_random_vs_deterministic() that returns a string explaining that
# these functions rely on a pseudo-random number generator, so their
# exact output differs on every run -- meaning tests should check a
# *property* of the result (like "is it in range" or "does it still
# contain the same elements") instead of one exact value. Call it and
# print the result.


# ============================================================
# Topic 6: Bringing It Together -- Modules in Production
# ============================================================

# TODO 6.1: Write a function generate_order_id(order_number) that gets
# today's date string with datetime.date.today().strftime("%Y%m%d"), then
# returns f"ORD-{today_str}-{order_number:04d}" (zero-padded to 4 digits).
# Call it with 7 and print the result.


# TODO 6.2: Write a function distance_between_points(x1, y1, x2, y2) that
# returns math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2). Call it with
# (0, 0, 3, 4) and print the result.


# TODO 6.3: Write a function pick_daily_special(menu_items) that returns
# random.choice(menu_items). Call it with
# menu = ["Pasta", "Salad", "Soup", "Sandwich"], store the result, and
# print whether it's in menu.


# TODO 6.4: Write a function subscription_status(start_date,
# length_days=30) that computes end_date as
# start_date + datetime.timedelta(days=length_days), gets today with
# datetime.date.today(), and returns "active" if today <= end_date else
# "expired". Call it with datetime.date(2020, 1, 1) and print the result.


# TODO 6.5 (Debug the Code): this function is supposed to apply a random
# discount percent to a price and return the discounted price rounded to
# 2 decimals, but it adds the discount instead of subtracting it, so the
# "discounted" price actually comes out *higher* than the original. Fix
# it so discounted is price - price * discount_percent / 100 instead of
# price + price * discount_percent / 100.
def price_after_random_discount(price, discount_percent):
    discounted = price + price * discount_percent / 100
    return round(discounted, 2)


final_price = price_after_random_discount(200, random.randint(5, 25))
print(final_price < 200)


# TODO 6.A (Scenario -- Production Order Confirmation Builder): write a
# function build_order_confirmation(order_number, price_per_item,
# quantity) that: computes total as round(price_per_item * quantity, 2);
# builds order_id by calling generate_order_id(order_number) (reuse your
# Topic 6 function above); computes processing_days as
# math.ceil(quantity / 10); computes ship_by as
# datetime.date.today() + datetime.timedelta(days=processing_days); and
# returns a dict with keys "order_id", "total", and "ship_by" (the
# ship_by date formatted with .strftime("%Y-%m-%d") so it's a plain
# string). Call it with (42, 9.99, 23) and print the order_id, the
# total, and whether "ship_by" is a key in the result.


# TODO 6.B (Scenario -- Interview Prep): an interviewer asks how the
# standard library shows up in real production code. Write a function
# explain_stdlib_value() that returns a string covering: math for
# pricing/geometry/rounding logic, datetime for order
# timestamps/subscription windows/deadlines, and random for A/B test
# assignment/sampling/generating test data -- and that using the
# standard library instead of hand-rolling this logic means fewer bugs
# (since it's already tested by millions of other programs) and instant
# recognition by any other Python developer. Call it and print the
# result.
