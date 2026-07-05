"""
Chapter 10 Project: Tip & Bill-Split Calculator Library -- reference solution.
See README.md in this folder for the full brief and example output.

This project is built AROUND functions as its core organizing principle --
every calculation lives in a small, reusable, well-designed function, and
the while-True menu loop at the bottom does nothing but call into that
library and print results. That's the whole point of this chapter: instead
of the flat if/elif calculator style from earlier chapters, real logic now
lives in named, testable functions with clear inputs and outputs.
"""


def calculate_tip(bill_amount, tip_percent=15):
    """Return the tip amount for a bill, given a tip percentage (default 15%)."""
    return round(bill_amount * (tip_percent / 100), 2)


def apply_discount(bill_amount, discount_percent=0):
    """Return the bill amount after applying a percentage discount (default: none)."""
    return round(bill_amount * (1 - discount_percent / 100), 2)


def apply_surcharges(bill_amount, *surcharges):
    """Add any number of flat surcharges (delivery fee, service fee, ...) to a bill.

    *surcharges demonstrates variable-length positional arguments: the caller
    can pass zero, one, or many flat fees, and this function doesn't need to
    know in advance how many there will be.
    """
    return round(bill_amount + sum(surcharges), 2)


def split_bill(total, num_people=1):
    """Split a total evenly across num_people (default 1, i.e. no split)."""
    if num_people <= 0:
        return total
    return round(total / num_people, 2)


def summarize_fees(**fees):
    """Total up any number of named fees passed in as keyword arguments.

    **fees demonstrates variable-length keyword arguments: the caller can
    attach any labeled fees (delivery_fee=5, service_fee=2, ...) without
    this function needing a fixed parameter for every possible fee name.
    """
    return round(sum(fees.values()), 2)


def build_receipt(bill_amount, tip_percent=15, discount_percent=0, num_people=1, **extra_fees):
    """Build one full receipt dict by composing the smaller functions above.

    This is the "bring it all together" function -- it doesn't duplicate any
    calculation logic itself, it just calls the other functions in the right
    order and assembles their results. That composition is exactly why
    breaking the math into small functions pays off: each piece is reused
    here instead of being retyped.
    """
    discounted_bill = apply_discount(bill_amount, discount_percent)
    tip_amount = calculate_tip(discounted_bill, tip_percent)
    fees_total = summarize_fees(**extra_fees)
    grand_total = apply_surcharges(discounted_bill + tip_amount, fees_total)
    per_person = split_bill(grand_total, num_people)

    return {
        "original_bill": bill_amount,
        "discount_percent": discount_percent,
        "discounted_bill": discounted_bill,
        "tip_percent": tip_percent,
        "tip_amount": tip_amount,
        "extra_fees": dict(extra_fees),
        "fees_total": fees_total,
        "grand_total": grand_total,
        "num_people": num_people,
        "per_person": per_person,
    }


def print_receipt(receipt):
    """Print a receipt dict (from build_receipt) as a formatted, aligned block."""
    print()
    print("--- Receipt ---")
    print(f"{'Original bill:':<22}${receipt['original_bill']:.2f}")
    if receipt["discount_percent"] > 0:
        print(f"{'Discount:':<22}{receipt['discount_percent']}% -> ${receipt['discounted_bill']:.2f}")
    print(f"{'Tip (' + str(receipt['tip_percent']) + '%):':<22}${receipt['tip_amount']:.2f}")
    for fee_name, fee_amount in receipt["extra_fees"].items():
        label = fee_name.replace("_", " ").title() + ":"
        print(f"{label:<22}${fee_amount:.2f}")
    print(f"{'Grand total:':<22}${receipt['grand_total']:.2f}")
    if receipt["num_people"] > 1:
        print(f"{'Per person (' + str(receipt['num_people']) + '):':<22}${receipt['per_person']:.2f}")


def read_float(prompt, default):
    """Read a number from the user, falling back to a default on blank input."""
    raw = input(prompt).strip()
    if raw == "":
        return default
    return float(raw)


def read_int(prompt, default):
    """Read a whole number from the user, falling back to a default on blank input."""
    raw = input(prompt).strip()
    if raw == "":
        return default
    return int(raw)


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
            while fee_num <= fee_count:
                fee_name = input(f"  Fee #{fee_num} name (e.g. delivery_fee): ").strip().replace(" ", "_")
                fee_amount = read_float(f"  Fee #{fee_num} amount: $", 0)
                extra_fees[fee_name] = fee_amount
                fee_num += 1

        receipt = build_receipt(bill, tip_percent, percent, people, **extra_fees)
        receipts.append(receipt)
        print_receipt(receipt)

    elif choice == "5":
        print()
        if len(receipts) == 0:
            print("No receipts built yet this session.")
        else:
            print(f"--- Session History ({len(receipts)} receipt(s)) ---")
            index = 1
            for receipt in receipts:
                print(f"{index}. Bill ${receipt['original_bill']:.2f} -> Grand total ${receipt['grand_total']:.2f}")
                index += 1

    elif choice == "6":
        print()
        print(f"Session summary: {len(receipts)} receipt(s) built.")
        print("Goodbye!")
        break

    else:
        print("Please choose 1-6.")
