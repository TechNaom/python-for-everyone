"""
Chapter 12 Practice Bank: Exception Handling
See README.md in this folder for full instructions.

Only uses what Chapters 1-12 covered: print()/input(), variables, basic
types, operators, if/elif/else, while/for/range/break/continue, strings,
lists/tuples, dicts/sets, comprehensions, lambda, map()/filter()/sorted(),
def, *args/**kwargs, scope, recursion, closures, decorators, import x /
from x import y / import x as y / from x import y as z, the math,
datetime, and random modules, and this chapter's own toolkit:
try/except/else/finally, raising exceptions with raise, accessing the
exception object (as e, str(e)), re-raising, and custom exception
classes that subclass Exception. No file I/O, no other class besides a
custom exception subclassing Exception, and no import beyond
math/datetime/random.
"""

import math
import datetime
import random

# ============================================================
# Topic 1: Try/Except Basics
# ============================================================

# TODO 1.1: Write a function safe_int(text) that tries to return
# int(text), and returns None if that raises a ValueError. Call it with
# "42" and with "abc", printing both results.


# TODO 1.2: Write a function safe_divide(a, b) that tries to return
# a / b, catching ZeroDivisionError and returning None instead. Call it
# with (10, 2) and with (10, 0), printing both results.


# TODO 1.3: Write a function safe_list_get(items, index) that tries to
# return items[index], catching IndexError and returning None for an
# out-of-range index. Call it with (["a", "b", "c"], 1) and with
# (["a", "b", "c"], 10), printing both results.


# TODO 1.4: Write a function safe_dict_get(data, key) that tries to
# return data[key], catching KeyError and returning None for a missing
# key. Call it with ({"a": 1, "b": 2}, "a") and with
# ({"a": 1, "b": 2}, "z"), printing both results.


# TODO 1.5 (Debug the Code): this function is supposed to catch a bad
# int conversion and return None, but its except clause catches
# TypeError instead of ValueError, so int("abc") still crashes the
# program with an uncaught ValueError. Fix it by catching ValueError.
def parse_score(text):
    try:
        return int(text)
    except TypeError:
        return None


print(parse_score("abc"))


# TODO 1.A (Scenario -- Validating Form Input): write a function
# parse_age_field(text) that tries to return int(text), catching
# ValueError and returning None instead -- modeling a signup form field
# that must not crash the whole page just because someone typed letters
# into an age box. Call it with "29" and with "twenty-nine", printing
# both results.


# TODO 1.B (Scenario -- Interview Prep): an interviewer asks what
# happens if no exception is raised inside a try block at all. Write a
# function explain_no_exception_case() that returns a string explaining
# that the except block is simply skipped entirely and execution
# continues normally after the try/except -- a try block doesn't slow
# down or change behavior for code that never actually fails. Call it
# and print the result.


# ============================================================
# Topic 2: Multiple Except Blocks, Else, Finally
# ============================================================

# TODO 2.1: Write a function describe_error(a, b) that tries to return
# a / b, with a separate "except ZeroDivisionError" returning
# "cannot divide by zero" and a separate "except TypeError" returning
# "both arguments must be numbers". Call it with (10, 0) and with
# (10, "two"), printing both results.


# TODO 2.2: Write a function divide_with_message(a, b) that uses
# try/except/else: the try computes result = a / b; except
# ZeroDivisionError returns "error: division by zero"; else returns
# f"success: {result}" (the else branch only runs when no error
# occurred). Call it with (10, 2) and with (10, 0), printing both
# results.


# TODO 2.3: Write a function parse_with_finally(text) that uses a list
# attempts = [] declared before the try, tries to return int(text) after
# appending "attempted" to attempts inside a finally block (finally
# always runs, success or failure), and returns None if int() raises
# ValueError. After calling it once with "10" and once with "nope",
# print len(attempts) to prove finally ran both times (declare attempts
# fresh for each call so the counts are 1 each).


# TODO 2.4: Write a function lookup_with_fallback(data, key,
# fallback=None) using try/except/else: the try does
# value = data[key]; except KeyError returns fallback; else returns
# value (only reached when the lookup succeeded). Call it with
# ({"a": 1}, "a", 0) and with ({"a": 1}, "z", 0), printing both results.


# TODO 2.5 (Debug the Code): this function is supposed to catch a
# ZeroDivisionError specifically and fall back to a broader
# "except Exception" for anything else, but the except blocks are
# ordered with the broad "except Exception" FIRST, so the specific
# ZeroDivisionError branch below it can never run (Python matches the
# first except clause that fits). Fix it by putting
# "except ZeroDivisionError" before "except Exception".
def safe_ratio(a, b):
    try:
        return a / b
    except Exception:
        return "unexpected error"
    except ZeroDivisionError:
        return "cannot divide by zero"


