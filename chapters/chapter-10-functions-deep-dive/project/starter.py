"""
Chapter 10 Project: Tip & Bill-Split Calculator Library
See README.md in this folder for the full brief and example output.

This project is built AROUND functions as its core organizing principle --
every calculation should live in a small, reusable, well-designed function,
and the while-True menu loop at the bottom should do nothing but call into
that library and print results. Fill in the numbered TODOs below.
"""


def calculate_tip(bill_amount, tip_percent=15):
    """Return the tip amount for a bill, given a tip percentage (default 15%)."""
    # TODO 1: Return bill_amount * (tip_percent / 100), rounded to 2 decimals
    # with round(...).
    pass


def apply_discount(bill_amount, discount_percent=0):
    """Return the bill amount after applying a percentage discount (default: none)."""
    # TODO 2: Return bill_amount * (1 - discount_percent / 100), rounded to
    # 2 decimals.
    pass


def apply_surcharges(bill_amount, *surcharges):
    """Add any number of flat surcharges (delivery fee, service fee, ...) to a bill.

    *surcharges demonstrates variable-length positional arguments: the caller
    can pass zero, one, or many flat fees, and this function doesn't need to
    know in advance how many there will be.
    """
    # TODO 3: Return bill_amount plus the sum of everything in the surcharges
    # tuple, rounded to 2 decimals.
    pass


def split_bill(total, num_people=1):
    """Split a total evenly across num_people (default 1, i.e. no split)."""
    # TODO 4: If num_people is 0 or negative, just return total unchanged
    # (can't split across zero or a negative number of people). Otherwise
    # return total / num_people, rounded to 2 decimals.
    pass


def summarize_fees(**fees):
    """Total up any number of named fees passed in as keyword arguments.

    **fees demonstrates variable-length keyword arguments: the caller can
    attach any labeled fees (delivery_fee=5, service_fee=2, ...) without
    this function needing a fixed parameter for every possible fee name.
    """
    # TODO 5: Return the sum of fees.values(), rounded to 2 decimals.
    pass


def build_receipt(bill_amount, tip_percent=15, discount_percent=0, num_people=1, **extra_fees):
    """Build one full receipt dict by composing the smaller functions above.

    This is the "bring it all together" function -- it shouldn't duplicate
    any calculation logic itself, it should just call the other functions
    in the right order and assemble their results.
    """
    # TODO 6: Call apply_discount(...) to get discounted_bill, then
    # calculate_tip(...) on the discounted amount to get tip_amount, then
    # summarize_fees(**extra_fees) to get fees_total, then
    # apply_surcharges(...) on (discounted_bill + tip_amount) with
    # fees_total to get grand_total, then split_bill(...) to get
    # per_person. Return a dict with keys: "original_bill",
    # "discount_percent", "discounted_bill", "tip_percent", "tip_amount",
    # "extra_fees" (as a plain dict), "fees_total", "grand_total",
    # "num_people", "per_person".
    pass


def print_receipt(receipt):
    """Print a receipt dict (from build_receipt) as a formatted, aligned block."""
    print()
    print("--- Receipt ---")
    # TODO 7: Print the original bill, the discount line (only if
    # discount_percent > 0), the tip line, one line per extra fee (loop
    # over receipt["extra_fees"].items()), the grand total, and the
    # per-person line (only if num_people > 1). Use f-strings with
    # :<22 alignment and :.2f for money values, matching this style:
    #   print(f"{'Original bill:':<22}${receipt['original_bill']:.2f}")
    pass


def read_float(prompt, default):
    """Read a number from the user, falling back to a default on blank input."""
    raw = input(prompt).strip()
    # TODO 8: If raw is an empty string, return default. Otherwise return
    # float(raw).
    pass


def read_int(prompt, default):
    """Read a whole number from the user, falling back to a default on blank input."""
    raw = input(prompt).strip()
    # TODO 9: Same idea as read_float, but return int(raw) instead.
    pass


receipts = []  # running session history of every receipt built

print("=== Tip & Bill-Split Calculator Library ===")

while True:
    print()
    print("1. Calculate a tip only")
    print("2. Apply a discount to a bill")
    print("3. Split a bill across people")
    print("4. Build a full receipt (discount + tip + fees + split)")
    print("5. Show session history")
    print("6. Quit")
    choice = input("Choose an option (1-6): ").strip()

    if choice == "1":
        bill = read_float("Bill amount: $", 0)
        percent = read_float("Tip percent (blank = 15): ", 15)
        tip = calculate_tip(bill, percent)
        print(f"\nTip on ${bill:.2f} at {percent}% is ${tip:.2f}.")

    elif choice == "2":
        bill = read_float("Bill amount: $", 0)
        percent = read_float("Discount percent (blank = 0): ", 0)
        discounted = apply_discount(bill, percent)
        print(f"\n${bill:.2f} with a {percent}% discount is ${discounted:.2f}.")

    elif choice == "3":
        total = read_float("Total amount: $", 0)
        people = read_int("Number of people (blank = 1): ", 1)
        share = split_bill(total, people)
        print(f"\nSplitting ${total:.2f} across {people} people is ${share:.2f} each.")

    elif choice == "4":
        bill = read_float("Bill amount: $", 0)
        percent = read_float("Discount percent (blank = 0): ", 0)
        tip_percent = read_float("Tip percent (blank = 15): ", 15)
        people = read_int("Number of people (blank = 1): ", 1)

        extra_fees = {}
        add_fees = input("Add extra fees? (y/n): ").strip().lower()
        if add_fees == "y":
            fee_count = read_int("How many fees to add? ", 0)
            fee_num = 1
            # TODO 10: Loop while fee_num <= fee_count. Each time, ask for
            # a fee name (strip it and replace spaces with underscores)
            # and a fee amount with read_float(...), store it in
            # extra_fees[fee_name], then increment fee_num.
            pass

        receipt = build_receipt(bill, tip_percent, percent, people, **extra_fees)
        receipts.append(receipt)
        print_receipt(receipt)

    elif choice == "5":
        print()
        if len(receipts) == 0:
            print("No receipts built yet this session.")
        else:
            # TODO 11: Print a header showing how many receipts are in
            # receipts, then loop over them printing a numbered line per
            # receipt showing its original_bill and grand_total (use a
            # running counter variable you increment yourself).
            pass

    elif choice == "6":
        print()
        # TODO 12: Print a one-line session summary showing how many
        # receipts were built, print "Goodbye!", then break out of the loop.
        pass

    else:
        print("Please choose 1-6.")
