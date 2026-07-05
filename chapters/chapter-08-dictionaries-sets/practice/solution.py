"""
Chapter 8 Practice Bank: Dictionaries & Sets — reference solution.
See README.md in this folder for full instructions.
"""

# ============================================================
# Topic 1: Creating Dictionaries & Accessing Values
# ============================================================

# TODO 1.1
student = {"name": "Asha", "age": 21, "major": "CS"}
print(student)
print(student["name"])
print(student["age"])


# TODO 1.2
prices = {"apple": 1.50, "banana": 0.75}
# print(prices["mango"]) would raise a KeyError, because "mango" is not
# a key in prices — square-bracket indexing crashes on a missing key.


# TODO 1.3
prices = {"apple": 1.50, "banana": 0.75}
print(prices.get("mango", 0))
print(prices.get("apple", 0))


# TODO 1.4
inventory = {"pens": 40, "notebooks": 15}
print("pens" in inventory)
print("erasers" in inventory)


# TODO 1.5 (Debug the Code)
prices = {"apple": 1.50, "banana": 0.75}
print(prices.get("kiwi", 0))


# TODO 1.A (Scenario — Employee Lookup)
employee = {"name": "Ravi", "id": 1042, "department": "Sales"}
print(employee["name"])
print(employee["department"])
print(employee.get("manager", "Unassigned"))


# TODO 1.B (Scenario — Interview Prep)
config = {"debug": True, "retries": 3}
# config["timeout"] would raise a KeyError since "timeout" isn't a key.
print(config.get("timeout", 30))
# .get() lets you supply a fallback default instead of crashing the
# whole program on a missing key, unlike square-bracket indexing.


# ============================================================
# Topic 2: Dict Methods That Add, Update & Remove
# ============================================================

# TODO 2.1
profile = {"name": "Meera", "age": 30}
profile.update({"age": 31, "city": "Pune"})
print(profile)


# TODO 2.2
cart = {"bread": 2, "milk": 1, "eggs": 12}
popped_eggs = cart.pop("eggs")
print(popped_eggs)
print(cart)


# TODO 2.3
counts = {"a": 1, "b": 2}
print(counts.setdefault("c", 0))
print(counts.setdefault("a", 0))
print(counts)


# TODO 2.4 (Debug the Code)
settings = {"volume": 80, "brightness": 70}
settings.pop("temp", None)
print(settings)


# TODO 2.5
scores = {"Asha": 90, "Ravi": 85, "Meera": 78}
print(list(scores.keys()))
print(list(scores.values()))
print(list(scores.items()))
del scores["Ravi"]
print(scores)


# TODO 2.A (Scenario — Shopping Cart Update)
cart = {"shirt": 2, "socks": 5}
cart.update({"socks": 3, "hat": 1})
popped_socks = cart.pop("socks")
print(popped_socks)
print(cart)


# TODO 2.B (Scenario — Interview Prep)
tally = {"views": 100}
print(tally.setdefault("clicks", 0))
print(tally)
# .get() never modifies the dictionary, even if the key is missing —
# it just returns the default. .setdefault() actually inserts the
# default value as a real key if it wasn't already present.


# ============================================================
# Topic 3: Looping Over Dictionaries
# ============================================================

# TODO 3.1
ages = {"Asha": 21, "Ravi": 24, "Meera": 19}
for name in ages:
    print(name)


# TODO 3.2
ages = {"Asha": 21, "Ravi": 24, "Meera": 19}
for name, age in ages.items():
    print(f"{name} is {age}")


# TODO 3.3
order = {}
order["bread"] = 2
order["milk"] = 1
order["eggs"] = 12
for item in order:
    print(item)


# TODO 3.4 (Debug the Code)
scores = {"Asha": 90, "Ravi": 85}
for name, score in scores.items():
    print(name, score)


# TODO 3.5
prices = {"apple": 1.50, "banana": 0.75, "cherry": 3.00}
total = 0
for name, price in prices.items():
    total = total + price
print(total)


# TODO 3.A (Scenario — Attendance Sheet)
attendance = {"Asha": "Present", "Ravi": "Absent", "Meera": "Present"}
for name, status in attendance.items():
    print(f"{name}: {status}")
present_count = 0
for name, status in attendance.items():
    if status == "Present":
        present_count = present_count + 1
print(present_count)


# TODO 3.B (Scenario — Interview Prep)
steps = {"first": "mix", "second": "bake", "third": "cool"}
for step_name, action in steps.items():
    print(step_name, action)
# Since Python 3.7, dictionaries preserve insertion order, so this loop
# always visits "first", "second", "third" in the order they were
# added — not some arbitrary or sorted order.


# ============================================================
# Topic 4: Sets — Unique Collections & Set Operations
# ============================================================

