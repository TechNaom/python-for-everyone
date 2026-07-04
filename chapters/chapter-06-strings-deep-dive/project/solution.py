"""
Chapter 6 Project: Password Strength & Policy Auditor -- reference solution.
See README.md in this folder for the full brief and example output.
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

        # Rule 1: length
        length_ok = len(password) >= 8

        # Rules 2-5: scan the password once, character by character
        has_upper = False
        has_lower = False
        has_digit = False
        has_special = False

        for char in password:
            if char.isupper():
                has_upper = True
            if char.islower():
                has_lower = True
            if char.isdigit():
                has_digit = True
            if char in SPECIAL_CHARS:
                has_special = True

        # Score out of 5 -- one point per satisfied rule
        score = 0
        if length_ok:
            score += 1
        if has_upper:
            score += 1
        if has_lower:
            score += 1
        if has_digit:
            score += 1
        if has_special:
            score += 1

        if score <= 2:
            rating = "Weak"
        elif score <= 4:
            rating = "Medium"
        else:
            rating = "Strong"

        # Update session accumulators
        passwords_checked += 1
        if rating == "Strong":
            strong_count += 1

        print()
        print(f"--- Result for '{password}' ---")
        print(f"Score: {score}/5  ->  Rating: {rating}")
        print("Checklist:")
        print(f"  [{'x' if length_ok else ' '}] At least 8 characters long")
        print(f"  [{'x' if has_upper else ' '}] Contains an uppercase letter")
        print(f"  [{'x' if has_lower else ' '}] Contains a lowercase letter")
        print(f"  [{'x' if has_digit else ' '}] Contains a digit")
        print(f"  [{'x' if has_special else ' '}] Contains a special character ({SPECIAL_CHARS})")

        if score < 5:
            print("Suggestions:")
            if not length_ok:
                print("  - Make it at least 8 characters long")
            if not has_upper:
                print("  - Add an uppercase letter")
            if not has_lower:
                print("  - Add a lowercase letter")
            if not has_digit:
                print("  - Add a digit")
            if not has_special:
                print(f"  - Add a special character, e.g. one of {SPECIAL_CHARS}")
        else:
            print("This password meets every rule. Nice work!")

    elif choice == "2":
        print()
        print("--- Session Stats ---")
        print(f"Passwords checked: {passwords_checked}")
        print(f"Strong passwords: {strong_count}")
        if passwords_checked > 0:
            strong_rate = (strong_count / passwords_checked) * 100
            print(f"Strong rate: {strong_rate:.1f}%")
        else:
            print("No passwords checked yet this session.")

    elif choice == "3":
        print()
        print(f"Session summary: checked {passwords_checked} password(s), {strong_count} rated Strong.")
        print("Goodbye!")
        break

    else:
        print("Please choose 1, 2, or 3.")
