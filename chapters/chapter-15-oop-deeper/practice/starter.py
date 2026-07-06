"""
Chapter 15 Practice Bank: OOP Deeper
See README.md in this folder for full instructions.
Run this from inside the practice/ folder: python3 starter.py
"""

# ============================================================
# Topic 1: @staticmethod
# ============================================================

# TODO 1.1: Write a class TemperatureConverter with a @staticmethod
# celsius_to_fahrenheit(celsius) that returns celsius * 9 / 5 + 32 --
# it doesn't need self or any instance data, just a plain calculation
# grouped inside the class because it's related to temperatures. Call
# TemperatureConverter.celsius_to_fahrenheit(100) directly on the
# class (no instance needed) and print the result.


# TODO 1.2: Write a class StringHelper with a @staticmethod
# is_palindrome(text) that returns True if text.lower() reads the
# same forwards and backwards, ignoring spaces (hint: build a cleaned
# version with text.lower().replace(" ", "") and compare it to its own
# reverse slice [::-1]). Call
# StringHelper.is_palindrome("Was it a car or a cat") and print the
# result (should be True).


# TODO 1.3: Write a class MathHelper with a @staticmethod
# is_prime(number) that returns False if number is less than 2, then
# checks divisibility from 2 up through number - 1 in a loop,
# returning False as soon as one divides evenly, and True if the loop
# finishes without finding one. Call MathHelper.is_prime(17) and
# MathHelper.is_prime(15), printing both results.


# TODO 1.4: Write a class Validator with a @staticmethod
# is_valid_email(email) that returns True only if email contains
# exactly one "@" and at least one "." after that "@" (hint: split on
# "@" with email.split("@"), check len() is 2, then check "." in the
# second part). Call Validator.is_valid_email("user@example.com") and
# Validator.is_valid_email("not-an-email"), printing both results.


# TODO 1.5 (Debug the Code): this @staticmethod is supposed to work
# without any instance, but it mistakenly includes self as its first
# parameter -- calling PriceHelper.apply_discount(100, 0.1) directly
# on the class raises a TypeError about a missing argument, because
# Python doesn't automatically pass an instance into a staticmethod
# the way it does for a regular instance method. Fix it by removing
# self from the parameter list.
class PriceHelper:
    @staticmethod
    def apply_discount(self, price, percent_off):
        return price * (1 - percent_off / 100)


print(PriceHelper.apply_discount(100, 10))


# TODO 1.A (Scenario -- A Shared Tax Calculator Utility): a checkout
# system needs a tax calculation that doesn't depend on any particular
# order's data -- it's just a pure formula every order can share.
# Write a class TaxCalculator with a @staticmethod
# calculate_tax(subtotal, tax_rate) that returns
# round(subtotal * tax_rate, 2) -- modeling how a utility calculation
# with no instance state belongs on the class itself, not tangled up
# with any one order object. Call
# TaxCalculator.calculate_tax(200, 0.0825) and print the result.


# TODO 1.B (Scenario -- Interview Prep): an interviewer asks why you'd
# ever use @staticmethod instead of just writing a plain standalone
# function outside the class. Write a function
# explain_staticmethod_purpose() that returns a string explaining that
# a @staticmethod is a method that doesn't need self or access to any
# instance or class data -- it behaves like a regular function, but
# living inside the class groups it with the related functionality it
# belongs to conceptually (like a unit converter living on the class
# it converts for), keeping the namespace organized and making the
# relationship discoverable to anyone reading the class, instead of
# leaving a loose function floating around the module with no clear
# tie to what it's for. Call it and print the result.


# ============================================================
# Topic 2: @classmethod and Alternative Constructors
# ============================================================

# TODO 2.1: Write a class Pizza with __init__(self, toppings) storing
# self.toppings = toppings, and a @classmethod margherita(cls) that
# returns cls(["tomato", "mozzarella", "basil"]) -- an alternative
# constructor that builds a specific, common kind of Pizza without the
# caller having to type out the topping list. Create
# pizza = Pizza.margherita() and print pizza.toppings.


