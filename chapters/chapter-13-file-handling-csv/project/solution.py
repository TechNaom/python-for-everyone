"""
Chapter 13 Project: Log-File Analyzer -- reference solution.
See README.md in this folder for the full brief and example output.

This project is built AROUND file handling and the csv module as its core
organizing principle -- every operation reads a real log file with `with`
open()`, processes it using plain Python (dicts, loops, string methods) from
earlier chapters, and the export option writes a real CSV report using
csv.writer. A try/except FileNotFoundError guards the very first read so a
missing log file fails gracefully with a helpful message instead of crashing,
exactly like Chapter 12's exception-handling pattern. Each operation lives in
its own small function, matching Chapter 10's function-library pattern.
"""
import csv


def load_log_lines(log_filename):
    """Return a list of stripped, non-blank lines from log_filename.

    Raises FileNotFoundError if the file doesn't exist -- callers are
    expected to catch it themselves so they can decide how to respond.
    """
    with open(log_filename) as file:
        lines = [line.strip() for line in file if line.strip()]
    return lines


def count_by_level(lines):
    """Return a dict of {level: count} for INFO/WARNING/ERROR lines."""
    counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}
    for line in lines:
        for level in counts:
            if f" {level} " in line:
                counts[level] += 1
                break
    return counts


def search_lines(lines, keyword):
    """Return a list of every line containing keyword (case-insensitive)."""
    matches = []
    for line in lines:
        if keyword.lower() in line.lower():
            matches.append(line)
    return matches


def most_common_error(lines):
    """Return (message, count) for the most frequent ERROR message.

    Returns (None, 0) if there are no ERROR lines at all.
    """
    error_counts = {}
    for line in lines:
        if " ERROR " in line:
            message = line.split("ERROR", 1)[1].strip()
            error_counts[message] = error_counts.get(message, 0) + 1

    if not error_counts:
        return None, 0

    best_message = None
    best_count = 0
    for message, count in error_counts.items():
        if count > best_count:
            best_message = message
            best_count = count
    return best_message, best_count


def export_summary(lines, report_filename):
    """Write a CSV summary of level counts and error-message counts."""
    level_counts = count_by_level(lines)

    error_counts = {}
    for line in lines:
        if " ERROR " in line:
            message = line.split("ERROR", 1)[1].strip()
            error_counts[message] = error_counts.get(message, 0) + 1

    with open(report_filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["category", "label", "count"])
        for level, count in level_counts.items():
            writer.writerow(["level", level, count])
        for message, count in error_counts.items():
            writer.writerow(["error_message", message, count])


def print_level_counts(level_counts):
    """Print level counts as a small aligned table."""
    for level, count in level_counts.items():
        print(f"  {level:<8} {count}")


# --- Session state ---
print("=== Log-File Analyzer ===")
log_filename = "server.log"

try:
    log_lines = load_log_lines(log_filename)
except FileNotFoundError as e:
    print(f"Could not open log file: {e}")
    print("Make sure you're running this from inside the project/ folder.")
    log_lines = None

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
            level_counts = count_by_level(log_lines)
            print("Counts by level:")
            print_level_counts(level_counts)

        elif choice == "2":
            print()
            keyword = input("Keyword to search for: ").strip()
            if not keyword:
                print("Please enter a non-empty keyword.")
            else:
                matches = search_lines(log_lines, keyword)
                if not matches:
                    print(f"No lines matched '{keyword}'.")
                else:
                    print(f"{len(matches)} matching line(s):")
                    for line in matches:
                        print(f"  {line}")

        elif choice == "3":
            print()
            message, count = most_common_error(log_lines)
            if message is None:
                print("No ERROR lines found in this log.")
            else:
                print(f"Most common error: '{message}' ({count} occurrence(s))")

        elif choice == "4":
            print()
            report_filename = input(
                "Report filename to write (e.g. summary.csv): "
            ).strip()
            if not report_filename:
                report_filename = "summary.csv"
            export_summary(log_lines, report_filename)
            print(f"Summary written to '{report_filename}'.")

        elif choice == "5":
            print()
            print("Goodbye!")
            break

        else:
            print("Please choose 1-5.")
