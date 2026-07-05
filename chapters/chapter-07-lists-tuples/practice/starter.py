"""
Chapter 7 Practice Bank: Lists & Tuples
See README.md in this folder for full instructions.

Only uses what Chapters 1-7 covered: print()/input(), variables, basic
types, operators, if/elif/else, while/for/range/break/continue, string
indexing/slicing/methods/f-strings, and this chapter's own toolkit:
list literals, indexing/negative indexing/slicing, mutability, len(),
the list methods covered in the lesson (append, insert, extend, remove,
pop, clear, sort, sorted(), reverse, count, index), tuples (creation,
indexing/slicing, packing/unpacking), nested lists, and copying lists
with .copy() or slicing. No dictionaries/sets, comprehensions, lambda,
functions (def), or try/except yet.
"""

# ============================================================
# Topic 1: Creating Lists & Accessing Elements
# ============================================================

# TODO 1.1: Given fruits = ["apple", "banana", "cherry", "date"], print
# the whole list, then print its length with len().


# TODO 1.2: Given scores = [88, 92, 79, 95, 84], print the first score
# using a positive index, then print the last score using a negative
# index.


# TODO 1.3: Given letters = ["a", "b", "c", "d", "e", "f"], print the
# sublist from index 1 up to (not including) index 4 using slicing,
# then print the whole list reversed using a slice with a step of -1.


# TODO 1.4: Given inventory = [10, 25, 30], change the second item
# (index 1) to 40 by assigning directly to inventory[1], and print the
# updated list. Then add a comment explaining why inventory[1] = 40
# works fine on a list, but the equivalent word[0] = "b" on a string
# would raise a TypeError.


# TODO 1.5 (Debug the Code): this is supposed to print the last item of
# nums, but it raises an IndexError because valid indices only go up to
# len(nums) - 1, not len(nums). Fix the index.
nums = [10, 20, 30]
print(nums[len(nums)])


# TODO 1.A (Scenario — Employee Roster): given
# roster = ["Asha", "Ravi", "Meera", "Devi", "Karan"], print the first
# employee and the last employee using indexing, then print how many
# employees are on the roster using len().


# TODO 1.B (Scenario — Interview Prep): an interviewer asks what the
# real difference is between a list and a string, since both support
# indexing. Given original = [1, 2, 3], mutate original[0] = 99 and
# print it, then add a comment naming the core distinction (lists are
# mutable, strings are immutable) and why that matters when two
# variables can end up pointing at the same list.


# ============================================================
# Topic 2: List Methods That Grow, Shrink & Reorder
# ============================================================

# TODO 2.1: Given cart = ["bread", "milk"], use .append() to add "eggs"
# to the end, then use .insert() to add "butter" at index 0. Print the
# final cart.


# TODO 2.2: Given weekday_tasks = ["email", "standup"] and
# weekend_tasks = ["laundry", "groceries"], use .extend() to add all of
# weekend_tasks onto weekday_tasks and print the result. Add a comment
# explaining how .extend() differs from .append() here (append would
# have added weekend_tasks as one single nested element instead).


# TODO 2.3: Given queue = ["Alice", "Bob", "Carol", "Dave"], use
# .remove() to remove "Bob" by value, then use .pop(0) to remove and
# return the first remaining item. Print the popped value and the
# final queue.


# TODO 2.4 (Debug the Code): this is supposed to remove "Eve" from
# attendees, but it raises a ValueError because "Eve" isn't in the
# list. Fix it by checking membership with `in` first, and print a
# message instead of crashing when the name isn't present.
attendees = ["Asha", "Ravi", "Meera"]
attendees.remove("Eve")
print(attendees)


# TODO 2.5: Given numbers = [5, 3, 8, 1, 9, 3], call sorted(numbers) and
# print the result alongside numbers (to show sorted() doesn't change
# the original). Then call numbers.sort() and print numbers (now
# changed in place). Then call numbers.reverse() and print numbers.
# Finally print numbers.count(3) and numbers.index(8).


# TODO 2.A (Scenario — To-Do List Manager): given
# todo = ["Write report", "Call client"], append a new task
# "Review budget", then remove "Call client" (marking it done), and
# print the remaining tasks.


