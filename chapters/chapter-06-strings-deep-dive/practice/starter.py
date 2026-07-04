"""
Chapter 6 Practice Bank: Strings Deep Dive
See README.md in this folder for full instructions.

Only uses what Chapters 1-6 covered: print(), variables, basic types,
input(), operators, if/elif/else, while/for + range(), the accumulator
pattern, len(), indexing/slicing, the string methods from this chapter,
f-strings, and iterating a string or a .split() result with a bare
for-loop. No lists/dicts, comprehensions, functions, or try/except yet.
"""

# ============================================================
# Topic 1: Indexing & Slicing
# ============================================================

# TODO 1.1: Given word = "Programming", print the first character using
# a positive index, then print the last character using a negative index.


# TODO 1.2: Given phrase = "Hello, World!", print its length with len(),
# then print the slice from index 7 up to (not including) index 12.


# TODO 1.3: Given code = "abcdefghij", print every other character
# starting from the beginning, using slicing with a step of 2.


# TODO 1.4: Given word = "Python", print the word reversed using slicing
# with a step of -1.


# TODO 1.5 (Debug the Code): this is supposed to print the last character
# of word, but it raises an IndexError because valid indices only go up
# to len(word) - 1, not len(word). Fix the index.
word = "Python"
print(word[len(word)])


# TODO 1.A (Scenario — Phone Number Parser): given
# phone = "(555) 123-4567", use slicing to pull out just the area code
# "555" (it sits at positions 1 through 3) and print it.


# TODO 1.B (Scenario — Interview Prep): an interviewer asks whether
# slicing out of range crashes the way indexing does. Given word = "cat",
# print word[0:100] to show slicing just stops at the end of the string
# instead of raising an error, then add a comment explaining why a plain
# index like word[100] would raise IndexError but this slice doesn't.


# ============================================================
# Topic 2: Common String Methods
# ============================================================

# TODO 2.1: Given raw_input_text = "   mpapasani   ", clean the leading
# and trailing whitespace with .strip() and print the cleaned value
# wrapped in square brackets, e.g. print("[" + cleaned + "]"), so the
# missing spaces are obvious.


# TODO 2.2: Given city = "new york", print city.upper(), city.lower(),
# city.title(), and city.capitalize() so you can compare all four side
# by side.


# TODO 2.3: Given phone_raw = "555-123-4567", use .replace() to remove
# the dashes and print the cleaned number.


# TODO 2.4 (Debug the Code): this code looks for "cat" inside text using
# .index(), which raises a ValueError and crashes because "cat" isn't
# present. Fix it by switching to .find() (which returns -1 instead of
# crashing) and print "Not found" when the result is -1, or the position
# otherwise.
text = "The quick brown fox"
position = text.index("cat")
print(position)


# TODO 2.5: Given text = "Hello World Hello Python", print how many times
# "Hello" appears using .count(). Then use text.split() with a bare
# for-loop and an accumulator variable to count the total number of
# words in text (don't index into the split result — just loop over it).


# TODO 2.A (Scenario — Filename Validator): given
# filename = "server_log_2024.txt", print whether it starts with
# "server_log" using .startswith() and whether it ends with ".txt" using
# .endswith().


# TODO 2.B (Scenario — Interview Prep): given
# stored_username = "Manohar" and typed_username = "manohar", print
# whether stored_username == typed_username (it will be False), then
# print whether their .lower() versions are equal. Add a comment
# explaining why a login check should usually compare lowercased text.


# ============================================================
# Topic 3: String Formatting with f-strings
# ============================================================

# TODO 3.1: Given name = "Asha" and age = 22, print a sentence using an
# f-string that embeds both variables, e.g. "Asha is 22 years old".


# TODO 3.2: Given price = 19.99 and quantity = 3, print an f-string whose
# {} computes the total directly, e.g. f"Total: {price * quantity}".


# TODO 3.3: Given pi_value = 3.14159265, print an f-string that rounds it
# to 2 decimal places using the :.2f format specifier.


# TODO 3.4 (Debug the Code): this line is supposed to embed the
# temperature variable into the printed sentence, but it's missing the
# f prefix, so Python prints the literal text "{temperature} F" instead
# of substituting the value. Fix it.
temperature = 98.6
print("Body temperature: {temperature} F")


# TODO 3.5: Given two name/score pairs — name_a = "Asha", score_a = 92
# and name_b = "Ravi", score_b = 87 — print each pair as one row of a
# simple text table using f-string padding: left-align each name in a
# 10-character field with :<10, and right-align each score in a
# 5-character field with :>5.


# TODO 3.A (Scenario — Receipt Line): given item_name = "Coffee",
# item_qty = 2, and item_price = 4.5, print one receipt line combining
# all three in an f-string, showing the line total formatted to 2
# decimal places (item_qty * item_price), e.g. "Coffee x2 - $9.00".


# TODO 3.B (Scenario — Interview Prep): given user_name = "Meera" and
# user_age = 29, first print a sentence built the "old style" way with
# + and str(), then print the same sentence as an f-string. Add a
# comment explaining why the f-string version is easier to read.


