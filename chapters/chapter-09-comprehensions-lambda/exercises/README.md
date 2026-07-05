# Chapter 9 Exercises: Comprehensions, Lambda & Functional Tools

These exercises use what Chapter 9 covered: list comprehensions, dict &
set comprehensions, nested comprehensions, lambda functions, and
functional tools (`map()`, `filter()`, `sorted()`/`.sort()` with `key=`).

## How to run

```bash
python3 starter.py
```

## Task 1 — List comprehensions

Find `# TODO 1`. Given `numbers = [3, 8, 12, 15, 20, 27]`, build a list
comprehension that squares every number. Then build a second list
comprehension that keeps only the numbers greater than 10.

## Task 2 — Dict & set comprehensions

Find `# TODO 2`. Given `inventory_prices = {"pens": 1.50, "notebooks":
3.00, "erasers": 0.75}`, build a dict comprehension that adds 7% tax to
every price, rounded to 2 decimal places. Then given
`tags = ["sale", "new", "sale", "clearance", "new"]`, build a set
comprehension of the unique tags.

## Task 3 — Nested comprehensions

Find `# TODO 3`. Given a nested `seating_chart` (a list of rows, each row
a list of names), use a nested comprehension to flatten it into one list
of every student's name.

## Task 4 — Lambda

Find `# TODO 4`. Write a lambda called `to_fahrenheit` that converts a
Celsius value to Fahrenheit, rounded to 1 decimal place:
`F = C * 9 / 5 + 32`. Call it with `20` and with `0`.

## Task 5 — Functional tools

Find `# TODO 5`. Given `order_totals = [45.00, 12.50, 99.99, 8.25]`, use
`map()` with a lambda to apply a 10% discount (rounded to 2 decimals) to
every total. Then use `filter()` with a lambda to keep only totals over
`20`. Finally, given a list of `employees` (each a dictionary with
`"name"` and `"salary"`), use `sorted()` with a lambda key to sort the
list by salary.

## Task 6 — Debug the Code

Find `# TODO 6`. This is supposed to keep only the scores that pass with
a score *strictly greater than* 60, but it wrongly includes the boundary
value 60 itself. Find and fix the off-by-one bug in the filter condition.

## Task 7 — Cleaning, filtering & ranking feedback

Find `# TODO 7`. Given a list of raw feedback entries (each a dictionary
with `"comment"` and `"rating"`), clean every comment by stripping
whitespace. Then filter the list down to only entries with a valid
(digit) rating, and print each remaining comment with its rating, ranked
from highest rating to lowest.

## Checking your work

Compare your output against `solution.py`.