# TODO 2.2: Write a class Date with __init__(self, year, month, day)
# storing all three, and a @classmethod from_string(cls, date_string)
# that splits date_string on "-" (format "YYYY-MM-DD"), converts each
# piece to int, and returns cls(year, month, day). Create
# date = Date.from_string("2026-07-04") and print date.year,
# date.month, date.day.


# TODO 2.3: Write a class Employee with __init__(self, name, salary)
# storing both, and a @classmethod entry_level(cls, name) that returns
# cls(name, 45000) -- an alternative constructor for the common case
# of hiring someone at the standard entry-level salary. Create
# employee = Employee.entry_level("Priya") and print employee.name and
# employee.salary.


# TODO 2.4: Write a class Rectangle with __init__(self, width, height)
# storing both, and a @classmethod square(cls, side_length) that
# returns cls(side_length, side_length) -- a square is just a
# rectangle with equal sides, so this alternative constructor builds
# one without the caller repeating the same value twice. Create
# square = Rectangle.square(5) and print square.width and
# square.height.


# TODO 2.5 (Debug the Code): this @classmethod is supposed to build a
# new instance using cls(...) so that it still works correctly if this
# class is ever renamed, but it hardcodes the class name Account(...)
# directly instead of using cls(...) -- printing account.balance still
# happens to work today, but hardcoding the class name is fragile and
# defeats the whole point of a classmethod (it's also what breaks
# immediately once inheritance is introduced next chapter). Fix it by
# replacing Account(balance) with cls(balance).
class Account:
    def __init__(self, balance):
        self.balance = balance

    @classmethod
    def starting_at_zero(cls):
        return Account(0)


account = Account.starting_at_zero()
print(account.balance)


# TODO 2.A (Scenario -- Building a User from an API Response): a web
# service returns user data as a dict, but the rest of the codebase
# works with a UserProfile object. Write a class UserProfile with
# __init__(self, username, email) storing both, and a @classmethod
# from_api_response(cls, data) that returns
# cls(data["username"], data["email"]) -- modeling how real code often
# needs an alternative constructor to translate one shape of incoming
# data (a dict from an API) into the class's normal instance shape.
# Create
# profile = UserProfile.from_api_response({"username": "mpapasani", "email": "mp@example.com"})
# and print profile.username and profile.email.


# TODO 2.B (Scenario -- Interview Prep): an interviewer asks why a
# class would need more than one way to construct an instance, and why
# @classmethod is the right tool for that instead of just adding more
# optional parameters to __init__. Write a function
# explain_classmethod_alternative_constructors() that returns a string
# explaining that @classmethod receives the class itself (cls) instead
# of an instance (self), which lets it build and return a new instance
# using cls(...) -- this is the standard pattern for "alternative
# constructors" that create an instance a different way (from a
# string, from a dict, with sensible defaults for a common case)
# without cramming every possible construction path into one
# increasingly complicated __init__ signature full of optional
# parameters that don't all make sense together. Call it and print the
# result.


# ============================================================
# Topic 3: Encapsulation & Privacy Conventions
# ============================================================

# TODO 3.1: Write a class BankAccount with __init__(self, balance)
# storing self._balance = balance (a single leading underscore --
# signaling "internal, please don't touch this from outside the
# class" by convention, even though Python doesn't enforce it), and a
# method get_balance(self) that returns self._balance. Create
# account = BankAccount(500) and print account.get_balance().


# TODO 3.2: Write a class Config with __init__(self) storing
# self.__secret_key = "abc123" (double leading underscore -- triggers
# Python's name-mangling, so it's stored internally as
# _Config__secret_key), and a method reveal_key(self) that returns
# self.__secret_key. Create config = Config() and print
# config.reveal_key() -- then print dir(config) is NOT required, just
# demonstrate that config.reveal_key() still returns "abc123" through
# the class's own method even though the attribute name is mangled.


