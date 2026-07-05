"""
Chapter 10 Exercises: Functions Deep Dive
See README.md in this folder for full instructions.
"""

# TODO 1: Write a function calculate_area(width, height) that returns the
# area of a rectangle. Then write a function describe_pet(name, species)
# that returns a string like "Rex is a dog". Call both and print the
# results.


# TODO 2: Write a function make_coffee(size="medium", extra_shot=False)
# that returns a label like "medium coffee", or "large coffee with an
# extra shot" if extra_shot is True. Call it once with no arguments, and
# once with "large" and True.


# TODO 3: Write a function total_cost(*prices) that returns the sum of any
# number of prices, rounded to 2 decimals. Then write a function
# build_order(item, **details) that returns a dictionary starting with
# {"item": item} and merges in whatever extra keyword arguments are
# passed.


# TODO 4: Given visits = 0 below, write a function record_visit() that
# uses the global keyword to increment visits by 1 each time it's called.
# Call it three times and print the final visits.
visits = 0


# TODO 5: Write a recursive function countdown(n) that prints each number
# from n down to 1, then prints "Liftoff!" — with a proper base case.
# Then write a recursive function sum_to_n(n) that returns the sum of
# every whole number from 1 to n.


# TODO 6: Write a function make_multiplier(factor) that returns an inner
# function multiply(n) which returns n * factor. Use it to create a
# double multiplier and a triple multiplier, and call both.


# TODO 7: Write a decorator shout(func) whose inner wrapper calls func
# with any arguments it receives, then returns the result in uppercase
# with an exclamation point added. Apply it with @shout to a function
# greet(name) that returns "hi " + name, and print the result of calling
# it.


# TODO 8 (Debug the Code): this function is supposed to build up a fresh
# task list on every call, but it reuses the same list across every call
# instead. Find and fix the bug.
def add_task(task, task_list=[]):
    task_list.append(task)
    return task_list

print(add_task("clean the kitchen"))
print(add_task("cook dinner"))


# TODO 9: Write two small helper functions, is_valid_username(username)
# (at least 3 characters and alphanumeric) and is_valid_pin(pin) (exactly
# 4 digits). Then write can_log_in(username, pin), which returns True
# only if both helpers pass. Test it with one valid and one invalid
# login.
