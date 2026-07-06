"""
Chapter 12 Project: ATM Simulator
See README.md in this folder for the full brief and example output.

This project is built AROUND custom exceptions as its core organizing
principle -- every rule about what makes a transaction valid (can't withdraw
more than the balance, can't deposit/withdraw a non-positive amount) is
enforced by *raising* a custom exception class subclassed from Exception,
and the menu loop's job is just to *catch* those exceptions and print a
friendly message, exactly like Chapter 11's project was organized around
math/datetime. Each operation lives in its own small function, matching
Chapter 10's function-library pattern. Fill in the numbered TODOs below.
"""
import datetime


class InsufficientFundsError(Exception):
    """Raised when a withdrawal would take the balance below zero."""
    def __init__(self, amount, balance):
        # TODO 1: Store amount and balance on self (self.amount, self.balance),
        # build a message like: f"cannot withdraw ${amount:.2f} -- balance is
        # only ${balance:.2f}", then call super().__init__(message) so the
        # exception's str() shows that message.
        pass


class InvalidAmountError(Exception):
    """Raised when an amount for a deposit/withdrawal isn't a positive number."""
    def __init__(self, amount):
        # TODO 2: Store amount on self (self.amount), then call
        # super().__init__(...) with a message like:
        # f"amount must be a positive number, got {amount!r}"
        pass


def validate_amount(amount):
    """Raise InvalidAmountError if amount isn't a positive number."""
    # TODO 3: If amount <= 0, raise InvalidAmountError(amount).
    pass


def parse_amount(raw):
    """Turn typed text into a positive float, or raise InvalidAmountError."""
    # TODO 4: Try converting raw to a float. If that raises ValueError,
    # raise InvalidAmountError(raw) instead (use "raise ... from e" so the
    # original ValueError stays attached as context). If the conversion
    # succeeds, call validate_amount(amount) on the result, then return it.
    pass


def deposit(balance, amount):
    """Return the new balance after depositing amount. Raises InvalidAmountError."""
    # TODO 5: Call validate_amount(amount), then return
    # round(balance + amount, 2).
    pass


def withdraw(balance, amount):
    """Return the new balance after withdrawing amount.

    Raises InvalidAmountError for a non-positive amount, and
    InsufficientFundsError if amount is more than the current balance.
    """
    # TODO 6: Call validate_amount(amount). If amount > balance, raise
    # InsufficientFundsError(amount, balance). Otherwise return
    # round(balance - amount, 2).
    pass


def record_transaction(history, kind, amount, balance_after, today):
    """Append one transaction dict to the running history list."""
    # TODO 7: Build a dict with keys "kind", "amount" (rounded to 2 decimals),
    # "balance_after", and "date" (today), and append it to history.
    pass


def print_transaction(entry, index):
    """Print one transaction as a numbered, aligned line."""
    # TODO 8: Print a line in this format, using an f-string with :<10 for
    # the kind and :.2f for both amounts:
    #   print(f"{index}. [{entry['date']}] {entry['kind']:<10} "
    #         f"${entry['amount']:.2f}  (balance after: ${entry['balance_after']:.2f})")
    pass


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
            # TODO 9: Parse raw into amount with parse_amount(raw), call
            # deposit(balance, amount) and reassign it to balance, call
            # record_transaction(history, "deposit", amount, balance, today),
            # then print f"Deposited ${amount:.2f}. New balance: ${balance:.2f}"
            pass
        except InvalidAmountError as e:
            print(f"Deposit failed: {e}")

    elif choice == "3":
        print()
        raw = input("Amount to withdraw: $")
        try:
            # TODO 10: Same idea as TODO 9, but call withdraw(balance, amount)
            # instead of deposit(...), record kind "withdraw", and print
            # f"Withdrew ${amount:.2f}. New balance: ${balance:.2f}". This
            # try block needs to catch BOTH InvalidAmountError (bad/blank
            # input) and InsufficientFundsError (amount bigger than
            # balance) -- see the except clauses below.
            pass
        except InvalidAmountError as e:
            print(f"Withdrawal failed: {e}")
        except InsufficientFundsError as e:
            print(f"Withdrawal failed: {e}")

    elif choice == "4":
        print()
        if len(history) == 0:
            print("No transactions recorded yet.")
        else:
            # TODO 11: Loop over history with a running counter variable you
            # increment yourself, calling print_transaction(entry, index)
            # for each one (same pattern as Chapter 10's project history
            # loop).
            pass

    elif choice == "5":
        print()
        # TODO 12: Print a one-line session summary showing how many
        # transactions were recorded and the final balance, print
        # "Goodbye!", then break out of the loop.
        pass

    else:
        print("Please choose 1-5.")
