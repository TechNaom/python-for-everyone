"""
Chapter 25 Practice Bank: Memory Management in Python -- reference solution.
Run this from inside the practice/ folder: python3 solution.py
"""

import sys
import gc
import tracemalloc

# ============================================================
# Topic 1: How Python Manages Memory & Reference Counting
# ============================================================

# TODO 1.1
def current_refcount(obj):
    return sys.getrefcount(obj)


print(current_refcount([1, 2, 3]))


# TODO 1.2
def refcount_increases_on_alias(obj):
    before = sys.getrefcount(obj)
    alias = obj
    after = sys.getrefcount(obj)
    return after > before


print(refcount_increases_on_alias([1, 2, 3]))


# TODO 1.3 (Debug the Code)
# Bug: claimed objects are freed on a fixed daily schedule -- in fact
# they're freed immediately once their refcount hits zero.
def explain_refcount():
    return (
        "Python frees an object the instant its reference count reaches "
        "zero -- there is no fixed schedule or delay for this common case."
    )


print(explain_refcount())


# TODO 1.A (Scenario -- Comparing Two Approaches)
def will_object_survive(still_referenced):
    return still_referenced is True


print(will_object_survive(True))
print(will_object_survive(False))


# TODO 1.B (Scenario -- Interview Prep)
def explain_getrefcount_off_by_one():
    return (
        "sys.getrefcount(obj) itself takes obj as an argument, which "
        "creates one temporary reference for the duration of the call -- "
        "so the reported count is always one higher than the 'real' "
        "references that exist in the surrounding code."
    )


print(explain_getrefcount_off_by_one())


# ============================================================
# Topic 2: Reference Cycles & the Garbage Collector
# ============================================================

class _CycleNode:
    def __init__(self, name):
        self.name = name
        self.partner = None


# TODO 2.1
def build_two_node_cycle():
    node_a = _CycleNode("A")
    node_b = _CycleNode("B")
    node_a.partner = node_b
    node_b.partner = node_a
    return node_a, node_b


a, b = build_two_node_cycle()
print(a.name, "<->", b.name)


# TODO 2.2
def collect_garbage():
    return gc.collect()


print("collect_garbage() returned an int:", isinstance(collect_garbage(), int))


# TODO 2.3 (Debug the Code)
# Bug: hardcoded 1 instead of checking the actual length of
# gc.get_count(), which is a 3-tuple (one count per generation).
def count_generations():
    return len(gc.get_count())


print("count_generations():", count_generations())


# TODO 2.A (Scenario -- Comparing Two Approaches)
def would_leak_without_gc(has_cycle, gc_enabled):
    return has_cycle and not gc_enabled


print(would_leak_without_gc(True, False))
print(would_leak_without_gc(True, True))
print(would_leak_without_gc(False, False))


# TODO 2.B (Scenario -- Interview Prep)
def explain_why_cycles_need_gc():
    return (
        "In a reference cycle, each object still holds a reference to "
        "another object in the cycle, so none of their refcounts ever "
        "reach zero on their own, even when nothing outside the cycle can "
        "reach any of them. The separate cyclic garbage collector detects "
        "groups like this that are unreachable from outside and frees "
        "them together."
    )


print(explain_why_cycles_need_gc())


# ============================================================
# Topic 3: The Mutable Default Argument Gotcha
# ============================================================

