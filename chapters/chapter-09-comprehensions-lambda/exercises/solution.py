"""
Chapter 9 Exercises: Comprehensions, Lambda & Functional Tools — reference solution.
"""

# TODO 1: Given numbers = [3, 8, 12, 15, 20, 27], build a list comprehension
# that squares every number. Then build a second list comprehension that
# keeps only the numbers greater than 10.
numbers = [3, 8, 12, 15, 20, 27]
squares = [n ** 2 for n in numbers]
print(squares)
big_numbers = [n for n in numbers if n > 10]
print(big_numbers)


# TODO 2: Given inventory_prices below, build a dict comprehension that adds
# 7% tax to every price, rounded to 2 decimal places. Then given tags below,
# build a set comprehension of the unique tags.
inventory_prices = {"pens": 1.50, "notebooks": 3.00, "erasers": 0.75}
taxed_prices = {item: round(price * 1.07, 2) for item, price in inventory_prices.items()}
print(taxed_prices)

tags = ["sale", "new", "sale", "clearance", "new"]
unique_tags = {tag for tag in tags}
print(unique_tags)


# TODO 3: Given the nested seating_chart below (a list of rows, each row a
# list of names), use a nested comprehension to flatten it into one list
# of every student's name.
seating_chart = [
    ["Priya", "Amir"],
    ["Zoe", "Leo", "Sam"],
    ["Mia"],
]
all_students = [name for row in seating_chart for name in row]
print(all_students)


# TODO 4: Write a lambda called to_fahrenheit that converts a Celsius value
# to Fahrenheit, rounded to 1 decimal place: F = C * 9 / 5 + 32. Call it
# with 20 and with 0.
to_fahrenheit = lambda c: round(c * 9 / 5 + 32, 1)
print(to_fahrenheit(20))
print(to_fahrenheit(0))


# TODO 5: Given order_totals below, use map() with a lambda to apply a 10%
# discount (rounded to 2 decimals) to every total. Then use filter() with a
# lambda to keep only totals over 20. Finally, given employees below, use
# sorted() with a lambda key to sort the list by salary.
order_totals = [45.00, 12.50, 99.99, 8.25]
with_discount = list(map(lambda t: round(t * 0.9, 2), order_totals))
print(with_discount)
over_20 = list(filter(lambda t: t > 20, order_totals))
print(over_20)

employees = [
    {"name": "Priya", "salary": 72000},
    {"name": "Amir", "salary": 65000},
    {"name": "Zoe", "salary": 81000},
]
by_salary = sorted(employees, key=lambda e: e["salary"])
print(by_salary)


# TODO 6 (Debug the Code): this is supposed to keep only the scores that
# pass with a score strictly greater than 60, but it wrongly includes the
# boundary value 60 itself. Find and fix the bug.
scores = [55, 62, 60, 71, 80, 45, 90]
passing = [s for s in scores if s > 60]
print(passing)


# TODO 7: Given raw_feedback below, clean every comment by stripping
# whitespace. Then filter the list down to only entries with a valid
# (digit) rating, and print each remaining comment with its rating,
# ranked from highest rating to lowest.
raw_feedback = [
    {"comment": "  Great course! ", "rating": "5"},
    {"comment": "could be better", "rating": "oops"},
    {"comment": "Loved it ", "rating": "4"},
]
cleaned = [entry["comment"].strip() for entry in raw_feedback]
print(cleaned)

valid_feedback = [entry for entry in raw_feedback if entry["rating"].isdigit()]
ranked_feedback = sorted(valid_feedback, key=lambda entry: int(entry["rating"]), reverse=True)
for entry in ranked_feedback:
    print(entry["comment"].strip(), "-", entry["rating"])
