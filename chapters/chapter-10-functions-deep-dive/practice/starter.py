"""
Chapter 10 Practice Bank: Functions Deep Dive
See README.md in this folder for full instructions.

Only uses what Chapters 1-10 covered: print()/input(), variables, basic
types, operators, if/elif/else, while/for/range/break/continue, strings,
lists/tuples, dicts/sets, comprehensions, lambda, map()/filter()/sorted(),
and this chapter's own toolkit: def, parameters and default arguments,
*args and **kwargs, local/global scope with global/nonlocal, recursion,
closures, and decorators (hand-written, no functools). No try/except,
file I/O, classes, or imports.
"""

# ============================================================
# Topic 1: Function Basics (def, parameters, return)
# ============================================================

# TODO 1.1: Write a function greet(name) that returns the string
# f"Hello, {name}!". Call it with "Asha" and print the result.


# TODO 1.2: Write a function add(a, b) that returns the sum of a and b.
# Call it with 3 and 4, and print the result.


# TODO 1.3: Write a function is_even(n) that returns True if n is
# divisible by 2, otherwise False. Call it with 4 and with 7, printing
# both results.


# TODO 1.4: Write a function describe_number(n) that returns "positive",
# "negative", or "zero" depending on n, using if/elif/else inside the
# function body. Call it with 5, -3, and 0, printing all three results.


# TODO 1.5 (Debug the Code): this function is supposed to return the
# square of n, but it prints the square instead of returning it, so
# result ends up being None. Fix it so square_of returns n * n instead
# of printing it.
def square_of(n):
    print(n * n)


result = square_of(6)
print(result)


# TODO 1.A (Scenario — Order Total Calculator): write a function
# calculate_total(price, quantity) that returns price multiplied by
# quantity. Call it with price=19.99 and quantity=3, and print the
# result formatted to 2 decimal places with an f-string.


# TODO 1.B (Scenario — Interview Prep): an interviewer asks you to
# explain the difference between a function that returns a value and one
# that only prints a value. Write two functions, add_return(a, b) (which
# returns a + b) and add_print(a, b) (which only prints a + b). Call
# add_return(2, 3) and store it in a variable, then call add_print(2, 3)
# and try to store its result in another variable. Print both stored
# variables, and add a comment explaining why the second one is None:
# a function with no return statement (or a bare return) always gives
# back None, even if it printed something useful along the way.


# ============================================================
# Topic 2: Default Arguments
# ============================================================

# TODO 2.1: Write a function power(base, exponent=2) that returns base
# raised to exponent using the ** operator. Call it once with just a
# base (relying on the default exponent) and once with both arguments,
# printing both results.


# TODO 2.2: Write a function make_greeting(name, greeting="Hello") that
# returns f"{greeting}, {name}!". Call it with just a name, then with a
# name and a custom greeting, printing both results.


# TODO 2.3: Write a function apply_discount(price, percent=10) that
# returns the price after subtracting percent% of it
# (price - price * percent / 100). Call it with just a price, then with
# a price and a custom percent, printing both results.


# TODO 2.4: Write a function build_profile(name, age=18, city="Unknown")
# that returns a dict with keys "name", "age", and "city" built from the
# parameters. Call it three ways: with only name, with name and age, and
# with all three as keyword arguments, printing all three results.


# TODO 2.5 (Debug the Code): this function is supposed to append a new
# item to a running list each time it's called, but it uses a mutable
# list as a default argument, so the *same* list is reused and grows
# across calls instead of starting fresh each time. Fix it by defaulting
# items to None and creating a brand new list inside the function body
# when no list was passed in.
def add_item(item, items=[]):
    items.append(item)
    return items


print(add_item("apple"))
print(add_item("banana"))


# TODO 2.A (Scenario — Configurable Report Header): write a function
# report_header(title, author="Unknown Author", year=2024) that returns
# a formatted string like "Sales Report by Asha (2024)" using
# f"{title} by {author} ({year})". Call it once with only a title, and
# once overriding all three, printing both results.


# TODO 2.B (Scenario — Interview Prep): an interviewer asks why using a
# mutable default argument (like a list or dict) is dangerous in Python.
# Write a function track_visits(user, log=None) that, if log is None,
# creates a fresh empty list inside the function, appends user to it,
# and returns it. Call track_visits("Asha") and track_visits("Ravi")
# separately, printing both results to show each call gets its own
# fresh list. Add a comment explaining that default argument values are
# evaluated only once, at function definition time, so a mutable default
# like [] would be shared and mutated across every call that relies on
# the default — using None and creating the mutable object inside the
# function body avoids that trap.


