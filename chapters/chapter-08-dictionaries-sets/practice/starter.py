"""
Chapter 8 Practice Bank: Dictionaries & Sets
See README.md in this folder for full instructions.

Only uses what Chapters 1-8 covered: print()/input(), variables, basic
types, operators, if/elif/else, while/for/range/break/continue, strings,
lists/tuples, and this chapter's own toolkit: dictionary literals,
indexing/KeyError, .get() with a default, `in` for key existence, dict
methods (.update(), .pop(), .setdefault(), .keys()/.values()/.items(),
del), looping over dictionaries (for key in dict, .items() unpacking,
insertion order), sets (creation, .add()/.remove(), union/intersection/
difference), and nested dictionaries. No comprehensions, lambda,
functions (def), try/except, file I/O, classes, or imports yet.
"""

# ============================================================
# Topic 1: Creating Dictionaries & Accessing Values
# ============================================================

# TODO 1.1: Given student = {"name": "Asha", "age": 21, "major": "CS"},
# print the whole dictionary, then print the value at key "name" and the
# value at key "age" using square-bracket indexing.


# TODO 1.2: Given prices = {"apple": 1.50, "banana": 0.75}, try to print
# prices["mango"] and add a comment explaining that this raises a
# KeyError because "mango" isn't a key in the dictionary.


# TODO 1.3: Given prices = {"apple": 1.50, "banana": 0.75}, use
# .get("mango", 0) to safely look up a missing key without crashing, and
# print the result. Then use .get("apple", 0) and print that too.


# TODO 1.4: Given inventory = {"pens": 40, "notebooks": 15}, check
# whether "pens" is in inventory and whether "erasers" is in inventory
# using the `in` operator, and print both True/False results.


# TODO 1.5 (Debug the Code): this is supposed to print the price of
# "kiwi", but kiwi isn't a key in prices, so it raises a KeyError. Fix it
# by using .get() with a default of 0 instead of square-bracket indexing.
prices = {"apple": 1.50, "banana": 0.75}
print(prices["kiwi"])


# TODO 1.A (Scenario — Employee Lookup): given
# employee = {"name": "Ravi", "id": 1042, "department": "Sales"}, print
# the employee's name and department using square-bracket indexing, then
# use .get("manager", "Unassigned") to safely print a manager field that
# doesn't exist in the dictionary.


# TODO 1.B (Scenario — Interview Prep): an interviewer asks why you'd
# ever use .get() instead of square brackets. Given
# config = {"debug": True, "retries": 3}, use config["timeout"] inside a
# comment (don't actually run it) to note it would raise a KeyError, then
# show the safe version config.get("timeout", 30) and print it. Add a
# comment explaining that .get() lets you supply a fallback default
# instead of crashing the whole program on a missing key.


# ============================================================
# Topic 2: Dict Methods That Add, Update & Remove
# ============================================================

# TODO 2.1: Given profile = {"name": "Meera", "age": 30}, use .update()
# with {"age": 31, "city": "Pune"} to update the existing "age" key and
# add a new "city" key in one call. Print the updated profile.


# TODO 2.2: Given cart = {"bread": 2, "milk": 1, "eggs": 12}, use .pop()
# to remove "eggs" and print the popped value, then print the remaining
# cart.


# TODO 2.3: Given counts = {"a": 1, "b": 2}, use .setdefault("c", 0) to
# add a new key "c" with default 0 (printing the result), then use
# .setdefault("a", 0) on the existing key "a" and print that it returns
# the existing value (1) without overwriting it. Print the final counts.


# TODO 2.4 (Debug the Code): this is supposed to remove the "temp" key
# from settings, but it raises a KeyError because .pop() with no default
# crashes on a missing key. Fix it by passing a default value to .pop()
# so it doesn't crash when "temp" isn't present.
settings = {"volume": 80, "brightness": 70}
settings.pop("temp")
print(settings)


# TODO 2.5: Given scores = {"Asha": 90, "Ravi": 85, "Meera": 78}, print
# scores.keys(), scores.values(), and scores.items() (each converted to
# a list with list(), e.g. list(scores.keys())). Then use `del` to remove
# the "Ravi" key and print the final scores.


# TODO 2.A (Scenario — Shopping Cart Update): given
# cart = {"shirt": 2, "socks": 5}, use .update() to change "socks" to 3
# and add a new item "hat": 1 in one call, then use .pop("socks") to
# remove socks entirely and print the popped quantity and the final cart.


