"""
Chapter 25 Exercises: Memory Management in Python -- reference solution.
Run this from inside the exercises/ folder: python3 solution.py
"""

import sys
import gc
import tracemalloc


# TODO 1
def refcount_of(obj):
    return sys.getrefcount(obj)


print("refcount_of([1, 2, 3]):", refcount_of([1, 2, 3]))


# TODO 2
class _CycleNode:
    def __init__(self):
        self.partner = None


def make_cycle():
    def build():
        a = _CycleNode()
        b = _CycleNode()
        a.partner = b
        b.partner = a

    gc.disable()
    build()
    collected = gc.collect()
    gc.enable()
    return collected


print("make_cycle() collected at least 2 objects:", make_cycle() >= 2)


# TODO 3
def add_item_safe(item, cart=None):
    if cart is None:
        cart = []
    cart.append(item)
    return cart


print(add_item_safe("apple"))
print(add_item_safe("banana"))


# TODO 4
class SlottedPoint:
    __slots__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y


def point_instance_size(x, y):
    p = SlottedPoint(x, y)
    return sys.getsizeof(p)


print("point_instance_size(1, 2):", point_instance_size(1, 2))


# TODO 5
def object_size(obj):
    return sys.getsizeof(obj)


print("object_size([1, 2, 3]):", object_size([1, 2, 3]))


# TODO 6
def peak_memory_of_list_build(n):
    tracemalloc.start()
    _ = [i * i for i in range(n)]
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return peak


print("peak_memory_of_list_build(10000):", peak_memory_of_list_build(10000))


# TODO 7
def peak_memory_of_generator_build(n):
    tracemalloc.start()
    _ = (i * i for i in range(n))
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return peak


print("peak_memory_of_generator_build(10000):", peak_memory_of_generator_build(10000))


# TODO 8
def is_generator_smaller(n):
    return peak_memory_of_generator_build(n) < peak_memory_of_list_build(n)


print("is_generator_smaller(10000):", is_generator_smaller(10000))


# TODO 9 (Debug the Code)
# Bug: log=[] is created once, at def time, and reused across every
# call -- fixed with the None-sentinel pattern.
def add_to_log(entry, log=None):
    if log is None:
        log = []
    log.append(entry)
    return log


print(add_to_log("first"))
print(add_to_log("second"))
