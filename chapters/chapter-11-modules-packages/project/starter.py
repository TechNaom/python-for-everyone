"""
Chapter 11 Project: Expense Tracker
See README.md in this folder for the full brief and example output.

This project is built AROUND the math and datetime modules as its core
organizing principle -- every date calculation goes through datetime, every
rounding/aggregation calculation goes through math or plain arithmetic, and
each operation lives in its own small function, exactly like Chapter 10's
function-library pattern. The while-True menu loop at the bottom does
nothing but call into those functions and print results. Fill in the
numbered TODOs below.
"""
import math
import datetime


def parse_date(raw, today):
    """Parse a 'YYYY-MM-DD' string into a date, or return today if raw is blank."""
    raw = raw.strip()
    # TODO 1: If raw is an empty string, return today. Otherwise split raw on
    # "-" into year/month/day parts (remember: parts come back as strings,
    # so convert each to int), and return datetime.date(year, month, day).
    pass


def add_expense(expenses, amount, category, note, expense_date):
    """Build one expense dict, append it to the running expenses list, and return it."""
    # TODO 2: Build a dict with keys "amount" (amount rounded to 2 decimals
    # with round(...)), "category", "note", and "date" (expense_date).
    # Append it to expenses, then return it.
    pass


def total_spent(expenses):
    """Return the total of every expense's amount, rounded to 2 decimals."""
    # TODO 3: Return round(sum(expense["amount"] for expense in expenses), 2).
    pass


def average_expense(expenses):
    """Return the average expense amount, or 0 if there are no expenses yet."""
    # TODO 4: If len(expenses) == 0, return 0. Otherwise return
    # round(total_spent(expenses) / len(expenses), 2).
    pass


def round_up_to_nearest(amount, nearest=1):
    """Round amount up to the nearest multiple of `nearest`, using math.ceil."""
    # TODO 5: Return math.ceil(amount / nearest) * nearest.
    pass


def days_since(expense_date, today):
    """Return how many days have passed between expense_date and today."""
    # TODO 6: Return (today - expense_date).days.
    pass


def days_until(target_date, today):
    """Return how many days remain between today and a future target_date."""
    # TODO 7: Return (target_date - today).days.
    pass


def month_key(expense_date):
    """Turn a date into a 'YYYY-MM' grouping key, e.g. 2026-07."""
    # TODO 8: Return an f-string built from expense_date.year and
    # expense_date.month, formatted as f"{expense_date.year}-{expense_date.month:02d}".
    pass


def summarize_by_month(expenses):
    """Return a dict of {'YYYY-MM': total_spent_that_month}."""
    # TODO 9: Build an empty dict called summary. Loop over expenses, compute
    # each expense's month_key(...), and add that expense's amount into
    # summary[key] (creating the key with a starting value of 0 first, if
    # it isn't already present). After the loop, round every value in
    # summary to 2 decimals, then return summary.
    pass


def summarize_by_category(expenses):
    """Return a dict of {category: total_spent_in_that_category}."""
    # TODO 10: Same idea as summarize_by_month, but group by
    # expense["category"] instead of a computed month key.
    pass


def print_expense(expense, index):
    """Print one expense as a numbered, aligned line."""
    # TODO 11: Print a line in this format, using an f-string with :<12 for
    # the category and :.2f for the amount:
    #   print(f"{index}. [{expense['date']}] {expense['category']:<12} ${expense['amount']:.2f}  {expense['note']}")
    pass


def read_float(prompt, default):
    """Read a number from the user, falling back to a default on blank input."""
    raw = input(prompt).strip()
    # TODO 12: If raw is an empty string, return default. Otherwise return
    # float(raw).
    pass


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
            # TODO 13: Loop over expenses with a running counter variable
            # you increment yourself, calling print_expense(expense, index)
            # for each one (same pattern as Chapter 10's project history
            # loop).
            pass

    elif choice == "3":
        print()
        if len(expenses) == 0:
            print("No expenses recorded yet.")
        else:
            # TODO 14: Compute total = total_spent(expenses), avg =
            # average_expense(expenses), and rounded_budget =
            # round_up_to_nearest(total, 10). Print all three, matching the
            # style: "Total spent: $..." / "Average per expense: $..." /
            # "Suggested round-number budget to set aside: $...".
            pass

    elif choice == "4":
        print()
        if len(expenses) == 0:
            print("No expenses recorded yet.")
        else:
            # TODO 15: Get summary = summarize_by_month(expenses), then loop
            # over sorted(summary) printing "{key}: ${summary[key]:.2f}" for
            # each one.
            pass

    elif choice == "5":
        print()
        if len(expenses) == 0:
            print("No expenses recorded yet.")
        else:
            # TODO 16: Same idea as TODO 15, but with
            # summarize_by_category(expenses), printing
            # f"{category:<12} ${summary[category]:.2f}" for each.
            pass

    elif choice == "6":
        print()
        if len(expenses) == 0:
            print("No expenses recorded yet, so no 'last expense' to compare.")
        else:
            # TODO 17: Get last_expense = expenses[-1], compute gap =
            # days_since(last_expense["date"], today), and print
            # "Days since last expense ({last_expense['date']}): {gap}".
            pass
        target_raw = input("Enter a target date (YYYY-MM-DD) to count down to (blank to skip): ").strip()
        if target_raw != "":
            # TODO 18: Parse target_raw into target_date with
            # parse_date(target_raw, today), compute remaining =
            # days_until(target_date, today), and print
            # "Days until {target_date}: {remaining}".
            pass

    elif choice == "7":
        print()
        # TODO 19: Print a one-line session summary showing how many
        # expenses were recorded and the total spent (use
        # total_spent(expenses)), print "Goodbye!", then break out of the
        # loop.
        pass

    else:
        print("Please choose 1-7.")
