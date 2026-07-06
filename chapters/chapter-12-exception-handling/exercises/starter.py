"""
Chapter 12 Exercises: Exception Handling
See README.md in this folder for full instructions.
"""

# TODO 1: Write a function parse_quantity(text) that returns int(text),
# but catches a ValueError - printing "Not a valid quantity:" followed
# by repr(text), and returning None. Call it with "5" and with "five"
# and print both results.


# TODO 2: Write a function safe_average(numbers) that computes
# sum(numbers) / len(numbers) inside a try. Catch ZeroDivisionError and
# print "Can't average an empty list." In an else block, print
# "Average:" followed by the result. In a finally block, print
# "Average check done." Call it with [10, 20, 30] and with [].


# TODO 3: Write a function parse_price(text) that returns float(text),
# catching a ValueError as e and printing "Could not parse price:"
# followed by str(e), then returning None. Call it with "19.99" and
# with "free".


# TODO 4: Write a function set_quantity(qty) that raises a
# ValueError("quantity must be at least 1") if qty < 1, otherwise
# returns qty. Call it with 0 inside a try/except ValueError as e that
# prints "Rejected:" followed by e.


# TODO 5: Define class OutOfStockError(Exception): pass. Write a
# function place_order(stock, requested) that raises an
# OutOfStockError with the message f"Only {stock} left, requested
# {requested}" if requested > stock, otherwise returns
# stock - requested. Call it with stock=3, requested=5 inside a
# try/except OutOfStockError as e that prints "Order failed:" followed
# by e.


# TODO 6: Write a function checkout(stock, requested) that calls
# place_order(stock, requested) inside a try. On OutOfStockError as e,
# print "Checkout failed:" followed by e and return None. In else,
# print "Checkout succeeded, remaining stock:" followed by the result,
# and return it. In finally, print "Checkout attempt logged." Call it
# with (10, 3) and then (10, 20).


# TODO 7 (Debug the Code): this code uses a bare except: that hides a
# real bug - a typo'd variable name inside the try block silently
# prints "Something went wrong" instead of surfacing the actual
# NameError. Find and fix the bug so the typo is visible and the
# working code still runs correctly.
def get_total(price, quantity):
    try:
        total = pryce * quantity
        print("Total:", total)
    except:
        print("Something went wrong.")

get_total(10, 3)


# TODO 8 (Debug the Code): this code has its except blocks in the
# wrong order, so the more specific ValueError can never be reached -
# the broader Exception earlier in the chain catches it first. Find
# and fix the ordering.
def parse_amount(text):
    try:
        return int(text)
    except Exception:
        print("General error.")
        return None
    except ValueError:
        print("Specifically not a valid number:", repr(text))
        return None

parse_amount("abc")
