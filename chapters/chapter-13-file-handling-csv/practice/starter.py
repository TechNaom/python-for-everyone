"""
Chapter 13 Practice Bank: File Handling & CSV
See README.md in this folder for full instructions.
Run this from inside the practice/ folder: python3 starter.py
"""

import csv

# ============================================================
# Topic 1: Opening & Reading Files
# ============================================================

# TODO 1.1: Write a function read_whole_file(filename) that opens the
# file with with and returns file.read() (the entire contents as one
# string). Call it with "notes.txt" and print the result.


# TODO 1.2: Write a function count_lines(filename) that opens the file
# with with, reads all its lines with .readlines(), and returns how
# many there are. Call it with "notes.txt" and print the result.


# TODO 1.3: Write a function first_line(filename) that opens the file
# with with and returns file.readline().strip() -- just the first
# line, with its trailing newline removed. Call it with "notes.txt"
# and print the result.


# TODO 1.4: Write a function lines_as_list(filename) that opens the
# file with with, loops over the file object directly, and returns a
# list of each line with .strip() applied. Call it with "notes.txt"
# and print the result.


# TODO 1.5 (Debug the Code): this function is supposed to read a whole
# file into a string using with, but it opens the file the manual way
# with no with statement and no .close() call at all -- a file handle
# leak. Fix it by opening the file with with instead.
def read_report(filename):
    file = open(filename)
    contents = file.read()
    return contents


print(read_report("notes.txt"))


# TODO 1.A (Scenario -- Loading a Config File at Startup): write a
# function load_startup_settings(filename) that opens filename with
# with and returns file.readlines() -- modeling how a real program
# reads its saved settings, one setting per line, the moment it
# starts up. Call it with "settings.txt" and print the result.


# TODO 1.B (Scenario -- Interview Prep): an interviewer asks the
# difference between .read() and .readlines(). Write a function
# explain_read_vs_readlines() that returns a string explaining that
# .read() returns the entire file as one single string, while
# .readlines() (or looping over the file directly) returns the
# content split into separate lines -- which is what a program
# actually wants when each line is its own record (a task, a log
# entry, a row of data) rather than one undifferentiated blob of
# text. Call it and print the result.


# ============================================================
# Topic 2: Writing to Files
# ============================================================

# TODO 2.1: Write a function save_lines(filename, lines) that opens
# filename in "w" mode and writes each string in the lines list on
# its own line (remember .write() doesn't add "\n" automatically).
# Call it with "saved_notes.txt" and ["Buy milk", "Call the bank"],
# then open the file again and print its contents.


# TODO 2.2: Write a function append_line(filename, line) that opens
# filename in "a" mode and writes line on a new line. Call it on
# "saved_notes.txt" with "Finish the report", then open the file
# again and print its contents -- the two lines from Topic 2.1 should
# still be there.


# TODO 2.3: Write a function overwrite_file(filename, text) that opens
# filename in "w" mode and writes text, erasing whatever was there
# before. Call it on "saved_notes.txt" with
# "Only this line survives now\n", then open the file again and print
# its contents -- everything from 2.1/2.2 should be gone.


# TODO 2.4: Write a function write_numbered_lines(filename, items)
# that opens filename in "w" mode and writes each item in items on
# its own line, prefixed with its 1-based position like "1. ", "2. ",
# using enumerate(items, start=1). Call it with "checklist.txt" and
# ["Pack bags", "Charge phone"], then open the file again and print
# its contents.


# TODO 2.5 (Debug the Code): this code is supposed to build up a log
# of events over multiple calls, but it opens the file in "w" mode
# instead of "a" mode -- every call wipes out every event logged
# before it, so only the most recent call's message ever survives.
# Fix the mode so every call's message is kept.
def log_message(filename, message):
    with open(filename, "w") as file:
        file.write(message + "\n")


log_message("app_events.txt", "started")
log_message("app_events.txt", "processed request")
with open("app_events.txt") as file:
    print(file.read())


# TODO 2.A (Scenario -- Appending to a Shared Audit Log): write a
# function record_audit_event(filename, username, action) that opens
# filename in "a" mode and writes f"{username}: {action}\n" --
# modeling a security audit log that must never lose a prior entry
# just because a new one is being added. Call it twice on
# "audit_log.txt": once with ("alice", "logged in") and once with
# ("bob", "updated profile"), then open the file and print its
# contents.


