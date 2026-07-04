"""
Chapter 1 Practice Bank: Your First Python Program — reference solution.
"""

# ============================================================
# Topic 1: print()
# ============================================================

# TODO 1.1
print("Hello, World!")
print("Manohar")


# TODO 1.2
print("Manohar")
print("123 Baker Street")
print("Hyderabad, 500001")


# TODO 1.3
print("--------------------")
print("   Order Summary")
print("--------------------")


# TODO 1.4
print("Loading...")
print("Loading...")
print("Loading...")
# Each print() call automatically ends with a newline, so every call
# starts fresh on its own line — even though the text is identical.


# TODO 1.5
print("*** Welcome! ***")
print("*** Enjoy your stay ***")


# TODO 1.A (Scenario — Internal Tool)
print("=== Deploy Helper v1 ===")
print("Type --help for options")


# TODO 1.B (Scenario — Interview Prep)
# Expectation: "First line" and "Second line" appear on two separate
# lines in the output, because print() always adds a newline character
# after whatever it displays — you never have to add one yourself.
print("First line")
print("Second line")


# ============================================================
# Topic 2: Variables
# ============================================================

# TODO 2.1
name = "Manohar"
age = 34
height = 5.9
print(name)
print(age)
print(height)


# TODO 2.2
score = 10
print(score)
score = 20
print(score)


# TODO 2.3
a = "first"
b = "second"
print(b)
print(a)


# TODO 2.4
balance = 100
balance = 80
print(balance)
balance = 95
print(balance)
balance = 60
print(balance)


# TODO 2.5
favorite_color = "blue"
favorite_color_backup = favorite_color
print(favorite_color)
print(favorite_color_backup)


# TODO 2.A (Scenario — Click Counter)
click_count = 0
print(click_count)
click_count = 1
print(click_count)
click_count = 2
print(click_count)
click_count = 3
print(click_count)


# TODO 2.B (Scenario — Debug the Code — Interview Prep)
# Bug: print() ran before the deposit was added to balance. Fix: add
# the deposit first, then print.
balance = 200
balance = balance + 50
print("Balance after deposit:", balance)


# ============================================================
# Topic 3: Basic Types (string / int / float)
# ============================================================

# TODO 3.1
product_name = "Wireless Mouse"
quantity = 3
price = 19.99
print("Product: " + product_name)
print("Quantity: " + str(quantity))
print("Price: " + str(price))


# TODO 3.2
item_count = 12
print("Total items: " + str(item_count))


# TODO 3.3 (Debug the Code)
total_price = 45
print("Total price: $" + str(total_price))


# TODO 3.4
id_name = "Asha"
id_age = 22
id_gpa = 3.8
print("Name: " + id_name + ", Age: " + str(id_age) + ", GPA: " + str(id_gpa))


# TODO 3.5
count_int = 5
count_float = 5.0
print(count_int)
print(count_float)


# TODO 3.A (Scenario — Till Receipt)
receipt_item = "Coffee"
receipt_price = 4.50
print(receipt_item + " - $" + str(receipt_price))


# TODO 3.B (Scenario — Interview Prep)
# "Age: " + 30 crashes because + means addition between two numbers
# but joining between two strings — Python won't guess which one you
# meant when one side is a string and the other is a plain number, so
# it raises a TypeError. str(30) converts the number to the text "30"
# first, so both sides of + are strings and Python can join them.
print("Age: " + str(30))


# ============================================================
# Topic 4: input()
# ============================================================

# TODO 4.1
user_name = input("What's your name? ")
print("Hello, " + user_name + "! Great to meet you.")


# TODO 4.2
user_name = input("What's your name? ")
hobby = input("What's your favorite hobby? ")
print(user_name + " enjoys " + hobby + " in their free time.")


# TODO 4.3
user_age = input("How old are you? ")
print("So you're " + user_age + " years old — thanks for sharing!")


# TODO 4.4 (Debug the Code)
age = 30
user_name = input("What's your name? ")
print("Hello " + user_name + ", did you know our app is " + str(age) + " years old?")


# TODO 4.5
favorite_food = input("What's your favorite food? ")
favorite_season = input("What's your favorite season? ")
print("You love " + favorite_food + " and the " + favorite_season + " season!")


# TODO 4.A (Scenario — Mini Mad Libs)
noun = input("Give me a noun: ")
adjective = input("Give me an adjective: ")
print("Today, a " + adjective + " " + noun + " walked into the room.")


# TODO 4.B (Scenario — Interview Prep)
# input() always returns a string, no matter what the user types — so
# joining it directly with another string here works fine with no
# str() needed. That's different from TODO 4.4, where `age` was
# already an int variable (not text from input()), so it needed
# str() before it could be joined with +.
typed_number = input("Type any number: ")
print("You typed: " + typed_number)
