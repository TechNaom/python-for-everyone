"""
Chapter 6 Practice Bank: Strings Deep Dive — reference solution.
See README.md in this folder for full instructions.
"""

# ============================================================
# Topic 1: Indexing & Slicing
# ============================================================

# TODO 1.1
word = "Programming"
print(word[0])
print(word[-1])


# TODO 1.2
phrase = "Hello, World!"
print(len(phrase))
print(phrase[7:12])


# TODO 1.3
code = "abcdefghij"
print(code[::2])


# TODO 1.4
word = "Python"
print(word[::-1])


# TODO 1.5 (Debug the Code)
word = "Python"
print(word[len(word) - 1])


# TODO 1.A (Scenario — Phone Number Parser)
phone = "(555) 123-4567"
area_code = phone[1:4]
print(area_code)


# TODO 1.B (Scenario — Interview Prep)
# Slicing never raises an error even when the range reaches past the end
# of the string — Python just stops at whatever characters exist. A single
# index like word[100] has no "stop early" option, so it raises an
# IndexError instead.
word = "cat"
print(word[0:100])


# ============================================================
# Topic 2: Common String Methods
# ============================================================

# TODO 2.1
raw_input_text = "   mpapasani   "
cleaned = raw_input_text.strip()
print("[" + cleaned + "]")


# TODO 2.2
city = "new york"
print(city.upper())
print(city.lower())
print(city.title())
print(city.capitalize())


# TODO 2.3
phone_raw = "555-123-4567"
phone_clean = phone_raw.replace("-", "")
print(phone_clean)


# TODO 2.4 (Debug the Code)
text = "The quick brown fox"
position = text.find("cat")
if position == -1:
    print("Not found")
else:
    print(position)


# TODO 2.5
text = "Hello World Hello Python"
print(text.count("Hello"))

word_count = 0
for piece in text.split():
    word_count = word_count + 1
print(word_count)


# TODO 2.A (Scenario — Filename Validator)
filename = "server_log_2024.txt"
print(filename.startswith("server_log"))
print(filename.endswith(".txt"))


# TODO 2.B (Scenario — Interview Prep)
# Comparing raw strings with == is case-sensitive, so "Manohar" != "manohar"
# even though a human would call them the same username. Lowercasing both
# sides first makes the comparison case-insensitive.
stored_username = "Manohar"
typed_username = "manohar"
print(stored_username == typed_username)
print(stored_username.lower() == typed_username.lower())


# ============================================================
# Topic 3: String Formatting with f-strings
# ============================================================

# TODO 3.1
name = "Asha"
age = 22
print(f"{name} is {age} years old")


# TODO 3.2
price = 19.99
quantity = 3
print(f"Total: {price * quantity}")


# TODO 3.3
pi_value = 3.14159265
print(f"Pi rounded: {pi_value:.2f}")


# TODO 3.4 (Debug the Code)
temperature = 98.6
print(f"Body temperature: {temperature} F")


# TODO 3.5
name_a, score_a = "Asha", 92
name_b, score_b = "Ravi", 87
print(f"{name_a:<10}{score_a:>5}")
print(f"{name_b:<10}{score_b:>5}")


# TODO 3.A (Scenario — Receipt Line)
item_name = "Coffee"
item_qty = 2
item_price = 4.5
print(f"{item_name} x{item_qty} - ${item_price * item_qty:.2f}")


# TODO 3.B (Scenario — Interview Prep)
# f-strings are easier to read (the values sit right where they're used,
# instead of scattered across + and str() calls) and they can evaluate
# expressions directly inside {}, so there's no need to manually convert
# numbers to strings first.
user_name = "Meera"
user_age = 29
print("Old style: " + user_name + " is " + str(user_age) + " years old")
print(f"New style: {user_name} is {user_age} years old")


# ============================================================
# Topic 4: Immutability & String Identity
# ============================================================

# TODO 4.1
# Strings are immutable in Python — you cannot change one character in
# place (something like s[0] = "b" raises a TypeError). Instead, you build
# a brand-new string, usually with slicing.
s = "cat"
new_s = "b" + s[1:]
print(new_s)