# TODO 3.3: Write a class Person with __init__(self, name, age)
# storing self.name = name and self._age = age (single underscore --
# "internal by convention, but consenting adults can still access it
# if they really need to"). Add a method have_birthday(self) that adds
# 1 to self._age. Create person = Person("Sam", 29), call
# person.have_birthday(), then print person._age directly from outside
# the class -- demonstrating that Python trusts the caller ("we're all
# consenting adults here") rather than blocking the access outright.


# TODO 3.4: Write a class Wallet with __init__(self, balance) storing
# self.__balance = balance (double underscore), and two methods:
# deposit(self, amount) that adds amount to self.__balance, and
# get_balance(self) that returns self.__balance. Create
# wallet = Wallet(100), call wallet.deposit(50), then print
# wallet.get_balance() (should be 150) -- showing double-underscore
# attributes are still fully usable from inside the class's own
# methods, just harder to reach accidentally from outside.


# TODO 3.5 (Debug the Code): this code is supposed to read a
# double-underscore attribute from outside the class using Python's
# name-mangled form, but it gets the mangled name wrong -- it tries
# account.__balance directly, which raises AttributeError, instead of
# the actual mangled name Python creates, _Account__balance. Fix the
# print statement to access account._Account__balance instead (the
# real lesson: this is exactly why double-underscore attributes are
# meant to be accessed through the class's own methods, not poked at
# from outside).
class Account:
    def __init__(self, balance):
        self.__balance = balance


account = Account(200)
print(account.__balance)


# TODO 3.A (Scenario -- Protecting an Internal Cache): a reporting
# system keeps an internal cache of computed results that callers
# should never modify directly, only read through a proper method.
# Write a class ReportCache with __init__(self) storing
# self.__cache = {} (double underscore), a method store(self, key,
# value) that sets self.__cache[key] = value, and a method
# get(self, key) that returns self.__cache.get(key, "not found") --
# modeling how a real system hides its internal storage behind
# methods instead of exposing the raw dict for any code anywhere to
# mutate directly. Create cache = ReportCache(), call
# cache.store("q3_revenue", 50000), then print
# cache.get("q3_revenue") and cache.get("q4_revenue").


# TODO 3.B (Scenario -- Interview Prep): an interviewer asks you to
# explain Python's "consenting adults" philosophy around private
# attributes, and how it differs from languages with true
# access-enforced private fields. Write a function
# explain_consenting_adults_philosophy() that returns a string
# explaining that Python doesn't have a way to truly block access to
# an attribute the way some other languages do -- a single leading
# underscore (_x) is just a convention signaling "this is internal,
# please treat it as implementation detail," and a double leading
# underscore (__x) triggers name-mangling that makes accidental
# outside access harder but not impossible, not true enforcement.
# Python's philosophy is that well-informed adults using a library
# responsibly shouldn't need the language to physically stop them from
# reaching into internals -- the underscore is a clear signal of
# intent that trusts the caller to respect it, rather than a lock.
# Call it and print the result.


# ============================================================
# Topic 4: @property Getters
# ============================================================

# TODO 4.1: Write a class Circle with __init__(self, radius) storing
# self._radius = radius, and a @property method radius(self) that
# returns self._radius -- so callers can read circle.radius like a
# plain attribute even though it's actually running a method behind
# the scenes. Create circle = Circle(5) and print circle.radius (note:
# no parentheses -- @property makes it look like plain attribute
# access).


# TODO 4.2: Write a class Rectangle with __init__(self, width, height)
# storing self._width = width and self._height = height, and a
# @property method area(self) that returns self._width * self._height
# -- a computed value that looks like a stored attribute but is
# actually calculated fresh every time it's read. Create
# rectangle = Rectangle(4, 5) and print rectangle.area.


