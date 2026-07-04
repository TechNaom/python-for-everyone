"""
Chapter 5 Practice Bank: Loops (while / for) -- reference solution.
"""

# ============================================================
# Topic 1: while loops
# ============================================================

# TODO 1.1
i = 1
while i <= 5:
    print(i)
    i = i + 1


# TODO 1.2
i = 10
while i >= 1:
    print(i)
    i = i - 1


# TODO 1.3
i = 2
while i <= 20:
    print(i)
    i += 2


# TODO 1.4
value = 1
while value <= 100:
    print(value)
    value = value * 2


# TODO 1.5 (Debug the Code)
# Bug: the original loop never updated i, so i stayed 1 forever and the
# loop never stopped. Fix: add i = i + 1 inside the loop body.
i = 1
while i <= 5:
    print(i)
    i = i + 1


# TODO 1.A (Scenario -- Launch Sequence)
i = 5
while i >= 1:
    print(i)
    i -= 1
print("Liftoff! \U0001F680")


# TODO 1.B (Scenario -- Interview Prep)
# while True: keeps looping because its condition is the literal value
# True, which can never become False on its own -- without a break
# statement, or some line that changes what's being checked, nothing
# ever stops it, so it runs forever. A bounded while loop like the one
# below always has a condition that eventually turns False.
i = 1
while i <= 3:
    print(i)
    i += 1


# ============================================================
# Topic 2: for loops and range()
# ============================================================

# TODO 2.1
for i in range(1, 6):
    print(i)


# TODO 2.2
for i in range(0, 50, 5):
    print(i)


# TODO 2.3
for i in range(10, 0, -1):
    print(i)


# TODO 2.4
for i in range(1, 21):
    if i % 2 == 0:
        print(i, "is even")
    else:
        print(i, "is odd")


# TODO 2.5 (Debug the Code)
# Bug: range(1, 10) stops at 9 because the stop value is always
# excluded. Fix: use range(1, 11) so 10 is included.
for i in range(1, 11):
    print(i)


# TODO 2.A (Scenario -- Multiplication Table)
for i in range(1, 11):
    print("12 x", i, "=", 12 * i)


# TODO 2.B (Scenario -- Interview Prep)
for i in range(2, 21, 2):
    print(i)


# ============================================================
# Topic 3: Common loop patterns (the accumulator pattern)
# ============================================================

# TODO 3.1
total = 0
i = 1
while i <= 10:
    total += i
    i += 1
print(total)


# TODO 3.2
total = 0
for i in range(1, 101):
    total += i
print(total)


# TODO 3.3
count = 0
for i in range(1, 51):
    if i % 3 == 0:
        count += 1
print(count)


# TODO 3.4 (Debug the Code)
# Bug: total = 0 was placed inside the loop, so it got wiped out on
# every single iteration instead of accumulating. Fix: initialize
# total = 0 once, before the loop starts.
total = 0
for i in range(1, 6):
    total += i
print(total)


# TODO 3.5
product = 1
for i in range(1, 6):
    product *= i
print(product)


# TODO 3.A (Scenario -- Daily Transactions)
attempt_count = 1
total = 0.0
while attempt_count <= 3:
    if attempt_count == 1:
        amount = 19.99
    elif attempt_count == 2:
        amount = 45.50
    else:
        amount = 12.25
    total += amount
    attempt_count += 1
print(total)


# TODO 3.B (Scenario -- Interview Prep -- Palindrome Check)
n = 1221
original = n
reversed_num = 0
while n > 0:
    reversed_num = reversed_num * 10 + n % 10
    n = n // 10
if reversed_num == original:
    print(original, "is a palindrome")
else:
    print(original, "is not a palindrome")


# ============================================================
# Topic 4: break & continue
# ============================================================

# TODO 4.1
for i in range(1, 21):
    if i == 15:
        break
    print(i)


# TODO 4.2
for i in range(1, 11):
    if i % 3 == 0:
        continue
    print(i)


# TODO 4.3
for i in range(1, 31):
    if i > 20:
        break
    if i % 2 != 0:
        continue
    print(i)


# TODO 4.4 (Debug the Code)
# Bug: break exits the loop completely at the first multiple of 4,
# instead of skipping just that one number. Fix: use continue instead
# of break.
for i in range(1, 21):
    if i % 4 == 0:
        continue
    print(i)


# TODO 4.5
n = 101
while True:
    if n % 7 == 0 and n % 3 == 0:
        print(n)
        break
    n += 1


# TODO 4.A (Scenario -- Retry Attempt Simulator -- Interview Prep)
correct_code = "1234"
attempt_number = 1
unlocked = False
while attempt_number <= 3:
    if attempt_number == 1:
        attempt = "0000"
    elif attempt_number == 2:
        attempt = "9999"
    else:
        attempt = "1234"
    if attempt == correct_code:
        print("Access granted")
        unlocked = True
        break
    else:
        print("Incorrect, try again")
    attempt_number += 1
if not unlocked:
    print("Account locked")


# TODO 4.B (Scenario -- Sensor Data Cleanup)
total = 0
for i in range(1, 6):
    reading = (i * 10) - 25
    if reading < 0:
        continue
    total += reading
print(total)
