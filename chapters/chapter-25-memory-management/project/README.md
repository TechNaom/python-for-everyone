# Chapter 25 Project: Memory Profiler for an Earlier Project

A small, standalone **memory profiler** (one Python file, standard
library only) that instruments any zero-argument function with
`tracemalloc`, reporting peak memory use and top allocations — then
uses it to run a real before/after comparison between a memory-heavy
version and a memory-optimized version of the same logic.

## What you'll build

A stand-in "earlier project" scenario: loading and averaging a batch
of student grade records, once as a fully materialized list
(`load_grades_heavy()`) and once as a lazy generator
(`load_grades_lazy()`, Chapter 17's technique). The profiler measures
both and reports:

1. **Peak memory** for each version, in bytes.
2. **Top allocations** — the source lines responsible for the most
   memory, via `tracemalloc.take_snapshot().statistics("lineno")`.
3. **Which version had the smaller peak** — the actual, measured
   answer, not a guess.

## Example run

```text
=== Memory Profiler Report ===

--- heavy (list) ---
Peak memory: 1,109,728 bytes
Top allocations:
  solution.py:62: size=17.3 KiB, count=255, average=70 B
  solution.py:78: size=64 B, count=2, average=32 B
  solution.py:22: size=64 B, count=2, average=32 B

--- optimized (generator) ---
Peak memory: 408 bytes
Top allocations:
  (none traced -- this version never held more than the interpreter's own baseline at once)

Smaller peak memory: optimized (generator)
```

(Your own exact byte counts and line numbers will differ slightly by
Python version/platform — the *comparison* is the point, not memorizing
one number.)

## How to run

```bash
cd chapters/chapter-25-memory-management/project
python3 starter.py
```

Fill in the numbered `# TODO` sections. Want to see a finished version?
Run `python3 solution.py`.

## The pieces

- **`profile_function(func)`** — the reusable core: instruments any zero-argument function with `tracemalloc`, returning its result plus peak/current memory and top allocations.
- **`compare_functions(label_a, func_a, label_b, func_b)`** — profiles two functions and reports which had the smaller peak.
- **`load_grades_heavy()`** / **`load_grades_lazy()`** — the "earlier project" logic being profiled, one materializing a full list, one a lazy generator.
- **`average_score_from_iterable()`** — consumer code that works identically on either version, since both are iterable.
- **`format_report()`** — combines everything into one readable report string.

## Ideas to make it your own

- Point `profile_function()` at a function from one of your own earlier chapter projects (the Chapter 13 CSV project, the Chapter 21 database project) instead of the built-in example.
- Add a third comparison: the same data loaded with `__slots__`-based record objects instead of plain dicts.
- Report the percentage memory reduction (`(heavy_peak - light_peak) / heavy_peak * 100`) alongside the raw byte counts.

## Why this project matters

"Is this actually faster/lighter, or does it just feel like it should
be?" is a question real engineers answer by measuring, not guessing —
this project builds a small, reusable tool for doing exactly that,
on any function, not just the one example built here.

## More project ideas (build one of these instead, or after)

From Chapter 7 onward, you get a genuine choice of what to build. The
Memory Profiler above is fully built out with a starter and reference
solution — the four ideas below are not. Each is a real, grounded use
case solvable with only what's been taught through Chapter 25. No
starter or solution files are provided on purpose — building one of
these unassisted is the point.

### 1. A Data-Structure Memory Comparison Tool

**Problem:** The same dataset can be stored as a list of tuples, a
list of dicts, or a list of `__slots__`-based objects — which one
actually uses the least memory?

**What it should do:** Build the same 10,000-row dataset three ways
and report each structure's peak memory via `tracemalloc`, ranked
smallest to largest.

**Suggested approach:** Reuse this project's `profile_function()`
directly — this is almost the same tool, pointed at three build
functions instead of two.

### 2. A `__slots__` Refactoring Exercise

**Problem:** A provided class with 5+ attributes and no `__slots__`
needs refactoring, and someone wants to know exactly how much memory
that refactor actually saves at scale.

**What it should do:** Take a class, build 10,000 instances of both
the original and a slotted version, and report the total memory
difference using `sys.getsizeof()` per instance times instance count.

**Suggested approach:** Sub-topic 4's `PointRegular`/`PointSlotted`
comparison, scaled up to a realistic instance count.

### 3. A Reference-Cycle Detector

**Problem:** Given a small object graph (nodes with `.next`/`.parent`
attributes), detect whether it contains a reference cycle before it
ever becomes a real memory problem.

**What it should do:** Walk the object graph from a starting node,
tracking visited object ids, and report `True`/`False` for whether a
cycle exists — a simplified, hand-rolled version of what `gc`'s
cycle-finder does internally.

**Suggested approach:** A visited-set walk using `id()` to track
already-seen objects, similar in spirit to graph traversal.

### 4. A "Memory Leak" Bug Hunt with `weakref`

**Problem:** A provided class has an intentional memory leak — a
cache dict that holds strong references to objects long after they
should be collectable.

**What it should do:** Diagnose why instances aren't being freed even
after all "real" references are dropped, then fix it using the
`weakref` module (a new, one-off tool worth introducing here: a weak
reference doesn't keep an object alive by itself).

**Suggested approach:** Reproduce the leak first with `gc.collect()`
showing 0 freed, then swap the cache's strong references for
`weakref.WeakValueDictionary` and show the same objects now get
collected once they're otherwise unreferenced.