# ============================================================
# Topic 4: Immutability & String Identity
# ============================================================

# TODO 4.1: Given s = "cat", add a comment explaining why a statement
# like s[0] = "b" is not allowed in Python (strings are immutable). Then
# show the correct way to get "bat": build a new string by combining
# "b" with a slice of s, and print it.


# TODO 4.2: Given a = "hello" and b = a (b now points at the same string
# object as a), print id(a) and id(b) to show they match. Then reassign
# b = b + " world" and print id(a) and id(b) again — a's id should be
# unchanged, but b's id should now be different.


# TODO 4.3: Starting from result = "", use a for loop with range(5) to
# build up result with result = result + "x" each time, printing id(result)
# inside the loop on every iteration. Notice the id changes each time —
# a brand-new string object is created on every += (note: Python may
# reuse a freed memory address, so an id can reappear later; what matters
# is that it's a different object than the one from the previous line).


# TODO 4.4 (Debug the Code): this code tries to change the first
# character of word in place, which raises a TypeError because strings
# can't be mutated. Fix it by rebuilding the string with slicing instead.
word = "java"
word[0] = "J"
print(word)


# TODO 4.5: Given x = "hello" and y = "hello" (two separate literals with
# the same text), print id(x), id(y), and x is y. Add a comment about
# what you observe (Python sometimes reuses the same object for identical
# short string literals — this is called interning).


# TODO 4.A (Scenario — Log Builder Anti-Pattern): starting from
# log_text = "", use a for loop with range(5) to append
# f"entry {i}; " to log_text each time with +=, printing id(log_text)
# on every iteration, then print the final log_text. Add a comment
# explaining why doing this for thousands of log lines (instead of 5)
# would be a real performance problem in production.


# TODO 4.B (Scenario — Interview Prep): given a = "draft" and b = a, then
# reassigning a = "final", print both a and b. Add a comment explaining
# why b still shows "draft" even though a changed.


# ============================================================
# Topic 5: Searching & Validating Strings
# ============================================================

# TODO 5.1: Given word = "python", print whether "th" in word, and
# whether "z" not in word.


# TODO 5.2: Given age_input = "25", print age_input.isdigit(). If it's
# True, convert it to an int with int() and print the converted value.


# TODO 5.3: Given name_input = "Asha123", print name_input.isalpha()
# (should be False because of the digits). Then given
# name_input2 = "Asha", print name_input2.isalpha() (should be True).


# TODO 5.4: Given code_word = "PYTHON", print code_word.isupper(). Given
# code_word2 = "python", print code_word2.islower().


# TODO 5.5: Given field = "   " (three spaces), print field.isspace() to
# detect a field that's only whitespace.


# TODO 5.A (Scenario — PIN Validator): given pin = "4821", check that it
# is all digits with .isdigit() and that it's exactly 4 characters long
# with len(). Print a single True/False result combining both checks
# with and.


# TODO 5.B (Scenario — Interview Prep): given username = "user_2024",
# print username.isalnum() (it will be False because of the underscore).
# Add a comment explaining why, then use a for loop and an accumulator
# boolean to check every character is either alphanumeric OR the
# underscore character, printing the final True/False result.


# ============================================================
# Topic 6: Real-World Text Processing
# ============================================================

# TODO 6.1: Given raw = "  MANOHAR@EXAMPLE.COM  ", clean it up by
# chaining .strip() and .lower() together into one new variable, then
# print both the original raw value and the cleaned value.


# TODO 6.2: Given sentence = "Python makes text processing fun", loop
# over sentence.lower() one character at a time with a bare for-loop,
# and use an accumulator variable to count how many of the characters
# are vowels (check with `char in "aeiou"`). Print the total.


# TODO 6.3: Given line = "level: ERROR", find the position of the colon
# with .find(":"), then use slicing to pull out the part before the
# colon as key and the part after it as value, .strip()-ing each piece,
# and print key and value on separate lines.


# TODO 6.4 (Debug the Code): this login check is supposed to accept the
# email regardless of how it was capitalized, but it compares user_email
# directly against expected_email (which is already lowercase) without
# normalizing case first, so a valid but differently-capitalized email
# incorrectly fails. Fix it.
user_email = "MANOHAR@EXAMPLE.COM"
expected_email = "manohar@example.com"
print(user_email == expected_email)


# TODO 6.5: Given card = "4111111122223333", build a masked version for a
# receipt that shows "*" for every character except the last 4, e.g.
# "************3333". Use string repetition ("*" * n) combined with
# slicing, and print the result.


# TODO 6.A (Scenario — Log Line Splitter): given
# log_line = "2024-01-15|ERROR|Disk quota exceeded", use
# log_line.split("|") together with a bare for-loop to print each piece
# on its own line (don't index into the split result).


# TODO 6.B (Scenario — Interview Prep): given
# paragraph = "the quick fox jumps over the lazy dog and there the fox runs",
# use .split() with a for-loop and an accumulator to count how many times
# "the" appears as a whole word. Then print paragraph.count("the")
# directly on the raw string, and add a comment explaining why the two
# numbers are different (hint: think about the word "there").