# TODO 4.2
a = "hello"
b = a
print(id(a))
print(id(b))
b = b + " world"
print(id(a))
print(id(b))


# TODO 4.3
result = ""
for i in range(5):
    result = result + "x"
    print(id(result))


# TODO 4.4 (Debug the Code)
word = "java"
word = "J" + word[1:]
print(word)


# TODO 4.5
x = "hello"
y = "hello"
print(id(x))
print(id(y))
print(x is y)


# TODO 4.A (Scenario — Log Builder Anti-Pattern)
# Each += below creates a brand-new string object and copies everything
# that came before it into that new object. For 5 short log entries this
# is invisible, but for thousands of log lines it means repeatedly
# recopying an ever-growing string — a real performance problem.
log_text = ""
for i in range(5):
    log_text = log_text + f"entry {i}; "
    print(id(log_text))
print(log_text)


# TODO 4.B (Scenario — Interview Prep)
# Reassigning `a` to a new string just points the name `a` at a different
# object — it doesn't reach back and change the object `b` still refers
# to, because strings can't be mutated in place. `b` keeps pointing at the
# original "draft" string.
a = "draft"
b = a
a = "final"
print(a)
print(b)


# ============================================================
# Topic 5: Searching & Validating Strings
# ============================================================

# TODO 5.1
word = "python"
print("th" in word)
print("z" not in word)


# TODO 5.2
age_input = "25"
print(age_input.isdigit())
if age_input.isdigit():
    age_number = int(age_input)
    print(age_number)


# TODO 5.3
name_input = "Asha123"
print(name_input.isalpha())
name_input2 = "Asha"
print(name_input2.isalpha())


# TODO 5.4
code_word = "PYTHON"
print(code_word.isupper())
code_word2 = "python"
print(code_word2.islower())


# TODO 5.5
field = "   "
print(field.isspace())


# TODO 5.A (Scenario — PIN Validator)
pin = "4821"
is_all_digits = pin.isdigit()
is_right_length = len(pin) == 4
print(is_all_digits and is_right_length)


# TODO 5.B (Scenario — Interview Prep)
# username.isalnum() returns False here because "_" isn't a letter or a
# digit. Real systems usually allow underscores explicitly by checking
# each character against a wider allowed set instead of relying on
# isalnum() alone.
username = "user_2024"
print(username.isalnum())

all_allowed = True
for char in username:
    if not (char.isalnum() or char == "_"):
        all_allowed = False
print(all_allowed)


# ============================================================
# Topic 6: Real-World Text Processing
# ============================================================

# TODO 6.1
raw = "  MANOHAR@EXAMPLE.COM  "
clean = raw.strip().lower()
print(raw)
print(clean)


# TODO 6.2
sentence = "Python makes text processing fun"
vowel_count = 0
for char in sentence.lower():
    if char in "aeiou":
        vowel_count = vowel_count + 1
print(vowel_count)


# TODO 6.3
line = "level: ERROR"
colon_position = line.find(":")
key = line[:colon_position].strip()
value = line[colon_position + 1:].strip()
print(key)
print(value)


# TODO 6.4 (Debug the Code)
user_email = "MANOHAR@EXAMPLE.COM"
expected_email = "manohar@example.com"
print(user_email.lower() == expected_email)


# TODO 6.5
card = "4111111122223333"
masked = "*" * (len(card) - 4) + card[-4:]
print(masked)


# TODO 6.A (Scenario — Log Line Splitter)
log_line = "2024-01-15|ERROR|Disk quota exceeded"
for piece in log_line.split("|"):
    print(piece)


# TODO 6.B (Scenario — Interview Prep)
# text.count("the") matches "the" as a raw substring, so it would also
# count the "the" hiding inside "there", "these", "other", etc. Splitting
# on whitespace and comparing whole words avoids that false match.
paragraph = "the quick fox jumps over the lazy dog and there the fox runs"
whole_word_count = 0
for w in paragraph.split():
    if w == "the":
        whole_word_count = whole_word_count + 1
print(whole_word_count)
print(paragraph.count("the"))
