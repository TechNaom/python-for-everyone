"""
Chapter 15 Practice Bank: OOP Deeper -- reference solution.
See README.md in this folder for full instructions.
Run this from inside the practice/ folder: python3 solution.py
"""

# ============================================================
# Topic 1: @staticmethod
# ============================================================

# TODO 1.1
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return celsius * 9 / 5 + 32


print(TemperatureConverter.celsius_to_fahrenheit(100))


# TODO 1.2
class StringHelper:
    @staticmethod
    def is_palindrome(text):
        cleaned = text.lower().replace(" ", "")
        return cleaned == cleaned[::-1]


print(StringHelper.is_palindrome("Was it a car or a cat"))


# TODO 1.3
class MathHelper:
    @staticmethod
    def is_prime(number):
        if number < 2:
            return False
        for divisor in range(2, number):
            if number % divisor == 0:
                return False
        return True


print(MathHelper.is_prime(17))
print(MathHelper.is_prime(15))


# TODO 1.4
class Validator:
    @staticmethod
    def is_valid_email(email):
        parts = email.split("@")
        if len(parts) != 2:
            return False
        return "." in parts[1]


print(Validator.is_valid_email("user@example.com"))
print(Validator.is_valid_email("not-an-email"))


# TODO 1.5 (Debug the Code)
class PriceHelper:
    @staticmethod
    def apply_discount(price, percent_off):
        return price * (1 - percent_off / 100)


print(PriceHelper.apply_discount(100, 10))


# TODO 1.A (Scenario -- A Shared Tax Calculator Utility)
class TaxCalculator:
    @staticmethod
    def calculate_tax(subtotal, tax_rate):
        return round(subtotal * tax_rate, 2)


print(TaxCalculator.calculate_tax(200, 0.0825))


# TODO 1.B (Scenario -- Interview Prep)
def explain_staticmethod_purpose():
    return (
        "A @staticmethod is a method that doesn't need self or access to "
        "any instance or class data -- it behaves like a regular function, "
        "but living inside the class groups it with the related "
        "functionality it belongs to conceptually (like a unit converter "
        "living on the class it converts for), keeping the namespace "
        "organized and making the relationship discoverable to anyone "
        "reading the class, instead of leaving a loose function floating "
        "around the module with no clear tie to what it's for."
    )


print(explain_staticmethod_purpose())


# ============================================================
# Topic 2: @classmethod and Alternative Constructors
# ============================================================

# TODO 2.1
class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings

    @classmethod
    def margherita(cls):
        return cls(["tomato", "mozzarella", "basil"])


pizza = Pizza.margherita()
print(pizza.toppings)


# TODO 2.2
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_string(cls, date_string):
        year, month, day = date_string.split("-")
        return cls(int(year), int(month), int(day))


date = Date.from_string("2026-07-04")
print(date.year)
print(date.month)
print(date.day)


# TODO 2.3
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def entry_level(cls, name):
        return cls(name, 45000)


employee = Employee.entry_level("Priya")
print(employee.name)
print(employee.salary)


# TODO 2.4
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @classmethod
    def square(cls, side_length):
        return cls(side_length, side_length)


square = Rectangle.square(5)
print(square.width)
print(square.height)


# TODO 2.5 (Debug the Code)
class Account:
    def __init__(self, balance):
        self.balance = balance

    @classmethod
    def starting_at_zero(cls):
        return cls(0)


account = Account.starting_at_zero()
print(account.balance)


# TODO 2.A (Scenario -- Building a User from an API Response)
class UserProfile:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    @classmethod
    def from_api_response(cls, data):
        return cls(data["username"], data["email"])


profile = UserProfile.from_api_response(
    {"username": "mpapasani", "email": "mp@example.com"}
)
print(profile.username)
print(profile.email)


# TODO 2.B (Scenario -- Interview Prep)
def explain_classmethod_alternative_constructors():
    return (
        "@classmethod receives the class itself (cls) instead of an "
        "instance (self), which lets it build and return a new instance "
        "using cls(...). This is the standard pattern for 'alternative "
        "constructors' that create an instance a different way (from a "
        "string, from a dict, with sensible defaults for a common case) "
        "without cramming every possible construction path into one "
        "increasingly complicated __init__ signature full of optional "
        "parameters that don't all make sense together."
    )


print(explain_classmethod_alternative_constructors())


# ============================================================
# Topic 3: Encapsulation & Privacy Conventions
# ============================================================

# TODO 3.1
class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    def get_balance(self):
        return self._balance


