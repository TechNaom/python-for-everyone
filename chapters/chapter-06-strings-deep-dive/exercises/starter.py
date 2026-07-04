"""
Chapter 6 Exercises: Strings Deep Dive
See README.md in this folder for full instructions.
"""

# TODO 1: Given filename = "vacation_photo.jpeg", use slicing to extract
# just the file extension (".jpeg") and print it.
filename = "vacation_photo.jpeg"


# TODO 2: Given email1 = "  Bob@Example.COM  " and email2 = "bob@example.com",
# normalize both (strip whitespace, lowercase) and print whether they match.
email1 = "  Bob@Example.COM  "
email2 = "bob@example.com"


# TODO 3: Given item = "Desk Lamp", price = 18.5, and qty = 3, use an
# f-string to print a receipt line in the form:
# "Desk Lamp x3 = $55.50"
item = "Desk Lamp"
price = 18.5
qty = 3


# TODO 4: Given username = "sky walker 99", check whether it contains a
# space. Print "Invalid username: no spaces allowed." if it does, or
# "Username OK." if it doesn't.
username = "sky walker 99"


# TODO 5 (Debug the Code): this is supposed to print "HELLO", but it
# prints "hello" instead. Find and fix the bug.
greeting = "hello"
greeting.upper()
print(greeting)


# TODO 6: Given the text and target word below, count how many times
# target appears in text (using .split() and an accumulator), then print
# the result in the form: "to" appeared 2 times
text = "to be or not to be that is the question"
target = "to"
