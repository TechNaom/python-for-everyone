# Chapter 26 Exercises: Debugging Production Issues (Category 1)

These exercises use what Category 1 covered: `KeyError`, `IndexError`,
bare `except:` vs. specific exceptions, `TypeError` from unvalidated
input, `AttributeError` from an implicit `None` return,
`ZeroDivisionError`, and `json.JSONDecodeError`. Every task here uses
only the standard library -- no installs needed.

## How to run

Run this **from inside this `exercises/` folder**:

```bash
cd exercises
python3 starter.py
```

## Task 1 — A safe dict lookup

Find `# TODO 1`. Write `safe_lookup(config, key, default)` — return
`config[key]` if present, otherwise `default`, never raising
`KeyError`.

## Task 2 — A safe top-N sum

Find `# TODO 2`. Write `safe_top_n(scores, n)` — sum the first `n`
items without ever indexing past the end of the list.

## Task 3 — Catching the specific exception, not a bare except

Find `# TODO 3`. Write `safe_int_lookup(raw, key, default)` — catch
only `KeyError`, not a bare `except:`.

## Task 4 — Validating input before arithmetic

Find `# TODO 4`. Write `safe_discount(price, percent_off)` — convert
`percent_off` to a float before using it, so it works whether it
arrives as a string or a number.

## Task 5 — Raising instead of implicitly returning None

Find `# TODO 5`. Write `find_user_or_raise(users, name)` — raise a
clear `ValueError` instead of implicitly returning `None` when no
match is found.

## Task 6 — Handling a zero denominator

Find `# TODO 6`. Write `average_or_none(total, count)` — return `None`
instead of crashing when `count` is 0.

## Task 7 — Handling a non-JSON response

Find `# TODO 7`. Write `parse_json_safe(raw_text)` — catch
`json.JSONDecodeError` specifically and return `None` for invalid
JSON.

## Task 8 — Debug the Code

Find `# TODO 8`. `load_timeout()` uses a bare `except:` that hides a
real typo (`"timeoout"` instead of `"timeout"`) in the config dict.
Fix the `except` clause to catch only `KeyError`.

## Checking your work

Compare your output against `solution.py`. Your exact wording doesn't
need to match on `find_user_or_raise`'s error message — the goal is
that your program runs without errors and does what each TODO asks.