account = BankAccount(500)
print(account.get_balance())


# TODO 3.2
class Config:
    def __init__(self):
        self.__secret_key = "abc123"

    def reveal_key(self):
        return self.__secret_key


config = Config()
print(config.reveal_key())


# TODO 3.3
class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age

    def have_birthday(self):
        self._age += 1


person = Person("Sam", 29)
person.have_birthday()
print(person._age)


# TODO 3.4
class Wallet:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance


wallet = Wallet(100)
wallet.deposit(50)
print(wallet.get_balance())


# TODO 3.5 (Debug the Code)
class Account:
    def __init__(self, balance):
        self.__balance = balance


account = Account(200)
print(account._Account__balance)


# TODO 3.A (Scenario -- Protecting an Internal Cache)
class ReportCache:
    def __init__(self):
        self.__cache = {}

    def store(self, key, value):
        self.__cache[key] = value

    def get(self, key):
        return self.__cache.get(key, "not found")


cache = ReportCache()
cache.store("q3_revenue", 50000)
print(cache.get("q3_revenue"))
print(cache.get("q4_revenue"))


# TODO 3.B (Scenario -- Interview Prep)
def explain_consenting_adults_philosophy():
    return (
        "Python doesn't have a way to truly block access to an attribute "
        "the way some other languages do -- a single leading underscore "
        "(_x) is just a convention signaling 'this is internal, please "
        "treat it as implementation detail,' and a double leading "
        "underscore (__x) triggers name-mangling that makes accidental "
        "outside access harder but not impossible, not true enforcement. "
        "Python's philosophy is that well-informed adults using a library "
        "responsibly shouldn't need the language to physically stop them "
        "from reaching into internals -- the underscore is a clear signal "
        "of intent that trusts the caller to respect it, rather than a "
        "lock."
    )


print(explain_consenting_adults_philosophy())


# ============================================================
# Topic 4: @property Getters
# ============================================================

# TODO 4.1
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius


circle = Circle(5)
print(circle.radius)


# TODO 4.2
class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def area(self):
        return self._width * self._height


rectangle = Rectangle(4, 5)
print(rectangle.area)


# TODO 4.3
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


person = Person("Ada", "Lovelace")
print(person.full_name)


# TODO 4.4
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def fahrenheit(self):
        return self._celsius * 9 / 5 + 32


temperature = Temperature(100)
print(temperature.fahrenheit)


# TODO 4.5 (Debug the Code)
class Order:
    def __init__(self, subtotal, tax):
        self._subtotal = subtotal
        self._tax = tax

    @property
    def total(self):
        return self._subtotal + self._tax


order = Order(100, 8.25)
print(order.total)


# TODO 4.A (Scenario -- A Read-Only Derived Field on a User Profile)
class UserProfile:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    @property
    def age(self):
        return 2026 - self.birth_year


profile = UserProfile("Dana", 1994)
print(profile.age)


# TODO 4.B (Scenario -- Interview Prep)
def explain_property_getters():
    return (
        "@property lets a method be accessed with plain attribute syntax "
        "(obj.area instead of obj.get_area()), which reads more naturally "
        "for values that feel like data even though they're actually "
        "computed. It also means a class can start with a plain stored "
        "attribute and later upgrade it to a computed one without "
        "breaking any code that reads it, since the calling syntax never "
        "has to change from obj.attribute either way."
    )


print(explain_property_getters())


# ============================================================
# Topic 5: @x.setter and Validation on Assignment
# ============================================================

# TODO 5.1
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("radius cannot be negative")
        self._radius = value


circle = Circle(5)
print(circle.radius)
try:
    circle.radius = -3
except ValueError as error:
    print(error)


# TODO 5.2
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("age cannot be negative")
        self._age = value


person = Person("Sam", 30)
print(person.age)
try:
    person.age = -5
except ValueError as error:
    print(error)


# TODO 5.3
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("price cannot be negative")
        self._price = value


product = Product("Widget", 9.99)
product.price = 12.5
print(product.price)


# TODO 5.4
class Email:
    def __init__(self, address):
        self.address = address

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        if "@" not in value:
            raise ValueError("invalid email address")
        self._address = value


email = Email("user@example.com")
print(email.address)
try:
    email.address = "not-an-email"
except ValueError as error:
    print(error)


# TODO 5.5 (Debug the Code)
class Thermostat:
    def __init__(self, target):
        self.target = target

    @property
    def target(self):
        return self._target

    @target.setter
    def target(self, value):
        if value < -273.15:
            raise ValueError("temperature cannot be below absolute zero")
        self._target = value


