"""
Chapter 15 Project: Bank Account System -- reference solution.
See README.md in this folder for the full brief and example output.

This project is built AROUND this chapter's deeper OOP tools. The
BankAccount class exposes balance as a @property with a validating
@balance.setter (rejects a direct negative assignment), a @classmethod
alternative constructor (open_new_account, which builds an account a
different way than a plain __init__ call, generating its own account
number), and a @staticmethod utility (is_valid_account_number) that
validates an account-number format with no need for any particular
instance's data. Encapsulation is practiced with a single leading
underscore (_balance, _owner, _account_number) -- an internal-use signal,
not enforced privacy -- matching this chapter's "consenting adults"
philosophy covered in interview-questions.html.

No inheritance is used anywhere in this file.
"""


class BankAccount:
    """One bank account, with an owner name, account number, and balance
    exposed through validated properties."""

    _next_suffix = 1000  # class attribute: shared counter for generated account numbers

    def __init__(self, owner, account_number, balance=0):
        self._owner = owner
        # TODO-equivalent note (solution has no TODOs): account_number is
        # validated once here via the staticmethod, then stored.
        if not BankAccount.is_valid_account_number(account_number):
            raise ValueError(f"Invalid account number format: {account_number!r}")
        self._account_number = account_number
        # Route the initial balance through the property setter too, so the
        # same validation rule applies whether an account starts at 0 or is
        # loaded with a starting balance.
        self.balance = balance

    @classmethod
    def open_new_account(cls, owner, opening_deposit=0):
        """Alternative constructor: opens a brand-new account for `owner`,
        generating its own account number instead of requiring the caller
        to supply one. This is the 'open a new account' menu path."""
        account_number = f"ACC-{cls._next_suffix}"
        cls._next_suffix += 1
        return cls(owner, account_number, opening_deposit)

    @staticmethod
    def is_valid_account_number(account_number):
        """Validate the account-number format: 'ACC-' followed by digits.
        Needs no instance or class data -- a pure format check."""
        if not isinstance(account_number, str):
            return False
        if not account_number.startswith("ACC-"):
            return False
        digits = account_number[len("ACC-"):]
        return digits.isdigit() and len(digits) > 0

    @property
    def balance(self):
        """Read-facing balance -- looks like plain attribute access at every
        call site, but is really a method running underneath."""
        return self._balance

    @balance.setter
    def balance(self, value):
        """Validates before storing: rejects a negative balance outright,
        no matter where the assignment comes from (deposit, withdraw, or a
        direct account.balance = ... assignment)."""
        if value < 0:
            raise ValueError("Balance cannot be set to a negative value.")
        self._balance = value

    @property
    def owner(self):
        return self._owner

    @property
    def account_number(self):
        return self._account_number

    def deposit(self, amount):
        """Deposit a positive amount. Returns True if it worked, False if
        the amount wasn't positive."""
        if amount <= 0:
            return False
        self.balance = self.balance + amount
        return True

    def withdraw(self, amount):
        """Withdraw a positive amount, up to the current balance. Returns
        True if it worked, False if the amount was invalid or exceeded the
        balance."""
        if amount <= 0:
            return False
        if amount > self.balance:
            return False
        self.balance = self.balance - amount
        return True

    def __str__(self):
        return (
            f"Account {self.account_number} ({self.owner}) "
            f"-- balance: ${self.balance:,.2f}"
        )


def find_account(accounts, account_number):
    """Look up an account by account number in a list of BankAccount
    objects. Returns the account, or None if no match."""
    for account in accounts:
        if account.account_number == account_number:
            return account
    return None


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
        if not owner:
            print("Owner name is required.")
            continue
        try:
            opening_deposit = float(deposit_str) if deposit_str else 0
        except ValueError:
            print("Opening deposit must be a number.")
            continue
        try:
            account = BankAccount.open_new_account(owner, opening_deposit)
        except ValueError as e:
            print(f"Could not open account: {e}")
        else:
            accounts.append(account)
            print(f"Opened: {account}")

    elif choice == "2":
        print()
        account_number = input("Account number: ").strip()
        account = find_account(accounts, account_number)
        if account is None:
            print(f"No account found with number {account_number}.")
        else:
            amount_str = input("Deposit amount: ").strip()
            try:
                amount = float(amount_str)
            except ValueError:
                print("Amount must be a number.")
                continue
            if account.deposit(amount):
                print(f"Deposited ${amount:,.2f}. New balance: ${account.balance:,.2f}")
            else:
                print("Deposit amount must be positive.")

    elif choice == "3":
        print()
        account_number = input("Account number: ").strip()
        account = find_account(accounts, account_number)
        if account is None:
            print(f"No account found with number {account_number}.")
        else:
            amount_str = input("Withdraw amount: ").strip()
            try:
                amount = float(amount_str)
            except ValueError:
                print("Amount must be a number.")
                continue
            if account.withdraw(amount):
                print(f"Withdrew ${amount:,.2f}. New balance: ${account.balance:,.2f}")
            else:
                print("Withdrawal failed -- amount must be positive and not exceed the balance.")

    elif choice == "4":
        print()
        account_number = input("Account number: ").strip()
        account = find_account(accounts, account_number)
        if account is None:
            print(f"No account found with number {account_number}.")
        else:
            # Reads the balance property -- looks like plain attribute
            # access, but runs BankAccount.balance's getter underneath.
            print(f"Balance for {account_number}: ${account.balance:,.2f}")

    elif choice == "5":
        print()
        account_number = input("Account number: ").strip()
        account = find_account(accounts, account_number)
        if account is None:
            print(f"No account found with number {account_number}.")
        else:
            print(account)

    elif choice == "6":
        print()
        if not accounts:
            print("No accounts to show.")
        else:
            print(f"All accounts ({len(accounts)}):")
            for account in accounts:
                print(f"  {account}")

    elif choice == "7":
        print()
        print("Goodbye!")
        break

    else:
        print("Please choose 1-7.")