# TODO 2.B (Scenario — Interview Prep): an interviewer asks the
# difference between sort() and sorted(). Given data = [4, 2, 7], call
# sorted(data) and print both the result and data (unchanged). Then
# call data.sort() and print data (now mutated). Add a comment
# explaining that sorted() returns a new list and leaves the original
# untouched, while .sort() mutates in place and returns None.


# ============================================================
# Topic 3: Tuples — Immutable Sequences & Packing/Unpacking
# ============================================================

# TODO 3.1: Given point = (3, 7), print point, then print point[0],
# point[1], and point[-1]. Then given coords = (10, 20, 30, 40), print
# the slice coords[1:3].


# TODO 3.2: Given person = ("Asha", 29, "Engineer"), unpack it into
# name, age, role in a single assignment, then print a sentence with an
# f-string using all three.


# TODO 3.3: Given sizes = ("S", "M", "L"), add a comment explaining why
# sizes[0] = "XS" would raise a TypeError (tuples are immutable, just
# like strings). Then build a brand-new tuple by concatenating ("XS",)
# with sizes[1:], reassign it to sizes, and print it.


# TODO 3.4 (Debug the Code): this is supposed to unpack all three
# fields of report, but it only provides two variables for three
# values, raising a ValueError. Fix it by unpacking into the correct
# number of variables.
report = ("Q1", 50000, "Approved")
status, total = report
print(status, total)


# TODO 3.5: Given a = 5 and b = 10, print both, then swap their values
# using tuple packing/unpacking in one line (a, b = b, a), and print
# both again to show the swap worked.


# TODO 3.A (Scenario — GPS Coordinates): given
# location = (12.9716, 77.5946), unpack it into latitude and longitude,
# then print an f-string report line like "Lat: 12.9716, Lon: 77.5946".


# TODO 3.B (Scenario — Interview Prep): an interviewer asks why you'd
# ever use a tuple instead of a list. Given
# weekday = ("Mon", "Tue", "Wed", "Thu", "Fri"), print it, then add a
# comment explaining that weekday.append("Sat") would raise an
# AttributeError (tuples have no append/insert/remove methods at all),
# and why choosing a tuple for data that truly shouldn't change protects
# it from being accidentally mutated elsewhere in a program.


# ============================================================
# Topic 4: Nested Lists & 2D Data
# ============================================================

# TODO 4.1: Given grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]], print grid,
# then print grid[1][2] (row 1, column 2). Then print len(grid) and
# len(grid[0]).


# TODO 4.2: Given grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]], mutate the
# top-left element with grid[0][0] = 100 and print the updated grid.


# TODO 4.3: Given grid = [[1, 2, 3], [4, 5, 6]], use a nested for loop
# (a for loop over each row, and inside it a for loop over each value in
# that row) to print every individual number on its own line.


# TODO 4.4 (Debug the Code): this is supposed to print the value in row
# 0, column 2 (which is 30), but it indexes [row][col] backwards and
# also uses a row index that's out of range (there are only 2 rows).
# Fix the indices.
matrix = [[10, 20, 30], [40, 50, 60]]
print(matrix[2][0])


# TODO 4.5: Given sales = [[100, 200], [150, 250], [300, 100]]
# (each inner list is one store's sales), use a nested for loop with an
# accumulator variable to add up every number in every row, and print
# the grand total.


# TODO 4.A (Scenario — Tic-Tac-Toe Board): given
# board = [["X", "O", "X"], ["O", "X", "O"], ["X", "X", "O"]], check
# whether the top row (board[0]) is all "X" by comparing all three
# positions with and, and print the True/False result.


# TODO 4.B (Scenario — Interview Prep): given matrix = [[1, 2], [3, 4]],
# print matrix[0] (a whole row) and then matrix[0][0] (a single value).
# Add a comment explaining the difference between the two: matrix[0]
# indexes once into the outer list and returns a row (itself a list),
# while matrix[0][0] indexes a second time into that row to reach a
# single element.


# ============================================================
# Topic 5: Copying Lists — Shallow Copies & the is-vs-== Trap
# ============================================================

# TODO 5.1: Given original = [1, 2, 3], set alias = original (not a
# copy), then alias.append(4). Print both original and alias — both
# will show the extra 4. Add a comment explaining that alias = original
# doesn't create a new list; both names point at the same list object.


