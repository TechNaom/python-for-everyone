"""
Chapter 10 Practice Bank: Functions Deep Dive — reference solution.
See README.md in this folder for full instructions.
"""

# ============================================================
# Topic 1: Function Basics (def, parameters, return)
# ============================================================

# TODO 1.1
def greet(name):
    return f"Hello, {name}!"


print(greet("Asha"))


# TODO 1.2
def add(a, b):
    return a + b


print(add(3, 4))


# TODO 1.3
def is_even(n):
    return n % 2 == 0


print(is_even(4))
print(is_even(7))


# TODO 1.4
def describe_number(n):
    if n > 0:
        return "positive"
    elif n < 0:
        return "negative"
    else:
        return "zero"


print(describe_number(5))
print(describe_number(-3))
print(describe_number(0))


# TODO 1.5 (Debug the Code)
def square_of(n):
    return n * n


result = square_of(6)
print(result)


# TODO 1.A (Scenario — Order Total Calculator)
def calculate_total(price, quantity):
    return price * quantity


print(f"${calculate_total(19.99, 3):.2f}")


# TODO 1.B (Scenario — Interview Prep)
def add_return(a, b):
    return a + b


def add_print(a, b):
    print(a + b)


returned_value = add_return(2, 3)
printed_value = add_print(2, 3)
print(returned_value)
print(printed_value)
# add_print has no return statement, so Python automatically gives back
# None once the function finishes — printing something to the screen is
# not the same as returning it to the caller, even though both add_return
# and add_print show the same information when you run them.


# ============================================================
# Topic 2: Default Arguments
# ============================================================

# TODO 2.1
def power(base, exponent=2):
    return base ** exponent


print(power(5))
print(power(2, 5))


# TODO 2.2
def make_greeting(name, greeting="Hello"):
    return f"{greeting}, {name}!"


print(make_greeting("Asha"))
print(make_greeting("Ravi", "Welcome"))


# TODO 2.3
def apply_discount(price, percent=10):
    return price - price * percent / 100


print(apply_discount(100))
print(apply_discount(100, 25))


# TODO 2.4
def build_profile(name, age=18, city="Unknown"):
    return {"name": name, "age": age, "city": city}


print(build_profile("Asha"))
print(build_profile("Ravi", 24))
print(build_profile(name="Meera", age=30, city="Pune"))


# TODO 2.5 (Debug the Code)
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items


print(add_item("apple"))
print(add_item("banana"))


# TODO 2.A (Scenario — Configurable Report Header)
def report_header(title, author="Unknown Author", year=2024):
    return f"{title} by {author} ({year})"


print(report_header("Sales Report"))
print(report_header("Sales Report", "Asha", 2026))


# TODO 2.B (Scenario — Interview Prep)
def track_visits(user, log=None):
    if log is None:
        log = []
    log.append(user)
    return log


print(track_visits("Asha"))
print(track_visits("Ravi"))
# Default argument values are evaluated only once, at function
# definition time, so a mutable default like [] would be shared and
# mutated across every call that relies on the default — using None
# and creating the mutable object inside the function body avoids that
# trap and gives every call its own fresh list.


# ============================================================
# Topic 3: *args and **kwargs
# ============================================================

# TODO 3.1
def sum_all(*args):
    return sum(args)


print(sum_all(1, 2, 3, 4))


# TODO 3.2
def join_words(*args):
    return " ".join(args)


print(join_words("Python", "is", "fun"))


# TODO 3.3
def print_profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_profile(name="Asha", age=21, city="Pune")


# TODO 3.4
def build_settings(*args, **kwargs):
    return (args, kwargs)


print(build_settings(1, 2, mode="fast", retries=3))


# TODO 3.5 (Debug the Code)
def average(*args):
    return sum(args) / len(args)


print(average(2, 4, 6))


# TODO 3.A (Scenario — Flexible Logger)
def log_event(event_name, **details):
    print(event_name)
    for key, value in details.items():
        print(f"  {key}: {value}")


log_event("login", user="asha", success=True, attempt=1)


# TODO 3.B (Scenario — Interview Prep)
def describe_call(*args, **kwargs):
    print(f"Got {len(args)} positional args and {len(kwargs)} keyword args.")


describe_call(1, 2, 3, x=1, y=2)
# *args collects any extra positional arguments into a tuple, while
# **kwargs collects any extra named/keyword arguments into a dict, and
# both let a function accept a flexible, variable number of arguments
# without the caller needing to match an exact parameter list.


# ============================================================
# Topic 4: Scope (local/global, global/nonlocal)
# ============================================================