print(safe_ratio(10, 0))


# TODO 2.A (Scenario -- Payment Processing Cleanup): write a function
# process_payment(amount) that uses try/except/finally: the try raises
# ValueError if amount <= 0, otherwise returns f"charged ${amount}";
# except ValueError returns "payment failed"; finally always appends
# "cleanup ran" to a list passed in as a mutable default-free local list
# -- instead, have finally simply print("cleanup step complete") so the
# "always runs" behavior is visible regardless of success or failure.
# Call it with 50 and with -10, observing "cleanup step complete" prints
# both times.


# TODO 2.B (Scenario -- Interview Prep): an interviewer asks the
# difference between putting code in an else block versus just leaving
# it at the end of the try block. Write a function
# explain_else_vs_try_tail() that returns a string explaining that code
# in try can accidentally have its own exceptions caught by the except
# blocks below it, while code in else only runs after the try succeeded
# with zero exceptions and any error inside else itself is NOT caught by
# the try's own except blocks -- so else keeps "did it succeed" logic
# clearly separate from "what could fail" logic. Call it and print the
# result.


# ============================================================
# Topic 3: The Exception Object
# ============================================================

# TODO 3.1: Write a function describe_value_error(text) that tries
# int(text), catching "ValueError as e" and returning str(e) (the
# exception's own message). Call it with "notanumber" and print the
# result.


# TODO 3.2: Write a function describe_zero_division(a, b) that tries
# a / b, catching "ZeroDivisionError as e" and returning str(e). Call it
# with (5, 0) and print the result.


# TODO 3.3: Write a function error_type_name(func, *args) that tries
# func(*args), catching "Exception as e" and returning
# type(e).__name__ (the exception class's name as a string) -- if no
# error occurs, return "no error". Call it with
# (lambda a, b: a / b, 5, 0) and print the result.


# TODO 3.4: Write a function safe_key_lookup(data, key) that tries
# data[key], catching "KeyError as e" and returning
# f"missing key: {e}" (str(e) on a KeyError gives back the missing key
# itself). Call it with ({"a": 1}, "z") and print the result.


# TODO 3.5 (Debug the Code): this function is supposed to return a
# helpful message built from the caught exception's own text, but it
# catches the exception "as e" and then never actually uses e anywhere
# in its return value, always returning a generic string instead. Fix it
# by returning f"conversion failed: {e}" so the real error message is
# included.
def parse_with_detail(text):
    try:
        return int(text)
    except ValueError as e:
        return "conversion failed"


print(parse_with_detail("xyz"))


# TODO 3.A (Scenario -- User-Friendly Error Messages): write a function
# friendly_parse_error(text) that tries int(text), catching
# "ValueError as e" and returning
# f"We couldn't read '{text}' as a number ({e})." -- modeling how a real
# app turns a raw Python exception message into something shown safely
# to an end user. Call it with "abc" and print the result.


# TODO 3.B (Scenario -- Interview Prep): an interviewer asks why str(e)
# is more useful to log than just the exception's type name alone.
# Write a function explain_str_e_value() that returns a string
# explaining that type(e).__name__ only tells you *what kind* of failure
# happened (like ValueError), while str(e) carries the actual message
# describing *what specifically* went wrong (like which value couldn't
# convert) -- production logs need both to actually debug an incident
# quickly. Call it and print the result.


# ============================================================
# Topic 4: Raising Exceptions Deliberately
# ============================================================

# TODO 4.1: Write a function require_positive(n) that raises
# ValueError(f"{n} is not positive") if n <= 0, and otherwise returns n.
# Call it inside a try/except that catches ValueError as e and prints
# str(e), passing -5. Also call it directly with 5 and print the result.


# TODO 4.2: Write a function validate_percentage(value) that raises
# ValueError(f"{value} is out of range 0-100") if value is outside
# 0-100 inclusive, and otherwise returns value. Call it inside a
# try/except with 150, printing str(e); also call it directly with 80
# and print the result.


# TODO 4.3: Write a function withdraw(balance, amount) that raises
# ValueError("insufficient funds") if amount > balance, and otherwise
# returns balance - amount. Call it inside a try/except with
# (100, 500), printing str(e); also call it directly with (100, 30) and
# print the result.


# TODO 4.4: Write a function reraise_with_context(func, *args) that
# tries to return func(*args), and if it raises any Exception as e,
# re-raises a new ValueError(f"operation failed: {e}") using
# "raise ValueError(...) from e" (re-raising with added context instead
# of silently hiding the original problem). Call it inside an outer
# try/except that catches ValueError as e and prints str(e), passing
# (lambda: 1 / 0,) as func with no extra args.


