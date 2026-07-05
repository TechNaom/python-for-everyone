"""
Chapter 9 Practice Bank: Comprehensions, Lambda & Functional Tools — reference solution.
See README.md in this folder for full instructions.
"""

# ============================================================
# Topic 1: List Comprehensions
# ============================================================

# TODO 1.1
numbers = [1, 2, 3, 4, 5]
squares_loop = []
for n in numbers:
    squares_loop.append(n * n)
squares_comp = [n * n for n in numbers]
print(squares_loop)
print(squares_comp)


# TODO 1.2
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [n for n in numbers if n % 2 == 0]
print(evens)


# TODO 1.3
words = ["cat", "elephant", "dog", "hippopotamus", "ox"]
long_words = [word for word in words if len(word) > 3]
print(long_words)


# TODO 1.4
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares = [n * n for n in numbers if n % 2 == 0]
print(even_squares)


# TODO 1.5 (Debug the Code)
names = ["Asha", "Ravi", "Meera"]
lengths = [len(name) for name in names]
print(lengths)


# TODO 1.A (Scenario — Cleaning Form Input)
raw_entries = ["  Asha  ", "Ravi ", "  Meera"]
cleaned_entries = [entry.strip() for entry in raw_entries]
print(cleaned_entries)


# TODO 1.B (Scenario — Interview Prep)
prices = [10, 20, 30]
doubled = [price * 2 for price in prices]
print(doubled)
# Comprehensions are usually shorter, avoid a manual .append() call, and
# make the "build a new list from an old one" intent obvious at a glance
# compared to a multi-line for loop.


# ============================================================
# Topic 2: Dict & Set Comprehensions
# ============================================================

# TODO 2.1
words = ["cat", "elephant", "dog"]
word_lengths = {word: len(word) for word in words}
print(word_lengths)


# TODO 2.2
scores = {"Asha": 90, "Ravi": 55, "Meera": 78}
passing = {name: score for name, score in scores.items() if score >= 60}
print(passing)


# TODO 2.3
words = ["cat", "dog", "owl", "elephant", "ox"]
unique_lengths = {len(word) for word in words}
print(unique_lengths)


# TODO 2.4
names = ["Asha", "Ravi", "Meera"]
ages = [21, 24, 19]
name_to_age = {names[i]: ages[i] for i in range(len(names))}
print(name_to_age)


# TODO 2.5 (Debug the Code)
numbers = [1, 2, 3, 4]
squares = {n: n * n for n in numbers}
print(squares)


# TODO 2.A (Scenario — Price Lookup Table)
products = ["pen", "notebook", "eraser"]
prices = [1.5, 3.0, 0.75]
price_lookup = {products[i]: prices[i] for i in range(len(products))}
print(price_lookup)


# TODO 2.B (Scenario — Interview Prep)
emails = ["a@x.com", "b@x.com", "a@x.com", "c@x.com"]
unique_domains = {email.split("@")[1] for email in emails}
print(unique_domains)
# A set comprehension is the right choice when you only care about
# distinct values and don't need to keep duplicates or a specific order.


# ============================================================
# Topic 3: Nested Comprehensions & Readability Limits
# ============================================================

# TODO 3.1
nested = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
flat = [value for row in nested for value in row]
print(flat)


# TODO 3.2
table = [[(i + 1) * (j + 1) for j in range(3)] for i in range(3)]
print(table)


# TODO 3.3
nested = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
flat_evens = [value for row in nested for value in row if value % 2 == 0]
print(flat_evens)


# TODO 3.4 (Debug the Code)
nested = [[1, 2], [3, 4]]
flat = [value for row in nested for value in row]
print(flat)


# TODO 3.5
nested = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
flat_readable = []
for row in nested:
    for value in row:
        flat_readable.append(value)
print(flat_readable)
# The plain nested for loop is easier to read step by step, but the
# comprehension is shorter once you're used to the pattern — for simple
# flattening like this, either is fine; the comprehension starts to hurt
# readability once more filters or transforms get added on top.


# TODO 3.A (Scenario — Flattening Nested Survey Data)
dept_names = [["Asha", "Ravi"], ["Meera"], ["Karan", "Priya", "Zoe"]]
all_names = [name for dept in dept_names for name in dept]
print(all_names)


# TODO 3.B (Scenario — Interview Prep)
matrix = [[1, 2], [3, 4], [5, 6]]
flat_matrix = [value for row in matrix for value in row]
print(flat_matrix)
# Once a comprehension needs more than one for clause or an if plus a
# for, it often becomes harder to read than a plain nested for loop, so
# production code should favor clarity over cleverness once nesting grows.


