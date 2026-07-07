"""
Chapter 18 Exercises: Regular Expressions
See README.md in this folder for full instructions.
Run this from inside the exercises/ folder: python3 starter.py
"""

import re

# TODO 1: Use re.search() with the pattern r"\d+" to find the first run of
# digits in the string "Order #4471 shipped". Print the Match object, then
# print match.group() to see just the matched text.


# TODO 2: Use re.findall() with the pattern r"[A-Z][a-z]+" to find every
# capitalized word in the string "Alice and Bob went to Paris". Store the
# result in a variable named names and print it.


# TODO 3: Use re.match() with the pattern r"(?P<area>\d{3})-(?P<number>\d{4})"
# on the string "555-1234 is the number". Print match.group("area") and
# match.group("number"), then print match.groupdict().


# TODO 4: Use re.sub() with the pattern r"\s+" to replace every run of one or
# more whitespace characters in "too    many     spaces" with a single space
# " ". Store the result in cleaned and print it.


# TODO 5: Use re.compile() to build a compiled pattern from r"^\d{5}$" (a
# valid 5-digit ZIP code, start to end). Then loop over the list
# ["90210", "1002", "733210", "60614"], and for each one, use the compiled
# pattern's .fullmatch() method to print whether it's a valid ZIP code
# (print f"{zip_code}: valid" or f"{zip_code}: invalid").


# TODO 6: Use re.findall() with a non-greedy pattern r"\(.*?\)" to find every
# parenthesized note in the string
# "Total (before tax) is $40 (approx.) for two items". Print the result --
# it should find both "(before tax)" and "(approx.)" as two separate
# matches, not one giant match spanning both.


# TODO 7 (Debug the Code): this pattern is supposed to match a literal price
# like "$19.99", but it forgot to escape the dot, so "$19x99" (with an "x"
# instead of a period) matches too, which is wrong -- an unescaped "." means
# "any character," not a literal period. Find and fix it.
price_pattern = r"\$\d+.\d{2}"
test_strings = ["$19.99", "$19x99", "$5.00"]
for s in test_strings:
    result = re.fullmatch(price_pattern, s)
    print(f"{s}: {'matches' if result else 'no match'}")


# TODO 8 (Debug the Code): this pattern is meant to match the standalone
# word "cat" using a word-boundary anchor, but the pattern string was
# written without the r prefix, so Python's own string-escaping rules
# silently turn \b into a backspace character instead of the word-boundary
# anchor -- meaning it never matches anything at all. Find and fix it.
word_pattern = "\bcat\b"
text = "cat catalog concatenate"
print(re.findall(word_pattern, text))