# TODO 2.B (Scenario -- Interview Prep): an interviewer asks what the
# real-world risk is of mixing up "w" and "a" mode. Write a function
# explain_w_vs_a_risk() that returns a string explaining that "w"
# mode erases a file's existing content the instant it's opened,
# before a single new byte is written, while "a" mode adds new
# content after what's already there -- and that the real risk in
# production code is opening a file meant to accumulate data (a log,
# a running history) in "w" mode by mistake, silently and permanently
# destroying every prior entry with no undo, often without the
# program raising any error at all. Call it and print the result.


# ============================================================
# Topic 3: File Modes & Paths
# ============================================================

# TODO 3.1: Write a function make_mode_summary() that returns a dict
# mapping each of the four core file modes to a short description:
# {"r": "read only, the default", "w": "write only, erases existing
# content", "a": "append only, adds after existing content", "r+":
# "read and write, without erasing first"}. Call it and print the
# result.


# TODO 3.2: Write a function increment_counter_file(filename) that
# opens filename in "r+" mode, reads its current value with
# int(file.read()), calls file.seek(0) to move back to the start, and
# writes back str(value + 1). Before calling it, write "5" to
# "counter.txt" in "w" mode. Then call increment_counter_file on
# "counter.txt", open it again, and print its contents (should be
# "6").


# TODO 3.3: Write a function describe_path_kind(path) that returns
# "absolute" if path starts with "/" (or has a drive letter like
# "C:"), and "relative" otherwise. Call it with "notes.txt" and with
# "/home/user/notes.txt", printing both results.


# TODO 3.4: Write a function read_with_explicit_mode(filename) that
# opens filename with the explicit mode "r" (instead of relying on
# the default) and returns file.read(). Call it with "notes.txt" and
# print the result.


# TODO 3.5 (Debug the Code): this function is supposed to add amount
# to a stored balance without erasing it first, but it opens the file
# in "w" mode -- which erases the file's existing content before
# int(file.read()) even runs, so the read always fails on an empty
# file. Fix it by opening the file in "r+" mode instead.
def top_up_balance(filename, amount):
    with open(filename, "w") as file:
        value = int(file.read())
        file.seek(0)
        file.write(str(value + amount))


with open("balance.txt", "w") as file:
    file.write("100")
top_up_balance("balance.txt", 25)
with open("balance.txt") as file:
    print(file.read())


# TODO 3.A (Scenario -- "It Works on My Machine"): write a function
# explain_relative_path_bug(cwd, script_folder) that returns a string
# explaining the bug when cwd != script_folder: running from cwd
# while the script and its data file live in script_folder means a
# relative path like "notes.txt" resolves against cwd instead, so
# Python looks in the wrong folder and raises FileNotFoundError --
# even though the file genuinely exists right next to the script. If
# cwd == script_folder, return a string saying the relative path
# resolves correctly instead. Call it with
# ("/home/alice", "/home/alice/project") and with
# ("/home/alice/project", "/home/alice/project"), printing both
# results.


# TODO 3.B (Scenario -- Interview Prep): an interviewer asks why
# absolute paths aren't just "the safer default". Write a function
# explain_absolute_path_tradeoff() that returns a string explaining
# that an absolute path always points to the exact same file no
# matter where a program is launched from, but it hard-codes one
# specific location on one specific machine, so the program breaks
# the moment the project moves to a different folder or computer --
# real projects usually prefer relative paths run from a known,
# consistent working directory instead. Call it and print the
# result.


# ============================================================
# Topic 4: The csv Module
# ============================================================

# TODO 4.1: Write a function read_csv_rows(filename) that opens
# filename, uses csv.reader(file), and returns a list of every row
# (each row is itself a list of strings). Call it with "sales.csv"
# and print the result.


# TODO 4.2: Write a function read_csv_as_dicts(filename) that opens
# filename, uses csv.DictReader(file), and returns a list of every
# row as a dictionary. Call it with "sales.csv" and print the result.


