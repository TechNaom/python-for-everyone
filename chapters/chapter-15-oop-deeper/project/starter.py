"""
Chapter 15 Project: Bank Account System
See README.md in this folder for the full brief and example output.

This project is built AROUND this chapter's deeper OOP tools. The
BankAccount class exposes balance as a @property with a validating
@balance.setter (rejects a direct negative assignment), a @classmethod
alternative constructor (open_new_account, which builds an account a
different way than a plain __init__ call, generating its own account
number), and a @staticmethod utility (is_valid_account_number) that
validates an account-number format with no need for any particular
instance's data. Fill in the numbered TODOs below.
"""


class BankAccount:
    """One bank account, with an owner name, account number, and balance
    exposed through validated properties."""

    _next_suffix = 1000  # class attribute: shared counter for generated account numbers

    def __init__(self, owner, account_number, balance=0):
        # TODO 1: Set self._owner = owner. Then, if
        # BankAccount.is_valid_account_number(account_number) is False,
        # raise ValueError(f"Invalid account number format: {account_number!r}").
        # Otherwise set self._account_number = account_number. Finally, set
        # self.balance = balance (this routes through the @balance.setter
        # below from TODO 5, so it gets validated too).
        pass

    @classmethod
    def open_new_account(cls, owner, opening_deposit=0):
        """Alternative constructor: opens a brand-new account for `owner`,
        generating its own account number instead of requiring the caller
        to supply one."""
        # TODO 2: Build account_number as f"ACC-{cls._next_suffix}", then
        # increment cls._next_suffix by 1. Return cls(owner, account_number,
        # opening_deposit) -- using cls (not the literal class name) is what
        # makes this a proper classmethod alternative constructor.
        pass

    @staticmethod
    def is_valid_account_number(account_number):
        """Validate the account-number format: 'ACC-' followed by digits.
        Needs no instance or class data -- a pure format check."""
        # TODO 3: Return False if account_number isn't a str. Return False
        # if it doesn't start with "ACC-". Otherwise take the substring
        # after "ACC-" and return True only if that substring is all digits
        # and non-empty (str.isdigit()).
        pass

    @property
    def balance(self):
        """Read-facing balance -- looks like plain attribute access at every
        call site, but is really a method running underneath."""
        # TODO 4: Return self._balance.
        pass

    @balance.setter
    def balance(self, value):
        """Validates before storing: rejects a negative balance outright."""
        # TODO 5: If value < 0, raise ValueError("Balance cannot be set to
        # a negative value."). Otherwise set self._balance = value.
        pass

    @property
    def owner(self):
        # TODO 6: Return self._owner.
        pass

    @property
    def account_number(self):
        # TODO 7: Return self._account_number.
        pass

    def deposit(self, amount):
        """Deposit a positive amount. Returns True if it worked, False if
        the amount wasn't positive."""
        # TODO 8: If amount <= 0, return False. Otherwise set
        # self.balance = self.balance + amount (through the property
        # setter, so it's still validated) and return True.
        pass

    def withdraw(self, amount):
        """Withdraw a positive amount, up to the current balance. Returns
        True if it worked, False if the amount was invalid or exceeded the
        balance."""
        # TODO 9: If amount <= 0 or amount > self.balance, return False.
        # Otherwise set self.balance = self.balance - amount and return True.
        pass

    def __str__(self):
        # TODO 10: Return an f-string like:
        # f"Account {self.account_number} ({self.owner}) -- balance:
        # ${self.balance:,.2f}"
        pass


def find_account(accounts, account_number):
    """Look up an account by account number in a list of BankAccount
    objects. Returns the account, or None if no match."""
    # TODO 11: Loop over accounts and return the first one whose
    # .account_number matches the account_number argument. If none match,
    # return None.
    pass


# --- Session state ---
print("=== Bank Account System ===")
accounts = []

# Seed a couple of starting accounts so the menu has something to work with.
accounts.append(BankAccount.open_new_account("Aria Chen", 500))
accounts.append(BankAccount.open_new_account("Devon Brooks", 150))
print(f"Loaded {len(accounts)} account(s).")

while True:
    print()
    print("1. Open a new account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check balance")
    print("5. View account details")
    print("6. List all accounts")
    print("7. Quit")
    choice = input("Choose an option (1-7): ").strip()

    if choice == "1":
        print()
        owner = input("Owner name: ").strip()
        deposit_str = input("Opening deposit (blank for 0): ").strip()
        # TODO 12: If owner is empty, print "Owner name is required." and
        # continue. Otherwise convert deposit_str to a float (0 if blank),
        # catching ValueError to print "Opening deposit must be a number."
        # and continue if it fails. Then try calling
        # BankAccount.open_new_account(owner, opening_deposit), catching
        # ValueError to print f"Could not open account: {e}" -- otherwise
        # append the new account to accounts and print f"Opened: {account}".
        pass

    elif choice == "2":
        print()
        account_number = input("Account number: ").strip()
        # TODO 13: Look the account up with find_account(accounts,
        # account_number). If None, print that no account was found.
        # Otherwise ask for a deposit amount, convert it to a float
        # (catching ValueError), and call account.deposit(amount) -- True
        # prints the new balance, False prints that the amount must be
        # positive.
        pass

    elif choice == "3":
        print()
        account_number = input("Account number: ").strip()
        # TODO 14: Same lookup pattern as TODO 13, but ask for a withdraw
        # amount and call account.withdraw(amount) instead -- True prints
        # the new balance, False prints that the withdrawal failed (amount
        # must be positive and not exceed the balance).
        pass

    elif choice == "4":
        print()
        account_number = input("Account number: ").strip()
        # TODO 15: Look the account up with find_account. If None, print
        # that no account was found. Otherwise print the balance using
        # account.balance (this reads through the @property getter).
        pass

    elif choice == "5":
        print()
        account_number = input("Account number: ").strip()
        # TODO 16: Look the account up with find_account. If None, print
        # that no account was found. Otherwise print(account) (relies on
        # __str__ from TODO 10).
        pass

    elif choice == "6":
        print()
        # TODO 17: If accounts is empty, print "No accounts to show."
        # Otherwise print f"All accounts ({len(accounts)}):" and loop over
        # accounts printing f"  {account}" for each one.
        pass

    elif choice == "7":
        print()
        print("Goodbye!")
        break

    else:
        print("Please choose 1-7.")