# ============================================================
# Topic 3: *args and **kwargs
# ============================================================

# TODO 3.1: Write a function sum_all(*args) that returns the sum of all
# positional arguments passed in, using a plain for loop over args (or
# the built-in sum() function). Call it with sum_all(1, 2, 3, 4) and
# print the result.


# TODO 3.2: Write a function join_words(*args) that returns all the
# words passed in joined together with a space, using
# " ".join(args). Call it with join_words("Python", "is", "fun") and
# print the result.


# TODO 3.3: Write a function print_profile(**kwargs) that loops over
# kwargs.items() and prints each key and value on its own line as
# f"{key}: {value}". Call it with
# print_profile(name="Asha", age=21, city="Pune").


# TODO 3.4: Write a function build_settings(*args, **kwargs) that
# returns a tuple (args, kwargs) so you can see both collected together.
# Call it with build_settings(1, 2, mode="fast", retries=3) and print
# the result.


# TODO 3.5 (Debug the Code): this function is supposed to accept any
# number of positional arguments and return their average, but it tries
# to treat args like a single number instead of a tuple of numbers,
# raising a TypeError. Fix it by summing args and dividing by len(args).
def average(*args):
    return args / len(args)


print(average(2, 4, 6))


# TODO 3.A (Scenario — Flexible Logger): write a function
# log_event(event_name, **details) that prints event_name, then loops
# over details.items() printing each key and value indented with two
# spaces, like "  user: asha". Call it with
# log_event("login", user="asha", success=True, attempt=1).


# TODO 3.B (Scenario — Interview Prep): an interviewer asks you to
# explain the difference between *args and **kwargs. Write a function
# describe_call(*args, **kwargs) that prints
# f"Got {len(args)} positional args and {len(kwargs)} keyword args."
# Call it with describe_call(1, 2, 3, x=1, y=2). Add a comment
# explaining that *args collects any extra positional arguments into a
# tuple, while **kwargs collects any extra named/keyword arguments into
# a dict, and both let a function accept a flexible, variable number of
# arguments.


# ============================================================
# Topic 4: Scope (local/global, global/nonlocal)
# ============================================================

# TODO 4.1: Given a global variable counter = 0, write a function
# show_local_shadow() that creates a *local* variable also named counter
# set to 100 and prints it, without touching the global counter. After
# calling show_local_shadow(), print the global counter to show it is
# still 0.


# TODO 4.2: Given a global variable total = 0, write a function
# add_to_total(amount) that uses the global keyword to modify the global
# total by adding amount to it (no return needed). Call
# add_to_total(10) and add_to_total(5), then print the global total.


# TODO 4.3: Write a function make_counter_pair() that defines a local
# variable count = 0 inside it, then defines and returns two nested
# functions, increment() and get_count(), where increment() uses
# nonlocal count to add 1 to count, and get_count() returns count. Have
# make_counter_pair() return both nested functions as a tuple
# (increment, get_count). Call increment() twice and then print
# get_count() to show the count reached 2.


# TODO 4.4: Given a global variable value = "outside", write a function
# reset_and_report(value) whose parameter is also named value (shadowing
# the global one) and returns f"local value is {value}", to demonstrate
# that a parameter is just a local variable scoped to the function. Call
# reset_and_report(42) and print the result, then print the global value
# afterward to show it's still "outside" and was never touched.


# TODO 4.5 (Debug the Code): this function is supposed to increase a
# global variable score by 10 every time it's called, but it's missing
# the global keyword, so it creates a brand-new local variable instead
# and raises an UnboundLocalError on the += line. Fix it by adding
# global score as the first line of the function.
score = 0


def boost_score():
    score += 10


boost_score()
print(score)


# TODO 4.A (Scenario — Shared Application Counter): given a global
# variable active_users = 0, write two functions, user_logged_in() and
# user_logged_out(), that use global active_users to increment and
# decrement it respectively. Call user_logged_in() twice and
# user_logged_out() once, then print the final active_users.


