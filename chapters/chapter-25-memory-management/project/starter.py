"""
Chapter 25 Project: Memory Profiler for an Earlier Project
See README.md in this folder for full instructions.
Run this from inside the project/ folder: python3 starter.py

Standard library only -- no installs needed.
"""

import tracemalloc


# TODO 1: Write profile_function(func). Run func() (a zero-argument
# callable) under tracemalloc: start tracing, call func(), read
# current/peak memory with get_traced_memory(), take a snapshot with
# take_snapshot(), stop tracing, and return a dict with keys "result"
# (func()'s return value), "current_bytes", "peak_bytes", and
# "top_allocations" (a list of the top 3 entries from
# snapshot.statistics("lineno"), each as a dict with "location"
# (str(stat)), "size_bytes" (stat.size), and "count" (stat.count)).


# TODO 2: Write compare_functions(label_a, func_a, label_b, func_b).
# Profile both zero-argument functions with profile_function(), and
# return a dict {label_a: profile_a, label_b: profile_b, "smaller":
# whichever label had the smaller peak_bytes}.


# --- The "earlier project" logic being profiled -----------------------

def load_grades_heavy(n):
    """Memory-heavy: builds and returns a full list of every record."""
    return [{"id": i, "score": (i * 7) % 101, "padding": "x" * 50} for i in range(n)]


def load_grades_lazy(n):
    """Optimized: returns a generator, producing one record at a time."""
    return ({"id": i, "score": (i * 7) % 101, "padding": "x" * 50} for i in range(n))


def average_score_from_iterable(records):
    """Works identically whether records is a list or a generator."""
    total = 0
    count = 0
    for r in records:
        total += r["score"]
        count += 1
    return total / count if count else 0


# TODO 3: Write format_report(comparison). Build and return a
# multi-line string report:
#   "=== Memory Profiler Report ==="
#   then for each label in comparison (skipping the "smaller" key):
#     "--- {label} ---"
#     "Peak memory: {peak_bytes:,} bytes"
#     "Top allocations:" followed by one line per allocation entry
#     ("  {location}"), or "  (none traced -- ...)" if the list is empty
#   finally: "Smaller peak memory: {comparison['smaller']}"


def run():
    n = 5000
    comparison = compare_functions(
        "heavy (list)",
        lambda: average_score_from_iterable(load_grades_heavy(n)),
        "optimized (generator)",
        lambda: average_score_from_iterable(load_grades_lazy(n)),
    )
    print(format_report(comparison))


if __name__ == "__main__":
    run()
