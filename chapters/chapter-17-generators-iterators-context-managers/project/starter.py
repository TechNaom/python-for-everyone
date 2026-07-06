"""
Chapter 17 Project: Large-File Streaming Log Analyzer
See README.md in this folder for the full brief and example output.

This project is built AROUND this chapter's core tools: a generator
function that reads a log file one line at a time using `yield` instead of
loading the whole file into a list, plus a custom context manager class
(built from __enter__/__exit__) that times how long each streaming
operation takes and reports it even if something goes wrong mid-read. Fill
in the numbered TODOs below.
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
        # TODO 1: Record the current time onto self.start using
        # time.perf_counter(). Print f"[timer] starting: {self.label}".
        # Return self, so `with SessionTimer(...) as t:` gives access to
        # this same object as `t`.
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        # TODO 2: Compute self.elapsed as time.perf_counter() - self.start.
        # If exc_type is None (no exception happened), print
        # f"[timer] finished: {self.label} ({self.elapsed:.4f}s)".
        # Otherwise (an exception occurred), print
        # f"[timer] {self.label} raised {exc_type.__name__} after "
        # f"{self.elapsed:.4f}s -- cleanup still ran".
        # Return False either way -- this timer only reports, it never
        # suppresses a real exception from propagating.
        pass


def generate_sample_log(path=SAMPLE_FILE, num_lines=400, seed=17):
    """Write a few hundred realistic-looking log lines to `path`. This is
    the file the rest of the project streams through -- a few hundred lines
    is plenty to demonstrate line-by-line processing without ever needing
    an actual multi-gigabyte file."""
    rng = random.Random(seed)
    # TODO 3: Open `path` for writing using a `with` statement (as f).
    # Loop `num_lines` times (use range(num_lines) with i as the loop
    # variable). Each iteration: pick a level with
    # rng.choices(LEVELS, weights=LEVEL_WEIGHTS, k=1)[0], pick a service
    # with rng.choice(SERVICES), pick a message with
    # rng.choice(MESSAGES[level]), build a fake timestamp string (see
    # solution.py for an example format using i), and write one line like
    # f"{timestamp} [{level}] {service}: {message}\n" to f.
    pass
    return num_lines


def stream_lines(path):
    """Generator: yields one line at a time from the file at `path`,
    stripped of its trailing newline. This is the core technique of the
    chapter -- the file is never read into a list. At any moment, only the
    current line is held in memory, so this same function would work
    identically on a 10GB file, not just a few hundred lines."""
    # TODO 4: Open `path` for reading using a `with` statement (as f).
    # Loop `for raw_line in f:` (a file object is itself an iterator over
    # its lines) and `yield raw_line.rstrip("\n")` for each one. Because
    # this is a generator function (it contains yield), calling
    # stream_lines(path) does not read anything yet -- it only starts
    # reading the file as something iterates over the returned generator.
    pass


def stream_matching(path, keyword):
    """Generator built on top of stream_lines: yields only the lines that
    contain `keyword` (case-insensitive). Still line-by-line -- filtering
    happens lazily as each line streams through, not on a pre-built list."""
    # TODO 5: Lowercase `keyword` into a variable (e.g. needle). Loop
    # `for line in stream_lines(path):` and yield `line` whenever
    # `needle in line.lower()`.
    pass


def summarize(path):
    """Streams the whole file once via the generator and builds a summary:
    total line count and a count per log level. Still never holds more
    than the current line in memory -- the counts are the only thing that
    accumulates."""
    # TODO 6: Start `total = 0` and `counts = {level: 0 for level in
    # LEVELS}`. Loop `for line in stream_lines(path):`, incrementing
    # `total` each time, and incrementing `counts[level]` for whichever
    # level's f"[{level}]" tag appears in that line (break out of the
    # inner level-checking loop once you find a match). Return
    # `total, counts`.
    pass


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
        # TODO 7: Use `with SessionTimer("generating sample log file") as
        # timer:` around a call to generate_sample_log(), capturing its
        # return value as num_lines. After the `with` block, set
        # file_ready = True, set last_timer = timer, and print
        # f"Wrote {num_lines} lines to {SAMPLE_FILE}.".
        pass

    elif choice == "2":
        print()
        if not file_ready:
            print("No sample file yet -- choose option 1 first.")
            continue
        keyword = input("Search for keyword (e.g. ERROR, billing): ").strip()
        if not keyword:
            print("Please enter a non-empty keyword.")
            continue
        # TODO 8: Use `with SessionTimer(f"streaming search for
        # '{keyword}'") as timer:` around a loop over
        # stream_matching(SAMPLE_FILE, keyword). Count matches, and print
        # up to the first 10 matching lines as they stream in (e.g.
        # `if matches <= 10: print(f"  {line}")`). After the `with` block,
        # set last_timer = timer, print how many more matches there were
        # beyond the first 10 (if any), and print the total match count.
        pass

    elif choice == "3":
        print()
        if not file_ready:
            print("No sample file yet -- choose option 1 first.")
            continue
        # TODO 9: Use `with SessionTimer("streaming summary") as timer:`
        # around a call to summarize(SAMPLE_FILE), capturing total, counts.
        # After the `with` block, set last_timer = timer and print the
        # summary: total line count, then each level's count from `counts`.
        pass

    elif choice == "4":
        print()
        # TODO 10: Try to print
        # f"Last timed operation: '{last_timer.label}' took "
        # f"{last_timer.elapsed:.4f}s" -- but last_timer only exists once
        # an earlier option has run, so wrap this in a try/except NameError
        # and print "No operation has been timed yet -- try options 1-3
        # first." in the except branch.
        pass

    elif choice == "5":
        print()
        print("Goodbye!")
        break

    else:
        print("Please choose 1-5.")
