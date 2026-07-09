# Chapter 26 Exercises: Debugging Production Issues (Categories 1-8)

These exercises use what all eight categories covered: `KeyError`,
`IndexError`, bare `except:` vs. specific exceptions, `TypeError` from
unvalidated input, `AttributeError` from an implicit `None` return,
`ZeroDivisionError`, `json.JSONDecodeError`, quadratic membership
checks, dict-based indexing, avoiding unnecessary full-list sorts
(Tasks 1-14, Categories 1-2), plus bounded collections, mutable class
attributes, shallow vs. deep copy, float comparison, integer rounding,
pagination off-by-one errors, dict key order, environment variable
validation, idempotent retries, avoiding N+1 lookups, structured
logging, and redacting sensitive fields before logging (Tasks 15-26,
Categories 3-8). Every task here uses only the standard library -- no
installs needed.

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

## Task 9 — Checking for a duplicate with a set

Find `# TODO 9`. Write `has_duplicate(items)` — return `True` if any
value appears more than once, using a set for the membership check.

## Task 10 — Deduplicating while preserving order

Find `# TODO 10`. Write `dedupe_preserve_order(items)` — remove
duplicates, keeping only the first occurrence of each value, using a
set to track what's been seen.

## Task 11 — Indexing records by key

Find `# TODO 11`. Write `index_by_key(records, key_name)` — build a
dict mapping each record's key value to the record itself.

## Task 12 — Min and max without sorting

Find `# TODO 12`. Write `smallest_and_largest(numbers)` — return
`(min(numbers), max(numbers))` without calling `sorted()`.

## Task 13 — Stopping at the first match

Find `# TODO 13`. Write `first_match_or_none(items, predicate)` —
return the first item where `predicate(item)` is `True`, stopping
immediately once found.

## Task 14 — Debug the Code

Find `# TODO 14`. `reversed_list()` uses `list.insert(0, x)` in a
loop, which is O(n) per call. Fix it to use `.append()` followed by
one `.reverse()` call instead.

## Task 15 — Bounding a "recent" collection

Find `# TODO 15`. Write `bounded_recent_events(events, maxlen)` — use
`collections.deque(maxlen=maxlen)` so the result never holds more than
`maxlen` items, no matter how large `events` is.

## Task 16 — Debug the Code

Find `# TODO 16`. `SharedCounter` uses a class-level `count = []`,
which is shared by every instance instead of being per-instance. Fix
it by creating `self.count = []` inside `__init__`.

## Task 17 — Deep copy for real independence

Find `# TODO 17`. Write `independent_copy(original)` — use
`copy.deepcopy()` so mutating a nested list/dict on the copy never
affects the original.

## Task 18 — Comparing floats safely

Find `# TODO 18`. Write `floats_equal(a, b)` — use `math.isclose()`,
never a plain `==`, since floating-point arithmetic accumulates
rounding error.

## Task 19 — Rounding instead of truncating

Find `# TODO 19`. Write `round_quantity(value)` — use `round()`, not
`int()`, which silently truncates toward zero instead of rounding.

## Task 20 — Debug the Code

Find `# TODO 20`. `get_page()` treats a 1-based `page_number` as if it
were already a 0-based offset, silently dropping the first page's
records. Fix it to convert with `(page_number - 1) * page_size`.

## Task 21 — Never rely on dict key order

Find `# TODO 21`. Write `row_from_fixed_columns(record, column_order)`
— look up each value by `column_order`'s order, never a dict's own key
insertion order.

## Task 22 — Missing environment variables, all at once

Find `# TODO 22`. Write `missing_env_keys(env, required_keys)` —
return a sorted list of every required key that's missing, the
env-var version of Task 1's `KeyError` fix.

## Task 23 — A safe retry with an idempotency key

Find `# TODO 23`. Write `charge_once(processed, idempotency_key,
amount)` — a retried call with the same key returns the original
result instead of charging twice.

## Task 24 — Avoiding the N+1 pattern

Find `# TODO 24`. Write `attach_names(records, lookup_table)` — build
the lookup once, up front, instead of scanning a second list per
record.

## Task 25 — Structured, not free-text, logging

Find `# TODO 25`. Write `build_log_record(order_id, amount, status)`
— return a dict with named fields, not a formatted string, so a log
aggregator can query it directly.

## Task 26 — Debug the Code

Find `# TODO 26`. `redact_password()` builds a redacted copy but
returns the original `request` dict by mistake, leaking the password.
Fix it to return `redacted` instead.

## Checking your work

Compare your output against `solution.py`. Your exact wording doesn't
need to match on `find_user_or_raise`'s error message — the goal is
that your program runs without errors and does what each TODO asks.
