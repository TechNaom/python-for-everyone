"""
Chapter 7 Exercises: Lists & Tuples — reference solution.
"""

# TODO 1: Given playlist = ["Intro", "Song A", "Song B", "Song C", "Outro"],
# use slicing to print the first 3 songs, then the last 2 songs.
playlist = ["Intro", "Song A", "Song B", "Song C", "Outro"]
print("First 3:", playlist[:3])
print("Last 2:", playlist[-2:])


# TODO 2: Given cart = ["notebook", "pen"], append "eraser", then insert
# "ruler" at position 1, then remove "pen". Print the cart after each step.
cart = ["notebook", "pen"]
cart.append("eraser")
print(cart)
cart.insert(1, "ruler")
print(cart)
cart.remove("pen")
print(cart)


# TODO 3: Given location = ("Austin", "TX", 78701), unpack it into city,
# state, and zip_code, then print: "Austin, TX 78701"
location = ("Austin", "TX", 78701)
city, state, zip_code = location
print(f"{city}, {state} {zip_code}")


# TODO 4: Given the grid below, print the value at row 1, column 2, then
# change row 0, column 0 to 100 and print the whole grid.
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
print(grid[1][2])
grid[0][0] = 100
print(grid)


# TODO 5 (Debug the Code): this is supposed to leave original untouched
# and only change backup, but it changes both. Find and fix the bug.
original = ["draft"]
backup = original.copy()
backup.append("final")
print("original:", original)
print("backup:", backup)


# TODO 6: Given the orders below, loop through them, and for every order
# with status "shipped", print its id and add its amount to a running
# total. Print the total in the form: "Total shipped: $107.25"
orders = [
    ["ORD-3001", 42.50, "shipped"],
    ["ORD-3002", 64.75, "shipped"],
    ["ORD-3003", 10.00, "pending"],
]
total = 0
for order in orders:
    if order[2] == "shipped":
        total = total + order[1]
        print(order[0])
print(f"Total shipped: ${total:.2f}")