# TODO 4.5 (Debug the Code): this function is supposed to guard against
# a negative width by raising a specific, meaningful exception, but it
# raises a bare Exception("bad value") instead of a specific type like
# ValueError, which makes it impossible for calling code to catch just
# this kind of problem without accidentally catching everything else
# too. Fix it by raising ValueError(f"width must be positive, got {width}")
# instead.
def rectangle_area(width, height):
    if width <= 0:
        raise Exception("bad value")
    return width * height


try:
    rectangle_area(-3, 5)
except ValueError as e:
    print(str(e))
except Exception as e:
    print("caught non-specific exception:", str(e))


# TODO 4.A (Scenario -- Input Validation Gate): write a function
# validate_signup_age(age) that raises ValueError(f"age {age} is invalid
# for signup") if age < 13 or age > 120, and otherwise returns age --
# modeling a signup flow that must reject bad ages before any account
# gets created. Call it inside a try/except with 8, printing str(e);
# also call it directly with 25 and print the result.


# TODO 4.B (Scenario -- Interview Prep): an interviewer asks when you'd
# choose to raise an exception instead of silently returning None. Write
# a function explain_raise_vs_none() that returns a string explaining
# that returning None fits situations where "not found" or "no value"
# is a normal, expected outcome the caller should handle quietly, while
# raising fits situations where continuing with bad data would be
# actively dangerous or nonsensical (like a negative withdrawal amount)
# -- raising forces the caller to notice and handle the problem instead
# of letting bad data flow silently downstream. Call it and print the
# result.


# ============================================================
# Topic 5: Custom Exception Classes
# ============================================================

# TODO 5.1: Define a custom exception class InsufficientFundsError that
# subclasses Exception (just "class InsufficientFundsError(Exception):"
# with a "pass" body). Then write a function withdraw_strict(balance,
# amount) that raises
# InsufficientFundsError(f"cannot withdraw {amount}, balance is only
# {balance}") if amount > balance, and otherwise returns
# balance - amount. Call it inside a try/except catching
# InsufficientFundsError as e and printing str(e), passing (100, 500).


# TODO 5.2: Define a custom exception class InvalidAgeError that
# subclasses Exception. Then write a function register_user(name, age)
# that raises InvalidAgeError(f"invalid age: {age}") if age < 0 or
# age > 130, and otherwise returns f"registered {name}, age {age}". Call
# it inside a try/except catching InvalidAgeError as e and printing
# str(e), passing ("Sam", -5).


# TODO 5.3: Write a function custom_error_message(balance, amount) that
# tries withdraw_strict(balance, amount) (reuse your Topic 5 function),
# catching "InsufficientFundsError as e" and returning str(e); if no
# error occurs, return "withdrawal succeeded". Call it with (50, 200)
# and print the result.


# TODO 5.4: Define a custom exception class NegativeValueError that
# subclasses Exception. Then write a function safe_sqrt(n) that raises
# NegativeValueError(f"cannot take sqrt of negative number {n}") if
# n < 0, and otherwise returns math.sqrt(n). Call it inside a
# try/except catching NegativeValueError as e and printing str(e),
# passing -9; also call it directly with 9 and print the result.


# TODO 5.5 (Debug the Code): this custom exception class is supposed to
# work as a normal exception that can be raised and caught, but it
# forgot to subclass Exception entirely (it subclasses nothing, which
# means Python won't allow it to be raised at all -- a TypeError:
# exceptions must derive from BaseException). Fix it by writing
# "class OutOfStockError(Exception):" instead.
class OutOfStockError:
    pass


def check_stock(quantity_available, quantity_requested):
    if quantity_requested > quantity_available:
        raise OutOfStockError(
            f"only {quantity_available} in stock, requested {quantity_requested}"
        )
    return quantity_available - quantity_requested


try:
    check_stock(2, 5)
except OutOfStockError as e:
    print(str(e))
except TypeError as e:
    print("class is not a valid exception type:", str(e))


# TODO 5.A (Scenario -- Domain-Specific Errors in a Banking App): reuse
# InsufficientFundsError from Topic 5. Write a function
# transfer_funds(balance, amount) that raises InsufficientFundsError
# with a clear message if amount > balance, and otherwise returns
# balance - amount -- modeling how a banking app uses a
# domain-specific exception name so any developer reading a stack trace
# immediately understands what went wrong, instead of a generic
# ValueError that could mean anything. Call it inside a try/except
# catching InsufficientFundsError as e and printing str(e), passing
# (200, 1000).


# TODO 5.B (Scenario -- Interview Prep): an interviewer asks why teams
# define custom exception classes instead of always raising a generic
# Exception or ValueError. Write a function
# explain_custom_exception_value() that returns a string explaining
# that a custom exception name is self-documenting (InsufficientFundsError
# says exactly what went wrong at a glance), lets calling code catch
# just that specific problem without accidentally swallowing unrelated
# errors, and still works everywhere a normal exception works since it
# subclasses Exception. Call it and print the result.