# TODO 4.B (Scenario — Interview Prep): an interviewer asks you to
# explain the difference between global and nonlocal. Write a function
# outer_counter() with a local variable count = 0 and a nested function
# bump() that uses nonlocal count to increment it and return the new
# count; have outer_counter() call bump() three times and return the
# final count. Call outer_counter() and print the result. Add a comment
# explaining that global reaches all the way out to module-level
# variables, while nonlocal reaches out only to the nearest *enclosing*
# function's local scope (not all the way to global), which is exactly
# what a nested function needs to modify a variable from its immediately
# enclosing function.


# ============================================================
# Topic 5: Recursion
# ============================================================

# TODO 5.1: Write a recursive function factorial(n) that returns 1 when
# n == 0 (the base case), and otherwise returns n * factorial(n - 1).
# Call it with 5 and print the result.


# TODO 5.2: Write a recursive function fibonacci(n) that returns n when
# n is 0 or 1 (the base cases), and otherwise returns
# fibonacci(n - 1) + fibonacci(n - 2). Call it with 7 and print the
# result.


# TODO 5.3: Write a recursive function sum_digits(n) that returns n when
# n is less than 10 (the base case, a single digit), and otherwise
# returns (n % 10) + sum_digits(n // 10). Call it with 12345 and print
# the result.


# TODO 5.4: Write a recursive function count_down(n) that prints n, and
# if n is greater than 0, calls count_down(n - 1); if n is 0 (the base
# case), it prints "Liftoff!" instead of recursing further. Call it with
# 5.


# TODO 5.5 (Debug the Code): this recursive function is supposed to
# compute factorial(n), but it's missing a base case entirely, so it
# recurses forever until Python raises a RecursionError. Fix it by
# adding a base case that returns 1 when n == 0.
def factorial_broken(n):
    return n * factorial_broken(n - 1)


print(factorial_broken(5))


# TODO 5.A (Scenario — Counting Items in Nested Categories): given
# nested_counts = [2, [3, 4], [5, [6, 7]], 1] (a nested list representing
# item counts across categories and subcategories, where some entries
# are themselves lists), write a recursive function total_items(data)
# that returns the sum of every number in data, recursing into any
# nested list it finds and adding a single number directly when it finds
# one (base case). Call total_items(nested_counts) and print the
# result.


# TODO 5.B (Scenario — Interview Prep): an interviewer asks you to
# explain what a base case is and why every recursive function needs
# one. Write a recursive function power_of(base, exponent) that returns
# 1 when exponent == 0 (the base case), and otherwise returns
# base * power_of(base, exponent - 1). Call it with power_of(2, 5) and
# print the result. Add a comment explaining that a base case is the
# condition where a recursive function stops calling itself and returns
# a direct answer instead — without one, every call would spawn another
# call forever until Python hits its recursion limit and raises a
# RecursionError.


# ============================================================
# Topic 6: Closures
# ============================================================

# TODO 6.1: Write a function make_multiplier(factor) that defines and
# returns a nested function multiply(n) which returns n * factor,
# capturing factor from the enclosing scope. Build
# triple = make_multiplier(3), call triple(5), and print the result.


# TODO 6.2: Write a function make_greeter(greeting) that returns a
# nested function greet(name) which returns f"{greeting}, {name}!",
# capturing greeting from the enclosing scope. Build
# say_hello = make_greeter("Hello") and
# say_hi = make_greeter("Hi"), then call say_hello("Asha") and
# say_hi("Ravi"), printing both results to show each closure remembers
# its own greeting.


# TODO 6.3: Write a function make_counter() that defines a local
# count = 0 and a nested function increment() that uses nonlocal count
# to add 1 and return the new value, returning increment as the result
# of make_counter(). Build counter_a = make_counter() and
# counter_b = make_counter(), then call counter_a() twice and
# counter_b() once, printing all three results to show the two counters
# track independent state.


# TODO 6.4: Write a function make_running_total() that defines a local
# total = 0 and a nested function add(amount) that uses nonlocal total
# to add amount to total and return the new total, returning add.
# Build tracker = make_running_total(), then call tracker(10),
# tracker(5), and tracker(20), printing each running total as it's
# returned.


