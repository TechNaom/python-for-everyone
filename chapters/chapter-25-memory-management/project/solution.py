"""
Chapter 25 Project: Memory Profiler for an Earlier Project -- reference solution.
Run this from inside the project/ folder: python3 solution.py

A small, standalone memory profiler that instruments any zero-argument
function with tracemalloc, reporting peak memory use and top
allocations -- then uses it to run a real before/after comparison
between a memory-heavy version and a memory-optimized version of the
same logic (a stand-in "earlier project": loading and averaging a
batch of student grade records, list vs. generator).
"""

import tracemalloc


def profile_function(func):
    """Run func() (a zero-argument callable) under tracemalloc and
    return a dict with its result, peak/current memory in bytes, and
    the top 3 allocations by source line."""
    tracemalloc.start()
    result = func()
    current, peak = tracemalloc.get_traced_memory()
    snapshot = tracemalloc.take_snapshot()
    tracemalloc.stop()

    top_stats = snapshot.statistics("lineno")
    top_allocations = [
        {"location": str(stat), "size_bytes": stat.size, "count": stat.count}
        for stat in top_stats[:3]
    ]

    return {
        "result": result,
        "current_bytes": current,
        "peak_bytes": peak,
        "top_allocations": top_allocations,
    }


def compare_functions(label_a, func_a, label_b, func_b):
    """Profile two zero-argument functions and report which one had
    the smaller peak memory footprint."""
    profile_a = profile_function(func_a)
    profile_b = profile_function(func_b)
    smaller_label = label_a if profile_a["peak_bytes"] < profile_b["peak_bytes"] else label_b
    return {
        label_a: profile_a,
        label_b: profile_b,
        "smaller": smaller_label,
    }


# --- The "earlier project" logic being profiled -----------------------
# Stands in for a function you might have written back in an earlier
# chapter's project (e.g. loading rows for the Chapter 13 CSV project,
# or grades for the Chapter 23 NumPy project) -- one heavy version that
# materializes every record into a list, one optimized version that
# streams them lazily with a generator (Chapter 17).

def load_grades_heavy(n):
    """Memory-heavy: builds and returns a full list of every record."""
    return [{"id": i, "score": (i * 7) % 101, "padding": "x" * 50} for i in range(n)]


def load_grades_lazy(n):
    """Optimized: returns a generator, producing one record at a time."""
    return ({"id": i, "score": (i * 7) % 101, "padding": "x" * 50} for i in range(n))


def average_score_from_iterable(records):
    """Works identically whether records is a list or a generator --
    the whole point of writing consumer code against the iterable
    protocol (Chapter 17) rather than assuming a list specifically."""
    total = 0
    count = 0
    for r in records:
        total += r["score"]
        count += 1
    return total / count if count else 0


def format_report(comparison):
    lines = []
    lines.append("=== Memory Profiler Report ===")
    for label in comparison:
        if label == "smaller":
            continue
        profile = comparison[label]
        lines.append(f"\n--- {label} ---")
        lines.append(f"Peak memory: {profile['peak_bytes']:,} bytes")
        lines.append("Top allocations:")
        if profile["top_allocations"]:
            for alloc in profile["top_allocations"]:
                lines.append(f"  {alloc['location']}")
        else:
            lines.append("  (none traced -- this version never held more than the interpreter's own baseline at once)")
    lines.append(f"\nSmaller peak memory: {comparison['smaller']}")
    return "\n".join(lines)


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
