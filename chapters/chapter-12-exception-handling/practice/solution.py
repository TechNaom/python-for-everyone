"""
Chapter 12 Practice Bank: Exception Handling -- reference solution.
See README.md in this folder for full instructions.
"""

import math
import datetime
import random

# ============================================================
# Topic 1: Try/Except Basics
# ============================================================

# TODO 1.1
def safe_int(text):
    try:
        return int(text)
    except ValueError:
        return None


print(safe_int("42"))
print(safe_int("abc"))


# TODO 1.2
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None


print(safe_divide(10, 2))
print(safe_divide(10, 0))


# TODO 1.3
def safe_list_get(items, index):
    try:
        return items[index]
    except IndexError:
        return None


print(safe_list_get(["a", "b", "c"], 1))
print(safe_list_get(["a", "b", "c"], 10))


# TODO 1.4
def safe_dict_get(data, key):
    try:
        return data[key]
    except KeyError:
        return None


print(safe_dict_get({"a": 1, "b": 2}, "a"))
print(safe_dict_get({"a": 1, "b": 2}, "z"))


# TODO 1.5 (Debug the Code)
def parse_score(text):
    try:
        return int(text)
    except ValueError:
        return None


print(parse_score("abc"))


# TODO 1.A (Scenario -- Validating Form Input)
def parse_age_field(text):
    try:
        return int(text)
    except ValueError:
        return None


print(parse_age_field("29"))
print(parse_age_field("twenty-nine"))


# TODO 1.B (Scenario -- Interview Prep)
def explain_no_exception_case():
    return (
        "If no exception is raised inside a try block, the except block is "
        "simply skipped entirely and execution continues normally right "
        "after the try/except -- a try block doesn't slow down or change "
        "the behavior of code that never actually fails."
    )


print(explain_no_exception_case())


# ============================================================
# Topic 2: Multiple Except Blocks, Else, Finally
# ============================================================