# TODO 6.5 (Debug the Code): this closure is supposed to remember and
# accumulate a list of names across calls, but add_name reassigns
# names = [] as a brand-new local list on every call instead of
# appending to the enclosing names list, so it never actually
# accumulates. Fix add_name by removing the `names = []` line so
# `names.append(name)` mutates the enclosing list from make_name_tracker
# instead of shadowing it.
def make_name_tracker():
    names = []

    def add_name(name):
        names = []
        names.append(name)
        return names

    return add_name


tracker = make_name_tracker()
print(tracker("Asha"))
print(tracker("Ravi"))


# TODO 6.A (Scenario — Per-User Rate Limiter Counter): write a function
# make_request_counter(limit) that defines a local count = 0 and a
# nested function record_request() which uses nonlocal count to
# increment count, then returns True if count is still less than or
# equal to limit (the request is allowed) or False otherwise (the
# request should be blocked); make_request_counter(limit) returns
# record_request. Build allow = make_request_counter(2), then call
# allow() three times in a row, printing each result to show the third
# call gets blocked.


# TODO 6.B (Scenario — Interview Prep): an interviewer asks you to
# explain what a closure is. Write a function make_adder(n) that returns
# a nested function add_n(x) which returns x + n, capturing n from the
# enclosing scope even after make_adder has finished running. Build
# add_5 = make_adder(5), call add_5(10), and print the result. Add a
# comment explaining that a closure is a nested function that
# "remembers" the variables from its enclosing function's scope even
# after that enclosing function has already returned, which is exactly
# how add_5 still has access to n even though make_adder(5) already
# finished executing.


# ============================================================
# Topic 7: Decorators
# ============================================================

# TODO 7.1: Write a decorator called shout that takes a function fn and
# returns a new nested function wrapper(*args, **kwargs) which calls
# fn(*args, **kwargs), converts the result to a string, uppercases it,
# and returns that. Apply @shout to a function greet(name) that returns
# f"hello, {name}", then call greet("asha") and print the result.


# TODO 7.2: Write a decorator called call_counter that takes a function
# fn and returns a new nested function wrapper(*args, **kwargs) which
# uses nonlocal to increment a counter defined in call_counter's
# enclosing scope (start it at 0 before defining wrapper), then calls
# and returns fn(*args, **kwargs). Give wrapper a way to expose the
# count by attaching it as wrapper.calls = count after incrementing.
# Apply @call_counter to a function ping() that returns "pong", call
# ping() three times, then print ping.calls to show it tracked 3 calls.


# TODO 7.3: Write a decorator called double_result that takes a function
# fn and returns wrapper(*args, **kwargs) which calls
# fn(*args, **kwargs) and returns the result multiplied by 2. Apply
# @double_result to a function add(a, b) that returns a + b, then call
# add(3, 4) and print the result (should be 14).


# TODO 7.4: Write a decorator called log_call that takes a function fn
# and returns wrapper(*args, **kwargs) which first prints
# f"Calling {fn.__name__} with {args}, {kwargs}", then calls and returns
# fn(*args, **kwargs). Apply @log_call to a function
# multiply(a, b) that returns a * b, then call multiply(3, 4) and print
# the result.


# TODO 7.5 (Debug the Code): this decorator is supposed to wrap a
# function so it prints "Starting..." before calling it and returns
# whatever the original function returns, but the wrapper forgets to
# return the inner function's result, so every decorated call silently
# gives back None instead of the real answer. Fix add_prefix so wrapper
# returns fn(*args, **kwargs) instead of just calling it.
def add_prefix(fn):
    def wrapper(*args, **kwargs):
        print("Starting...")
        fn(*args, **kwargs)

    return wrapper


@add_prefix
def compute(a, b):
    return a + b


print(compute(2, 3))


# TODO 7.A (Scenario — Timing-Style Instrumentation Without a Timer):
# write a decorator called track_calls that takes a function fn, keeps a
# local calls_made = 0 in its enclosing scope, and returns
# wrapper(*args, **kwargs) which uses nonlocal calls_made to increment
# it, prints f"{fn.__name__} has been called {calls_made} time(s)", and
# then calls and returns fn(*args, **kwargs). Apply @track_calls to a
# function process_order(order_id) that returns f"Processed {order_id}",
# then call process_order("A1") and process_order("A2"), printing both
# results.


