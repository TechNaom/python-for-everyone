"""
Chapter 13 Exercises: File Handling & CSV — reference solution.
Run this from inside the exercises/ folder: python3 solution.py
"""

import csv

# TODO 1: Write a function count_lines(filename) that opens the file
# with with, reads all its lines with .readlines(), and returns how
# many there are. Call it with "tasks.txt" and print the result.
def count_lines(filename):
    with open(filename) as file:
        lines = file.readlines()
    return len(lines)

print(count_lines("tasks.txt"))


# TODO 2: Write a function save_tasks(filename, tasks) that opens
# filename in write mode ("w") and writes each string in the tasks
# list on its own line. Call it with "new_tasks.txt" and
# ["Buy stamps", "Renew license"], then open the file again and print
# its contents.
def save_tasks(filename, tasks):
    with open(filename, "w") as file:
        for task in tasks:
            file.write(task + "\n")

save_tasks("new_tasks.txt", ["Buy stamps", "Renew license"])
with open("new_tasks.txt") as file:
    print(file.read())


# TODO 3: Write a function add_task(filename, task) that opens filename
# in append mode ("a") and writes task on a new line. Call it on
# "new_tasks.txt" with "Schedule dentist", then open the file again and
# print its contents - the two tasks from Task 2 should still be there.
def add_task(filename, task):
    with open(filename, "a") as file:
        file.write(task + "\n")

add_task("new_tasks.txt", "Schedule dentist")
with open("new_tasks.txt") as file:
    print(file.read())


# TODO 4: Write a function total_inventory_value(filename) that opens
# filename with csv.DictReader and returns the sum of
# quantity * price across every row (convert row["quantity"] to int
# and row["price"] to float). Call it with "inventory.csv" and print
# the result.
def total_inventory_value(filename):
    total = 0.0
    with open(filename) as file:
        reader = csv.DictReader(file)
        for row in reader:
            total += int(row["quantity"]) * float(row["price"])
    return total

print(total_inventory_value("inventory.csv"))


# TODO 5: Write a function
# export_low_stock(input_filename, output_filename, threshold) that
# reads input_filename with csv.DictReader, collects every row where
# int(row["quantity"]) < threshold, and writes those rows to
# output_filename using csv.DictWriter with
# fieldnames=["item", "quantity", "price"] (remember newline="" and
# .writeheader()). Call it with "inventory.csv", "low_stock.csv", and
# 20, then open "low_stock.csv" and print its contents.
def export_low_stock(input_filename, output_filename, threshold):
    low_stock = []
    with open(input_filename) as file:
        reader = csv.DictReader(file)
        for row in reader:
            if int(row["quantity"]) < threshold:
                low_stock.append(row)

    with open(output_filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["item", "quantity", "price"])
        writer.writeheader()
        writer.writerows(low_stock)

export_low_stock("inventory.csv", "low_stock.csv", 20)
with open("low_stock.csv") as file:
    print(file.read())


# TODO 6: Write a function read_safely(filename) that tries to open and
# read filename, returning its contents. If a FileNotFoundError
# happens, print f"'{filename}' was not found." and return None. Call
# it with "does_not_exist.txt" and print the result.
def read_safely(filename):
    try:
        with open(filename) as file:
            return file.read()
    except FileNotFoundError:
        print(f"'{filename}' was not found.")
        return None

print(read_safely("does_not_exist.txt"))


# TODO 7 (Debug the Code): this code logs each visit to a file, but it
# opens the file in "w" mode instead of "a" mode - every call wipes out
# every visit logged before it, so only the most recent visit ever
# survives. Find and fix the mode so every visit is kept.
# Bug: "w" mode erases the file on every call. Fix: use "a" (append)
# mode so each visit is added instead of replacing the last one.
def log_visit(filename, username):
    with open(filename, "a") as file:
        file.write(username + " visited\n")

log_visit("visits.txt", "alice")
log_visit("visits.txt", "bob")

with open("visits.txt") as file:
    print(file.read())


# TODO 8 (Debug the Code): this code opens a file the manual way, with
# no with statement and no .close() call at all - a file handle leak.
# Find and fix it so the file is opened with with instead, guaranteeing
# it gets closed automatically.
# Bug: the file is opened with open() directly and never closed - a
# file handle leak. Fix: use a with block instead, which closes the
# file automatically as soon as the block ends.
def read_report(filename):
    with open(filename) as file:
        contents = file.read()
    return contents

print(read_report("inventory.csv"))