# TODO 4.1
counter = 0


def show_local_shadow():
    counter = 100
    print(counter)


show_local_shadow()
print(counter)


# TODO 4.2
total = 0


def add_to_total(amount):
    global total
    total += amount


add_to_total(10)
add_to_total(5)
print(total)


# TODO 4.3
def make_counter_pair():
    count = 0

    def increment():
        nonlocal count
        count += 1

    def get_count():
        return count

    return (increment, get_count)


increment, get_count = make_counter_pair()
increment()
increment()
print(get_count())


# TODO 4.4
value = "outside"


def reset_and_report(value):
    return f"local value is {value}"


print(reset_and_report(42))
print(value)


# TODO 4.5 (Debug the Code)
score = 0


def boost_score():
    global score
    score += 10


boost_score()
print(score)


# TODO 4.A (Scenario — Shared Application Counter)
active_users = 0


def user_logged_in():
    global active_users
    active_users += 1


def user_logged_out():
    global active_users
    active_users -= 1


user_logged_in()
user_logged_in()
user_logged_out()
print(active_users)


# TODO 4.B (Scenario — Interview Prep)
def outer_counter():
    count = 0

    def bump():
        nonlocal count
        count += 1
        return count

    bump()
    bump()
    return bump()


print(outer_counter())
# global reaches all the way out to module-level variables, while
# nonlocal reaches out only to the nearest *enclosing* function's local
# scope (not all the way to global), which is exactly what a nested
# function needs to modify a variable from its immediately enclosing
# function.


# ============================================================
# Topic 5: Recursion
# ============================================================

# TODO 5.1
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


print(factorial(5))


# TODO 5.2
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(7))


