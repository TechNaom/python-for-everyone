"""
Chapter 14 Practice Bank: OOP Basics -- reference solution.
See README.md in this folder for full instructions.
Run this from inside the practice/ folder: python3 solution.py
"""

# ============================================================
# Topic 1: Classes & Objects
# ============================================================

# TODO 1.1
class Book:
    pass


book_one = Book()
book_two = Book()
print(type(book_one))
print(book_one is book_two)


# TODO 1.2
class Dog:
    pass


dog = Dog()
dog.name = "Rex"
dog.breed = "Labrador"
print(dog.name)
print(dog.breed)


# TODO 1.3
def describe_instance(obj):
    return f"{obj} is an instance of {type(obj).__name__}"


class Car:
    pass


car = Car()
print(describe_instance(car))


# TODO 1.4
class Wallet:
    pass


wallet_a = Wallet()
wallet_b = Wallet()
wallet_a.balance = 100
print(wallet_a.balance)
try:
    print(wallet_b.balance)
except AttributeError:
    print("wallet_b has no balance attribute yet")


# TODO 1.5 (Debug the Code)
class Ticket:
    pass


ticket_one = Ticket()
ticket_two = Ticket()
print(ticket_one is ticket_two)


# TODO 1.A (Scenario -- Modeling Real-World "Things" as Objects)
class SupportTicket:
    pass


ticket_a = SupportTicket()
ticket_b = SupportTicket()
ticket_a.subject = "Password reset"
ticket_b.subject = "Billing question"
print(ticket_a.subject)
print(ticket_b.subject)


# TODO 1.B (Scenario -- Interview Prep)
def explain_class_vs_object():
    return (
        "A class is a blueprint describing what attributes and behavior "
        "its instances will have, while an object (or instance) is one "
        "actual, independent thing built from that blueprint. Many "
        "different objects can come from the same class, each with its "
        "own separate data, the same way many different houses can be "
        "built from one blueprint without sharing walls."
    )


print(explain_class_vs_object())


# ============================================================
# Topic 2: __init__ and Instance Attributes
# ============================================================

# TODO 2.1
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


book = Book("Dune", "Frank Herbert")
print(book.title)
print(book.author)


# TODO 2.2
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


point = Point(3, 4)
print(point.x)
print(point.y)


# TODO 2.3
class Employee:
    def __init__(self, name, salary=50000):
        self.name = name
        self.salary = salary


employee_one = Employee("Priya")
employee_two = Employee("Sam", 65000)
print(employee_one.name)
print(employee_one.salary)
print(employee_two.name)
print(employee_two.salary)


# TODO 2.4
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height


rectangle = Rectangle(4, 5)
print(rectangle.width)
print(rectangle.height)


# TODO 2.5 (Debug the Code)
class Customer:
    def __init__(self, name):
        self.name = name


customer = Customer("Alice")
print(customer.name)


# TODO 2.A (Scenario -- Building a User Record at Signup)
class UserAccount:
    def __init__(self, username, email):
        self.username = username
        self.email = email


user = UserAccount("mpapasani", "mp@example.com")
print(user.username)
print(user.email)


# TODO 2.B (Scenario -- Interview Prep)
def explain_init():
    return (
        "__init__ is a special method Python calls automatically every "
        "time a new instance is created, right after the object itself "
        "is built. Its job is to set up that instance's own initial "
        "attributes from whatever arguments were passed in -- it is not "
        "something a programmer calls directly, Python calls it for you "
        "as part of ClassName(...)."
    )


print(explain_init())


# ============================================================
# Topic 3: Instance Methods & self
# ============================================================

# TODO 3.1
class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1


counter = Counter()
counter.increment()
counter.increment()
counter.increment()
print(counter.value)


# TODO 3.2
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount


account = BankAccount(100)
account.deposit(50)
account.withdraw(30)
print(account.balance)


# TODO 3.3
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


rectangle = Rectangle(4, 5)
print(rectangle.area())


# TODO 3.4
class Greeter:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}!"


greeter = Greeter("Sam")
print(greeter.greet())


# TODO 3.5 (Debug the Code)
class Item:
    def __init__(self, value):
        self.value = value

    def double(self):
        self.value *= 2