thermostat = Thermostat(21)
print(thermostat.target)


# TODO 5.A (Scenario -- Validating Signup Form Data)
class UserAccount:
    def __init__(self, username):
        self.username = username

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        if not value.strip():
            raise ValueError("username cannot be blank")
        self._username = value.strip()


user = UserAccount("mpapasani")
print(user.username)
try:
    user.username = "   "
except ValueError as error:
    print(error)


# TODO 5.B (Scenario -- Interview Prep)
def explain_property_setters():
    return (
        "A @x.setter runs its validation every single time the attribute "
        "is assigned -- not just once in __init__ -- so "
        "obj.attribute = new_value is guarded the same way the very "
        "first assignment was, closing the door on a class ever "
        "silently drifting into an invalid state through some later "
        "assignment elsewhere in the codebase. This keeps the validation "
        "rule defined in exactly one place instead of being repeated (or "
        "forgotten) at every call site that happens to set the "
        "attribute."
    )


print(explain_property_setters())


# ============================================================
# Topic 6: Bringing It Together -- Deeper OOP in Production
# ============================================================

# TODO 6.1
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("price cannot be negative")
        self._price = value

    @staticmethod
    def apply_tax(price, tax_rate):
        return round(price * (1 + tax_rate), 2)

    @classmethod
    def on_sale(cls, name, original_price, discount_percent):
        return cls(name, original_price * (1 - discount_percent / 100))


product = Product.on_sale("Headphones", 100, 20)
print(product.price)
print(Product.apply_tax(product.price, 0.08))


# TODO 6.2
class Employee:
    __next_id = 1000

    def __init__(self, name, salary):
        self.name = name
        self._salary = salary
        self.id = Employee.__next_id
        Employee.__next_id += 1

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("salary cannot be negative")
        self._salary = value

    @classmethod
    def hire_intern(cls, name):
        return cls(name, 40000)


intern = Employee.hire_intern("Jordan")
print(intern.id)
print(intern.salary)


# TODO 6.3
class InventoryItem:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if value < 0:
            raise ValueError("quantity cannot be negative")
        self._quantity = value

    def restock(self, amount):
        self.quantity = self.quantity + amount

    @staticmethod
    def reorder_threshold():
        return 10


item = InventoryItem("Widget", 5)
item.restock(20)
print(item.quantity)
print(item.quantity > InventoryItem.reorder_threshold())


# TODO 6.4
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("balance cannot be negative")
        self._balance = value

    def withdraw(self, amount):
        self.balance = self.balance - amount

    @classmethod
    def open_with_bonus(cls, owner):
        return cls(owner, 25)


account = BankAccount.open_with_bonus("Dana")
print(account.balance)
try:
    account.withdraw(100)
except ValueError as error:
    print(error)


# TODO 6.5 (Debug the Code)
class Subscription:
    def __init__(self, plan_name, price):
        self.plan_name = plan_name
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("price cannot be negative")
        self._price = value


try:
    subscription = Subscription("Basic", -5)
    print(subscription.price)
except ValueError as error:
    print(error)


# TODO 6.A (Scenario -- A Small Payroll System)
class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    @property
    def base_salary(self):
        return self._base_salary

    @base_salary.setter
    def base_salary(self, value):
        if value < 0:
            raise ValueError("base salary cannot be negative")
        self._base_salary = value

    @staticmethod
    def annual_from_monthly(monthly_amount):
        return round(monthly_amount * 12, 2)

    @classmethod
    def salaried_from_monthly(cls, name, monthly_amount):
        return cls(name, cls.annual_from_monthly(monthly_amount))


employee = Employee.salaried_from_monthly("Priya", 5000)
print(employee.base_salary)


# TODO 6.B (Scenario -- Interview Prep)
def explain_deeper_oop_production_value():
    return (
        "These three tools solve different but related problems in the "
        "same class: @staticmethod groups a pure utility calculation "
        "with the class it conceptually belongs to even though it needs "
        "no instance data; @classmethod provides alternative, more-"
        "convenient ways to construct a valid instance without bloating "
        "__init__ with optional parameters; and @property (with its "
        "setter) lets attribute-style access stay simple for callers "
        "while the class quietly enforces its own validation rules on "
        "every read or write. Together they let a class expose a clean, "
        "attribute-like surface to the rest of the program while keeping "
        "its internal rules and invariants fully under its own control, "
        "which is exactly the kind of class real production codebases "
        "are built from."
    )


print(explain_deeper_oop_production_value())