# TODO 2.B (Scenario — Interview Prep): an interviewer asks the
# difference between .get() and .setdefault(). Given
# tally = {"views": 100}, use tally.setdefault("clicks", 0) and print the
# result and the updated tally (notice "clicks" is now actually a key in
# tally). Add a comment explaining that .get() never modifies the
# dictionary, while .setdefault() inserts the default key if it was
# missing.


# ============================================================
# Topic 3: Looping Over Dictionaries
# ============================================================

# TODO 3.1: Given ages = {"Asha": 21, "Ravi": 24, "Meera": 19}, use a for
# loop over `for name in ages` to print each name on its own line (looping
# over a dict directly loops over its keys).


# TODO 3.2: Given ages = {"Asha": 21, "Ravi": 24, "Meera": 19}, use a for
# loop with .items() and tuple unpacking (`for name, age in ages.items()`)
# to print an f-string line like "Asha is 21" for each person.


# TODO 3.3: Given order = {}, add keys one at a time in this exact order:
# "bread", then "milk", then "eggs" (each mapped to any quantity you
# like), then loop over order with `for item in order` and print each key
# to show that dictionaries preserve insertion order in Python.


# TODO 3.4 (Debug the Code): this is supposed to print each name and
# score on its own line, but it loops over `for pair in scores` and tries
# to print pair[0] and pair[1] as if scores.items() were being unpacked,
# which is wrong because looping over a dict directly only gives you the
# keys, not (key, value) pairs. Fix it by looping over scores.items()
# with name, score unpacking instead.
scores = {"Asha": 90, "Ravi": 85}
for pair in scores:
    print(pair[0], pair[1])


# TODO 3.5: Given prices = {"apple": 1.50, "banana": 0.75, "cherry": 3.00},
# loop over prices.items() with an accumulator variable to add up every
# price, and print the total.


# TODO 3.A (Scenario — Attendance Sheet): given
# attendance = {"Asha": "Present", "Ravi": "Absent", "Meera": "Present"},
# loop over attendance.items() and print an f-string line for each person
# like "Asha: Present", then use a for loop over attendance.items() with
# an accumulator to count how many people are "Present".


# TODO 3.B (Scenario — Interview Prep): an interviewer asks what order a
# for loop visits dictionary keys in. Given
# steps = {"first": "mix", "second": "bake", "third": "cool"}, loop over
# steps.items() and print each step in order, then add a comment
# explaining that since Python 3.7, dictionaries preserve insertion
# order, so this loop always visits "first", "second", "third" in the
# order they were added — not some arbitrary or sorted order.


# ============================================================
# Topic 4: Sets — Unique Collections & Set Operations
# ============================================================

# TODO 4.1: Create a set called colors from the list
# ["red", "blue", "red", "green", "blue"] by calling set() on it, and
# print it to show duplicates are automatically removed. Then create an
# empty set with empty_set = set() (not {}, which makes a dict) and print
# it.


# TODO 4.2: Given tags = {"python", "beginner"}, use .add() to add "free"
# to the set and print the result. Then use .remove() to remove
# "beginner" and print the final set.


# TODO 4.3: Given team_a = {"Asha", "Ravi", "Meera"} and
# team_b = {"Ravi", "Karan"}, print their union with team_a | team_b (or
# team_a.union(team_b)), then print their intersection with
# team_a & team_b (or team_a.intersection(team_b)).


# TODO 4.4 (Debug the Code): this is supposed to remove "cherry" from
# fruits, but "cherry" was never added to the set, so .remove() raises a
# KeyError. Fix it by checking membership with `in` before calling
# .remove(), so it only removes when the value is actually present.
fruits = {"apple", "banana"}
fruits.remove("cherry")
print(fruits)


# TODO 4.5: Given all_students = {"Asha", "Ravi", "Meera", "Karan"} and
# passed_students = {"Asha", "Meera"}, print the difference
# all_students - passed_students (or .difference()) to find which
# students did not pass.


# TODO 4.A (Scenario — Tag Deduplication): given
# raw_tags = ["python", "beginner", "python", "coding", "beginner"],
# build a set called unique_tags from raw_tags to automatically dedupe
# them, and print it.


# TODO 4.B (Scenario — Interview Prep): an interviewer asks why you'd
# use a set instead of a list to check membership. Given
# allowed_ids = {101, 102, 103, 104, 105}, check whether 103 is in
# allowed_ids and whether 999 is in allowed_ids using `in`, and print
# both results. Add a comment explaining that checking `in` on a set is
# much faster than on a list for large collections, because sets use
# hashing instead of scanning every element one by one.


# ============================================================
# Topic 5: Nested Dictionaries & Real-World Records
# ============================================================

