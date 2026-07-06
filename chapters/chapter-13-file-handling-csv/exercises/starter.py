"""
Chapter 13 Exercises: File Handling & CSV
See README.md in this folder for full instructions.
Run this from inside the exercises/ folder: python3 starter.py
"""

# TODO 1: Write a function count_lines(filename) that opens the file
# with with, reads all its lines with .readlines(), and returns how
# many there are. Call it with "tasks.txt" and print the result.


# TODO 2: Write a function save_tasks(filename, tasks) that opens
# filename in write mode ("w") and writes each string in the tasks
# list on its own line. Call it with "new_tasks.txt" and
# ["Buy stamps", "Renew license"], then open the file again and print
# its contents.


# TODO 3: Write a function add_task(filename, task) that opens filename
# in append mode ("a") and writes task on a new line. Call it on
# "new_tasks.txt" with "Schedule dentist", then open the file again and
# print its contents - the two tasks from Task 2 should still be there.


# TODO 4: Write a function total_inventory_value(filename) that opens
# filename with csv.DictReader and returns the sum of
# quantity * price across every row (convert row["quantity"] to int
# and row["price"] to float). Call it with "inventory.csv" and print
# the result.


# TODO 5: Write a function
# export_low_stock(input_filename, output_filename, threshold) that
# reads input_filename with csv.DictReader, collects every row where
# int(row["quantity"]) < threshold, and writes those rows to
# output_filename using csv.DictWriter with
# fieldnames=["item", "quantity", "price"] (remember newline="" and
# .writeheader()). Call it with "inventory.csv", "low_stock.csv", and
# 20, then open "low_stock.csv" and print its contents.


# TODO 6: Write a function read_safely(filename) that tries to open and
# read filename, returning its contents. If a FileNotFoundError
# happens, print f"'{filename}' was not found." and return None. Call
# it with "does_not_exist.txt" and print the result.


# TODO 7 (Debug the Code): this code logs each visit to a file, but it
# opens the file in "w" mode instead of "a" mode - every call wipes out
# every visit logged before it, so only the most recent visit ever
# survives. Find and fix the mode so every visit is kept.
def log_visit(filename, username):
    with open(filename, "w") as file:
        file.write(username + " visited\n")

log_visit("visits.txt", "alice")
log_visit("visits.txt", "bob")

with open("visits.txt") as file:
    print(file.read())


# TODO 8 (Debug the Code): this code opens a file the manual way, with
# no with statement and no .close() call at all - a file handle leak.
# Find and fix it so the file is opened with with instead, guaranteeing
# it gets closed automatically.
def read_report(filename):
    file = open(filename)
    contents = file.read()
    return contents

print(read_report("inventory.csv"))