# TODO 4.3: Write a function total_sales_value(filename) that opens
# filename with csv.DictReader and returns the sum of
# float(row["price"]) across every row, rounded to 2 decimal places.
# Call it with "sales.csv" and print the result.


# TODO 4.4: Write a function write_products_csv(filename, products)
# that opens filename in "w" mode with newline="", uses csv.writer,
# writes a header row ["product", "price"], then writes one row per
# (product, price) tuple in the products list. Call it with
# "new_products.csv" and [("Widget", 19.99), ("Gadget", 34.50)], then
# open the file again and print its contents.


# TODO 4.5 (Debug the Code): this function is supposed to write a
# list of dictionaries to a CSV file using csv.DictWriter, but it
# forgot to pass newline="" when opening the file -- on some systems
# this causes extra blank lines to appear between each written row.
# Fix it by adding newline="" to the open() call.
def write_records_csv(filename, records):
    with open(filename, "w") as file:
        writer = csv.DictWriter(file, fieldnames=["product", "quantity"])
        writer.writeheader()
        writer.writerows(records)


write_records_csv(
    "restock.csv",
    [{"product": "Widget", "quantity": 4}, {"product": "Gadget", "quantity": 2}],
)
with open("restock.csv") as file:
    print(file.read())


# TODO 4.A (Scenario -- Importing a Spreadsheet Export): write a
# function find_expensive_products(filename, minimum_price) that
# opens filename with csv.DictReader and returns a list of every
# row["product"] where float(row["price"]) >= minimum_price --
# modeling a real task of filtering an exported spreadsheet for
# products above a price threshold. Call it with "sales.csv" and 20,
# printing the result.


# TODO 4.B (Scenario -- Interview Prep): an interviewer asks why
# production code should use the csv module instead of hand-splitting
# lines with .split(","). Write a function explain_csv_module_value()
# that returns a string explaining that hand-splitting breaks the
# instant a field itself contains a comma (like a quoted company
# name), silently turning one row into the wrong number of fields,
# while the csv module understands quoting rules and parses every row
# correctly regardless -- a subtly wrong field count can corrupt
# downstream data without ever raising an error to notice. Call it and
# print the result.


# ============================================================
# Topic 5: Handling File-Related Exceptions
# ============================================================

# TODO 5.1: Write a function read_safely(filename) that tries to open
# and read filename, returning its contents. If a FileNotFoundError
# happens, return None instead. Call it with "does_not_exist.txt" and
# print the result.


# TODO 5.2: Write a function read_safely_with_message(filename) that
# tries to open and read filename, returning its contents. Catch
# "FileNotFoundError as e" and return f"Could not open file: {e}"
# instead. Call it with "does_not_exist.txt" and print the result.


# TODO 5.3: Write a function load_or_default(filename, default_text)
# that tries to open and read filename, returning its contents. Catch
# FileNotFoundError and return default_text instead. Call it with
# ("does_not_exist.txt", "default content") and print the result.


# TODO 5.4: Write a function open_for_either_error(filename) that
# tries to open and read filename, returning its contents, with a
# separate "except FileNotFoundError" returning "not found" and a
# separate "except PermissionError" returning "not permitted". Call
# it with "does_not_exist.txt" and print the result.


# TODO 5.5 (Debug the Code): this function is supposed to safely
# return an empty string when a config file is missing, but it
# catches TypeError instead of FileNotFoundError, so a genuinely
# missing file still crashes the program with an uncaught
# FileNotFoundError. Fix it by catching FileNotFoundError.
def load_config(filename):
    try:
        with open(filename) as file:
            return file.read()
    except TypeError:
        return ""


print(load_config("missing_config.txt"))


# TODO 5.A (Scenario -- Defensive Startup Loader): write a function
# load_user_preferences(filename) that tries to open and read
# filename, returning its contents. Catch FileNotFoundError, printing
# f"'{filename}' doesn't exist yet -- using default preferences." and
# returning "theme=light\n" instead. Also catch PermissionError,
# printing f"Not allowed to read '{filename}' -- using default
# preferences." and returning "theme=light\n" -- modeling a real app
# that must never crash just because a user's settings file hasn't
# been created yet. Call it with "preferences.txt" and print the
# result.