# TODO 5.1: Given
# students = {"Asha": {"age": 21, "major": "CS"}, "Ravi": {"age": 24, "major": "EE"}},
# print Asha's age and Ravi's major using double indexing
# (students["Asha"]["age"] and students["Ravi"]["major"]).


# TODO 5.2: Given the same nested students dictionary as above, mutate
# Asha's major with students["Asha"]["major"] = "Data Science" and print
# the updated students dictionary.


# TODO 5.3: Given
# inventory = {"pens": {"price": 1.5, "stock": 100}, "pencils": {"price": 0.5, "stock": 200}},
# loop over inventory.items() with name, details unpacking, and inside
# the loop print an f-string line like "pens: $1.5, 100 in stock" using
# details["price"] and details["stock"].


# TODO 5.4 (Debug the Code): this is supposed to print Ravi's department,
# but it indexes the outer key and the inner key in the wrong order
# (looking up "department" in the outer dict instead of "Ravi" first).
# Fix the indexing order.
records = {"Ravi": {"department": "Sales", "years": 3}}
print(records["department"]["Ravi"])


# TODO 5.5: Given
# company = {"engineering": ["Asha", "Ravi"], "sales": ["Meera", "Karan"]}
# (a dict mapping department names to lists of employee names), print
# the engineering team and the sales team, then loop over
# company.items() with dept, team unpacking and print an f-string line
# like "engineering has 2 people" using len(team) for each department.


# TODO 5.A (Scenario — Customer Order Record): given
# order = {"customer": "Asha", "items": ["pen", "notebook"], "total": 12.50},
# print the customer's name, loop over order["items"] with a for loop to
# print each item, and print the total.


# TODO 5.B (Scenario — Interview Prep): an interviewer asks how you'd
# model "a user with multiple phone numbers" using dicts and lists
# together. Given
# user = {"name": "Meera", "phones": ["555-0100", "555-0199"]}, print the
# user's name, then loop over user["phones"] to print each number. Add a
# comment explaining that combining a dict (for named fields) with a list
# (for a field that can hold many values) is a common pattern for
# modeling real-world records before you learn classes.


# ============================================================
# Topic 6: Real-World Dicts & Sets in Production
# ============================================================

# TODO 6.1: Given
# words = ["cat", "dog", "cat", "bird", "dog", "cat"], build a frequency
# dictionary called counts by looping over words and, for each word,
# using counts[word] = counts.get(word, 0) + 1. Print the final counts.


# TODO 6.2: Given
# emails = ["a@x.com", "b@x.com", "a@x.com", "c@x.com", "b@x.com"], build
# a set called unique_emails from the list to deduplicate it, and print
# both len(emails) and len(unique_emails) to show how many duplicates
# were removed.


# TODO 6.3: Given
# user_lookup = {"u1": "Asha", "u2": "Ravi", "u3": "Meera"} (a lookup
# table mapping user IDs to names), look up "u2" and print the result,
# then use .get("u9", "Unknown user") to safely handle an ID that
# doesn't exist, and print that result too.


# TODO 6.4 (Debug the Code): this is supposed to count how many times
# each grade letter appears in grades, but it uses counts[grade] += 1
# directly without first making sure the key exists, so it raises a
# KeyError the first time a new grade letter shows up. Fix it using
# .get(grade, 0) the same way TODO 6.1 did.
grades = ["A", "B", "A", "C", "B", "A"]
counts = {}
for grade in grades:
    counts[grade] += 1
print(counts)


# TODO 6.5: Given
# team_a_emails = {"asha@x.com", "ravi@x.com", "meera@x.com"} and
# team_b_emails = {"ravi@x.com", "karan@x.com"} (two sets of email
# addresses), print the people who are on both teams using intersection,
# and print the people who are only on team_a using difference.


# TODO 6.A (Scenario — Log Line Word Frequency): given
# log_words = ["error", "timeout", "error", "error", "retry", "timeout"]
# (words pulled from a server log), build a frequency dictionary the same
# way as TODO 6.1, then loop over the frequency dictionary's .items() to
# print each word and its count as an f-string line like "error: 3".


# TODO 6.B (Scenario — Interview Prep): an interviewer gives you
# visitor_ids = ["v1", "v2", "v1", "v3", "v2", "v1"] (a list of visitor
# IDs recorded once per page view) and asks you to find how many unique
# visitors there were. Build a set called unique_visitors from
# visitor_ids and print len(unique_visitors). Then add a comment
# explaining why a set is the right tool here instead of a list: a set
# automatically discards duplicates, so its length alone gives you the
# unique count without writing any extra dedup logic.
