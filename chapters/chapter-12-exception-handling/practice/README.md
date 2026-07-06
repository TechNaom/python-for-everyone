# Chapter 12 Practice Bank: Exception Handling

A deeper set of practice problems, organized by topic, on top of the
main `exercises/` folder — including scenario-based problems written
in the same style you'll see in real interviews. Uses everything from
Chapters 1-11 plus this chapter's own toolkit: `try`/`except`/`else`/
`finally`, accessing the exception object (`as e`, `str(e)`), `raise`
(including re-raising), and custom exception classes that subclass
`Exception`. No file I/O (that's Chapter 13), no other class besides a
custom exception subclassing `Exception` (that's Chapter 14), and no
import beyond `math`/`datetime`/`random`.

Note: any problem involving `random` or `datetime.date.today()` has
output that's different every time you run it (that's the whole point
of "random") — the solution checks a *property* of the result instead
of one exact value, so don't worry if your printed output doesn't match
someone else's.

## How to run

```bash
python3 starter.py
```

## Topic 1: Try/Except Basics

1. Write `safe_int(text)`, converting `text` to an `int` inside a `try`, returning `None` if it fails.
2. Write `safe_divide(a, b)`, returning `a / b` inside a `try`, catching `ZeroDivisionError` and returning `None`.
3. Write `safe_list_get(items, index)`, catching `IndexError` and returning `None` for an out-of-range index.
4. Write `safe_dict_get(data, key)`, catching `KeyError` and returning `None` for a missing key.
5. **Debug the Code:** fix a function whose `except` clause never matches because it's built to catch the wrong exception type.
6. **Scenario — Validating Form Input:** write `parse_age_field(text)` for a signup form that must not crash on bad input.
7. **Scenario — Interview Prep:** explain what happens if no exception is raised inside a `try` block at all.

## Topic 2: Multiple Except Blocks, Else, Finally

1. Write `describe_error(a, b)`, using separate `except ZeroDivisionError` and `except TypeError` blocks.
2. Write `divide_with_message(a, b)`, using `try`/`except`/`else` so the "success" print only happens when no error occurred.
3. Write `parse_with_finally(text)`, using a `finally` block that always increments an attempt counter.
4. Write `lookup_with_fallback(data, key)`, combining `except` and `else` to return a fallback only when no error occurred.
5. **Debug the Code:** fix a function whose `except` blocks are ordered so a more specific exception is never reached.
6. **Scenario — Payment Processing Cleanup:** write `process_payment(amount)` that always logs a "cleanup" step in `finally` regardless of success or failure.
7. **Scenario — Interview Prep:** explain the difference between putting code in `else` versus just leaving it at the end of `try`.

## Topic 3: The Exception Object

1. Write `describe_value_error(text)`, catching `ValueError as e` and returning `str(e)`.
2. Write `describe_zero_division(a, b)`, catching `ZeroDivisionError as e` and returning `str(e)`.
3. Write `error_type_name(func, *args)`, catching any `Exception as e` and returning `type(e).__name__`.
4. Write `safe_key_lookup(data, key)`, catching `KeyError as e` and returning a formatted string using `str(e)`.
5. **Debug the Code:** fix a function that catches the exception with `as e` but never actually uses `e` where the message needs it.
6. **Scenario — User-Friendly Error Messages:** write `friendly_parse_error(text)` that turns a raw `ValueError` message into a message a non-technical user could read.
7. **Scenario — Interview Prep:** explain why `str(e)` is more useful to log than just the exception's type name alone.

## Topic 4: Raising Exceptions Deliberately

1. Write `require_positive(n)`, raising `ValueError` with a message if `n` is not positive.
2. Write `validate_percentage(value)`, raising `ValueError` if `value` is outside 0-100.
3. Write `withdraw(balance, amount)`, raising `ValueError` if `amount` exceeds `balance`.
4. Write `reraise_with_context(func, *args)`, catching an exception, then re-raising it after adding context.
5. **Debug the Code:** fix a function that raises a bare `Exception("...")` instead of a specific, meaningful exception type.
6. **Scenario — Input Validation Gate:** write `validate_signup_age(age)` for a signup flow that must raise on invalid ages before any account gets created.
7. **Scenario — Interview Prep:** explain when you'd choose to `raise` instead of silently returning `None`.

## Topic 5: Custom Exception Classes

1. Define `class InsufficientFundsError(Exception)` and write `withdraw_strict(balance, amount)`, raising it when funds are short.
2. Define `class InvalidAgeError(Exception)` and write `register_user(age)`, raising it for an invalid age.
3. Write `custom_error_message(balance, amount)`, catching your own `InsufficientFundsError as e` and returning `str(e)`.
4. Define `class NegativeValueError(Exception)` and write `safe_sqrt(n)`, raising it for a negative input.
5. **Debug the Code:** fix a custom exception class that forgot to subclass `Exception` at all.
6. **Scenario — Domain-Specific Errors in a Banking App:** write `transfer_funds(balance, amount)` using `InsufficientFundsError` to make the failure self-documenting.
7. **Scenario — Interview Prep:** explain why teams define custom exception classes instead of always raising a generic `Exception` or `ValueError`.

## Topic 6: Bringing It Together — Exception Handling in Production

1. Write `safe_api_response(status_code, payload)`, combining multiple `except` blocks and a custom exception to return a structured result dict.
2. Write `process_order(item_price, quantity, discount_percent)`, validating every input and raising specific exceptions for each bad case.
3. Write `retry_flaky_operation(func, max_attempts=3)`, retrying a function that might raise, and returning whether it eventually succeeded.
4. Write `safe_batch_process(items)`, processing a list of inputs where some may fail, collecting successes and failures separately.
5. **Debug the Code:** fix a function whose broad `except Exception:` silently swallows an error instead of surfacing it usefully.
6. **Scenario — Production-Grade Checkout Validator:** write `validate_checkout(cart_total, payment_amount)` combining custom exceptions, `finally` logging, and a structured return value.
7. **Scenario — Interview Prep:** explain why catching `Exception` too broadly is considered a code smell in production code.

## Checking your work

Compare your output against `solution.py`. Your exact wording doesn't
need to match — the goal is that your program runs without errors and
does what each TODO asks. Remember that any random or "today's date"
output will legitimately differ each time you run it.