# TODO 5.B (Scenario -- Interview Prep): an interviewer asks why
# Python code usually prefers catching FileNotFoundError over
# checking if a file exists first. Write a function
# explain_check_first_vs_try_it() that returns a string explaining
# that checking "does this file exist?" before calling open() leaves
# a timing gap between the check and the actual open -- the file
# could be deleted, moved, or have its permissions changed in
# between, however unlikely that sounds -- while catching
# FileNotFoundError directly around the open() call is both simpler
# and immune to that gap. Call it and print the result.


# ============================================================
# Topic 6: Bringing It Together -- File & CSV Processing in Production
# ============================================================

# TODO 6.1: Write a function count_error_lines(log_filename) that
# tries to open log_filename, count how many lines contain "ERROR",
# and return that count -- catching FileNotFoundError and returning 0
# instead of crashing. Call it with "app.log" and print the result.


# TODO 6.2: Write a function export_summary_csv(counts,
# report_filename) that opens report_filename in "w" mode with
# newline="", uses csv.writer, writes a header row
# ["level", "count"], then writes one row per (level, count) pair
# from the counts dict's .items(). Call it with
# {"ERROR": 3, "WARNING": 1, "INFO": 3} and "level_summary.csv", then
# open the file again and print its contents.


# TODO 6.3: Write a function count_log_levels(log_filename) that
# tries to open log_filename, and for each line, checks each of
# "ERROR", "WARNING", "INFO" in turn -- incrementing a counts dict
# entry for the first one found in that line and then breaking out of
# that inner loop (so a line is only counted once, under its highest-
# priority matching level). Catch FileNotFoundError and return {}
# instead of crashing. Call it with "app.log" and print the result.


# TODO 6.4: Write a function merge_csv_reports(filenames,
# output_filename) that loops over filenames, tries opening each one
# with csv.DictReader (catching FileNotFoundError per file and
# skipping to the next one with continue if a file is missing),
# collects every row from every file that does open successfully
# into one combined list, and writes that combined list to
# output_filename using csv.DictWriter with the fieldnames captured
# from the first successfully opened file's reader.fieldnames (don't
# forget newline="", .writeheader(), and .writerows()). Call it with
# ["sales.csv", "sales_extra.csv"] and "combined_sales.csv", then
# open the output file and print its contents.


# TODO 6.5 (Debug the Code): this function is supposed to sum the
# "amount" column from an orders CSV file, returning 0.0 if the file
# is missing, but it never actually catches FileNotFoundError at all
# -- open()'s exception is completely unhandled, so a missing orders
# file crashes the whole function instead of returning a safe
# fallback. Fix it by wrapping the body in try/except FileNotFoundError.
def process_orders_file(filename):
    total = 0.0
    with open(filename) as file:
        reader = csv.DictReader(file)
        for row in reader:
            total += float(row["amount"])
    return round(total, 2)


print(process_orders_file("orders.csv"))


# TODO 6.A (Scenario -- Nightly Batch Report Job): write a function
# run_nightly_report(log_filename, report_filename) that tries
# opening log_filename, and for each line containing "ERROR", splits
# out the message after "ERROR" and counts occurrences per distinct
# message in a counts dict. If log_filename is missing, catch
# FileNotFoundError, print
# f"Log file '{log_filename}' not found -- skipping tonight's
# report." and return False. Otherwise, write the counts dict out to
# report_filename as a CSV with header ["error_message",
# "occurrences"] (remember newline=""), and return True -- modeling a
# real batch job that must never crash the whole nightly run just
# because one night's log file wasn't generated. Call it with
# ("app.log", "nightly_report.csv"), print the True/False result,
# then open "nightly_report.csv" and print its contents.


# TODO 6.B (Scenario -- Interview Prep): an interviewer asks you to
# describe the overall pattern real production code uses for file and
# CSV processing. Write a function explain_production_file_pattern()
# that returns a string explaining that real production file
# processing follows one repeated shape: read defensively with
# try/except so a missing or unreadable input file can't crash an
# entire batch job, process the data with plain Python logic, and
# write the result back out with the csv module so another tool or a
# spreadsheet can consume it -- all of it wrapped in with so every
# file handle, on both the read side and the write side, gets closed
# automatically even if something above it fails. Call it and print
# the result.
