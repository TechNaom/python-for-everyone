"""
Chapter 4 Practice Bank: Control Flow (if / elif / else) — reference solution.
"""

# ============================================================
# Topic 1: Simple if
# ============================================================

# TODO 1.1
temperature = 35
if temperature > 32:
    print("Above freezing.")
print("Weather check complete.")


# TODO 1.2
email = "manohar@example.com"
if "@" in email:
    print("Looks like a valid email format.")


# TODO 1.3
number = 17
if number & 1 == 1:
    print(number, "is odd (bitwise check).")


# TODO 1.4
logged_in = True
if logged_in is True:
    print("Welcome back!")


# TODO 1.5
entered_password = input("Enter the password: ")
if entered_password == "letmein123":
    print("Access granted.")


# TODO 1.A (Scenario — Free Shipping Threshold)
cart_total = 82.50
if cart_total >= 75:
    print("You qualify for free shipping!")


# TODO 1.B (Scenario — Interview Prep)
# Expectation: nothing prints from the if block (checkout_step isn't
# "shipping"), but "Checkout flow continues..." still prints, because
# it sits at the same indent level as the if, not inside it — code
# outside an if block always runs regardless of the condition's result.
checkout_step = "payment"
if checkout_step == "shipping":
    print("Collecting shipping address...")
print("Checkout flow continues to the next step regardless.")


# ============================================================
# Topic 2: if-else
# ============================================================

# TODO 2.1
price_a = 42.00
price_b = 37.50
if price_a > price_b:
    print("Price A is more expensive.")
else:
    print("Price B is more expensive or equal.")


# TODO 2.2
completion_percent = 104
if 0 <= completion_percent <= 100:
    print("Valid percentage:", completion_percent)
else:
    print("Invalid percentage:", completion_percent)


# TODO 2.3
letter = "e"
vowels = "aeiouAEIOU"
if letter in vowels:
    print(letter, "is a vowel.")
else:
    print(letter, "is a consonant.")


# TODO 2.4
value = 24
if value & 1 == 1:
    print(value, "is odd.")
else:
    print(value, "is even.")


# TODO 2.5
signup_answer = input("Subscribe to our newsletter? (yes/no): ")
if signup_answer == "yes":
    print("You're subscribed!")
else:
    print("No worries, maybe next time.")


# TODO 2.A (Scenario — Age-Based Ticket Pricing)
visitor_age = 15
if visitor_age < 18:
    print("Child ticket: $8")
else:
    print("Adult ticket: $15")


# TODO 2.B (Scenario — Login Permission Check — Interview Prep)
stored_username = "admin"
stored_password = "secure99"
entered_username = "admin"
entered_password = "secure99"
if entered_username == stored_username and entered_password == stored_password:
    print("Access granted.")
else:
    print("Access denied.")


# ============================================================
# Topic 3: elif chains
# ============================================================

# TODO 3.1
signal_color = "yellow"
if signal_color == "red":
    print("Stop")
elif signal_color == "yellow":
    print("Slow down")
elif signal_color == "green":
    print("Go")
else:
    print("Unknown signal")


# TODO 3.2
number = -6
if number > 0:
    print(number, "is positive")
elif number < 0:
    print(number, "is negative")
else:
    print(number, "is zero")


# TODO 3.3 (Debug the Code)
# Bug: three independent `if` statements each ran their own check, so a
# temperature of 95 first set category to "hot", then the very next
# `if` (also True, since 95 >= 60) overwrote it to "warm". Fix: chain
# the checks with elif so only the first True branch runs.
temperature = 95
category = "cold"
if temperature >= 90:
    category = "hot"
elif temperature >= 60:
    category = "warm"
elif temperature < 60:
    category = "cold"
print("Category:", category)


# TODO 3.4
n = 45
if n % 15 == 0:
    print("FizzBuzz")
elif n % 3 == 0:
    print("Fizz")
elif n % 5 == 0:
    print("Buzz")
else:
    print(n)


# TODO 3.5
day_number = input("Enter a day number (1-7): ")
day_number = int(day_number)
if day_number == 1:
    print("Monday")
elif day_number == 2:
    print("Tuesday")
elif day_number == 3:
    print("Wednesday")
elif day_number == 4:
    print("Thursday")
elif day_number == 5:
    print("Friday")
elif day_number == 6:
    print("Saturday")
elif day_number == 7:
    print("Sunday")
else:
    print("Not a valid day number")


# TODO 3.A (Scenario — Discount Tier by Purchase Amount)
purchase_amount = 650
if purchase_amount >= 1000:
    print("Tier: Platinum")
elif purchase_amount >= 500:
    print("Tier: Gold")
elif purchase_amount >= 100:
    print("Tier: Silver")
else:
    print("No discount tier")


# TODO 3.B (Scenario — Interview Prep)
# Order matters because Python stops at the first True condition and
# never looks at the rest. If >= 70 were checked before >= 90, a score
# of 82 would incorrectly stop at "C" and never get the chance to match
# "B" — so an elif chain must always go from the highest (or most
# specific) threshold down to the lowest.
score = 82
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")


# ============================================================
# Topic 4: Nested if
# ============================================================

# TODO 4.1
number = 14
if number > 0:
    if number % 2 == 0:
        print(number, "is positive and even")
    else:
        print(number, "is positive and odd")
else:
    print(number, "is not positive")


# TODO 4.2
stored_username = "admin"
stored_password = "hunter2"
entered_username = "admin"
entered_password = "wrongpass"
if entered_username == stored_username:
    if entered_password == stored_password:
        print("Login successful.")
    else:
        print("Incorrect password.")
else:
    print("Username not found.")


# TODO 4.3
exam_score = 62
attendance_percent = 80
if exam_score >= 50:
    if attendance_percent >= 75:
        print("Pass: exam and attendance both meet requirements.")
    else:
        print("Not eligible: attendance below 75% despite passing score.")
else:
    print("Fail: exam score below 50.")


# TODO 4.4
value = 250
if value > 0:
    if value > 100:
        print("Large positive number.")
    else:
        print("Small positive number.")
else:
    print("Not a positive number.")


# TODO 4.5
visitor_age = input("Enter your age: ")
visitor_age = int(visitor_age)
if visitor_age >= 18:
    has_id = input("Do you have a valid ID? (yes/no): ")
    if has_id == "yes":
        print("Entry allowed.")
    else:
        print("ID required for entry.")
else:
    print("Sorry, you must be 18 or older.")


# TODO 4.A (Scenario — Bank Withdrawal)
balance = 500
withdrawal_amount = 200
if balance >= withdrawal_amount:
    if withdrawal_amount > 0:
        print("Withdrawal successful. New balance:", balance - withdrawal_amount)
    else:
        print("Invalid withdrawal amount.")
else:
    print("Insufficient funds.")


# TODO 4.B (Scenario — Interview Prep)
a = 10
b = 5
c = 4
# Nested version
if a > b:
    if a > c:
        print("a is the biggest (nested if):", a)
# Equivalent single-condition version
if a > b and a > c:
    print("a is the biggest (and):", a)
# Both print the same result here because both conditions must be True
# either way. Nesting only becomes genuinely necessary once the inner
# check needs its own separate else that's different from the outer
# else — a single `and` condition can't express two different "false"
# outcomes at once, but two nested ifs can.