# TODO 5.2: Given original = [1, 2, 3], create an independent copy with
# safe_copy = original.copy(), append 4 to safe_copy, and print both to
# show original is unaffected. Then do the same thing again using
# slicing instead: another_copy = original[:], append 99 to it, and
# print both original and another_copy.


# TODO 5.3: Given list_a = [1, 2, 3] and list_b = [1, 2, 3] (two
# separately-built lists with equal contents), print list_a == list_b
# and list_a is list_b. Then set list_c = list_a and print
# list_a is list_c.


# TODO 5.4 (Debug the Code): this is supposed to make an independent
# backup of original_scores before editing it, but backup_scores =
# original_scores is just an alias, not a copy — so appending to
# backup_scores incorrectly changes original_scores too. Fix it using
# .copy().
original_scores = [70, 80, 90]
backup_scores = original_scores
backup_scores.append(100)
print(original_scores)


# TODO 5.5: Given nested = [[1, 2], [3, 4]], make a copy with
# shallow = nested.copy(), then mutate shallow[0][0] = 99. Print both
# nested and shallow — notice both show the change. Add a comment
# explaining that .copy() only copies the outer list; the inner lists
# inside it are still the same shared objects, which is why it's called
# a "shallow" copy.


# TODO 5.A (Scenario — Backup Before Editing): given
# original_records = [10, 20, 30], make a true independent copy with
# working_copy = original_records.copy(), then append 40 to working_copy
# and also change working_copy[0] = 999. Print original_records
# (unchanged) and working_copy (edited) to show the backup is safe.


# TODO 5.B (Scenario — Interview Prep): given a = [1, 2] and b = [1, 2],
# print a == b and a is b. Add a comment explaining that == compares
# values (do the lists contain the same elements?) while is compares
# identity (are these literally the same object in memory?) — two
# separately-built lists with equal contents are == but not is.


# ============================================================
# Topic 6: Real-World Lists & Tuples in Production
# ============================================================

# TODO 6.1: Given order_totals = [45.50, 12.00, 78.25, 30.00], use the
# accumulator pattern with a for loop to add them all up, print the
# total, then print the average (total divided by len(order_totals)).


# TODO 6.2: Given points = [(0, 0), (3, 4), (6, 8)] (a list of (x, y)
# tuples), loop over points, unpack each tuple into x and y, and print
# the squared distance from the origin (x ** 2 + y ** 2) for each point.


# TODO 6.3: Given scores = [55, 82, 90, 40, 71], loop over scores and
# use two accumulator variables (passed and failed) to count how many
# scores are >= 60 versus below 60 (a passing threshold). Print both
# counts using f-strings, e.g. f"Passed: {passed}".


# TODO 6.4 (Debug the Code): this is supposed to add up every day's
# sales into a running total, but it uses = instead of += inside the
# loop, so running_total just gets overwritten with the last amount
# instead of accumulating. Fix it.
sales_today = [120, 80, 45, 60]
running_total = 0
for amount in sales_today:
    running_total = amount
print(running_total)


# TODO 6.5: Given raw = [12, 5, 42, 7, 3, 50], build a new list called
# filtered containing only the values >= 10 (loop over raw and
# .append() the ones that qualify), then call filtered.sort() and
# print filtered.


# TODO 6.A (Scenario — Sales Report): given
# sales = [("Widget", 9.99, 3), ("Gadget", 19.99, 1), ("Gizmo", 4.50, 10)]
# (a list of (product, price, qty) tuples), loop over sales, unpack
# each tuple, compute each line's total (price * qty), add it to a
# grand_total accumulator, and print one f-string report line per
# product plus a final grand total line.


# TODO 6.B (Scenario — Interview Prep): given
# readings = [72, 75, 72, 80, 75, 68] (a list of temperature readings
# with duplicates), build a new list unique_readings that keeps only
# the first occurrence of each value (loop over readings, and only
# .append() a value if it's not already in unique_readings). Print
# unique_readings, then — without using min()/max() — use a loop with
# two comparison variables to find and print the lowest and highest
# values, and finally print the average of unique_readings.