# TODO 4.3: Write a class Person with __init__(self, first_name,
# last_name) storing both, and a @property method full_name(self) that
# returns f"{self.first_name} {self.last_name}". Create
# person = Person("Ada", "Lovelace") and print person.full_name.


# TODO 4.4: Write a class Temperature with __init__(self, celsius)
# storing self._celsius = celsius, and a @property method
# fahrenheit(self) that returns self._celsius * 9 / 5 + 32 -- a
# read-only computed view of the underlying Celsius value, expressed
# in a different unit. Create temperature = Temperature(100) and print
# temperature.fahrenheit.


# TODO 4.5 (Debug the Code): this @property method is supposed to let
# callers read order.total like a plain attribute, but the method is
# still named with parentheses when it's called (order.total()) as if
# it were a regular method -- since @property makes it behave like an
# attribute, calling order.total() actually tries to call whatever
# order.total returns (a plain number), raising TypeError: 'float'
# object is not callable. Fix the print statement to use order.total
# without parentheses.
class Order:
    def __init__(self, subtotal, tax):
        self._subtotal = subtotal
        self._tax = tax

    @property
    def total(self):
        return self._subtotal + self._tax


order = Order(100, 8.25)
print(order.total())


# TODO 4.A (Scenario -- A Read-Only Derived Field on a User Profile):
# a user system stores a birth year but should always display a
# freshly computed age, never a stored age that could quietly go
# stale. Write a class UserProfile with __init__(self, name,
# birth_year) storing both, and a @property method age(self) that
# returns 2026 - self.birth_year -- modeling how a real profile page
# derives "age" from birth_year every time it's displayed instead of
# storing a separate age field that has to be remembered and updated
# every year. Create
# profile = UserProfile("Dana", 1994) and print profile.age.


# TODO 4.B (Scenario -- Interview Prep): an interviewer asks why you'd
# use @property instead of just calling a regular method like
# get_area(). Write a function explain_property_getters() that returns
# a string explaining that @property lets a method be accessed with
# plain attribute syntax (obj.area instead of obj.get_area()), which
# reads more naturally for values that feel like data even though
# they're actually computed -- it also means a class can start with a
# plain stored attribute and later upgrade it to a computed one
# without breaking any code that reads it, since the calling syntax
# never has to change from obj.attribute either way. Call it and print
# the result.


# ============================================================
# Topic 5: @x.setter and Validation on Assignment
# ============================================================

# TODO 5.1: Write a class Circle with __init__(self, radius) that
# calls self.radius = radius (through the setter, not
# self._radius = radius directly), a @property getter radius(self)
# returning self._radius, and a @radius.setter radius(self, value)
# that raises ValueError("radius cannot be negative") if value < 0,
# otherwise sets self._radius = value. Create circle = Circle(5) and
# print circle.radius, then try circle.radius = -3 inside a
# try/except ValueError block, printing the exception's message if it
# raises.


# TODO 5.2: Write a class Person with __init__(self, name, age) that
# calls self.age = age (through the setter), a @property getter
# age(self) returning self._age, and a @age.setter age(self, value)
# that raises ValueError("age cannot be negative") if value < 0,
# otherwise sets self._age = value. Create person = Person("Sam", 30)
# and print person.age, then try person.age = -5 inside a
# try/except ValueError block, printing the exception's message if it
# raises.


# TODO 5.3: Write a class Product with __init__(self, name, price)
# that calls self.price = price (through the setter), a @property
# getter price(self) returning self._price, and a @price.setter
# price(self, value) that raises ValueError("price cannot be
# negative") if value < 0, otherwise sets self._price = value. Create
# product = Product("Widget", 9.99), set product.price = 12.5 (valid,
# through the setter), and print product.price.


# TODO 5.4: Write a class Email with __init__(self, address) that
# calls self.address = address (through the setter), a @property
# getter address(self) returning self._address, and a
# @address.setter address(self, value) that raises
# ValueError("invalid email address") if "@" not in value, otherwise
# sets self._address = value. Create email = Email("user@example.com")
# and print email.address, then try email.address = "not-an-email"
# inside a try/except ValueError block, printing the exception's
# message if it raises.