# TODO 2.1
def describe_error(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "cannot divide by zero"
    except TypeError:
        return "both arguments must be numbers"


print(describe_error(10, 0))
print(describe_error(10, "two"))


# TODO 2.2
def divide_with_message(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "error: division by zero"
    else:
        return f"success: {result}"


print(divide_with_message(10, 2))
print(divide_with_message(10, 0))


# TODO 2.3
def parse_with_finally(text):
    attempts = []
    try:
        return int(text)
    except ValueError:
        return None
    finally:
        attempts.append("attempted")


parse_with_finally("10")
attempts_a = []
try:
    result = int("10")
finally:
    attempts_a.append("attempted")
print(len(attempts_a))

attempts_b = []
try:
    result = int("nope")
except ValueError:
    result = None
finally:
    attempts_b.append("attempted")
print(len(attempts_b))


# TODO 2.4
def lookup_with_fallback(data, key, fallback=None):
    try:
        value = data[key]
    except KeyError:
        return fallback
    else:
        return value


print(lookup_with_fallback({"a": 1}, "a", 0))
print(lookup_with_fallback({"a": 1}, "z", 0))


# TODO 2.5 (Debug the Code)
def safe_ratio(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "cannot divide by zero"
    except Exception:
        return "unexpected error"


print(safe_ratio(10, 0))


# TODO 2.A (Scenario -- Payment Processing Cleanup)
def process_payment(amount):
    try:
        if amount <= 0:
            raise ValueError("invalid amount")
        return f"charged ${amount}"
    except ValueError:
        return "payment failed"
    finally:
        print("cleanup step complete")


print(process_payment(50))
print(process_payment(-10))


# TODO 2.B (Scenario -- Interview Prep)
def explain_else_vs_try_tail():
    return (
        "Code placed in try can accidentally have its own exceptions "
        "caught by the except blocks below it, while code in else only "
        "runs after the try block succeeded with zero exceptions -- and "
        "any error raised inside else itself is NOT caught by that same "
        "try's except blocks. This keeps 'did the risky part succeed' "
        "logic clearly separate from 'what could actually fail' logic."
    )


print(explain_else_vs_try_tail())


# ============================================================
# Topic 3: The Exception Object
# ============================================================

# TODO 3.1
def describe_value_error(text):
    try:
        return int(text)
    except ValueError as e:
        return str(e)


print(describe_value_error("notanumber"))


# TODO 3.2
def describe_zero_division(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        return str(e)


print(describe_zero_division(5, 0))


# TODO 3.3
def error_type_name(func, *args):
    try:
        func(*args)
    except Exception as e:
        return type(e).__name__
    return "no error"


print(error_type_name(lambda a, b: a / b, 5, 0))


# TODO 3.4
def safe_key_lookup(data, key):
    try:
        return data[key]
    except KeyError as e:
        return f"missing key: {e}"


print(safe_key_lookup({"a": 1}, "z"))


# TODO 3.5 (Debug the Code)
def parse_with_detail(text):
    try:
        return int(text)
    except ValueError as e:
        return f"conversion failed: {e}"


print(parse_with_detail("xyz"))


# TODO 3.A (Scenario -- User-Friendly Error Messages)
def friendly_parse_error(text):
    try:
        return int(text)
    except ValueError as e:
        return f"We couldn't read '{text}' as a number ({e})."


print(friendly_parse_error("abc"))


# TODO 3.B (Scenario -- Interview Prep)
def explain_str_e_value():
    return (
        "type(e).__name__ only tells you *what kind* of failure happened "
        "(like ValueError), while str(e) carries the actual message "
        "describing *what specifically* went wrong, like which value "
        "couldn't convert -- production logs need both to actually debug "
        "an incident quickly instead of guessing from the type alone."
    )


print(explain_str_e_value())


# ============================================================
# Topic 4: Raising Exceptions Deliberately
# ============================================================

# TODO 4.1
def require_positive(n):
    if n <= 0:
        raise ValueError(f"{n} is not positive")
    return n


try:
    require_positive(-5)
except ValueError as e:
    print(str(e))

print(require_positive(5))


# TODO 4.2
def validate_percentage(value):
    if value < 0 or value > 100:
        raise ValueError(f"{value} is out of range 0-100")
    return value


try:
    validate_percentage(150)
except ValueError as e:
    print(str(e))

print(validate_percentage(80))


# TODO 4.3
def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("insufficient funds")
    return balance - amount


try:
    withdraw(100, 500)
except ValueError as e:
    print(str(e))

print(withdraw(100, 30))


# TODO 4.4
def reraise_with_context(func, *args):
    try:
        return func(*args)
    except Exception as e:
        raise ValueError(f"operation failed: {e}") from e


try:
    reraise_with_context(lambda: 1 / 0)
except ValueError as e:
    print(str(e))


# TODO 4.5 (Debug the Code)
def rectangle_area(width, height):
    if width <= 0:
        raise ValueError(f"width must be positive, got {width}")
    return width * height


try:
    rectangle_area(-3, 5)
except ValueError as e:
    print(str(e))
except Exception as e:
    print("caught non-specific exception:", str(e))


# TODO 4.A (Scenario -- Input Validation Gate)
def validate_signup_age(age):
    if age < 13 or age > 120:
        raise ValueError(f"age {age} is invalid for signup")
    return age


try:
    validate_signup_age(8)
except ValueError as e:
    print(str(e))

print(validate_signup_age(25))


# TODO 4.B (Scenario -- Interview Prep)
def explain_raise_vs_none():
    return (
        "Returning None fits situations where 'not found' or 'no value' "
        "is a normal, expected outcome the caller should handle quietly, "
        "while raising fits situations where continuing with bad data "
        "would be actively dangerous or nonsensical, like a negative "
        "withdrawal amount -- raising forces the caller to notice and "
        "handle the problem instead of letting bad data flow silently "
        "downstream."
    )


print(explain_raise_vs_none())


# ============================================================
# Topic 5: Custom Exception Classes
# ============================================================

# TODO 5.1
class InsufficientFundsError(Exception):
    pass


def withdraw_strict(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(
            f"cannot withdraw {amount}, balance is only {balance}"
        )
    return balance - amount


try:
    withdraw_strict(100, 500)
except InsufficientFundsError as e:
    print(str(e))


# TODO 5.2
class InvalidAgeError(Exception):
    pass


def register_user(name, age):
    if age < 0 or age > 130:
        raise InvalidAgeError(f"invalid age: {age}")
    return f"registered {name}, age {age}"


try:
    register_user("Sam", -5)
except InvalidAgeError as e:
    print(str(e))


# TODO 5.3
def custom_error_message(balance, amount):
    try:
        withdraw_strict(balance, amount)
    except InsufficientFundsError as e:
        return str(e)
    return "withdrawal succeeded"


print(custom_error_message(50, 200))


# TODO 5.4
class NegativeValueError(Exception):
    pass


def safe_sqrt(n):
    if n < 0:
        raise NegativeValueError(f"cannot take sqrt of negative number {n}")
    return math.sqrt(n)


try:
    safe_sqrt(-9)
except NegativeValueError as e:
    print(str(e))

print(safe_sqrt(9))


# TODO 5.5 (Debug the Code)
class OutOfStockError(Exception):
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


# TODO 5.A (Scenario -- Domain-Specific Errors in a Banking App)
def transfer_funds(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(
            f"cannot transfer {amount}, balance is only {balance}"
        )
    return balance - amount


try:
    transfer_funds(200, 1000)
except InsufficientFundsError as e:
    print(str(e))


# TODO 5.B (Scenario -- Interview Prep)
def explain_custom_exception_value():
    return (
        "A custom exception name is self-documenting -- "
        "InsufficientFundsError says exactly what went wrong at a glance "
        "-- and it lets calling code catch just that specific problem "
        "without accidentally swallowing unrelated errors, while still "
        "working everywhere a normal exception works since it subclasses "
        "Exception."
    )


print(explain_custom_exception_value())


# ============================================================
# Topic 6: Bringing It Together -- Exception Handling in Production
# ============================================================

# TODO 6.1
class ApiError(Exception):
    pass


def safe_api_response(status_code, payload):
    try:
        if status_code >= 500:
            raise ApiError(f"server error {status_code}")
        if status_code >= 400:
            raise ValueError(f"bad request {status_code}")
        return {"ok": True, "data": payload}
    except ApiError as e:
        return {"ok": False, "error": "server", "detail": str(e)}
    except ValueError as e:
        return {"ok": False, "error": "client", "detail": str(e)}


print(safe_api_response(200, {"id": 1}))
print(safe_api_response(404, {"id": 1}))
print(safe_api_response(500, {"id": 1}))


# TODO 6.2
def process_order(item_price, quantity, discount_percent):
    if item_price <= 0:
        raise ValueError(f"item_price must be positive, got {item_price}")
    if quantity <= 0:
        raise ValueError(f"quantity must be positive, got {quantity}")
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError(
            f"discount_percent must be 0-100, got {discount_percent}"
        )
    return round(item_price * quantity * (1 - discount_percent / 100), 2)


try:
    process_order(10, -2, 5)
except ValueError as e:
    print(str(e))

print(process_order(10, 2, 10))


# TODO 6.3
def retry_flaky_operation(func, max_attempts=3):
    for _attempt in range(max_attempts):
        try:
            return func()
        except Exception:
            continue
    return None


attempts_left = [2]


def flaky():
    if attempts_left[0] > 0:
        attempts_left[0] -= 1
        raise ValueError("not yet")
    return "succeeded"


print(retry_flaky_operation(flaky))


# TODO 6.4
def safe_batch_process(items):
    successes = []
    failures = []
    for item in items:
        try:
            successes.append(int(item))
        except ValueError:
            failures.append(item)
    return {"successes": successes, "failures": failures}


print(safe_batch_process(["1", "2", "abc", "4", "xyz"]))


# TODO 6.5 (Debug the Code)
def validate_username(username):
    try:
        if len(username) < 3:
            raise ValueError("username too short")
        cleaned = username.strip()
        return cleaned
    except ValueError:
        return None


print(validate_username("abcdef"))


# TODO 6.A (Scenario -- Production-Grade Checkout Validator)
class CheckoutError(Exception):
    pass


def validate_checkout(cart_total, payment_amount):
    try:
        if cart_total <= 0:
            raise CheckoutError("cart total must be positive")
        if payment_amount < cart_total:
            raise CheckoutError(
                f"payment {payment_amount} does not cover total {cart_total}"
            )
        change = round(payment_amount - cart_total, 2)
    except CheckoutError as e:
        return {"ok": False, "error": str(e)}
    else:
        return {"ok": True, "change": change}
    finally:
        print("checkout validation complete")


print(validate_checkout(50, 20))
print(validate_checkout(50, 60))


# TODO 6.B (Scenario -- Interview Prep)
def explain_broad_except_risk():
    return (
        "A broad 'except Exception:' (or worse, a bare 'except:') can "
        "silently swallow completely unrelated bugs -- like a typo "
        "causing a NameError -- making real problems invisible instead "
        "of surfacing a traceback that would get noticed and fixed; "
        "production code should catch the *specific* exception types it "
        "actually expects and knows how to handle."
    )


print(explain_broad_except_risk())