item = Item(5)
item.double()
print(item.value)


# TODO 3.A (Scenario -- A Shopping Cart's Running Total)
class ShoppingCart:
    def __init__(self):
        self.items = []
        self.total = 0

    def add_item(self, name, price):
        self.items.append(name)
        self.total += price


cart = ShoppingCart()
cart.add_item("Shirt", 25)
cart.add_item("Hat", 15)
print(cart.items)
print(cart.total)


# TODO 3.B (Scenario -- Interview Prep)
def explain_self():
    return (
        "self refers to the specific instance a method was called on, "
        "and Python passes it in automatically -- instance.method(args) "
        "really runs as ClassName.method(instance, args) behind the "
        "scenes. self is how a method reaches that one instance's own "
        "attributes instead of some other instance's, or no instance's "
        "data at all."
    )


print(explain_self())


# ============================================================
# Topic 4: Class Attributes vs. Instance Attributes
# ============================================================

# TODO 4.1
class Circle:
    pi = 3.14159

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return Circle.pi * self.radius ** 2


circle = Circle(2)
print(circle.area())


# TODO 4.2
class Employee:
    company_name = "Acme Corp"

    def __init__(self, name):
        self.name = name


employee_one = Employee("Priya")
employee_two = Employee("Sam")
print(employee_one.company_name)
print(employee_two.company_name)


# TODO 4.3
class Product:
    total_products_created = 0

    def __init__(self, name):
        self.name = name
        Product.total_products_created += 1


Product("Widget")
Product("Gadget")
Product("Gizmo")
print(Product.total_products_created)


# TODO 4.4
class Vehicle:
    wheels = 4

    def __init__(self, make):
        self.make = make


car = Vehicle("Toyota")
car.wheels = 3
print(car.wheels)
print(Vehicle.wheels)


# TODO 4.5 (Debug the Code -- the Mutable Class Attribute Gotcha)
class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)


cart_one = Cart()
cart_two = Cart()
cart_one.add_item("Book")
print(cart_two.items)


# TODO 4.A (Scenario -- A Shared Interest Rate Across All Accounts)
class SavingsAccount:
    interest_rate = 0.02

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def apply_interest(self):
        self.balance += self.balance * SavingsAccount.interest_rate


account = SavingsAccount("Dana", 1000)
account.apply_interest()
print(account.balance)


# TODO 4.B (Scenario -- Interview Prep)
def explain_mutable_class_attribute_bug():
    return (
        "A class attribute is stored once on the class itself and shared "
        "by every instance that doesn't set its own instance attribute of "
        "the same name -- harmless for immutable values like numbers or "
        "strings, but dangerous for mutable ones like a list or dict, "
        "because every instance ends up mutating that exact same shared "
        "object, so a change made through one instance silently shows up "
        "on every other instance too. The fix is creating that attribute "
        "fresh inside __init__ as an instance attribute instead of at "
        "the class level."
    )


print(explain_mutable_class_attribute_bug())


# ============================================================
# Topic 5: __str__ and __repr__
# ============================================================

# TODO 5.1
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"


book = Book("Dune", "Frank Herbert")
print(book)


# TODO 5.2
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


point = Point(3, 4)
print(repr(point))


# TODO 5.3
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def __str__(self):
        return f"{self.celsius}°C"

    def __repr__(self):
        return f"Temperature({self.celsius})"


temperature = Temperature(25)
print(str(temperature))
print(repr(temperature))


# TODO 5.4
class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __str__(self):
        return f"{self.amount:.2f} {self.currency}"


price = Money(19.9, "USD")
print(price)


# TODO 5.5 (Debug the Code)
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: ${self.price}"


product = Product("Widget", 9.99)
print(product)


# TODO 5.A (Scenario -- Friendly Logging Output)
class OrderEvent:
    def __init__(self, order_id, status):
        self.order_id = order_id
        self.status = status

    def __str__(self):
        return f"Order #{self.order_id} is now {self.status}"


event = OrderEvent(1024, "shipped")
print(event)


