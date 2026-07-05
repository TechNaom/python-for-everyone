"""
Chapter 7 Practice Bank: Lists & Tuples — reference solution.
See README.md in this folder for full instructions.
"""

# ============================================================
# Topic 1: Creating Lists & Accessing Elements
# ============================================================

# TODO 1.1
fruits = ["apple", "banana", "cherry", "date"]
print(fruits)
print(len(fruits))


# TODO 1.2
scores = [88, 92, 79, 95, 84]
print(scores[0])
print(scores[-1])


# TODO 1.3
letters = ["a", "b", "c", "d", "e", "f"]
print(letters[1:4])
print(letters[::-1])


# TODO 1.4
inventory = [10, 25, 30]
inventory[1] = 40
print(inventory)
# Lists are mutable, so inventory[1] = 40 changes the list in place.
# Strings are immutable, so the equivalent word[0] = "b" would raise a
# TypeError — you'd have to build a brand-new string instead.


# TODO 1.5 (Debug the Code)
nums = [10, 20, 30]
print(nums[len(nums) - 1])


# TODO 1.A (Scenario — Employee Roster)
roster = ["Asha", "Ravi", "Meera", "Devi", "Karan"]
print(roster[0])
print(roster[-1])
print(len(roster))


# TODO 1.B (Scenario — Interview Prep)
original = [1, 2, 3]
original[0] = 99
print(original)
# Lists are mutable — you can change an element in place with index
# assignment. Strings are immutable, so the equivalent word[0] = "Z"
# would raise a TypeError; you'd have to build a new string instead.
# This matters because two variables pointing at the same list can see
# each other's in-place changes, while two variables pointing at the
# same string never can (more on this in the copying-lists topic).


# ============================================================
# Topic 2: List Methods That Grow, Shrink & Reorder
# ============================================================

# TODO 2.1
cart = ["bread", "milk"]
cart.append("eggs")
cart.insert(0, "butter")
print(cart)


# TODO 2.2
weekday_tasks = ["email", "standup"]
weekend_tasks = ["laundry", "groceries"]
weekday_tasks.extend(weekend_tasks)
print(weekday_tasks)
# extend() adds each item from weekend_tasks individually, while
# append(weekend_tasks) would have added the whole list as one single
# nested element instead.


# TODO 2.3
queue = ["Alice", "Bob", "Carol", "Dave"]
queue.remove("Bob")
first_in_line = queue.pop(0)
print(first_in_line)
print(queue)


# TODO 2.4 (Debug the Code)
attendees = ["Asha", "Ravi", "Meera"]
if "Eve" in attendees:
    attendees.remove("Eve")
else:
    print("Eve is not in the list")
print(attendees)


# TODO 2.5
numbers = [5, 3, 8, 1, 9, 3]
ascending = sorted(numbers)
print(ascending)
print(numbers)
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
print(numbers.count(3))
print(numbers.index(8))


# TODO 2.A (Scenario — To-Do List Manager)
todo = ["Write report", "Call client"]
todo.append("Review budget")
todo.remove("Call client")
print(todo)


# TODO 2.B (Scenario — Interview Prep)
data = [4, 2, 7]
ascending_data = sorted(data)
print(ascending_data)
print(data)
data.sort()
print(data)
# sorted(data) builds and returns a brand-new sorted list, leaving data
# untouched. data.sort() instead mutates data in place and returns
# None — calling print(data.sort()) would print "None".


# ============================================================
# Topic 3: Tuples — Immutable Sequences & Packing/Unpacking
# ============================================================

# TODO 3.1
point = (3, 7)
print(point)
print(point[0])
print(point[1])
print(point[-1])
coords = (10, 20, 30, 40)
print(coords[1:3])


# TODO 3.2
person = ("Asha", 29, "Engineer")
name, age, role = person
print(f"{name} is a {age}-year-old {role}")


# TODO 3.3
sizes = ("S", "M", "L")
# Tuples are immutable, just like strings — sizes[0] = "XS" would raise
# a TypeError. To change a "size", build a brand-new tuple instead.
sizes = ("XS",) + sizes[1:]
print(sizes)


# TODO 3.4 (Debug the Code)
report = ("Q1", 50000, "Approved")
status, total, note = report
print(status, total, note)


# TODO 3.5
a = 5
b = 10
print(a, b)
a, b = b, a
print(a, b)


# TODO 3.A (Scenario — GPS Coordinates)
location = (12.9716, 77.5946)
latitude, longitude = location
print(f"Lat: {latitude}, Lon: {longitude}")


# TODO 3.B (Scenario — Interview Prep)
weekday = ("Mon", "Tue", "Wed", "Thu", "Fri")
print(weekday)
# A tuple signals "this data is fixed" — weekday.append("Sat") would
# raise an AttributeError because tuples have no append/insert/remove
# methods at all, unlike lists. Choosing a tuple for data that truly
# shouldn't change (like a fixed set of weekdays or a coordinate pair)
# protects it from being accidentally mutated elsewhere in a program.


# ============================================================
# Topic 4: Nested Lists & 2D Data
# ============================================================

