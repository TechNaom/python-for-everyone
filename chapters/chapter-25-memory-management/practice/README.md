# Chapter 25 Practice Bank: Memory Management in Python

A deeper set of practice problems, organized by topic, on top of the
main `exercises/` folder — including scenario-based problems written
in the same style you'll see in real interviews. Every task here uses
only the standard library — no installs needed.

## How to run

```bash
cd practice
python3 starter.py
```

## Topic 1: How Python Manages Memory & Reference Counting

1. Read an object's current refcount.
2. Show that aliasing an object increases its refcount.
3. **Debug the Code:** fix a wrong claim that Python frees objects on a fixed schedule.
4. **Scenario — Comparing Two Approaches:** write `will_object_survive()`.
5. **Scenario — Interview Prep:** explain the `getrefcount()` off-by-one.

## Topic 2: Reference Cycles & the Garbage Collector

1. Build a two-node reference cycle.
2. Trigger `gc.collect()` manually.
3. **Debug the Code:** fix code that hardcoded the generation count instead of reading it.
4. **Scenario — Comparing Two Approaches:** write `would_leak_without_gc()`.
5. **Scenario — Interview Prep:** explain why cycles need a separate collector.

## Topic 3: The Mutable Default Argument Gotcha

1. Write a safe append function using the `None`-sentinel pattern.
2. Prove a broken function reuses the same default object with `id()`.
3. **Debug the Code:** fix a classic `tags=[]` mutable default bug.
4. **Scenario — Cleaning Up a Shared Utility:** write `make_empty_report()`.
5. **Scenario — Interview Prep:** explain the `None`-sentinel fix.

## Topic 4: `__slots__`

1. Measure a regular class instance's total size (instance + `__dict__`).
2. Measure a slotted class instance's size.
3. **Debug the Code:** fix code that tested dynamic-attribute rejection on the wrong class.
4. **Scenario — Choosing __slots__ for a Hot Path:** write `should_use_slots()`.
5. **Scenario — Interview Prep:** explain what `__slots__` saves and costs.

## Topic 5: Memory Profiling Basics

1. Measure one object's size with `sys.getsizeof()`.
2. Measure a whole function's peak memory with `tracemalloc`.
3. **Debug the Code:** fix code that returned "current" instead of "peak".
4. **Scenario — Comparing Two Data Structures:** write `smaller_container()`.
5. **Scenario — Interview Prep:** explain `sys.getsizeof()` vs. `tracemalloc`.

## Topic 6: Generators as the Memory-Efficient Alternative

1. Build the list version of a sequence.
2. Build the generator version of the same sequence.
3. **Debug the Code:** fix code that measured a generator's memory only after consuming it.
4. **Scenario — Streaming a Large Report:** write `should_use_generator()`.
5. **Scenario — Interview Prep:** explain the generator memory trade-off.

## Checking your work

Compare your output against `solution.py`. Your exact wording doesn't
need to match on the explanation-style tasks — the goal is that your
program runs without errors and does what each TODO asks. Exact byte
counts may vary slightly by Python version/platform; the *pattern*
(e.g. slotted smaller than regular) should always hold.