# TODO 4.1
colors = set(["red", "blue", "red", "green", "blue"])
print(colors)
empty_set = set()
print(empty_set)


# TODO 4.2
tags = {"python", "beginner"}
tags.add("free")
print(tags)
tags.remove("beginner")
print(tags)


# TODO 4.3
team_a = {"Asha", "Ravi", "Meera"}
team_b = {"Ravi", "Karan"}
print(team_a | team_b)
print(team_a & team_b)


# TODO 4.4 (Debug the Code)
fruits = {"apple", "banana"}
if "cherry" in fruits:
    fruits.remove("cherry")
print(fruits)


# TODO 4.5
all_students = {"Asha", "Ravi", "Meera", "Karan"}
passed_students = {"Asha", "Meera"}
print(all_students - passed_students)


# TODO 4.A (Scenario — Tag Deduplication)
raw_tags = ["python", "beginner", "python", "coding", "beginner"]
unique_tags = set(raw_tags)
print(unique_tags)


# TODO 4.B (Scenario — Interview Prep)
allowed_ids = {101, 102, 103, 104, 105}
print(103 in allowed_ids)
print(999 in allowed_ids)
# Checking `in` on a set is much faster than on a list for large
# collections, because sets use hashing to look values up directly
# instead of scanning every element one by one.


# ============================================================
# Topic 5: Nested Dictionaries & Real-World Records
# ============================================================

# TODO 5.1
students = {"Asha": {"age": 21, "major": "CS"}, "Ravi": {"age": 24, "major": "EE"}}
print(students["Asha"]["age"])
print(students["Ravi"]["major"])


# TODO 5.2
students = {"Asha": {"age": 21, "major": "CS"}, "Ravi": {"age": 24, "major": "EE"}}
students["Asha"]["major"] = "Data Science"
print(students)


# TODO 5.3
inventory = {"pens": {"price": 1.5, "stock": 100}, "pencils": {"price": 0.5, "stock": 200}}
for name, details in inventory.items():
    print(f"{name}: ${details['price']}, {details['stock']} in stock")


# TODO 5.4 (Debug the Code)
records = {"Ravi": {"department": "Sales", "years": 3}}
print(records["Ravi"]["department"])


# TODO 5.5
company = {"engineering": ["Asha", "Ravi"], "sales": ["Meera", "Karan"]}
print(company["engineering"])
print(company["sales"])
for dept, team in company.items():
    print(f"{dept} has {len(team)} people")


# TODO 5.A (Scenario — Customer Order Record)
order = {"customer": "Asha", "items": ["pen", "notebook"], "total": 12.50}
print(order["customer"])
for item in order["items"]:
    print(item)
print(order["total"])


# TODO 5.B (Scenario — Interview Prep)
user = {"name": "Meera", "phones": ["555-0100", "555-0199"]}
print(user["name"])
for phone in user["phones"]:
    print(phone)
# Combining a dict (for named fields like "name") with a list (for a
# field that can hold many values, like "phones") is a common pattern
# for modeling real-world records before you learn classes.


# ============================================================
# Topic 6: Real-World Dicts & Sets in Production
# ============================================================

# TODO 6.1
words = ["cat", "dog", "cat", "bird", "dog", "cat"]
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
print(counts)


# TODO 6.2
emails = ["a@x.com", "b@x.com", "a@x.com", "c@x.com", "b@x.com"]
unique_emails = set(emails)
print(len(emails))
print(len(unique_emails))


# TODO 6.3
user_lookup = {"u1": "Asha", "u2": "Ravi", "u3": "Meera"}
print(user_lookup["u2"])
print(user_lookup.get("u9", "Unknown user"))


# TODO 6.4 (Debug the Code)
grades = ["A", "B", "A", "C", "B", "A"]
counts = {}
for grade in grades:
    counts[grade] = counts.get(grade, 0) + 1
print(counts)


# TODO 6.5
team_a_emails = {"asha@x.com", "ravi@x.com", "meera@x.com"}
team_b_emails = {"ravi@x.com", "karan@x.com"}
print(team_a_emails & team_b_emails)
print(team_a_emails - team_b_emails)


# TODO 6.A (Scenario — Log Line Word Frequency)
log_words = ["error", "timeout", "error", "error", "retry", "timeout"]
word_freq = {}
for word in log_words:
    word_freq[word] = word_freq.get(word, 0) + 1
for word, freq in word_freq.items():
    print(f"{word}: {freq}")


# TODO 6.B (Scenario — Interview Prep)
visitor_ids = ["v1", "v2", "v1", "v3", "v2", "v1"]
unique_visitors = set(visitor_ids)
print(len(unique_visitors))
# A set automatically discards duplicates, so its length alone gives
# you the unique count without writing any extra dedup logic — no
# manual "if not in" checks needed like with a list.
