"""
Chapter 25 Practice Bank: Memory Management in Python
See README.md in this folder for full instructions.
Run this from inside the practice/ folder: python3 starter.py

Standard library only -- no installs needed.
"""

import sys
import gc
import tracemalloc

# ============================================================
# Topic 1: How Python Manages Memory & Reference Counting
# ============================================================

# TODO 1.1: Write current_refcount(obj). Return sys.getrefcount(obj).


# TODO 1.2: Write refcount_increases_on_alias(obj). Given an object,
# take its refcount, create a second reference to it (alias = obj),
# take the refcount again, and return True if the second reading is
# strictly greater than the first.


# TODO 1.3 (Debug the Code): explain_refcount() below wrongly claims
# Python frees objects once a day on a schedule. Fix its return value.
def explain_refcount():
    return "Python frees objects once a day, on a fixed schedule, regardless of how many references point to them."


print(explain_refcount())


# TODO 1.A (Scenario -- Comparing Two Approaches): write
# will_object_survive(still_referenced). Return True if
# still_referenced is True (something still points to it, so it
# survives), else False.


# TODO 1.B (Scenario -- Interview Prep): write
# explain_getrefcount_off_by_one() describing why sys.getrefcount()
# reports one more than expected.


# ============================================================
# Topic 2: Reference Cycles & the Garbage Collector
# ============================================================

class _CycleNode:
    def __init__(self, name):
        self.name = name
        self.partner = None


# TODO 2.1: Write build_two_node_cycle(). Create two _CycleNode
# instances, link them to each other via .partner, and return the
# tuple (node_a, node_b).


# TODO 2.2: Write collect_garbage(). Return gc.collect() (an int).


# TODO 2.3 (Debug the Code): count_generations() below is supposed to
# return how many generations gc.get_count() reports, but it hardcodes
# 1 instead of actually checking the tuple's length. Fix it.
def count_generations():
    return 1


print("count_generations():", count_generations())


# TODO 2.A (Scenario -- Comparing Two Approaches): write
# would_leak_without_gc(has_cycle, gc_enabled). Return True (a leak
# risk) only if has_cycle is True AND gc_enabled is False.


# TODO 2.B (Scenario -- Interview Prep): write
# explain_why_cycles_need_gc() describing why reference counting alone
# can't free a reference cycle.


# ============================================================
# Topic 3: The Mutable Default Argument Gotcha
# ============================================================

# TODO 3.1: Write append_safe(item, items=None). Fix the mutable
# default gotcha -- return a list with item appended, starting fresh
# each call unless items is provided.


# TODO 3.2: Write same_default_object(func). Given a function with
# exactly one default argument, call it twice with no arguments and
# return True if id() of the two returned mutable defaults are equal
# (demonstrating the same object is reused).


# TODO 3.3 (Debug the Code): collect_tags() below has the classic
# mutable default bug. Fix it.
def collect_tags(tag, tags=[]):
    tags.append(tag)
    return tags


print(collect_tags("python"))
print(collect_tags("memory"))


# TODO 3.A (Scenario -- Cleaning Up a Shared Utility): write
# make_empty_report(). This stands in for a reporting utility used
# across a codebase -- return a NEW empty dict every call (no shared
# mutable default at all).


# TODO 3.B (Scenario -- Interview Prep): write
# explain_mutable_default_fix() describing the None-sentinel pattern
# and why it works.


# ============================================================
# Topic 4: __slots__
# ============================================================

class RegularUser:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class SlottedUser:
    __slots__ = ("name", "age")

    def __init__(self, name, age):
        self.name = name
        self.age = age


# TODO 4.1: Write regular_user_total_size(name, age). Build a
# RegularUser, return sys.getsizeof(instance) + sys.getsizeof(instance.__dict__).


# TODO 4.2: Write slotted_user_size(name, age). Build a SlottedUser,
# return sys.getsizeof(instance).


# TODO 4.3 (Debug the Code): try_dynamic_attr() below is supposed to
# demonstrate that a SlottedUser rejects a new dynamic attribute, but
# it wrongly tries this on a RegularUser (which allows it). Fix it so
# it tests the SlottedUser and catches the AttributeError.
def try_dynamic_attr():
    u = RegularUser("Ana", 30)
    try:
        u.email = "ana@example.com"
        return "no error raised"
    except AttributeError as e:
        return f"AttributeError: {e}"


print(try_dynamic_attr())


# TODO 4.A (Scenario -- Choosing __slots__ for a Hot Path): write
# should_use_slots(instance_count, needs_dynamic_attrs). Return True
# if instance_count is greater than 10000 AND needs_dynamic_attrs is
# False, else False.


# TODO 4.B (Scenario -- Interview Prep): write
# explain_slots_tradeoff() describing what __slots__ saves and what it
# costs.


# ============================================================
# Topic 5: Memory Profiling Basics
# ============================================================

# TODO 5.1: Write size_of_object(obj). Return sys.getsizeof(obj).


# TODO 5.2: Write traced_peak_of(build_fn). Start tracemalloc, call
# build_fn() (a zero-argument function), read peak memory, stop
# tracemalloc, and return the peak (an int).


# TODO 5.3 (Debug the Code): measure_dict_build() below is supposed to
# return the PEAK memory of building a dict, but it returns the
# CURRENT value at a point where current and peak might differ. Fix it
# to always return the peak.
def measure_dict_build(n):
    tracemalloc.start()
    d = {i: i * i for i in range(n)}
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return current


print("measure_dict_build(1000):", measure_dict_build(1000))


# TODO 5.A (Scenario -- Comparing Two Data Structures): write
# smaller_container(n). Using traced_peak_of()-style measurement
# inline, compare a list of n ints vs. a set of the same n ints; return
# the string "list" or "set", whichever measured smaller peak memory.


# TODO 5.B (Scenario -- Interview Prep): write
# explain_getsizeof_vs_tracemalloc() describing the difference between
# the two tools.


# ============================================================
# Topic 6: Generators as the Memory-Efficient Alternative
# ============================================================

# TODO 6.1: Write list_version(n). Return [i for i in range(n)].


# TODO 6.2: Write generator_version(n). Return (i for i in range(n)).


# TODO 6.3 (Debug the Code): peak_of_generator() below is supposed to
# measure the generator BEFORE consuming it, but it sums the generator
# first, which forces every value to be produced, before taking the
# memory reading. Fix the order so the peak is captured right after
# creation, before consumption.
def peak_of_generator(n):
    tracemalloc.start()
    gen = generator_version(n)
    total = sum(gen)
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return peak


print("peak_of_generator(1000):", peak_of_generator(1000))


# TODO 6.A (Scenario -- Streaming a Large Report): write
# should_use_generator(passes_needed, needs_random_access). Return
# True (use a generator) only if passes_needed == 1 AND
# needs_random_access is False.


# TODO 6.B (Scenario -- Interview Prep): write
# explain_generator_memory_tradeoff() describing why a generator uses
# less memory and what it gives up to do so.
