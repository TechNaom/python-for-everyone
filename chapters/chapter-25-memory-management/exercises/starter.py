"""
Chapter 25 Exercises: Memory Management in Python
See README.md in this folder for full instructions.
Run this from inside the exercises/ folder: python3 starter.py

Every task here uses only the standard library -- no installs needed.
"""

import sys
import gc


# TODO 1: Write refcount_of(obj). Return sys.getrefcount(obj).


# TODO 2: Write make_cycle(). Create two plain objects (e.g. two empty
# lists, or two small classes) that reference each other, then return
# how many objects gc.collect() reports freeing. Hint: build the cycle
# inside a helper so both objects go out of scope, then call
# gc.collect() and return its result.


# TODO 3: Write add_item_safe(item, cart=None). Fix the classic mutable
# default argument gotcha -- return a list with item appended, starting
# fresh every call unless an existing cart list is passed in.


# TODO 4: Write class SlottedPoint using __slots__ = ("x", "y"), with
# an __init__(self, x, y) storing both. Then write
# point_instance_size(x, y) that builds a SlottedPoint and returns
# sys.getsizeof() of the instance.


# TODO 5: Write object_size(obj). Return sys.getsizeof(obj).


# TODO 6: Write peak_memory_of_list_build(n). Use tracemalloc to
# measure building a list of n squared integers ([i*i for i in
# range(n)]), and return the peak bytes traced (an int).


# TODO 7: Write peak_memory_of_generator_build(n). Same idea as TODO 6,
# but for the equivalent GENERATOR expression instead of a list
# comprehension -- return the peak bytes traced for just creating it
# (do not consume the generator before measuring).


# TODO 8: Write is_generator_smaller(n). Return True if
# peak_memory_of_generator_build(n) is strictly less than
# peak_memory_of_list_build(n), else False.


# TODO 9 (Debug the Code): this is supposed to give every call to
# add_to_log() its own fresh list when no log is passed in, but it
# reuses the same list across every call because of the mutable
# default argument gotcha. Find and fix it.
def add_to_log(entry, log=[]):
    log.append(entry)
    return log


print(add_to_log("first"))
print(add_to_log("second"))
