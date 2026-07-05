"""
Chapter 9 Practice Bank: Comprehensions, Lambda & Functional Tools
See README.md in this folder for full instructions.

Only uses what Chapters 1-9 covered: print()/input(), variables, basic
types, operators, if/elif/else, while/for/range/break/continue, strings,
lists/tuples, dicts/sets, and this chapter's own toolkit: list
comprehensions (with and without a filter if), dict and set
comprehensions, nested comprehensions, lambda functions, and the
functional tools map(), filter(), and sorted()/.sort() with
key=lambda. No def (that's Chapter 10), try/except, file I/O, classes,
or imports yet.
"""

# ============================================================
# Topic 1: List Comprehensions
# ============================================================

# TODO 1.1: Given numbers = [1, 2, 3, 4, 5], build squares_loop with a
# plain for loop and .append(), then build squares_comp with a list
# comprehension that does the same thing. Print both lists.


# TODO 1.2: Given numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], use a list
# comprehension with an if filter to build evens, a list containing only
# the even numbers. Print evens.


# TODO 1.3: Given words = ["cat", "elephant", "dog", "hippopotamus", "ox"],
# use a list comprehension with an if filter to build long_words, a list
# of only the words with more than 3 letters. Print long_words.


# TODO 1.4: Given numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], use one list
# comprehension that both filters (keep only even numbers) and
# transforms (square them) to build even_squares. Print even_squares.


# TODO 1.5 (Debug the Code): this is supposed to build a list of each
# name's length, but the comprehension is missing the expression before
# the for clause, so it raises a SyntaxError. Fix it by adding len(name)
# as the expression.
names = ["Asha", "Ravi", "Meera"]
lengths = [for name in names]
print(lengths)


# TODO 1.A (Scenario — Cleaning Form Input): given
# raw_entries = ["  Asha  ", "Ravi ", "  Meera"] (raw values typed into a
# form, with stray whitespace), use a list comprehension with .strip()
# to build cleaned_entries, and print it.


# TODO 1.B (Scenario — Interview Prep): an interviewer asks why you'd
# prefer a list comprehension over a manual for loop with .append() for a
# simple transform. Given prices = [10, 20, 30], build doubled using a
# list comprehension and print it. Add a comment explaining that
# comprehensions are usually shorter, avoid a manual .append() call, and
# make the "build a new list from an old one" intent obvious at a glance.


# ============================================================
# Topic 2: Dict & Set Comprehensions
# ============================================================

# TODO 2.1: Given words = ["cat", "elephant", "dog"], build a dict
# comprehension word_lengths mapping each word to its length
# (len(word)), and print it.


# TODO 2.2: Given scores = {"Asha": 90, "Ravi": 55, "Meera": 78}, use a
# dict comprehension with an if filter to build passing, a dict
# containing only the entries where the value is 60 or higher. Print
# passing.


# TODO 2.3: Given words = ["cat", "dog", "owl", "elephant", "ox"], use a
# set comprehension to build unique_lengths, a set of the distinct word
# lengths that appear. Print unique_lengths.


# TODO 2.4: Given names = ["Asha", "Ravi", "Meera"] and
# ages = [21, 24, 19] (two parallel lists, same order), use a dict
# comprehension over range(len(names)) to build name_to_age, mapping
# names[i] to ages[i] for each index i. Print name_to_age.


# TODO 2.5 (Debug the Code): this is supposed to build a dict mapping
# each number to its square, but it uses square brackets instead of
# curly braces with a colon, which builds a list of tuples instead of a
# dict comprehension. Fix it to use { } with a colon between key and
# value.
numbers = [1, 2, 3, 4]
squares = [n: n * n for n in numbers]
print(squares)


# TODO 2.A (Scenario — Price Lookup Table): given
# products = ["pen", "notebook", "eraser"] and prices = [1.5, 3.0, 0.75]
# (two parallel lists), use a dict comprehension over range(len(products))
# to build a lookup table price_lookup mapping each product to its price,
# and print it.


# TODO 2.B (Scenario — Interview Prep): an interviewer asks when you'd
# use a set comprehension instead of a list comprehension. Given
# emails = ["a@x.com", "b@x.com", "a@x.com", "c@x.com"], build
# unique_domains as a set comprehension that pulls out the part after
# "@" for each email using email.split("@")[1]. Print unique_domains, and
# add a comment explaining that a set comprehension is the right choice
# when you only care about distinct values and don't need to keep
# duplicates or a specific order.


# ============================================================
# Topic 3: Nested Comprehensions & Readability Limits
# ============================================================

