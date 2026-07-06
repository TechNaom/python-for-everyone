"""
Chapter 13 Project: Log-File Analyzer
See README.md in this folder for the full brief and example output.

This project is built AROUND file handling and the csv module as its core
organizing principle -- every operation reads a real log file with `with
open()`, processes it using plain Python (dicts, loops, string methods) from
earlier chapters, and the export option writes a real CSV report using
csv.writer. A try/except FileNotFoundError guards the very first read so a
missing log file fails gracefully with a helpful message instead of crashing,
exactly like Chapter 12's exception-handling pattern. Each operation lives in
its own small function, matching Chapter 10's function-library pattern. Fill
in the numbered TODOs below.
"""
import csv


def load_log_lines(log_filename):
    """Return a list of stripped, non-blank lines from log_filename.

    Raises FileNotFoundError if the file doesn't exist -- callers are
    expected to catch it themselves so they can decide how to respond.
    """
    # TODO 1: Open log_filename with `with open(...) as file:`, and build a
    # list of file.strip()'d lines, skipping any line that's blank after
    # stripping (a list comprehension with an `if line.strip()` filter works
    # well here). Return that list. Do NOT catch FileNotFoundError here --
    # let it propagate so the caller can handle it.
    pass


def count_by_level(lines):
    """Return a dict of {level: count} for INFO/WARNING/ERROR lines."""
    # TODO 2: Start counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}. Loop over
    # lines, and for each line check whether f" {level} " appears in it for
    # each level in counts -- if so, increment that level's count and stop
    # checking the other levels for this line (use `break`). Return counts.
    pass


def search_lines(lines, keyword):
    """Return a list of every line containing keyword (case-insensitive)."""
    # TODO 3: Build and return a list of every line in lines where
    # keyword.lower() is found in line.lower().
    pass


def most_common_error(lines):
    """Return (message, count) for the most frequent ERROR message.

    Returns (None, 0) if there are no ERROR lines at all.
    """
    # TODO 4: Build an error_counts dict by looping over lines: whenever
    # " ERROR " is in a line, split it on "ERROR" (line.split("ERROR", 1))
    # and take [1].strip() as the message, then increment
    # error_counts[message] (use .get(message, 0) + 1). If error_counts ends
    # up empty, return (None, 0). Otherwise loop over error_counts.items()
    # tracking the message/count pair with the highest count seen so far,
    # and return (best_message, best_count).
    pass


def export_summary(lines, report_filename):
    """Write a CSV summary of level counts and error-message counts."""
    # TODO 5: Call count_by_level(lines) to get level_counts. Then build an
    # error_counts dict the same way TODO 4 does (loop over lines, split on
    # "ERROR", count each distinct message). Open report_filename with
    # `with open(report_filename, "w", newline="") as file:`, create
    # `writer = csv.writer(file)`, write a header row
    # ["category", "label", "count"], then one row per level
    # (["level", level, count]) and one row per error message
    # (["error_message", message, count]).
    pass


def print_level_counts(level_counts):
    """Print level counts as a small aligned table."""
    # TODO 6: Loop over level_counts.items() and print each as
    # f"  {level:<8} {count}".
    pass


# --- Session state ---
print("=== Log-File Analyzer ===")
log_filename = "server.log"

# TODO 7: Wrap a call to load_log_lines(log_filename) in a try/except
# FileNotFoundError as e. On success, store the result in log_lines. On
# failure, print a helpful message using e (e.g. f"Could not open log file:
# {e}"), remind the learner to cd into the project/ folder, and set
# log_lines = None.

if log_lines is not None:
    print(f"Loaded {len(log_lines)} line(s) from '{log_filename}'.")

    while True:
        print()
        print("1. Show counts by log level")
        print("2. Search for a keyword")
        print("3. Show the most common error message")
        print("4. Export summary to CSV")
        print("5. Quit")
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            print()
            # TODO 8: Call count_by_level(log_lines), print "Counts by
            # level:", then call print_level_counts(...) on the result.
            pass

        elif choice == "2":
            print()
            keyword = input("Keyword to search for: ").strip()
            if not keyword:
                print("Please enter a non-empty keyword.")
            else:
                # TODO 9: Call search_lines(log_lines, keyword). If there are
                # no matches, print f"No lines matched '{keyword}'." Otherwise
                # print how many lines matched, then print each matching
                # line indented with two spaces.
                pass

        elif choice == "3":
            print()
            # TODO 10: Call most_common_error(log_lines). If the message
            # comes back None, print "No ERROR lines found in this log."
            # Otherwise print
            # f"Most common error: '{message}' ({count} occurrence(s))".
            pass

        elif choice == "4":
            print()
            report_filename = input(
                "Report filename to write (e.g. summary.csv): "
            ).strip()
            if not report_filename:
                report_filename = "summary.csv"
            # TODO 11: Call export_summary(log_lines, report_filename), then
            # print f"Summary written to '{report_filename}'."
            pass

        elif choice == "5":
            print()
            print("Goodbye!")
            break

        else:
            print("Please choose 1-5.")
