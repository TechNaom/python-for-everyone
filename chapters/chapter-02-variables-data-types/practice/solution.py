"""
Chapter 2 Practice Bank: Variables & Data Types -- reference solution.
"""

# ============================================================
# Topic 1: Naming variables properly
# ============================================================

# TODO 1.1
first_name = "Asha"
last_name = "Rao"
age = 22
print(first_name)
print(last_name)
print(age)


# TODO 1.2
cart_total = 49.99
print(cart_total)


# TODO 1.3
total = 100
Total = 200
TOTAL = 300
print(total)
print(Total)
print(TOTAL)


# TODO 1.4
_session_id = "sess_9f8a"
print(_session_id)


# TODO 1.5
second_place = "Priya"
user_name = "priya_codes"
api_key = "sk_test_12345"
print(second_place)
print(user_name)
print(api_key)


# TODO 1.A (Scenario -- Config Keys)
max_retry_count = 3
api_timeout_seconds = 30
is_debug_mode = False
print(max_retry_count)
print(api_timeout_seconds)
print(is_debug_mode)


# TODO 1.B (Scenario -- Interview Prep)
total = 100
Total = 200
TOTAL = 300
print(total)
print(Total)
print(TOTAL)
# Python is case-sensitive when it comes to identifiers, so it reads
# every difference in letter casing as a completely different name.
# total, Total, and TOTAL are three separate labels pointing at three
# separate values -- changing one never touches the other two.


# ============================================================
# Topic 2: Python decides the type for you
# ============================================================

# TODO 2.1
username = "asha_codes"
follower_count = 482
rating = 4.7
is_verified = True
print(username, follower_count, rating, is_verified)


# TODO 2.2
signal = 10
print(signal)
signal = "ten"
print(signal)


# TODO 2.3
ready = True
print(ready)
ready = "yes"
print(ready)


# TODO 2.4
reading = 3 + 4j
print(reading)


# TODO 2.5
temp = 98.6
print(temp)
temp = 100
print(temp)


# TODO 2.A (Scenario -- Feature Flag)
feature_enabled = True
print(feature_enabled)
feature_enabled = "enabled"
print(feature_enabled)
# In a statically typed language like Java, a boolean variable can
# never be reassigned to a String -- that would be a compile error.
# Python allows it because a variable's type is decided by its current
# value, not declared upfront, so feature_enabled simply points at a
# different kind of value now.


# TODO 2.B (Scenario -- Debug the Code -- Interview Prep)
# Bug: item_count is an int, and joining an int directly to a string
# with + crashes with a TypeError. Fix: convert it with str() first.
item_count = 3
print("Items in cart: " + str(item_count))


# ============================================================
# Topic 3: type() and id()
# ============================================================

# TODO 3.1
price = 49.99
print(type(price))


# TODO 3.2
a = 7
b = 7
print(id(a))
print(id(b))


# TODO 3.3
label = "hello"
print(type(label))
print(id(label))


# TODO 3.4
x = 500
y = 500
print(id(x))
print(id(y))
# These ids may or may not match depending on the Python interpreter
# running this file -- the lesson's small-integer caching trick is
# only guaranteed for small values (roughly -5 to 256), not for 500.


# TODO 3.5
flag = True
print(type(flag))
flag = 42
print(type(flag))


# TODO 3.A (Scenario -- QA Type Check)
user_id = 1001
print(type(user_id))


# TODO 3.B (Scenario -- Interview Prep)
x = 5
y = 5
print(id(x))
print(id(y))
# Yes -- these ids will be the same. Small integers like 5 are
# immutable, so Python reuses one shared object in memory for that
# value instead of creating a new one every time it's assigned. Both
# x and y just end up pointing at that same cached object.


# ============================================================
# Topic 4: Converting between types
# ============================================================

# TODO 4.1
age_text = input("How old are you? ")
age_number = int(age_text)
print(age_number)
print(type(age_number))


# TODO 4.2
pi_text = "3.14"
pi_value = float(pi_text)
print(pi_value)


# TODO 4.3
count = 42
count_str = str(count)
print(count_str)
print(type(count_str))


# TODO 4.4
switch = 0
print(bool(switch))
switch2 = 1
print(bool(switch2))


# TODO 4.5 (Debug the Code)
# Bug: "three" is text, not a numeral, so int() can't parse it and
# raises a ValueError. Fix: use a numeral string like "3" instead.
food_quantity = "3"
quantity_number = int(food_quantity)
print("You have " + str(quantity_number) + " items.")


# TODO 4.A (Scenario -- Signup Form)
current_age_text = input("How old are you? ")
current_age = int(current_age_text)
next_year_age = current_age + 1
print("Next year you'll be " + str(next_year_age) + ".")


# TODO 4.B (Scenario -- Interview Prep)
trick = bool("False")
print(trick)
# bool() on a string never reads the actual text -- it only checks
# whether the string is empty or not. "False" is a non-empty string,
# so it converts to True. Only bool("") (the empty string) gives
# False.