# TODO 3.1: Given
# nested = [[1, 2, 3], [4, 5], [6, 7, 8, 9]] (a list of lists), use a
# nested list comprehension (for row in nested for value in row) to build
# flat, a single flattened list of every number. Print flat.


# TODO 3.2: Use a nested list comprehension to build a multiplication
# table called table as a list of lists, where table[i][j] holds
# (i + 1) * (j + 1) for i and j both ranging over range(3). Print table.


# TODO 3.3: Given
# nested = [[1, 2, 3], [4, 5], [6, 7, 8, 9]], use a nested list
# comprehension with an if filter (for row in nested for value in row if
# value % 2 == 0) to build flat_evens, containing only the even numbers
# across every inner list. Print flat_evens.


# TODO 3.4 (Debug the Code): this is supposed to flatten nested into flat,
# but the for clauses are written in the wrong order (iterating value
# before row is defined), which raises a NameError. Fix the order so row
# comes before value.
nested = [[1, 2], [3, 4]]
flat = [value for value in row for row in nested]
print(flat)


# TODO 3.5: Given the same nested = [[1, 2, 3], [4, 5], [6, 7, 8, 9]],
# rewrite the flattening from TODO 3.1 as an equivalent, more readable for
# loop (two nested for loops with .append()) into flat_readable, print it,
# then add a comment saying which version (the comprehension or the
# loop) you find easier to read and why.


# TODO 3.A (Scenario — Flattening Nested Survey Data): given
# dept_names = [["Asha", "Ravi"], ["Meera"], ["Karan", "Priya", "Zoe"]]
# (a list of per-department name lists), use a nested list comprehension
# to build all_names, one flat list of every name across every
# department. Print all_names.


# TODO 3.B (Scenario — Interview Prep): an interviewer asks why deeply
# nested comprehensions can be a problem in production code. Given
# matrix = [[1, 2], [3, 4], [5, 6]], build flat_matrix with a nested
# comprehension and print it. Add a comment explaining that once a
# comprehension needs more than one for clause or an if plus a for, it
# often becomes harder to read than a plain nested for loop, so
# production code should favor clarity over cleverness once nesting
# grows.


# ============================================================
# Topic 4: Lambda Functions
# ============================================================

# TODO 4.1: Write a lambda called double that takes one argument n and
# returns n * 2. Call double(5) and print the result.


# TODO 4.2: Write a lambda called add that takes two arguments a and b
# and returns their sum. Call add(3, 4) and print the result.


# TODO 4.3: Store a lambda called square (takes n, returns n * n) in a
# variable, then call it three times with 2, 5, and 10, printing each
# result.


# TODO 4.4: Write a lambda called even_or_odd that takes one argument n
# and returns the string "even" if n is divisible by 2, otherwise "odd",
# using a conditional expression (`"even" if n % 2 == 0 else "odd"`)
# inside the lambda body. Call it with 4 and with 7, printing both
# results.


# TODO 4.5 (Debug the Code): this is supposed to be a lambda that triples
# a number, but it incorrectly uses a return statement inside the lambda
# body, which raises a SyntaxError (lambda bodies are a single expression
# with no return keyword). Fix it by removing return.
triple = lambda n: return n * 3
print(triple(4))


# TODO 4.A (Scenario — Quick One-Off Formatter): write a lambda called
# format_price that takes a number price and returns an f-string like
# "$9.99" using an f-string inside the lambda (f"${price:.2f}"). Call it
# with 9.5 and print the result.


# TODO 4.B (Scenario — Interview Prep): an interviewer asks about the
# single-expression limitation of lambda and when you'd reach for def
# instead. Write a lambda called is_adult that takes age and returns
# age >= 18, call it with 16 and with 21, and print both results. Add a
# comment explaining that a lambda can only contain one expression (no
# statements, no multiple lines, no loops), so anything needing several
# steps, a loop, or a docstring should be a regular def function instead.


# ============================================================
# Topic 5: map(), filter(), and sorted() with key=lambda
# ============================================================

# TODO 5.1: Given words = ["cat", "elephant", "dog"], use map() with a
# lambda to build word_lengths, converting each word to its length.
# Wrap the map() result in list() and print it.


# TODO 5.2: Given numbers = [-3, 5, -1, 8, 0, -7, 2], use filter() with a
# lambda to build positives, keeping only numbers greater than 0. Wrap
# the filter() result in list() and print it.


