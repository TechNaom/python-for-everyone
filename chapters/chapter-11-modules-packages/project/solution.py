"""
Chapter 11 Project: Expense Tracker -- reference solution.
See README.md in this folder for the full brief and example output.

This project is built AROUND the math and datetime modules as its core
organizing principle -- every date calculation goes through datetime, every
rounding/aggregation calculation goes through math or plain arithmetic, and
each operation lives in its own small function, exactly like Chapter 10's
function-library pattern. The while-True menu loop at the bottom does
nothing but call into those functions and print results.
"""
import math
import datetime


def parse_date(raw, today):
    """Parse a 'YYYY-MM-DD' string into a date, or return today if raw is blank."""
    raw = raw.strip()
    if raw == "":
        return today
    parts = raw.split("-")
    year = int(parts[0])
    month = int(parts[1])
    day = int(parts[2])
    return datetime.date(year, month, day)


def add_expense(expenses, amount, category, note, expense_date):
    """Build one expense dict, append it to the running expenses list, and return it."""
    expense = {
        "amount": round(amount, 2),
        "category": category,
        "note": note,
        "date": expense_date,
    }
    expenses.append(expense)
    return expense


def total_spent(expenses):
    """Return the total of every expense's amount, rounded to 2 decimals."""
    return round(sum(expense["amount"] for expense in expenses), 2)


def average_expense(expenses):
    """Return the average expense amount, or 0 if there are no expenses yet."""
    if len(expenses) == 0:
        return 0
    return round(total_spent(expenses) / len(expenses), 2)


def round_up_to_nearest(amount, nearest=1):
    """Round amount up to the nearest multiple of `nearest`, using math.ceil."""
    return math.ceil(amount / nearest) * nearest


def days_since(expense_date, today):
    """Return how many days have passed between expense_date and today."""
    return (today - expense_date).days


def days_until(target_date, today):
    """Return how many days remain between today and a future target_date."""
    return (target_date - today).days


def month_key(expense_date):
    """Turn a date into a 'YYYY-MM' grouping key, e.g. 2026-07."""
    return f"{expense_date.year}-{expense_date.month:02d}"


def summarize_by_month(expenses):
    """Return a dict of {'YYYY-MM': total_spent_that_month}."""
    summary = {}
    for expense in expenses:
        key = month_key(expense["date"])
        if key not in summary:
            summary[key] = 0
        summary[key] += expense["amount"]
    for key in summary:
        summary[key] = round(summary[key], 2)
    return summary


def summarize_by_category(expenses):
    """Return a dict of {category: total_spent_in_that_category}."""
    summary = {}
    for expense in expenses:
        category = expense["category"]
        if category not in summary:
            summary[category] = 0
        summary[category] += expense["amount"]
    for category in summary:
        summary[category] = round(summary[category], 2)
    return summary


def print_expense(expense, index):
    """Print one expense as a numbered, aligned line."""
    print(f"{index}. [{expense['date']}] {expense['category']:<12} ${expense['amount']:.2f}  {expense['note']}")


def read_float(prompt, default):
    """Read a number from the user, falling back to a default on blank input."""
    raw = input(prompt).strip()
    if raw == "":
        return default
    return float(raw)


expenses = []  # running session history of every expense recorded
today = datetime.date.today()

print("=== Expense Tracker ===")
print(f"Today's date: {today}")

while True:
    print()
    print("1. Add an expense")
    print("2. Show all expenses")
    print("3. Show totals & average")
    print("4. Show monthly summary")
    print("5. Show category breakdown")
    print("6. Days since last expense / days until a target date")
    print("7. Quit")
    choice = input("Choose an option (1-7): ").strip()

    if choice == "1":
        amount = read_float("Amount: $", 0)
        category = input("Category (e.g. food, rent, transport): ").strip().lower()
        note = input("Note (optional): ").strip()
        date_raw = input("Date (YYYY-MM-DD, blank = today): ")
        expense_date = parse_date(date_raw, today)
        expense = add_expense(expenses, amount, category, note, expense_date)
        print(f"\nAdded: ${expense['amount']:.2f} in {expense['category']} on {expense['date']}.")

    elif choice == "2":
        print()
        if len(expenses) == 0:
            print("No expenses recorded yet.")
        else:
            index = 1
            for expense in expenses:
                print_expense(expense, index)
                index += 1

    elif choice == "3":
        print()
        if len(expenses) == 0:
            print("No expenses recorded yet.")
        else:
            total = total_spent(expenses)
            avg = average_expense(expenses)
            rounded_budget = round_up_to_nearest(total, 10)
            print(f"Total spent: ${total:.2f}")
            print(f"Average per expense: ${avg:.2f}")
            print(f"Suggested round-number budget to set aside: ${rounded_budget:.2f}")

    elif choice == "4":
        print()
        if len(expenses) == 0:
            print("No expenses recorded yet.")
        else:
            summary = summarize_by_month(expenses)
            for key in sorted(summary):
                print(f"{key}: ${summary[key]:.2f}")

    elif choice == "5":
        print()
        if len(expenses) == 0:
            print("No expenses recorded yet.")
        else:
            summary = summarize_by_category(expenses)
            for category in sorted(summary):
                print(f"{category:<12} ${summary[category]:.2f}")

    elif choice == "6":
        print()
        if len(expenses) == 0:
            print("No expenses recorded yet, so no 'last expense' to compare.")
        else:
            last_expense = expenses[-1]
            gap = days_since(last_expense["date"], today)
            print(f"Days since last expense ({last_expense['date']}): {gap}")
        target_raw = input("Enter a target date (YYYY-MM-DD) to count down to (blank to skip): ").strip()
        if target_raw != "":
            target_date = parse_date(target_raw, today)
            remaining = days_until(target_date, today)
            print(f"Days until {target_date}: {remaining}")

    elif choice == "7":
        print()
        print(f"Session summary: {len(expenses)} expense(s) recorded, ${total_spent(expenses):.2f} total.")
        print("Goodbye!")
        break

    else:
        print("Please choose 1-7.")