# TODO 5.B (Scenario -- Interview Prep)
def explain_str_vs_repr():
    return (
        "__str__ is meant to produce a readable, user-facing description "
        "-- what print() and str() use -- while __repr__ is meant to "
        "produce an unambiguous, developer-facing description useful for "
        "debugging -- what repr() uses, and what the interactive shell "
        "falls back on if __str__ isn't defined. If a class only defines "
        "__repr__, Python will use it for both, but a class that defines "
        "both gets to show something friendlier to end users while still "
        "keeping a precise version available for debugging."
    )


print(explain_str_vs_repr())


# ============================================================
# Topic 6: Bringing It Together -- OOP Basics in Production
# ============================================================

# TODO 6.1
class InventoryItem:
    def __init__(self, name, quantity, unit_price):
        self.name = name
        self.quantity = quantity
        self.unit_price = unit_price

    def total_value(self):
        return self.quantity * self.unit_price

    def __str__(self):
        return f"{self.name}: {self.quantity} units @ ${self.unit_price:.2f} each"


item = InventoryItem("Widget", 10, 2.5)
print(item)
print(item.total_value())


# TODO 6.2
class Task:
    next_id = 1

    def __init__(self, description):
        self.id = Task.next_id
        self.description = description
        self.done = False
        Task.next_id += 1

    def mark_done(self):
        self.done = True

    def __str__(self):
        status = "done" if self.done else "pending"
        return f"Task #{self.id}: {self.description} ({status})"


task_one = Task("Write report")
task_two = Task("Review PR")
task_one.mark_done()
print(task_one)
print(task_two)


# TODO 6.3
class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, title):
        self.songs.append(title)

    def total_songs(self):
        return len(self.songs)

    def __str__(self):
        return f"{self.name} ({self.total_songs()} songs)"


playlist = Playlist("Road Trip")
playlist.add_song("Song A")
playlist.add_song("Song B")
print(playlist)
print(playlist.songs)


# TODO 6.4
class TemperatureLog:
    def __init__(self, city):
        self.city = city
        self.readings = []

    def add_reading(self, celsius):
        self.readings.append(celsius)

    def average(self):
        if not self.readings:
            return 0.0
        return round(sum(self.readings) / len(self.readings), 1)

    def __str__(self):
        return f"{self.city}: avg {self.average()}°C over {len(self.readings)} readings"


log = TemperatureLog("Austin")
log.add_reading(30)
log.add_reading(32)
log.add_reading(28)
print(log)


# TODO 6.5 (Debug the Code)
class Team:
    def __init__(self, name):
        self.name = name
        self.members = []

    def add_member(self, member_name):
        self.members.append(member_name)


team_a = Team("Alpha")
team_b = Team("Beta")
team_a.add_member("Priya")
print(team_b.members)


# TODO 6.A (Scenario -- A Small Order-Processing System)
class Order:
    def __init__(self, order_id, customer_name):
        self.order_id = order_id
        self.customer_name = customer_name
        self.line_items = []
        self.status = "pending"

    def add_line_item(self, product_name, quantity, unit_price):
        self.line_items.append(
            {"product": product_name, "quantity": quantity, "unit_price": unit_price}
        )

    def total(self):
        return round(
            sum(item["quantity"] * item["unit_price"] for item in self.line_items), 2
        )

    def mark_shipped(self):
        self.status = "shipped"

    def __str__(self):
        return (
            f"Order #{self.order_id} for {self.customer_name}: "
            f"{self.status}, total ${self.total():.2f}"
        )


order = Order(501, "Dana")
order.add_line_item("Widget", 3, 9.99)
order.add_line_item("Gadget", 1, 24.5)
order.mark_shipped()
print(order)


# TODO 6.B (Scenario -- Interview Prep)
def explain_oop_basics_production_value():
    return (
        "Bundling related data and the behavior that acts on it into one "
        "class keeps a program's building blocks self-contained and "
        "harder to misuse -- a BankAccount object always carries its own "
        "balance alongside the deposit/withdraw methods that know how to "
        "change it correctly, instead of a bare balance number floating "
        "around a codebase next to loose functions that any code "
        "anywhere could apply incorrectly or forget to call altogether. "
        "This is exactly the same instinct behind grouping a person's "
        "data in a dict or a file's operations behind a with block: keep "
        "the data and the rules for changing it safely as close together "
        "as possible."
    )


print(explain_oop_basics_production_value())
