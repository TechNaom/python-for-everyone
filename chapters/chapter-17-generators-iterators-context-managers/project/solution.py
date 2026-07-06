"""
Chapter 17 Project: Large-File Streaming Log Analyzer -- reference solution.
See README.md in this folder for the full brief and example output.

This project is built AROUND this chapter's core tools: a generator function
(stream_lines) that reads a log file one line at a time using `yield`,
instead of loading the whole file into a list, plus a custom context manager
class (SessionTimer) built from __enter__/__exit__ that times how long each
streaming operation takes and reports it even if something goes wrong
mid-read. The menu loop never does `lines = file.readlines()` anywhere --
every option that touches the log file goes through the generator.
"""

import random
import time

SAMPLE_FILE = "sample_log.txt"

LEVELS = ["INFO", "WARNING", "ERROR", "DEBUG"]
LEVEL_WEIGHTS = [55, 20, 10, 15]
SERVICES = ["auth", "billing", "search", "checkout", "notifications"]
MESSAGES = {
    "INFO": [
        "request completed successfully",
        "user session started",
        "cache warmed",
        "health check passed",
        "background job finished",
    ],
    "WARNING": [
        "response time above threshold",
        "retrying request after timeout",
        "deprecated endpoint called",
        "queue depth increasing",
    ],
    "ERROR": [
        "database connection failed",
        "unhandled exception in handler",
        "payment gateway timeout",
        "failed to write to disk",
    ],
    "DEBUG": [
        "cache miss for key",
        "entering function with args",
        "computed intermediate value",
    ],
}


class SessionTimer:
    """Custom context manager: times an operation and prints how long it
    took, even if the operation raises an exception partway through."""

    def __init__(self, label):
        self.label = label
        self.start = None
        self.elapsed = None

    def __enter__(self):
        self.start = time.perf_counter()
        print(f"[timer] starting: {self.label}")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.elapsed = time.perf_counter() - self.start
        if exc_type is None:
            print(f"[timer] finished: {self.label} ({self.elapsed:.4f}s)")
        else:
            print(f"[timer] {self.label} raised {exc_type.__name__} "
                  f"after {self.elapsed:.4f}s -- cleanup still ran")
        # Returning False (or None) means any exception keeps propagating --
        # this timer only reports, it never silently swallows a real error.
        return False


def generate_sample_log(path=SAMPLE_FILE, num_lines=400, seed=17):
    """Write a few hundred realistic-looking log lines to `path`. This is
    the file the rest of the project streams through -- a few hundred lines
    is plenty to demonstrate line-by-line processing without ever needing
    an actual multi-gigabyte file."""
    rng = random.Random(seed)
    with open(path, "w") as f:
        for i in range(num_lines):
            level = rng.choices(LEVELS, weights=LEVEL_WEIGHTS, k=1)[0]
            service = rng.choice(SERVICES)
            message = rng.choice(MESSAGES[level])
            timestamp = f"2026-07-{(i % 28) + 1:02d} {(i % 24):02d}:{(i * 7) % 60:02d}:{(i * 13) % 60:02d}"
            f.write(f"{timestamp} [{level}] {service}: {message}\n")
    return num_lines


def stream_lines(path):
    """Generator: yields one line at a time from the file at `path`,
    stripped of its trailing newline. This is the core technique of the
    chapter -- the file is never read into a list. At any moment, only the
    current line is held in memory, so this same function would work
    identically on a 10GB file, not just a few hundred lines."""
    with open(path, "r") as f:
        for raw_line in f:
            yield raw_line.rstrip("\n")


def stream_matching(path, keyword):
    """Generator built on top of stream_lines: yields only the lines that
    contain `keyword` (case-insensitive). Still line-by-line -- filtering
    happens lazily as each line streams through, not on a pre-built list."""
    needle = keyword.lower()
    for line in stream_lines(path):
        if needle in line.lower():
            yield line


def summarize(path):
    """Streams the whole file once via the generator and builds a summary:
    total line count and a count per log level. Still never holds more
    than the current line in memory -- the counts are the only thing that
    accumulates."""
    total = 0
    counts = {level: 0 for level in LEVELS}
    for line in stream_lines(path):
        total += 1
        for level in LEVELS:
            if f"[{level}]" in line:
                counts[level] += 1
                break
    return total, counts


# --- Session state ---
print("=== Large-File Streaming Log Analyzer ===")
file_ready = False

while True:
    print()
    print("1. Generate sample log file")
    print("2. Stream & search for a keyword")
    print("3. Stream & summarize (line/level counts)")
    print("4. Show last operation's timing info")
    print("5. Quit")
    choice = input("Choose an option (1-5): ").strip()

    if choice == "1":
        print()
        with SessionTimer("generating sample log file") as timer:
            num_lines = generate_sample_log()
        file_ready = True
        last_timer = timer
        print(f"Wrote {num_lines} lines to {SAMPLE_FILE}.")

    elif choice == "2":
        print()
        if not file_ready:
            print(f"No sample file yet -- choose option 1 first.")
            continue
        keyword = input("Search for keyword (e.g. ERROR, billing): ").strip()
        if not keyword:
            print("Please enter a non-empty keyword.")
            continue
        with SessionTimer(f"streaming search for '{keyword}'") as timer:
            matches = 0
            for line in stream_matching(SAMPLE_FILE, keyword):
                matches += 1
                if matches <= 10:
                    print(f"  {line}")
        last_timer = timer
        if matches > 10:
            print(f"  ... and {matches - 10} more match(es)")
        print(f"Found {matches} matching line(s) for '{keyword}'.")

    elif choice == "3":
        print()
        if not file_ready:
            print("No sample file yet -- choose option 1 first.")
            continue
        with SessionTimer("streaming summary") as timer:
            total, counts = summarize(SAMPLE_FILE)
        last_timer = timer
        print(f"Summary of {SAMPLE_FILE}:")
        print(f"  Total lines: {total}")
        for level in LEVELS:
            print(f"  {level}: {counts[level]}")

    elif choice == "4":
        print()
        try:
            print(f"Last timed operation: '{last_timer.label}' "
                  f"took {last_timer.elapsed:.4f}s")
        except NameError:
            print("No operation has been timed yet -- try options 1-3 first.")

    elif choice == "5":
        print()
        print("Goodbye!")
        break

    else:
        print("Please choose 1-5.")