# ============================================================
# Topic 4: Lambda Functions
# ============================================================

# TODO 4.1
double = lambda n: n * 2
print(double(5))


# TODO 4.2
add = lambda a, b: a + b
print(add(3, 4))


# TODO 4.3
square = lambda n: n * n
print(square(2))
print(square(5))
print(square(10))


# TODO 4.4
even_or_odd = lambda n: "even" if n % 2 == 0 else "odd"
print(even_or_odd(4))
print(even_or_odd(7))


# TODO 4.5 (Debug the Code)
triple = lambda n: n * 3
print(triple(4))


# TODO 4.A (Scenario — Quick One-Off Formatter)
format_price = lambda price: f"${price:.2f}"
print(format_price(9.5))


# TODO 4.B (Scenario — Interview Prep)
is_adult = lambda age: age >= 18
print(is_adult(16))
print(is_adult(21))
# A lambda can only contain one expression (no statements, no multiple
# lines, no loops), so anything needing several steps, a loop, or a
# docstring should be a regular def function instead.


# ============================================================
# Topic 5: map(), filter(), and sorted() with key=lambda
# ============================================================

# TODO 5.1
words = ["cat", "elephant", "dog"]
word_lengths = list(map(lambda word: len(word), words))
print(word_lengths)


# TODO 5.2
numbers = [-3, 5, -1, 8, 0, -7, 2]
positives = list(filter(lambda n: n > 0, numbers))
print(positives)


# TODO 5.3
pairs = [("Asha", 90), ("Ravi", 55), ("Meera", 78)]
by_score = sorted(pairs, key=lambda pair: pair[1])
print(by_score)


# TODO 5.4
people = [{"name": "Asha", "age": 21}, {"name": "Ravi", "age": 19}, {"name": "Meera", "age": 24}]
people.sort(key=lambda person: person["age"])
print(people)


# TODO 5.5 (Debug the Code)
products = [{"name": "pen", "price": 1.5}, {"name": "bag", "price": 20.0}]
by_price = sorted(products, key=lambda item: item["price"])
print(by_price)


# TODO 5.A (Scenario — Sorting Employee Records)
employees = [{"name": "Asha", "salary": 72000}, {"name": "Ravi", "salary": 65000}, {"name": "Meera", "salary": 81000}]
by_salary_desc = sorted(employees, key=lambda emp: emp["salary"], reverse=True)
print(by_salary_desc)


# TODO 5.B (Scenario — Interview Prep)
numbers = [1, 2, 3]
print(map(lambda n: n * 2, numbers))
print(list(map(lambda n: n * 2, numbers)))
# map() and filter() return lazy iterator objects, not lists, so you must
# wrap them in list() (or loop over them) to see or use their contents.


# ============================================================
# Topic 6: Real-World Comprehensions & Functional Tools in Production
# ============================================================

# TODO 6.1
raw_lines = ["  error: timeout\n", "", "  retry attempt\n", "   ", "ok\n"]
cleaned_lines = [line.strip() for line in raw_lines if line.strip() != ""]
print(cleaned_lines)


# TODO 6.2
records = [{"id": "u1", "name": "Asha"}, {"id": "u2", "name": "Ravi"}]
id_to_name = {record["id"]: record["name"] for record in records}
print(id_to_name)


# TODO 6.3
raw_ages = ["21", "nineteen", "24", "30", "abc"]
numeric_ages = filter(lambda a: a.isdigit(), raw_ages)
valid_ages = [int(a) for a in numeric_ages]
print(valid_ages)


# TODO 6.4 (Debug the Code)
raw_ages = ["16", "21", "30", "17"]
adults = [int(a) for a in raw_ages if int(a) > 18]
print(adults)


# TODO 6.5
products = [{"name": "pen", "score": 4.2}, {"name": "bag", "score": 3.8}, {"name": "mug", "score": 4.9}]
ranked = sorted(products, key=lambda p: p["score"], reverse=True)
print(ranked)


# TODO 6.A (Scenario — Deduplicating and Sorting API Results)
raw_results = ["banana", "apple", "banana", "cherry", "apple"]
unique_results = {name for name in raw_results}
sorted_results = sorted(unique_results)
print(sorted_results)


# TODO 6.B (Scenario — Interview Prep)
raw_scores = [" 88", "92 ", " 75 ", "60"]
clean_scores = [int(score.strip()) for score in raw_scores]
ranked_scores = sorted(clean_scores, reverse=True)
print(clean_scores)
print(ranked_scores)
# Comprehensions and functional tools let you express an entire "clean,
# filter, transform, sort" pipeline in a few readable lines instead of
# many lines of manual loops with temporary lists.
