"""
Chapter 6 Exercises: Strings Deep Dive — reference solution.
"""

# TODO 1: Given filename = "vacation_photo.jpeg", use slicing to extract
# just the file extension (".jpeg") and print it.
filename = "vacation_photo.jpeg"
extension = filename[-5:]
print("File extension:", extension)


# TODO 2: Given email1 = "  Bob@Example.COM  " and email2 = "bob@example.com",
# normalize both (strip whitespace, lowercase) and print whether they match.
email1 = "  Bob@Example.COM  "
email2 = "bob@example.com"
if email1.strip().lower() == email2.strip().lower():
    print("Match: these are the same email address.")
else:
    print("No match.")


# TODO 3: Given item = "Desk Lamp", price = 18.5, and qty = 3, use an
# f-string to print a receipt line in the form:
# "Desk Lamp x3 = $55.50"
item = "Desk Lamp"
price = 18.5
qty = 3
print(f"{item} x{qty} = ${price * qty:.2f}")


# TODO 4: Given username = "sky walker 99", check whether it contains a
# space. Print "Invalid username: no spaces allowed." if it does, or
# "Username OK." if it doesn't.
username = "sky walker 99"
if " " in username:
    print("Invalid username: no spaces allowed.")
else:
    print("Username OK.")


# TODO 5 (Debug the Code): this is supposed to print "HELLO", but it
# prints "hello" instead. Find and fix the bug.
greeting = "hello"
greeting = greeting.upper()
print(greeting)


# TODO 6: Given the text and target word below, count how many times
# target appears in text (using .split() and an accumulator), then print
# the result in the form: "to" appeared 2 times
text = "to be or not to be that is the question"
target = "to"
count = 0
for word in text.split():
    if word == target:
        count += 1
print(f'"{target}" appeared {count} times')
