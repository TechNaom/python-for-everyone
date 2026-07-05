# Chapter 10 Exercises: Functions Deep Dive

These exercises use what Chapter 10 covered: defining functions with
`def`, default arguments, `*args`/`**kwargs`, variable scope and
`global`, recursion, closures with `nonlocal`, and decorators.

## How to run

```bash
python3 starter.py
```

## Task 1 — Defining functions

Find `# TODO 1`. Write a function `calculate_area(width, height)` that
returns the area of a rectangle. Then write a function
`describe_pet(name, species)` that returns a string like `"Rex is a
dog"`. Call both and print the results.

## Task 2 — Default arguments

Find `# TODO 2`. Write a function `make_coffee(size="medium",
extra_shot=False)` that returns a label like `"medium coffee"`, or
`"large coffee with an extra shot"` if `extra_shot` is `True`. Call it
once with no arguments, and once with `"large"` and `True`.

## Task 3 — `*args` and `**kwargs`

Find `# TODO 3`. Write a function `total_cost(*prices)` that returns the
sum of any number of prices, rounded to 2 decimals. Then write a
function `build_order(item, **details)` that returns a dictionary
starting with `{"item": item}` and merges in whatever extra keyword
arguments are passed.

## Task 4 — Scope and `global`

Find `# TODO 4`. Given the module-level variable `visits = 0`, write a
function `record_visit()` that uses the `global` keyword to increment
`visits` by 1 each time it's called. Call it three times and print the
final `visits`.

## Task 5 — Recursion

Find `# TODO 5`. Write a recursive function `countdown(n)` that prints
each number from `n` down to `1`, then prints `"Liftoff!"` — with a
proper base case. Then write a recursive function `sum_to_n(n)` that
returns the sum of every whole number from `1` to `n`.

## Task 6 — Closures

Find `# TODO 6`. Write a function `make_multiplier(factor)` that returns
an inner function `multiply(n)` which returns `n * factor`. Use it to
create a `double` multiplier and a `triple` multiplier, and call both.

## Task 7 — Decorators

Find `# TODO 7`. Write a decorator `shout(func)` whose inner `wrapper`
calls `func` with any arguments it receives, then returns the result
in uppercase with an exclamation point added. Apply it with `@shout` to
a function `greet(name)` that returns `"hi " + name`, and print the
result of calling it.

## Task 8 — Debug the Code

Find `# TODO 8`. This function is supposed to build up a fresh task
list on every call, but it reuses the same list across every call
instead — the classic mutable default argument trap. Find and fix the
bug.

## Task 9 — Bringing it together: login validation helpers

Find `# TODO 9`. Write two small helper functions,
`is_valid_username(username)` (at least 3 characters and alphanumeric)
and `is_valid_pin(pin)` (exactly 4 digits). Then write
`can_log_in(username, pin)`, which returns `True` only if both helpers
pass. Test it with one valid and one invalid login.

## Checking your work

Compare your output against `solution.py`.
