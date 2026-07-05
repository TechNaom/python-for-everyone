"""
Chapter 8 Exercises: Dictionaries & Sets — reference solution.
"""

# TODO 1: Given student = {"name": "Maria", "age": 20, "major": "Biology"},
# print the student's name and major. Then use .get() to safely print the
# student's "gpa" with a fallback of "N/A", since "gpa" isn't a key here.
student = {"name": "Maria", "age": 20, "major": "Biology"}
print(student["name"])
print(student["major"])
print(student.get("gpa", "N/A"))


# TODO 2: Given inventory = {"pens": 40, "notebooks": 25}, add a new key
# "erasers" set to 15. Then use .update() to add "markers": 10 and change
# "pens" to 35, both in one call. Print the inventory after each step.
inventory = {"pens": 40, "notebooks": 25}
inventory["erasers"] = 15
print(inventory)
inventory.update({"markers": 10, "pens": 35})
print(inventory)


# TODO 3: Given scores = {"Maria": 88, "Jae": 95, "Tomas": 71}, loop over
# the dictionary with .items() and print each name and score. Also build
# a running total of every score and print the average score.
scores = {"Maria": 88, "Jae": 95, "Tomas": 71}
total = 0
for name, score in scores.items():
    print(name, "-", score)
    total = total + score
print("Average:", total / len(scores))


# TODO 4: Given the two sets below, print the union, the intersection, and
# the difference (people in weekday_class but not weekend_class).
weekday_class = {"Maria", "Jae", "Tomas"}
weekend_class = {"Jae", "Priya"}
print(weekday_class | weekend_class)
print(weekday_class & weekend_class)
print(weekday_class - weekend_class)


# TODO 5: Given the nested dictionary below, print Jae's major, then add
# a new "gpa" field to Tomas's record set to 3.4, then print Tomas's whole
# record.
students = {
    "Jae": {"age": 24, "major": "Physics"},
    "Tomas": {"age": 21, "major": "History"},
}
print(students["Jae"]["major"])
students["Tomas"]["gpa"] = 3.4
print(students["Tomas"])


# TODO 6 (Debug the Code): this is supposed to tally how many times each
# fruit appears in the list below, but it crashes. Find and fix the bug.
fruits = ["apple", "banana", "apple", "cherry", "banana", "apple"]
tally = {}
for fruit in fruits:
    tally[fruit] = tally.get(fruit, 0) + 1
print(tally)


# TODO 7: Given the list of orders below (each one a dictionary with
# "id", "amount", and "status" keys), loop through them, and for every
# order with status "shipped", print its id and add its amount to a
# running total. Print the total in the form: "Total shipped: $107.25"
orders = [
    {"id": "ORD-4001", "amount": 42.50, "status": "shipped"},
    {"id": "ORD-4002", "amount": 64.75, "status": "shipped"},
    {"id": "ORD-4003", "amount": 10.00, "status": "pending"},
]
total = 0
for order in orders:
    if order["status"] == "shipped":
        total = total + order["amount"]
        print(order["id"])
print(f"Total shipped: ${total:.2f}")