# TODO 7.B (Scenario — Interview Prep): an interviewer asks you to
# explain, in your own words, what a decorator actually does under the
# hood. Write a decorator called ensure_positive that takes a function
# fn and returns wrapper(n) which, if n is less than 0, returns the
# string "invalid input" instead of calling fn at all, and otherwise
# calls and returns fn(n). Apply @ensure_positive to a function
# square(n) that returns n * n, then call square(5) and square(-3),
# printing both results. Add a comment explaining that a decorator is
# just a function that takes another function as input and returns a
# new function that wraps it, adding behavior before/after/instead of
# the original call, all without changing the original function's own
# source code — @ensure_positive above square(n) is shorthand for
# square = ensure_positive(square).


# ============================================================
# Topic 8: Bringing It Together — Real-World Functions in Production
# ============================================================

# TODO 8.1: Write a function validate_and_format_price(price) that
# returns f"${price:.2f}" if price is greater than or equal to 0, and
# returns "invalid price" otherwise (a small validation helper like you'd
# see guarding a checkout flow). Call it with 19.999 and with -5,
# printing both results.


# TODO 8.2: Write a function retry_with_default(values, index, default=None)
# that returns values[index] if index is a valid position in values
# (0 <= index < len(values)), and returns default otherwise — a
# defensive pattern for safely reading from a list that might be
# shorter than expected. Call it with values=[10, 20, 30], index=5,
# default=0, and print the result, then call it with index=1 (a valid
# index) and print that result too.


# TODO 8.3: Write a function build_api_response(status, **data) that
# returns a dict with a "status" key set to status and a "data" key set
# to the kwargs dict data — modeling how a real API response wrapper
# often bundles a status with a flexible bag of extra fields. Call it
# with build_api_response("ok", user="asha", role="admin") and print the
# result.


# TODO 8.4: Write a decorator called retry_once that takes a function fn
# and returns wrapper(*args, **kwargs) which calls
# fn(*args, **kwargs) and, if the result is None, calls fn(*args,
# **kwargs) one more time and returns that second result instead —
# modeling a simple "retry a flaky call once" pattern (without
# try/except, just reacting to a None result). Apply @retry_once to a
# function flaky_lookup(cache, key) that returns cache.get(key), call it
# with cache={"a": 1} and key="b" (missing, so it returns None both
# times), printing the final result.


# TODO 8.5 (Debug the Code): this recursive function is supposed to
# calculate a discounted price by applying a 10% discount repeatedly for
# a given number of rounds, but it never reduces rounds on the recursive
# call, so it recurses forever until a RecursionError. Fix it by
# decrementing rounds by 1 on the recursive call.
def apply_discount_rounds(price, rounds):
    if rounds == 0:
        return price
    return apply_discount_rounds(price * 0.9, rounds)


print(apply_discount_rounds(100, 3))


# TODO 8.A (Scenario — Production-Style Input Sanitizer Pipeline): write
# a function sanitize_signup_data(name, email, age=None, **extra) that
# returns a dict with "name" set to name.strip().title(), "email" set to
# email.strip().lower(), "age" set to age if age is not None else
# "not provided", and "extra" set to the extra kwargs dict as-is —
# modeling a realistic signup-form cleaning function that combines
# required params, a default, and **kwargs for anything else the form
# happened to submit. Call it with
# sanitize_signup_data("  asha KUMAR ", " ASHA@EXAMPLE.COM ", referral="friend")
# and print the result.


# TODO 8.B (Scenario — Interview Prep): an interviewer gives you a
# take-home style prompt: "write a function that returns a running
# average tracker using a closure, then wrap it with a decorator that
# logs every update." Write make_average_tracker() that keeps local
# total = 0 and count = 0, and returns a nested function update(value)
# which uses nonlocal total, count to add value to total and 1 to
# count, then returns total / count (the running average so far). Then
# write a decorator called log_updates that takes a function fn and
# returns wrapper(*args, **kwargs) which calls result = fn(*args,
# **kwargs), prints f"New average: {result}", and returns result. Build
# tracker = make_average_tracker(), wrap it manually with
# tracker = log_updates(tracker) (since you can't put @log_updates
# directly above a variable assignment), then call tracker(10),
# tracker(20), and tracker(30), letting the printed log lines show the
# running average update each time. Add a comment explaining how this
# combines a closure (the running total/count state) with a decorator
# (the logging behavior wrapped around every call) — exactly the kind
# of composition real production code leans on.
