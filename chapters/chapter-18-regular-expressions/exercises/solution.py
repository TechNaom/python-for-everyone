"""
Chapter 18 Exercises: Regular Expressions -- reference solution.
Run this from inside the exercises/ folder: python3 solution.py
"""

import re

# TODO 1
match = re.search(r"\d+", "Order #4471 shipped")
print(match)
print(match.group())


# TODO 2
names = re.findall(r"[A-Z][a-z]+", "Alice and Bob went to Paris")
print(names)


# TODO 3
match = re.match(r"(?P<area>\d{3})-(?P<number>\d{4})", "555-1234 is the number")
print(match.group("area"))
print(match.group("number"))
print(match.groupdict())


# TODO 4
cleaned = re.sub(r"\s+", " ", "too    many     spaces")
print(cleaned)


# TODO 5
zip_pattern = re.compile(r"^\d{5}$")
for zip_code in ["90210", "1002", "733210", "60614"]:
    if zip_pattern.fullmatch(zip_code):
        print(f"{zip_code}: valid")
    else:
        print(f"{zip_code}: invalid")


# TODO 6
notes = re.findall(r"\(.*?\)", "Total (before tax) is $40 (approx.) for two items")
print(notes)


# TODO 7 (Debug the Code)
# Bug: r"\$\d+.\d{2}" uses an unescaped "." which matches ANY character, not
# just a literal period -- so "$19x99" wrongly matches too. Fix: escape the
# dot as \. so it only matches an actual decimal point.
price_pattern = r"\$\d+\.\d{2}"
test_strings = ["$19.99", "$19x99", "$5.00"]
for s in test_strings:
    result = re.fullmatch(price_pattern, s)
    print(f"{s}: {'matches' if result else 'no match'}")


# TODO 8 (Debug the Code)
# Bug: "\bcat\b" without the r prefix lets Python's own string-escaping
# rules turn \b into an actual backspace character (\x08) before re ever
# sees the pattern, so it can never match. Fix: use a raw string, r"\bcat\b",
# so \b is passed through literally and re interprets it as the
# word-boundary anchor.
word_pattern = r"\bcat\b"
text = "cat catalog concatenate"
print(re.findall(word_pattern, text))
