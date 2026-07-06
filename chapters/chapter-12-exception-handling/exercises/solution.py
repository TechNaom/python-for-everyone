"""
Chapter 12 Exercises: Exception Handling — reference solution.
"""

# TODO 1: Write a function parse_quantity(text) that returns int(text),
# but catches a ValueError - printing "Not a valid quantity:" followed
# by repr(text), and returning None. Call it with "5" and with "five"
# and print both results.
def parse_quantity(text):
    try:
        return int(text)
    except ValueError:
        print("Not a valid quantity:", repr(text))
        return None

print(parse_quantity("5"))
print(parse_quantity("five"))


# TODO 2: Write a function safe_average(numbers) that computes
# sum(numbers) / len(numbers) inside a try. Catch ZeroDivisionError and
# print "Can't average an empty list." In an else block, print
# "Average:" followed by the result. In a finally block, print
# "Average check done." Call it with [10, 20, 30] and with [].
def safe_average(numbers):
    try:
        total = sum(numbers)
        average = total / len(numbers)
    except ZeroDivisionError:
        print("Can't average an empty list.")
    else:
        print("Average:", average)
    finally:
        print("Average check done.")

safe_average([10, 20, 30])
safe_average([])


# TODO 3: Write a function parse_price(text) that returns float(text),
# catching a ValueError as e and printing "Could not parse price:"
# followed by str(e), then returning None. Call it with "19.99" and
# with "free".
def parse_price(text):
    try:
        return float(text)
    except ValueError as e:
        print("Could not parse price:", str(e))
        return None

print(parse_price("19.99"))
print(parse_price("free"))


# TODO 4: Write a function set_quantity(qty) that raises a
# ValueError("quantity must be at least 1") if qty < 1, otherwise
# returns qty. Call it with 0 inside a try/except ValueError as e that
# prints "Rejected:" followed by e.
def set_quantity(qty):
    if qty < 1:
        raise ValueError("quantity must be at least 1")
    return qty

try:
    set_quantity(0)
except ValueError as e:
    print("Rejected:", e)


# TODO 5: Define class OutOfStockError(Exception): pass. Write a
# function place_order(stock, requested) that raises an
# OutOfStockError with the message f"Only {stock} left, requested
# {requested}" if requested > stock, otherwise returns
# stock - requested. Call it with stock=3, requested=5 inside a
# try/except OutOfStockError as e that prints "Order failed:" followed
# by e.
class OutOfStockError(Exception):
    pass

def place_order(stock, requested):
    if requested > stock:
        raise OutOfStockError(f"Only {stock} left, requested {requested}")
    return stock - requested

try:
    place_order(3, 5)
except OutOfStockError as e:
    print("Order failed:", e)


# TODO 6: Write a function checkout(stock, requested) that calls
# place_order(stock, requested) inside a try. On OutOfStockError as e,
# print "Checkout failed:" followed by e and return None. In else,
# print "Checkout succeeded, remaining stock:" followed by the result,
# and return it. In finally, print "Checkout attempt logged." Call it
# with (10, 3) and then (10, 20).
def checkout(stock, requested):
    try:
        remaining = place_order(stock, requested)
    except OutOfStockError as e:
        print("Checkout failed:", e)
        return None
    else:
        print("Checkout succeeded, remaining stock:", remaining)
        return remaining
    finally:
        print("Checkout attempt logged.")

checkout(10, 3)
checkout(10, 20)


# TODO 7 (Debug the Code): this code uses a bare except: that hides a
# real bug - a typo'd variable name inside the try block silently
# prints "Something went wrong" instead of surfacing the actual
# NameError. Find and fix the bug so the typo is visible and the
# working code still runs correctly.
# Bug: "pryce" is a typo for "price"; the bare except: silently hid the
# resulting NameError. Fix: correct the typo, and catch a specific
# exception type instead of using a bare except.
def get_total(price, quantity):
    try:
        total = price * quantity
        print("Total:", total)
    except NameError as e:
        print("Bug found:", e)

get_total(10, 3)


# TODO 8 (Debug the Code): this code has its except blocks in the
# wrong order, so the more specific ValueError can never be reached -
# the broader Exception earlier in the chain catches it first. Find
# and fix the ordering.
# Bug: "except Exception:" comes before "except ValueError:", so it
# catches everything first and the ValueError block is unreachable.
# Fix: put the more specific exception type first.
def parse_amount(text):
    try:
        return int(text)
    except ValueError:
        print("Specifically not a valid number:", repr(text))
        return None
    except Exception:
        print("General error.")
        return None

parse_amount("abc")