# TODO 5.5 (Debug the Code): this setter is supposed to validate that
# a Thermostat's target temperature never goes below absolute zero
# (-273.15 Celsius), but the condition is backwards -- it raises
# ValueError only when value is ABOVE -273.15 (which is every normal
# temperature), instead of when value is BELOW -273.15. Fix the
# condition from "value > -273.15" to "value < -273.15".
class Thermostat:
    def __init__(self, target):
        self.target = target

    @property
    def target(self):
        return self._target

    @target.setter
    def target(self, value):
        if value > -273.15:
            raise ValueError("temperature cannot be below absolute zero")
        self._target = value


thermostat = Thermostat(21)
print(thermostat.target)


# TODO 5.A (Scenario -- Validating Signup Form Data): a signup form
# must never let a UserAccount end up with a blank username. Write a
# class UserAccount with __init__(self, username) that calls
# self.username = username (through the setter), a @property getter
# username(self) returning self._username, and a
# @username.setter username(self, value) that raises
# ValueError("username cannot be blank") if not value.strip(),
# otherwise sets self._username = value.strip() -- modeling how a
# real signup form rejects bad input the instant it's assigned, not
# later when something downstream breaks mysteriously. Create
# user = UserAccount("mpapasani") and print user.username, then try
# user.username = "   " inside a try/except ValueError block, printing
# the exception's message if it raises.


# TODO 5.B (Scenario -- Interview Prep): an interviewer asks why you'd
# put validation logic in a @property setter instead of just checking
# the value in __init__ or trusting the caller to pass good data.
# Write a function explain_property_setters() that returns a string
# explaining that a @x.setter runs its validation every single time
# the attribute is assigned -- not just once in __init__ -- so
# obj.attribute = new_value is guarded the same way the very first
# assignment was, closing the door on a class ever silently drifting
# into an invalid state through some later assignment elsewhere in the
# codebase; this keeps the validation rule defined in exactly one
# place instead of being repeated (or forgotten) at every call site
# that happens to set the attribute. Call it and print the result.


# ============================================================
# Topic 6: Bringing It Together -- Deeper OOP in Production
# ============================================================

# TODO 6.1: Write a class Product with __init__(self, name, price)
# that calls self.price = price (through the setter), a @property
# getter price(self) returning self._price, a @price.setter
# price(self, value) raising ValueError("price cannot be negative") if
# value < 0 otherwise setting self._price = value, a @staticmethod
# apply_tax(price, tax_rate) returning round(price * (1 + tax_rate), 2),
# and a @classmethod on_sale(cls, name, original_price, discount_percent)
# returning cls(name, original_price * (1 - discount_percent / 100)) --
# combining a validated property, a static utility, and an alternative
# constructor on one class. Create
# product = Product.on_sale("Headphones", 100, 20) and print
# product.price, then print
# Product.apply_tax(product.price, 0.08).


# TODO 6.2: Write a class Employee with a class attribute
# __next_id = 1000 (double underscore -- internal counter), __init__
# storing self.name = name, self._salary = salary, and self.id =
# Employee.__next_id, then incrementing Employee.__next_id by 1, plus
# a @property getter salary(self) returning self._salary and a
# @salary.setter salary(self, value) raising ValueError("salary cannot
# be negative") if value < 0 otherwise setting self._salary = value,
# and a @classmethod hire_intern(cls, name) returning cls(name, 40000)
# -- modeling a real HR system where every employee record gets a
# private auto-incrementing id, a validated salary, and a shortcut
# constructor for a common hiring case. Create
# intern = Employee.hire_intern("Jordan") and print intern.id and
# intern.salary.