# TODO 3.1
def append_safe(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items


print(append_safe("a"))
print(append_safe("b"))


# TODO 3.2
def same_default_object(func):
    first = func()
    second = func()
    return id(first) == id(second)


def _demo_broken(cart=[]):
    return cart


print(same_default_object(_demo_broken))


# TODO 3.3 (Debug the Code)
# Bug: tags=[] is created once, at def time, and reused across every
# call -- fixed with the None-sentinel pattern.
def collect_tags(tag, tags=None):
    if tags is None:
        tags = []
    tags.append(tag)
    return tags


print(collect_tags("python"))
print(collect_tags("memory"))


# TODO 3.A (Scenario -- Cleaning Up a Shared Utility)
def make_empty_report():
    return {}


r1 = make_empty_report()
r2 = make_empty_report()
r1["total"] = 100
print(r1, r2, id(r1) != id(r2))


# TODO 3.B (Scenario -- Interview Prep)
def explain_mutable_default_fix():
    return (
        "Default to None, then check 'if x is None: x = []' as the first "
        "line in the function body. None is still one shared default "
        "object reused across calls, but since it's immutable, sharing it "
        "is harmless -- the 'is None' check then builds a genuinely new "
        "mutable object fresh, every call that actually needs one."
    )


print(explain_mutable_default_fix())


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


# TODO 4.1
def regular_user_total_size(name, age):
    u = RegularUser(name, age)
    return sys.getsizeof(u) + sys.getsizeof(u.__dict__)


print("regular_user_total_size:", regular_user_total_size("Ana", 30))


# TODO 4.2
def slotted_user_size(name, age):
    u = SlottedUser(name, age)
    return sys.getsizeof(u)


print("slotted_user_size:", slotted_user_size("Ana", 30))


# TODO 4.3 (Debug the Code)
# Bug: tested dynamic-attribute rejection on RegularUser, which allows
# it -- SlottedUser is the one that should raise AttributeError.
def try_dynamic_attr():
    u = SlottedUser("Ana", 30)
    try:
        u.email = "ana@example.com"
        return "no error raised"
    except AttributeError as e:
        return f"AttributeError: {e}"


print(try_dynamic_attr())


# TODO 4.A (Scenario -- Choosing __slots__ for a Hot Path)
def should_use_slots(instance_count, needs_dynamic_attrs):
    return instance_count > 10000 and not needs_dynamic_attrs


print(should_use_slots(50000, False))
print(should_use_slots(50000, True))
print(should_use_slots(5, False))


# TODO 4.B (Scenario -- Interview Prep)
def explain_slots_tradeoff():
    return (
        "__slots__ removes a class instance's per-instance __dict__, "
        "storing only the named attributes in a fixed, compact layout -- "
        "a real, measurable memory saving per instance. The cost: no "
        "attribute beyond what's listed can be added dynamically, and "
        "multiple inheritance across two different non-empty-__slots__ "
        "classes is restricted."
    )


print(explain_slots_tradeoff())


# ============================================================
# Topic 5: Memory Profiling Basics
# ============================================================

# TODO 5.1
def size_of_object(obj):
    return sys.getsizeof(obj)


print("size_of_object([1,2,3]):", size_of_object([1, 2, 3]))


# TODO 5.2
def traced_peak_of(build_fn):
    tracemalloc.start()
    build_fn()
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return peak


print("traced_peak_of(lambda: [i for i in range(1000)]):", traced_peak_of(lambda: [i for i in range(1000)]))


# TODO 5.3 (Debug the Code)
# Bug: returned "current" when the task specifically asked for "peak".
def measure_dict_build(n):
    tracemalloc.start()
    d = {i: i * i for i in range(n)}
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return peak


print("measure_dict_build(1000):", measure_dict_build(1000))


# TODO 5.A (Scenario -- Comparing Two Data Structures)
def smaller_container(n):
    tracemalloc.start()
    lst = [i for i in range(n)]
    _, list_peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    tracemalloc.start()
    st = {i for i in range(n)}
    _, set_peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return "list" if list_peak < set_peak else "set"


print("smaller_container(1000):", smaller_container(1000))


# TODO 5.B (Scenario -- Interview Prep)
def explain_getsizeof_vs_tracemalloc():
    return (
        "sys.getsizeof(obj) measures one object's own size, not what it "
        "references. tracemalloc tracks every allocation across a whole "
        "block of code, reporting current/peak memory for everything "
        "allocated in that window -- the right tool for comparing two "
        "whole approaches, not just one value's size."
    )


print(explain_getsizeof_vs_tracemalloc())


# ============================================================
# Topic 6: Generators as the Memory-Efficient Alternative
# ============================================================

# TODO 6.1
def list_version(n):
    return [i for i in range(n)]


print(len(list_version(10)))


# TODO 6.2
def generator_version(n):
    return (i for i in range(n))


print(sum(generator_version(10)))


# TODO 6.3 (Debug the Code)
# Bug: summed the generator (forcing every value to be produced)
# BEFORE taking the memory reading -- fixed by measuring immediately
# after creation, before consumption.
def peak_of_generator(n):
    tracemalloc.start()
    gen = generator_version(n)
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return peak


print("peak_of_generator(1000):", peak_of_generator(1000))


# TODO 6.A (Scenario -- Streaming a Large Report)
def should_use_generator(passes_needed, needs_random_access):
    return passes_needed == 1 and not needs_random_access


print(should_use_generator(1, False))
print(should_use_generator(2, False))
print(should_use_generator(1, True))


# TODO 6.B (Scenario -- Interview Prep)
def explain_generator_memory_tradeoff():
    return (
        "A generator computes one value at a time, on demand, instead of "
        "storing every value upfront -- so at creation it costs a small, "
        "fixed amount of memory regardless of how many values it will "
        "eventually produce. The trade-off: it's single-use and "
        "forward-only, with no len(), no indexing, and no way to iterate "
        "it a second time once exhausted."
    )


print(explain_generator_memory_tradeoff())