# TODO 4.1
grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(grid)
print(grid[1][2])
print(len(grid))
print(len(grid[0]))


# TODO 4.2
grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
grid[0][0] = 100
print(grid)


# TODO 4.3
grid = [[1, 2, 3], [4, 5, 6]]
for row in grid:
    for value in row:
        print(value)


# TODO 4.4 (Debug the Code)
matrix = [[10, 20, 30], [40, 50, 60]]
print(matrix[0][2])


# TODO 4.5
sales = [[100, 200], [150, 250], [300, 100]]
grand_total = 0
for row in sales:
    for amount in row:
        grand_total = grand_total + amount
print(grand_total)


# TODO 4.A (Scenario — Tic-Tac-Toe Board)
board = [["X", "O", "X"], ["O", "X", "O"], ["X", "X", "O"]]
top_row_all_x = board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X"
print(top_row_all_x)


# TODO 4.B (Scenario — Interview Prep)
matrix = [[1, 2], [3, 4]]
print(matrix[0])
print(matrix[0][0])
# matrix[0] indexes once into the outer list and returns a whole row (a
# list, e.g. [1, 2]). matrix[0][0] indexes a second time — first into
# the outer list to get that row, then again into the row itself to
# reach a single value.


# ============================================================
# Topic 5: Copying Lists — Shallow Copies & the is-vs-== Trap
# ============================================================

# TODO 5.1
original = [1, 2, 3]
alias = original
alias.append(4)
print(original)
print(alias)
# alias = original doesn't make a copy — both names point at the same
# list object, so appending through alias also changes what original
# sees.


# TODO 5.2
original = [1, 2, 3]
safe_copy = original.copy()
safe_copy.append(4)
print(original)
print(safe_copy)
another_copy = original[:]
another_copy.append(99)
print(original)
print(another_copy)


# TODO 5.3
list_a = [1, 2, 3]
list_b = [1, 2, 3]
print(list_a == list_b)
print(list_a is list_b)
list_c = list_a
print(list_a is list_c)


# TODO 5.4 (Debug the Code)
original_scores = [70, 80, 90]
backup_scores = original_scores.copy()
backup_scores.append(100)
print(original_scores)


# TODO 5.5
nested = [[1, 2], [3, 4]]
shallow = nested.copy()
shallow[0][0] = 99
print(nested)
print(shallow)
# .copy() only copies the outer list — the inner lists inside it are
# still the same shared objects, so mutating a nested element through
# shallow also changes nested. This is why it's called a "shallow"
# copy.


# TODO 5.A (Scenario — Backup Before Editing)
original_records = [10, 20, 30]
working_copy = original_records.copy()
working_copy.append(40)
working_copy[0] = 999
print(original_records)
print(working_copy)


# TODO 5.B (Scenario — Interview Prep)
a = [1, 2]
b = [1, 2]
print(a == b)
print(a is b)
# == compares values (do the lists contain the same elements?), while
# is compares identity (are these literally the same object in
# memory?). Two separately-built lists with equal contents are ==
# but not is.


# ============================================================
# Topic 6: Real-World Lists & Tuples in Production
# ============================================================

# TODO 6.1
order_totals = [45.50, 12.00, 78.25, 30.00]
total = 0
for amount in order_totals:
    total = total + amount
print(total)
print(total / len(order_totals))


# TODO 6.2
points = [(0, 0), (3, 4), (6, 8)]
for point in points:
    x, y = point
    squared_distance = x ** 2 + y ** 2
    print(squared_distance)


# TODO 6.3
scores = [55, 82, 90, 40, 71]
passed = 0
failed = 0
for score in scores:
    if score >= 60:
        passed = passed + 1
    else:
        failed = failed + 1
print(f"Passed: {passed}")
print(f"Failed: {failed}")


# TODO 6.4 (Debug the Code)
sales_today = [120, 80, 45, 60]
running_total = 0
for amount in sales_today:
    running_total = running_total + amount
print(running_total)


# TODO 6.5
raw = [12, 5, 42, 7, 3, 50]
filtered = []
for value in raw:
    if value >= 10:
        filtered.append(value)
filtered.sort()
print(filtered)


# TODO 6.A (Scenario — Sales Report)
sales = [("Widget", 9.99, 3), ("Gadget", 19.99, 1), ("Gizmo", 4.50, 10)]
grand_total = 0
for item in sales:
    name, price, qty = item
    line_total = price * qty
    grand_total = grand_total + line_total
    print(f"{name:<10}{line_total:>8.2f}")
print(f"Grand total: {grand_total:.2f}")


# TODO 6.B (Scenario — Interview Prep)
readings = [72, 75, 72, 80, 75, 68]
unique_readings = []
for value in readings:
    if value not in unique_readings:
        unique_readings.append(value)
print(unique_readings)

lowest = unique_readings[0]
highest = unique_readings[0]
for value in unique_readings:
    if value < lowest:
        lowest = value
    if value > highest:
        highest = value
print(lowest)
print(highest)

reading_total = 0
for value in unique_readings:
    reading_total = reading_total + value
print(reading_total / len(unique_readings))