# TODO 5.3
def sum_digits(n):
    if n < 10:
        return n
    return (n % 10) + sum_digits(n // 10)


print(sum_digits(12345))


# TODO 5.4
def count_down(n):
    print(n)
    if n == 0:
        print("Liftoff!")
    else:
        count_down(n - 1)


count_down(5)


# TODO 5.5 (Debug the Code)
def factorial_broken(n):
    if n == 0:
        return 1
    return n * factorial_broken(n - 1)


print(factorial_broken(5))


# TODO 5.A (Scenario — Counting Items in Nested Categories)
def total_items(data):
    total = 0
    for item in data:
        if isinstance(item, list):
            total += total_items(item)
        else:
            total += item
    return total


nested_counts = [2, [3, 4], [5, [6, 7]], 1]
print(total_items(nested_counts))


# TODO 5.B (Scenario — Interview Prep)
def power_of(base, exponent):
    if exponent == 0:
        return 1
    return base * power_of(base, exponent - 1)


print(power_of(2, 5))
# A base case is the condition where a recursive function stops calling
# itself and returns a direct answer instead — without one, every call
# would spawn another call forever until Python hits its recursion limit
# and raises a RecursionError.


# ============================================================
# Topic 6: Closures
# ============================================================

# TODO 6.1
def make_multiplier(factor):
    def multiply(n):
        return n * factor

    return multiply


triple = make_multiplier(3)
print(triple(5))


# TODO 6.2
def make_greeter(greeting):
    def greet(name):
        return f"{greeting}, {name}!"

    return greet


say_hello = make_greeter("Hello")
say_hi = make_greeter("Hi")
print(say_hello("Asha"))
print(say_hi("Ravi"))


# TODO 6.3
def make_counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment


counter_a = make_counter()
counter_b = make_counter()
print(counter_a())
print(counter_a())
print(counter_b())


# TODO 6.4
def make_running_total():
    total = 0

    def add(amount):
        nonlocal total
        total += amount
        return total

    return add


tracker = make_running_total()
print(tracker(10))
print(tracker(5))
print(tracker(20))


# TODO 6.5 (Debug the Code)
def make_name_tracker():
    names = []

    def add_name(name):
        names.append(name)
        return names

    return add_name


tracker = make_name_tracker()
print(tracker("Asha"))
print(tracker("Ravi"))


# TODO 6.A (Scenario — Per-User Rate Limiter Counter)
def make_request_counter(limit):
    count = 0

    def record_request():
        nonlocal count
        count += 1
        return count <= limit

    return record_request


allow = make_request_counter(2)
print(allow())
print(allow())
print(allow())


# TODO 6.B (Scenario — Interview Prep)
def make_adder(n):
    def add_n(x):
        return x + n

    return add_n


add_5 = make_adder(5)
print(add_5(10))
# A closure is a nested function that "remembers" the variables from its
# enclosing function's scope even after that enclosing function has
# already returned, which is exactly how add_5 still has access to n
# even though make_adder(5) already finished executing.


# ============================================================
# Topic 7: Decorators
# ============================================================

# TODO 7.1
def shout(fn):
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        return str(result).upper()

    return wrapper


@shout
def greet(name):
    return f"hello, {name}"


print(greet("asha"))


# TODO 7.2
def call_counter(fn):
    count = 0

    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        wrapper.calls = count
        return fn(*args, **kwargs)

    return wrapper


@call_counter
def ping():
    return "pong"


ping()
ping()
ping()
print(ping.calls)


# TODO 7.3
def double_result(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs) * 2

    return wrapper


@double_result
def add(a, b):
    return a + b


print(add(3, 4))


# TODO 7.4
def log_call(fn):
    def wrapper(*args, **kwargs):
        print(f"Calling {fn.__name__} with {args}, {kwargs}")
        return fn(*args, **kwargs)

    return wrapper


@log_call
def multiply(a, b):
    return a * b


print(multiply(3, 4))


# TODO 7.5 (Debug the Code)
def add_prefix(fn):
    def wrapper(*args, **kwargs):
        print("Starting...")
        return fn(*args, **kwargs)

    return wrapper


@add_prefix
def compute(a, b):
    return a + b


print(compute(2, 3))


# TODO 7.A (Scenario — Timing-Style Instrumentation Without a Timer)
def track_calls(fn):
    calls_made = 0

    def wrapper(*args, **kwargs):
        nonlocal calls_made
        calls_made += 1
        print(f"{fn.__name__} has been called {calls_made} time(s)")
        return fn(*args, **kwargs)

    return wrapper


@track_calls
def process_order(order_id):
    return f"Processed {order_id}"


print(process_order("A1"))
print(process_order("A2"))


# TODO 7.B (Scenario — Interview Prep)
def ensure_positive(fn):
    def wrapper(n):
        if n < 0:
            return "invalid input"
        return fn(n)

    return wrapper


@ensure_positive
def square(n):
    return n * n


print(square(5))
print(square(-3))
# A decorator is just a function that takes another function as input
# and returns a new function that wraps it, adding behavior
# before/after/instead of the original call, all without changing the
# original function's own source code — @ensure_positive above
# square(n) is shorthand for square = ensure_positive(square).


# ============================================================
# Topic 8: Bringing It Together — Real-World Functions in Production
# ============================================================

# TODO 8.1
def validate_and_format_price(price):
    if price >= 0:
        return f"${price:.2f}"
    return "invalid price"


print(validate_and_format_price(19.999))
print(validate_and_format_price(-5))


# TODO 8.2
def retry_with_default(values, index, default=None):
    if 0 <= index < len(values):
        return values[index]
    return default


print(retry_with_default([10, 20, 30], 5, default=0))
print(retry_with_default([10, 20, 30], 1))


# TODO 8.3
def build_api_response(status, **data):
    return {"status": status, "data": data}


print(build_api_response("ok", user="asha", role="admin"))


# TODO 8.4
def retry_once(fn):
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        if result is None:
            result = fn(*args, **kwargs)
        return result

    return wrapper


@retry_once
def flaky_lookup(cache, key):
    return cache.get(key)


print(flaky_lookup({"a": 1}, "b"))


# TODO 8.5 (Debug the Code)
def apply_discount_rounds(price, rounds):
    if rounds == 0:
        return price
    return apply_discount_rounds(price * 0.9, rounds - 1)


print(apply_discount_rounds(100, 3))


# TODO 8.A (Scenario — Production-Style Input Sanitizer Pipeline)
def sanitize_signup_data(name, email, age=None, **extra):
    return {
        "name": name.strip().title(),
        "email": email.strip().lower(),
        "age": age if age is not None else "not provided",
        "extra": extra,
    }


print(sanitize_signup_data("  asha KUMAR ", " ASHA@EXAMPLE.COM ", referral="friend"))


# TODO 8.B (Scenario — Interview Prep)
def make_average_tracker():
    total = 0
    count = 0

    def update(value):
        nonlocal total, count
        total += value
        count += 1
        return total / count

    return update


def log_updates(fn):
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        print(f"New average: {result}")
        return result

    return wrapper


tracker = make_average_tracker()
tracker = log_updates(tracker)
tracker(10)
tracker(20)
tracker(30)
# This combines a closure (the running total/count state living inside
# make_average_tracker) with a decorator (the logging behavior wrapped
# around every call via log_updates) — exactly the kind of composition
# real production code leans on, where independent small pieces of
# behavior get layered together instead of rewritten from scratch.
