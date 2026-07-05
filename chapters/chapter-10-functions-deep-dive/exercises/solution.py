"""
Chapter 10 Exercises: Functions Deep Dive — reference solution.
"""

# TODO 1: Write a function calculate_area(width, height) that returns the
# area of a rectangle. Then write a function describe_pet(name, species)
# that returns a string like "Rex is a dog". Call both and print the
# results.
def calculate_area(width, height):
    return width * height

def describe_pet(name, species):
    return name + " is a " + species

print(calculate_area(4, 5))
print(describe_pet("Rex", "dog"))


# TODO 2: Write a function make_coffee(size="medium", extra_shot=False)
# that returns a label like "medium coffee", or "large coffee with an
# extra shot" if extra_shot is True. Call it once with no arguments, and
# once with "large" and True.
def make_coffee(size="medium", extra_shot=False):
    label = size + " coffee"
    if extra_shot:
        label += " with an extra shot"
    return label

print(make_coffee())
print(make_coffee("large", True))


# TODO 3: Write a function total_cost(*prices) that returns the sum of any
# number of prices, rounded to 2 decimals. Then write a function
# build_order(item, **details) that returns a dictionary starting with
# {"item": item} and merges in whatever extra keyword arguments are
# passed.
def total_cost(*prices):
    return round(sum(prices), 2)

def build_order(item, **details):
    order = {"item": item}
    order.update(details)
    return order

print(total_cost(4.50, 9.99, 2.00))
print(build_order("Latte", size="large", oat_milk=True))


# TODO 4: Given visits = 0 below, write a function record_visit() that
# uses the global keyword to increment visits by 1 each time it's called.
# Call it three times and print the final visits.
visits = 0

def record_visit():
    global visits
    visits += 1

record_visit()
record_visit()
record_visit()
print(visits)


# TODO 5: Write a recursive function countdown(n) that prints each number
# from n down to 1, then prints "Liftoff!" — with a proper base case.
# Then write a recursive function sum_to_n(n) that returns the sum of
# every whole number from 1 to n.
def countdown(n):
    if n <= 0:
        print("Liftoff!")
        return
    print(n)
    countdown(n - 1)

countdown(3)

def sum_to_n(n):
    if n == 0:
        return 0
    return n + sum_to_n(n - 1)

print(sum_to_n(5))


# TODO 6: Write a function make_multiplier(factor) that returns an inner
# function multiply(n) which returns n * factor. Use it to create a
# double multiplier and a triple multiplier, and call both.
def make_multiplier(factor):
    def multiply(n):
        return n * factor
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)
print(double(6))
print(triple(6))


# TODO 7: Write a decorator shout(func) whose inner wrapper calls func
# with any arguments it receives, then returns the result in uppercase
# with an exclamation point added. Apply it with @shout to a function
# greet(name) that returns "hi " + name, and print the result of calling
# it.
def shout(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper() + "!"
    return wrapper

@shout
def greet(name):
    return "hi " + name

print(greet("sam"))


# TODO 8 (Debug the Code): this function is supposed to build up a fresh
# task list on every call, but it reuses the same list across every call
# instead. Find and fix the bug.
def add_task(task, task_list=None):
    if task_list is None:
        task_list = []
    task_list.append(task)
    return task_list

print(add_task("clean the kitchen"))
print(add_task("cook dinner"))


# TODO 9: Write two small helper functions, is_valid_username(username)
# (at least 3 characters and alphanumeric) and is_valid_pin(pin) (exactly
# 4 digits). Then write can_log_in(username, pin), which returns True
# only if both helpers pass. Test it with one valid and one invalid
# login.
def is_valid_username(username):
    return len(username) >= 3 and username.isalnum()

def is_valid_pin(pin):
    return pin.isdigit() and len(pin) == 4

def can_log_in(username, pin):
    return is_valid_username(username) and is_valid_pin(pin)

print(can_log_in("zoe1", "1234"))
print(can_log_in("z", "12"))
