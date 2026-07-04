"""
Chapter 6 Project: Password Strength & Policy Auditor
See README.md in this folder for the full brief and example output.

A menu-driven tool that scores a password against 5 rules and tracks
session stats using the accumulator pattern from Chapter 5.
"""

SPECIAL_CHARS = "!@#$%^&*()-_=+"

passwords_checked = 0
strong_count = 0

print("=== Password Strength & Policy Auditor ===")

while True:
    print()
    print("1. Check a password")
    print("2. View session stats")
    print("3. Quit")
    choice = input("Choose an option (1-3): ").strip()

    if choice == "1":
        password = input("Enter a password to check: ")

        # TODO 1: Check whether len(password) >= 8 and store the
        # True/False result in a variable called length_ok.

        # TODO 2: Set up four flags -- has_upper, has_lower, has_digit,
        # has_special -- all starting as False. Then loop over every
        # character in password with a for-loop and, inside the loop,
        # flip the matching flag to True whenever you see:
        #   - an uppercase letter        -> char.isupper()
        #   - a lowercase letter         -> char.islower()
        #   - a digit                    -> char.isdigit()
        #   - a special character        -> char in SPECIAL_CHARS

        # TODO 3: Compute score as a whole number out of 5 -- add 1 for
        # each of length_ok, has_upper, has_lower, has_digit, has_special
        # that is True.

        # TODO 4: Turn score into a rating string:
        #   0-2 points -> "Weak"
        #   3-4 points -> "Medium"
        #   5 points   -> "Strong"

        # TODO 5: Update the session accumulators -- passwords_checked
        # goes up by 1 on every check; strong_count goes up by 1 only
        # when rating is "Strong".

        # TODO 6: Print the score, the rating, and a checklist line for
        # each of the 5 rules showing whether it passed. See README.md
        # for the exact expected format.

        # TODO 7: If score is less than 5, print one specific suggestion
        # line for every rule that failed (e.g. "Add a digit"). If
        # score is 5, print a short congratulations line instead.
        pass

    elif choice == "2":
        # TODO 8: Print passwords_checked and strong_count. If
        # passwords_checked is greater than 0, also print the strong
        # rate as a percentage (strong_count / passwords_checked * 100),
        # formatted to 1 decimal place. Otherwise print a message saying
        # nothing has been checked yet -- don't divide by zero!
        pass

    elif choice == "3":
        print()
        print(f"Session summary: checked {passwords_checked} password(s), {strong_count} rated Strong.")
        print("Goodbye!")
        break

    else:
        print("Please choose 1, 2, or 3.")