# TODO 5.3: Given
# pairs = [("Asha", 90), ("Ravi", 55), ("Meera", 78)] (a list of
# name-score tuples), use sorted() with key=lambda pair: pair[1] to build
# by_score, sorted from lowest score to highest. Print by_score.


# TODO 5.4: Given
# people = [{"name": "Asha", "age": 21}, {"name": "Ravi", "age": 19},
# {"name": "Meera", "age": 24}] (a list of dicts), use .sort() in place
# with key=lambda person: person["age"] to sort people by age. Print
# people afterward.


# TODO 5.5 (Debug the Code): this is supposed to sort products by price,
# but the lambda references "cost" instead of "price", which raises a
# KeyError. Fix the key name.
products = [{"name": "pen", "price": 1.5}, {"name": "bag", "price": 20.0}]
by_price = sorted(products, key=lambda item: item["cost"])
print(by_price)


# TODO 5.A (Scenario — Sorting Employee Records): given
# employees = [{"name": "Asha", "salary": 72000},
# {"name": "Ravi", "salary": 65000}, {"name": "Meera", "salary": 81000}],
# use sorted() with key=lambda emp: emp["salary"] to build
# by_salary_desc, sorted from highest to lowest salary (use
# reverse=True). Print by_salary_desc.


# TODO 5.B (Scenario — Interview Prep): an interviewer asks why
# map(lambda n: n * 2, numbers) doesn't print anything useful by itself.
# Given numbers = [1, 2, 3], print(map(lambda n: n * 2, numbers)) first
# to see the map object printed, then print(list(map(lambda n: n * 2,
# numbers))) to see the actual values. Add a comment explaining that
# map() and filter() return lazy iterator objects, not lists, so you
# must wrap them in list() (or loop over them) to see or use their
# contents.


# ============================================================
# Topic 6: Real-World Comprehensions & Functional Tools in Production
# ============================================================

# TODO 6.1: Given
# raw_lines = ["  error: timeout\n", "", "  retry attempt\n", "   ", "ok\n"]
# (raw lines pulled from a log file, with stray whitespace and blank
# lines), use a list comprehension that strips each line with .strip()
# and keeps it only if the stripped result is not an empty string, to
# build cleaned_lines. Print cleaned_lines.


# TODO 6.2: Given
# records = [{"id": "u1", "name": "Asha"}, {"id": "u2", "name": "Ravi"}],
# use a dict comprehension over records to build id_to_name, mapping each
# record's "id" to its "name". Print id_to_name.


# TODO 6.3: Given
# raw_ages = ["21", "nineteen", "24", "30", "abc"] (a batch of user-
# submitted ages, some not valid numbers), use filter() with a lambda
# (lambda a: a.isdigit()) to keep only the numeric-looking strings, then
# use a list comprehension to convert the filtered results to integers
# with int(a). Store the final list in valid_ages and print it.


# TODO 6.4 (Debug the Code): this pipeline is supposed to convert a batch
# of numeric strings to integers and then keep only the ones over 18, but
# it filters with `a > 18` before converting from strings to integers, so
# comparing a string to an int raises a TypeError. Fix it by converting
# to int first (with a comprehension or map()) and then filtering.
raw_ages = ["16", "21", "30", "17"]
adults = [a for a in raw_ages if a > 18]
print(adults)


# TODO 6.5: Given
# products = [{"name": "pen", "score": 4.2}, {"name": "bag", "score": 3.8},
# {"name": "mug", "score": 4.9}], use sorted() with
# key=lambda p: p["score"] and reverse=True to build ranked, sorted from
# highest score to lowest. Print ranked.


# TODO 6.A (Scenario — Deduplicating and Sorting API Results): given
# raw_results = ["banana", "apple", "banana", "cherry", "apple"] (a raw
# list of names returned by an API call, possibly with duplicates), build
# a set comprehension unique_results from raw_results, convert it to a
# list with sorted() (which also sorts it alphabetically), and print the
# final sorted_results.


# TODO 6.B (Scenario — Interview Prep): an interviewer asks why
# comprehensions and functional tools like map()/filter()/sorted() show
# up so often in real data-cleaning pipelines. Given
# raw_scores = [" 88", "92 ", " 75 ", "60"], use a list comprehension
# with .strip() and int() to build clean_scores, then use sorted() to
# build ranked_scores from highest to lowest with reverse=True. Print
# both clean_scores and ranked_scores. Add a comment explaining that
# comprehensions and functional tools let you express an entire
# "clean, filter, transform, sort" pipeline in a few readable lines
# instead of many lines of manual loops with temporary lists.
