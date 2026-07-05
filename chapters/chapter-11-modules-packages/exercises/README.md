# Chapter 11 Exercises: Modules & Packages

These exercises use what Chapter 11 covered: what a module is, the
`import` variations (`import x`, `from x import y`, `import x as y`,
`from x import y as z`), and three standard-library modules — `math`,
`datetime`, and `random`.

## How to run

```bash
python3 starter.py
```

## Task 1 — Importing the math module

Find `# TODO 1`. Import the `math` module. Write a function
`hypotenuse(a, b)` that returns the length of a right triangle's
hypotenuse, using `math.sqrt(a ** 2 + b ** 2)`. Call it with `3` and `4`
and print the result.

## Task 2 — Import variations

Find `# TODO 2`. Using `from math import ceil, floor`, write a function
`billing_and_stock(actual_weight, egg_count)` that returns a tuple of
`(ceil(actual_weight), floor(egg_count / 12))`. Call it with `3.2` and
`50` and print the result.

## Task 3 — The math module

Find `# TODO 3`. Write a function `circle_area(radius)` that returns
`math.pi * radius ** 2`, rounded to 2 decimals. Call it with `5` and
print the result.

## Task 4 — The datetime module

Find `# TODO 4`. Using the `datetime` module, write a function
`days_until(target_date, from_date)` that returns `(target_date -
from_date).days`. Call it with `datetime.date(2026, 12, 25)` as the
target and `datetime.date(2026, 7, 5)` as the "from" date, and print the
result.

## Task 5 — Formatting dates with strftime

Find `# TODO 5`. Write a function `format_nicely(a_date)` that returns
`a_date.strftime("%B %d, %Y")`. Call it with `datetime.date(2026, 3,
15)` and print the result.

## Task 6 — The random module

Find `# TODO 6`. Write a function `roll_dice(sides=6)` that returns
`random.randint(1, sides)`. Then write a function `pick_winner(names)`
that returns `random.choice(names)`. Call `roll_dice()` once and
`pick_winner(["Priya", "Amir", "Zoe"])` once, and print both results
(your output will be different every run — that's expected).

## Task 7 — Debug the Code

Find `# TODO 7`. This code tries to use `sqrt` directly without
importing it correctly, and raises a `NameError`. Find and fix the bug.

## Task 8 — Bringing it together: order confirmation

Find `# TODO 8`. Write a function `build_confirmation(item, price,
order_date)` that: rounds `price` up to a whole number with
`math.ceil`, computes a delivery date 5 days after `order_date` using
`datetime.timedelta(days=5)`, and returns a string like `"Desk Lamp
confirmed at $25 — arriving by July 10, 2026"` (use `strftime("%B %d,
%Y")` for the delivery date). Call it with `"Desk Lamp"`, `24.10`, and
`datetime.date(2026, 7, 5)`, and print the result.

## Checking your work

Compare your output against `solution.py`. Note: your own system clock
isn't used anywhere in these exercises — every date is built explicitly
with `datetime.date(...)`, so your output should match `solution.py`
exactly, except for Task 6's random results.