# TODO 6.3: Write a class InventoryItem with __init__(self, name,
# quantity) that calls self.quantity = quantity (through the setter),
# a @property getter quantity(self) returning self._quantity, a
# @quantity.setter quantity(self, value) raising ValueError("quantity
# cannot be negative") if value < 0 otherwise setting self._quantity =
# value, a method restock(self, amount) that sets
# self.quantity = self.quantity + amount (going back through the
# setter, so restocking still gets validated), and a @staticmethod
# reorder_threshold() returning 10 (a shared business rule, not tied
# to any one item). Create item = InventoryItem("Widget", 5), call
# item.restock(20), then print item.quantity and whether
# item.quantity is above InventoryItem.reorder_threshold() as a
# boolean.


# TODO 6.4: Write a class BankAccount with __init__(self, owner,
# balance) that stores self.owner = owner and calls
# self.balance = balance (through the setter), a @property getter
# balance(self) returning self._balance, a @balance.setter
# balance(self, value) raising ValueError("balance cannot be
# negative") if value < 0 otherwise setting self._balance = value, a
# method withdraw(self, amount) that sets
# self.balance = self.balance - amount (routed back through the
# setter so an over-withdrawal is caught by the same validation), and
# a @classmethod open_with_bonus(cls, owner) returning
# cls(owner, 25) -- modeling a bank's new-account promotional bonus as
# an alternative constructor. Create
# account = BankAccount.open_with_bonus("Dana") and print
# account.balance, then try account.withdraw(100) inside a
# try/except ValueError block, printing the exception's message if it
# raises.


# TODO 6.5 (Debug the Code): this class is supposed to keep
# __init__ routing through the validated setter so no Subscription can
# ever be created with a negative price, but __init__ assigns
# self._price = price directly instead of self.price = price -- so
# the constructor bypasses the setter's validation entirely, letting
# Subscription("Basic", -5) create an invalid object with no error at
# all. Fix __init__ to assign self.price = price instead of
# self._price = price so construction is validated the same way any
# later assignment would be.
class Subscription:
    def __init__(self, plan_name, price):
        self.plan_name = plan_name
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("price cannot be negative")
        self._price = value


subscription = Subscription("Basic", -5)
print(subscription.price)


# TODO 6.A (Scenario -- A Small Payroll System): write a class
# Employee with __init__(self, name, base_salary) that stores
# self.name = name and calls self.base_salary = base_salary (through
# the setter), a @property getter base_salary(self) returning
# self._base_salary, a @base_salary.setter base_salary(self, value)
# raising ValueError("base salary cannot be negative") if value < 0
# otherwise setting self._base_salary = value, a @staticmethod
# annual_from_monthly(monthly_amount) returning
# round(monthly_amount * 12, 2), and a @classmethod
# salaried_from_monthly(cls, name, monthly_amount) returning
# cls(name, cls.annual_from_monthly(monthly_amount)) -- modeling how a
# real payroll system converts a monthly rate into a validated annual
# salary using both a static conversion utility and an alternative
# constructor together. Create
# employee = Employee.salaried_from_monthly("Priya", 5000) and print
# employee.base_salary.


# TODO 6.B (Scenario -- Interview Prep): an interviewer asks you to
# describe, in your own words, how @staticmethod, @classmethod, and
# @property work together in a real, well-designed class instead of
# being three unrelated features. Write a function
# explain_deeper_oop_production_value() that returns a string
# explaining that these three tools solve different but related
# problems in the same class: @staticmethod groups a pure utility
# calculation with the class it conceptually belongs to even though it
# needs no instance data; @classmethod provides alternative,
# more-convenient ways to construct a valid instance without bloating
# __init__ with optional parameters; and @property (with its setter)
# lets attribute-style access stay simple for callers while the class
# quietly enforces its own validation rules on every read or write --
# together they let a class expose a clean, attribute-like surface to
# the rest of the program while keeping its internal rules and
# invariants fully under its own control, which is exactly the kind of
# class real production codebases are built from. Call it and print
# the result.