# ============================================================
# Topic 6: Bringing It Together -- Exception Handling in Production
# ============================================================

# TODO 6.1: Define a custom exception class ApiError that subclasses
# Exception. Write a function safe_api_response(status_code, payload)
# that: raises ApiError(f"server error {status_code}") if
# status_code >= 500; raises ValueError(f"bad request {status_code}") if
# 400 <= status_code < 500; otherwise returns
# {"ok": True, "data": payload}. Wrap the call in a try/except/else that
# catches ApiError as e returning {"ok": False, "error": "server",
# "detail": str(e)}, catches ValueError as e returning
# {"ok": False, "error": "client", "detail": str(e)}, and put the
# success path in a helper you call directly (since the raising
# function itself already returns the success dict in its non-error
# branch). Build this as one function safe_api_response(status_code,
# payload) that does the try/except itself internally and returns the
# structured dict. Call it with (200, {"id": 1}), with
# (404, {"id": 1}), and with (500, {"id": 1}), printing all three
# results.


# TODO 6.2: Write a function process_order(item_price, quantity,
# discount_percent) that validates all three inputs, raising
# ValueError(f"item_price must be positive, got {item_price}") if
# item_price <= 0, raising ValueError(f"quantity must be positive, got
# {quantity}") if quantity <= 0, and raising
# ValueError(f"discount_percent must be 0-100, got {discount_percent}")
# if discount_percent is outside 0-100 -- otherwise returns
# round(item_price * quantity * (1 - discount_percent / 100), 2). Call
# it inside a try/except catching ValueError as e and printing str(e),
# passing (10, -2, 5); also call it directly with (10, 2, 10) and print
# the result.


# TODO 6.3: Write a function retry_flaky_operation(func, max_attempts=3)
# that loops up to max_attempts times, trying to return func() inside
# each iteration's try, and if it raises any Exception, continues to the
# next attempt (do not re-raise inside the loop) -- if every attempt
# fails, return None after the loop ends. Use a closure counter so a
# deterministic test is possible: build attempts_left = [2] (a
# one-item list acting as a mutable counter) and a function flaky() that
# decrements attempts_left[0] and raises ValueError("not yet") while
# attempts_left[0] > 0, otherwise returns "succeeded". Call
# retry_flaky_operation(flaky) and print the result (should be
# "succeeded" since the 3rd attempt finally works).


# TODO 6.4: Write a function safe_batch_process(items) that loops over
# items, trying int(item) for each one inside a try/except, appending
# successful conversions to a successes list and the failing raw item to
# a failures list when ValueError is caught, and after the loop returns
# a dict {"successes": successes, "failures": failures}. Call it with
# ["1", "2", "abc", "4", "xyz"] and print the result.


# TODO 6.5 (Debug the Code): this function is supposed to validate a
# username and only swallow the *specific* validation error it raises
# itself, but its "except Exception:" is so broad it also silently
# swallows an unrelated bug elsewhere in the function (a NameError from
# a typo'd variable), making that bug invisible instead of surfacing it
# with a traceback. Fix it by catching the specific ValueError it
# actually expects instead of the broad Exception.
def validate_username(username):
    try:
        if len(username) < 3:
            raise ValueError("username too short")
        cleaned = usrname.strip()  # typo'd variable name -- real bug
        return cleaned
    except Exception:
        return None


print(validate_username("abcdef"))


# TODO 6.A (Scenario -- Production-Grade Checkout Validator): define a
# custom exception class CheckoutError that subclasses Exception. Write
# a function validate_checkout(cart_total, payment_amount) that: uses a
# try that raises CheckoutError("cart total must be positive") if
# cart_total <= 0, raises CheckoutError(f"payment {payment_amount} does
# not cover total {cart_total}") if payment_amount < cart_total,
# otherwise computes change = round(payment_amount - cart_total, 2);
# uses except CheckoutError as e to return
# {"ok": False, "error": str(e)}; uses else to return
# {"ok": True, "change": change}; uses finally to print
# "checkout validation complete" (runs regardless of outcome). Call it
# with (50, 20) and with (50, 60), printing both results.


# TODO 6.B (Scenario -- Interview Prep): an interviewer asks why
# catching Exception too broadly is considered a code smell in
# production code. Write a function explain_broad_except_risk() that
# returns a string explaining that a broad "except Exception:" (or
# worse, a bare "except:") can silently swallow completely unrelated
# bugs -- like a typo causing a NameError -- making real problems
# invisible instead of surfacing a traceback that would get noticed and
# fixed; production code should catch the *specific* exception types it
# actually expects and knows how to handle. Call it and print the
# result.
