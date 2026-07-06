# Chapter 12 Exercises: Exception Handling

These exercises use what Chapter 12 covered: `try`/`except` basics,
multiple `except` blocks with `else` and `finally`, accessing the
exception object with `as e`, raising exceptions with `raise`, and
defining a custom exception class.

## How to run

```bash
python3 starter.py
```

## Task 1 — try/except basics

Find `# TODO 1`. Write a function `parse_quantity(text)` that returns
`int(text)`, but catches a `ValueError` — printing `"Not a valid
quantity:"` followed by `repr(text)`, and returning `None`. Call it with
`"5"` and with `"five"` and print both results.

## Task 2 — else and finally

Find `# TODO 2`. Write a function `safe_average(numbers)` that computes
`sum(numbers) / len(numbers)` inside a `try`. Catch `ZeroDivisionError`
and print `"Can't average an empty list."`. In an `else` block, print
`"Average:"` followed by the result. In a `finally` block, print
`"Average check done."` Call it with `[10, 20, 30]` and with `[]`.

## Task 3 — Accessing the exception object

Find `# TODO 3`. Write a function `parse_price(text)` that returns
`float(text)`, catching a `ValueError as e` and printing `"Could not
parse price:"` followed by `str(e)`, then returning `None`. Call it
with `"19.99"` and with `"free"`.

## Task 4 — Raising exceptions deliberately

Find `# TODO 4`. Write a function `set_quantity(qty)` that raises a
`ValueError("quantity must be at least 1")` if `qty < 1`, otherwise
returns `qty`. Call it with `0` inside a `try`/`except ValueError as e`
that prints `"Rejected:"` followed by `e`.

## Task 5 — Custom exception classes

Find `# TODO 5`. Define `class OutOfStockError(Exception): pass`. Write
a function `place_order(stock, requested)` that raises an
`OutOfStockError` with the message `f"Only {stock} left, requested
{requested}"` if `requested > stock`, otherwise returns `stock -
requested`. Call it with `stock=3, requested=5` inside a
`try`/`except OutOfStockError as e` that prints `"Order failed:"`
followed by `e`.

## Task 6 — Bringing it together: checkout flow

Find `# TODO 6`. Write a function `checkout(stock, requested)` that
calls `place_order(stock, requested)` inside a `try`. On
`OutOfStockError as e`, print `"Checkout failed:"` followed by `e` and
return `None`. In `else`, print `"Checkout succeeded, remaining
stock:"` followed by the result, and return it. In `finally`, print
`"Checkout attempt logged."` Call it with `(10, 3)` and then `(10,
20)`.

## Task 7 — Debug the Code

Find `# TODO 7`. This code uses a bare `except:` that hides a real bug
— a typo'd variable name inside the `try` block silently prints
"Something went wrong" instead of surfacing the actual `NameError`.
Find and fix the bug so the typo is visible and the working code still
runs correctly.

## Task 8 — Debug the Code: wrong except order

Find `# TODO 8`. This code has its `except` blocks in the wrong order,
so a more specific exception can never be reached — a broader
exception type earlier in the chain catches it first. Find and fix the
ordering.

## Checking your work

Compare your output against `solution.py`. Every example here uses
fixed, explicit values, so your output should match `solution.py`
exactly.
