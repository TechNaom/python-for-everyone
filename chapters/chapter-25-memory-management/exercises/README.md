# Chapter 25 Exercises: Memory Management in Python

These exercises use what Chapter 25 covered: reference counting,
reference cycles and `gc`, the mutable default argument gotcha,
`__slots__`, and memory profiling with `sys.getsizeof()` and
`tracemalloc`. Every task here uses only the standard library -- no
installs needed.

## How to run

Run this **from inside this `exercises/` folder**:

```bash
cd exercises
python3 starter.py
```

## Task 1 — Reading a refcount

Find `# TODO 1`. Write `refcount_of(obj)` — return
`sys.getrefcount(obj)`.

## Task 2 — Building and collecting a reference cycle

Find `# TODO 2`. Write `make_cycle()` — build two objects that
reference each other (so refcounting alone can't free them), then
return how many objects `gc.collect()` reports freeing.

## Task 3 — Fixing a mutable default argument

Find `# TODO 3`. Write `add_item_safe(item, cart=None)` — the safe
version of the classic gotcha, starting a fresh list every call unless
an existing one is passed in.

## Task 4 — `__slots__`

Find `# TODO 4`. Write `class SlottedPoint` with `__slots__ = ("x",
"y")`, and `point_instance_size(x, y)` returning `sys.getsizeof()` of
an instance.

## Task 5 — Measuring one object's size

Find `# TODO 5`. Write `object_size(obj)` — return
`sys.getsizeof(obj)`.

## Task 6 — Peak memory of a list build

Find `# TODO 6`. Write `peak_memory_of_list_build(n)` — use
`tracemalloc` to measure building a list of `n` squared integers, and
return the peak bytes traced.

## Task 7 — Peak memory of a generator build

Find `# TODO 7`. Write `peak_memory_of_generator_build(n)` — the same
idea, for the equivalent generator expression.

## Task 8 — Comparing the two

Find `# TODO 8`. Write `is_generator_smaller(n)` — return `True` if
the generator version's peak memory is strictly less than the list
version's.

## Task 9 — Debug the Code

Find `# TODO 9`. This is supposed to give every call to `add_to_log()`
its own fresh list when no log is passed in, but it reuses the same
list every call because of the mutable default argument gotcha. Find
and fix it.

## Checking your work

Compare your output against `solution.py`. Exact byte counts
(`sys.getsizeof()`, `tracemalloc` peaks) may differ slightly on your
own machine/Python version — that's expected and explained in the
lesson. The *pattern* (e.g. generator smaller than list) should always
hold.
