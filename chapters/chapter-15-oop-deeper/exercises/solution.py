"""
Chapter 15 Exercises: OOP Deeper — reference solution.
Run this from inside the exercises/ folder: python3 solution.py
"""

# TODO 1: Write a class TemperatureTools with a static method
# is_valid_celsius(value) that returns True if value is an int or
# float and is greater than or equal to -273.15 (absolute zero), and
# False otherwise. Call it with 25 and with -500 and print both
# results.
class TemperatureTools:
    @staticmethod
    def is_valid_celsius(value):
        return isinstance(value, (int, float)) and value >= -273.15

print(TemperatureTools.is_valid_celsius(25))
print(TemperatureTools.is_valid_celsius(-500))


# TODO 2: Write a class Employee whose __init__ takes name and salary,
# storing both as instance attributes. Add a class method
# from_string(cls, employee_data) that takes one comma-separated
# string like "Alice,60000", splits it, and returns a new Employee
# built with cls(...). Create one Employee with Employee("Priya", 72000)
# and one with Employee.from_string("Sam,58000"), then print each
# one's name and salary.
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def from_string(cls, employee_data):
        name, salary = employee_data.split(",")
        return cls(name, float(salary))

emp1 = Employee("Priya", 72000)
emp2 = Employee.from_string("Sam,58000")
print(emp1.name, emp1.salary)
print(emp2.name, emp2.salary)


# TODO 3: Write a class Vault whose __init__ takes contents and stores
# it as self._contents (single underscore, by convention). Give it an
# instance method peek(self) that returns self._contents. Create a
# Vault with "gold bars" and print the result of calling peek().
class Vault:
    def __init__(self, contents):
        self._contents = contents

    def peek(self):
        return self._contents

vault = Vault("gold bars")
print(vault.peek())


# TODO 4: Write a class Circle whose __init__ takes radius and stores
# it as self._radius. Add a read-only property radius that returns
# self._radius. Create a Circle with radius 4 and print circle.radius
# (no parentheses).
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

circle = Circle(4)
print(circle.radius)


# TODO 5: Write a class Thermostat whose __init__ takes temperature
# and stores it as self._temperature. Add a temperature property with
# a getter that returns self._temperature, and a setter that raises
# ValueError if the new value is below -50 or above 150, otherwise
# stores it. Create a Thermostat at 70, set its temperature to 72 and
# print it, then try setting it to 200 inside a try/except ValueError
# block and print the caught error message.
class Thermostat:
    def __init__(self, temperature):
        self._temperature = temperature

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -50 or value > 150:
            raise ValueError("Temperature out of range.")
        self._temperature = value

thermostat = Thermostat(70)
thermostat.temperature = 72
print(thermostat.temperature)
try:
    thermostat.temperature = 200
except ValueError as e:
    print("ValueError:", e)


# TODO 6: Write a class Product that combines this chapter's tools: a
# class attribute store_name = "Downtown Market"; __init__ taking name
# and price, storing price through the property (not directly as
# self._price) so validation runs immediately; a static method
# is_valid_price(value) returning True only for a positive int/float;
# a price property with a getter and a setter that raises ValueError
# for any non-positive value using is_valid_price; and a __str__
# returning f"{self.name}: ${self.price:.2f}". Create a Product named
# "Notebook" priced at 2.5, print it, then try setting its price to -1
# inside a try/except ValueError block and print the caught error
# message.
class Product:
    store_name = "Downtown Market"

    def __init__(self, name, price):
        self.name = name
        self.price = price

    @staticmethod
    def is_valid_price(value):
        return isinstance(value, (int, float)) and value > 0

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not Product.is_valid_price(value):
            raise ValueError("Price must be a positive number.")
        self._price = value

    def __str__(self):
        return f"{self.name}: ${self.price:.2f}"

product = Product("Notebook", 2.5)
print(product)
try:
    product.price = -1
except ValueError as e:
    print("ValueError:", e)


# TODO 7 (Debug the Code): this Circle class's area is meant to be a
# property but is missing the @property decorator, so circle.area
# (accessed like an attribute) raises a TypeError instead of returning
# the computed area. Find and fix it.
# Bug: def area(self): has no @property decorator, so "area" is a
# plain method, and circle.area returns the method object itself
# rather than calling it. Fix: add @property above the method.
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return 3.14159 * self.radius ** 2

circle = Circle(3)
print(round(circle.area, 2))


# TODO 8 (Debug the Code): this Account class has a balance property
# and a @balance.setter, but the setter accepts any value at all --
# including negative numbers -- defeating the entire point of wrapping
# _balance in a property. Find and fix the setter so it raises
# ValueError for any negative value instead of silently accepting it.
# Bug: the setter just does self._balance = value with no check at
# all. Fix: raise ValueError when value < 0, matching the property's
# intended purpose.
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative.")
        self._balance = value

acct = Account("Alice", 100)
acct.balance = 250
print(acct.balance)
try:
    acct.balance = -30
except ValueError as e:
    print("ValueError:", e)
print(acct.balance)
