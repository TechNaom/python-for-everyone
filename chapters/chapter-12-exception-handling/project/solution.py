"""
Chapter 12 Project: ATM Simulator -- reference solution.
See README.md in this folder for the full brief and example output.

This project is built AROUND custom exceptions as its core organizing
principle -- every rule about what makes a transaction valid (can't withdraw
more than the balance, can't deposit/withdraw a non-positive amount) is
enforced by *raising* a custom exception class subclassed from Exception,
and the menu loop's job is just to *catch* those exceptions and print a
friendly message, exactly like Chapter 11's project was organized around
math/datetime. Each operation lives in its own small function, matching
Chapter 10's function-library pattern.
"""
import datetime


class InsufficientFundsError(Exception):
    """Raised when a withdrawal would take the balance below zero."""
    def __init__(self, amount, balance):
        self.amount = amount
        self.balance = balance
        message = f"cannot withdraw ${amount:.2f} -- balance is only ${balance:.2f}"
        super().__init__(message)


class InvalidAmountError(Exception):
    """Raised when an amount for a deposit/withdrawal isn't a positive number."""
    def __init__(self, amount):
        self.amount = amount
        super().__init__(f"amount must be a positive number, got {amount!r}")


def validate_amount(amount):
    """Raise InvalidAmountError if amount isn't a positive number."""
    if amount <= 0:
        raise InvalidAmountError(amount)


def parse_amount(raw):
    """Turn typed text into a positive float, or raise InvalidAmountError."""
    try:
        amount = float(raw)
    except ValueError:
        raise InvalidAmountError(raw)
    validate_amount(amount)
    return amount


def deposit(balance, amount):
    """Return the new balance after depositing amount. Raises InvalidAmountError."""
    validate_amount(amount)
    return round(balance + amount, 2)


def withdraw(balance, amount):
    """Return the new balance after withdrawing amount.

    Raises InvalidAmountError for a non-positive amount, and
    InsufficientFundsError if amount is more than the current balance.
    """
    validate_amount(amount)
    if amount > balance:
        raise InsufficientFundsError(amount, balance)
    return round(balance - amount, 2)


def record_transaction(history, kind, amount, balance_after, today):
    """Append one transaction dict to the running history list."""
    history.append({
        "kind": kind,
        "amount": round(amount, 2),
        "balance_after": balance_after,
        "date": today,
    })


def print_transaction(entry, index):
    """Print one transaction as a numbered, aligned line."""
    print(
        f"{index}. [{entry['date']}] {entry['kind']:<10} "
        f"${entry['amount']:.2f}  (balance after: ${entry['balance_after']:.2f})"
    )


# --- Session state ---
balance = 100.00  # starting balance for this simulated account
history = []       # running list of every transaction this session
today = datetime.date.today()

print("=== ATM Simulator ===")
print(f"Today's date: {today}")
print(f"Starting balance: ${balance:.2f}")

while True:
    print()
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. View transaction history")
    print("5. Quit")
    choice = input("Choose an option (1-5): ").strip()

    if choice == "1":
        print()
        print(f"Current balance: ${balance:.2f}")

    elif choice == "2":
        print()
        raw = input("Amount to deposit: $")
        try:
            amount = parse_amount(raw)
            balance = deposit(balance, amount)
            record_transaction(history, "deposit", amount, balance, today)
            print(f"Deposited ${amount:.2f}. New balance: ${balance:.2f}")
        except InvalidAmountError as e:
            print(f"Deposit failed: {e}")

    elif choice == "3":
        print()
        raw = input("Amount to withdraw: $")
        try:
            amount = parse_amount(raw)
            balance = withdraw(balance, amount)
            record_transaction(history, "withdraw", amount, balance, today)
            print(f"Withdrew ${amount:.2f}. New balance: ${balance:.2f}")
        except InvalidAmountError as e:
            print(f"Withdrawal failed: {e}")
        except InsufficientFundsError as e:
            print(f"Withdrawal failed: {e}")

    elif choice == "4":
        print()
        if len(history) == 0:
            print("No transactions recorded yet.")
        else:
            index = 1
            for entry in history:
                print_transaction(entry, index)
                index += 1

    elif choice == "5":
        print()
        print(f"Session summary: {len(history)} transaction(s), final balance ${balance:.2f}.")
        print("Goodbye!")
        break

    else:
        print("Please choose 1-5.")
