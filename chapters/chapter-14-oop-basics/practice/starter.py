"""
Chapter 14 Practice Bank: OOP Basics
See README.md in this folder for full instructions.
Run this from inside the practice/ folder: python3 starter.py
"""

# ============================================================
# Topic 1: Classes & Objects
# ============================================================

# TODO 1.1: Write a class Book with no __init__ (yet) -- just
# "pass" in the body for now. Create two separate instances,
# book_one = Book() and book_two = Book(). Print type(book_one) and
# print whether book_one is book_two (should be False -- two
# separate objects from the same blueprint).


# TODO 1.2: Write a class Dog with no __init__ -- just "pass". After
# the class, set book_one.title = "Dune" style attributes directly on
# an instance: create dog = Dog(), then set dog.name = "Rex" and
# dog.breed = "Labrador" as plain attribute assignments from outside
# the class. Print dog.name and dog.breed.


# TODO 1.3: Write a function describe_instance(obj) that returns a
# string f"{obj} is an instance of {type(obj).__name__}" using
# Python's built-in str() conversion implicitly via f-string. Create
# a class Car with "pass" in its body, make car = Car(), and call
# describe_instance(car), printing the result (the {obj} part will
# show Python's default object repr -- that's expected before Topic
# 5 covers custom __str__/__repr__).


# TODO 1.4: Write a class Wallet with "pass" in its body. Create two
# instances, wallet_a = Wallet() and wallet_b = Wallet(). Set
# wallet_a.balance = 100 directly from outside the class. Print
# wallet_a.balance, then try to print wallet_b.balance inside a
# try/except AttributeError block, printing "wallet_b has no balance
# attribute yet" if it raises -- demonstrating that each instance
# only has the attributes it was actually given, not whatever some
# other instance of the same class has.


# TODO 1.5 (Debug the Code): this code is supposed to create two
# separate Ticket instances, but it accidentally assigns the same
# object to both names instead of calling Ticket() twice -- so
# ticket_one and ticket_two are really just two names for the one
# same object, not two independent objects. Fix it so each name gets
# its own separate instance.
class Ticket:
    pass


ticket_one = Ticket()
ticket_two = ticket_one
print(ticket_one is ticket_two)


# TODO 1.A (Scenario -- Modeling Real-World "Things" as Objects): a
# help desk system needs to represent support tickets in code. Write
# a class SupportTicket with "pass" in its body (attributes come in
# Topic 2). Create two instances, ticket_a = SupportTicket() and
# ticket_b = SupportTicket(), then set ticket_a.subject = "Password
# reset" and ticket_b.subject = "Billing question" directly from
# outside the class -- modeling how each real support ticket is its
# own independent record even though they're built from the same
# blueprint. Print both subjects.


# TODO 1.B (Scenario -- Interview Prep): an interviewer asks you to
# explain the difference between a class and an object in your own
# words. Write a function explain_class_vs_object() that returns a
# string explaining that a class is a blueprint describing what
# attributes and behavior its instances will have, while an object
# (or instance) is one actual, independent thing built from that
# blueprint -- many different objects can come from the same class,
# each with its own separate data, the same way many different houses
# can be built from one blueprint without sharing walls. Call it and
# print the result.


# ============================================================
# Topic 2: __init__ and Instance Attributes
# ============================================================

# TODO 2.1: Write a class Book with an __init__(self, title, author)
# that stores self.title = title and self.author = author. Create
# book = Book("Dune", "Frank Herbert") and print book.title and
# book.author.


# TODO 2.2: Write a class Point with an __init__(self, x, y) that
# stores self.x = x and self.y = y. Create point = Point(3, 4) and
# print point.x and point.y.


# TODO 2.3: Write a class Employee with an __init__(self, name,
# salary=50000) that stores self.name = name and self.salary =
# salary, using a default value so salary is optional. Create
# employee_one = Employee("Priya") and employee_two = Employee("Sam",
# 65000). Print both employees' .name and .salary.


# TODO 2.4: Write a class Rectangle with an __init__(self, width,
# height) that stores self.width = width and self.height = height.
# Create rectangle = Rectangle(4, 5) and print rectangle.width and
# rectangle.height.


# TODO 2.5 (Debug the Code): this class's __init__ is supposed to
# store the name argument onto the instance, but it assigns to a
# plain local variable name instead of self.name -- so the value is
# lost the moment __init__ returns, and any later access to
# customer.name raises AttributeError. Fix it by assigning to
# self.name instead.
class Customer:
    def __init__(self, name):
        name = name


customer = Customer("Alice")
print(customer.name)


# TODO 2.A (Scenario -- Building a User Record at Signup): write a
# class UserAccount with __init__(self, username, email) storing
# self.username = username and self.email = email -- modeling how a
# real signup form immediately builds one independent record per new
# user the moment they submit the form. Create
# user = UserAccount("mpapasani", "mp@example.com") and print
# user.username and user.email.


# TODO 2.B (Scenario -- Interview Prep): an interviewer asks what
# __init__ actually is and when it runs. Write a function
# explain_init() that returns a string explaining that __init__ is a
# special method Python calls automatically every time a new instance
# is created (right after the object itself is built), and its job is
# to set up that instance's own initial attributes from whatever
# arguments were passed in -- it is not something a programmer calls
# directly, Python calls it for you as part of ClassName(...). Call it
# and print the result.


# ============================================================
# Topic 3: Instance Methods & self
# ============================================================

# TODO 3.1: Write a class Counter with __init__(self) storing
# self.value = 0, and a method increment(self) that adds 1 to
# self.value. Create counter = Counter(), call counter.increment()
# three times, then print counter.value.


# TODO 3.2: Write a class BankAccount with __init__(self, balance)
# storing self.balance = balance, a method deposit(self, amount) that
# adds amount to self.balance, and a method withdraw(self, amount)
# that subtracts amount from self.balance. Create
# account = BankAccount(100), call account.deposit(50), then
# account.withdraw(30), then print account.balance (should be 120).


# TODO 3.3: Write a class Rectangle with __init__(self, width,
# height) storing both, and a method area(self) that returns
# self.width * self.height. Create rectangle = Rectangle(4, 5) and
# print rectangle.area().


# TODO 3.4: Write a class Greeter with __init__(self, name) storing
# self.name = name, and a method greet(self) that returns
# f"Hello, {self.name}!". Create greeter = Greeter("Sam") and print
# greeter.greet().


# TODO 3.5 (Debug the Code): this method is supposed to double the
# instance's stored value, but it forgot to include self as the
# first parameter -- so calling item.double() raises a TypeError
# about too many positional arguments, since Python automatically
# passes the instance itself as the first argument to every instance
# method call. Fix it by adding self as the first parameter.
class Item:
    def __init__(self, value):
        self.value = value

    def double(): # noqa: this signature is intentionally broken
        pass


item = Item(5)
item.double()
print(item.value)


# TODO 3.A (Scenario -- A Shopping Cart's Running Total): write a
# class ShoppingCart with __init__(self) storing self.items = [] and
# self.total = 0, a method add_item(self, name, price) that appends
# name to self.items and adds price to self.total -- modeling how a
# real checkout page updates its own running total as a shopper adds
# products, one method call per click. Create cart = ShoppingCart(),
# call cart.add_item("Shirt", 25) and cart.add_item("Hat", 15), then
# print cart.items and cart.total.


# TODO 3.B (Scenario -- Interview Prep): an interviewer asks what
# self actually refers to and why every instance method needs it as
# the first parameter. Write a function explain_self() that returns
# a string explaining that self refers to the specific instance a
# method was called on, and Python passes it in automatically --
# instance.method(args) really runs as ClassName.method(instance,
# args) behind the scenes -- so self is how a method reaches that
# one instance's own attributes instead of some other instance's, or
# no instance's data at all. Call it and print the result.


# ============================================================
# Topic 4: Class Attributes vs. Instance Attributes
# ============================================================

# TODO 4.1: Write a class Circle with a class attribute
# pi = 3.14159 (shared by every instance) and __init__(self, radius)
# storing self.radius = radius. Add a method area(self) that returns
# Circle.pi * self.radius ** 2. Create circle = Circle(2) and print
# circle.area().


# TODO 4.2: Write a class Employee with a class attribute
# company_name = "Acme Corp" and __init__(self, name) storing
# self.name = name. Create employee_one = Employee("Priya") and
# employee_two = Employee("Sam"). Print employee_one.company_name and
# employee_two.company_name -- both should show the same shared
# value even though neither instance was given it directly.


# TODO 4.3: Write a class Product with a class attribute
# total_products_created = 0 and __init__(self, name) that stores
# self.name = name and increments Product.total_products_created by
# 1 every time a new instance is created. Create three products,
# Product("Widget"), Product("Gadget"), Product("Gizmo"), then print
# Product.total_products_created (should be 3).


# TODO 4.4: Write a class Vehicle with a class attribute
# wheels = 4 and __init__(self, make) storing self.make = make.
# Create car = Vehicle("Toyota"), then set car.wheels = 3 directly on
# just that one instance (simulating a modified vehicle). Print
# car.wheels (3, the instance-level override) and
# Vehicle.wheels (still 4, the class attribute is untouched).


# TODO 4.5 (Debug the Code -- the Mutable Class Attribute Gotcha):
# this class is supposed to give every Cart instance its own
# independent list of items, but it defines items = [] as a class
# attribute instead of creating it fresh inside __init__ -- so every
# instance shares the exact same list object, and adding an item
# through one cart's add_item() call shows up in every other cart
# too. Fix it by moving items into __init__ as self.items = [].
class Cart:
    items = []

    def __init__(self):
        pass

    def add_item(self, item):
        self.items.append(item)


cart_one = Cart()
cart_two = Cart()
cart_one.add_item("Book")
print(cart_two.items)


# TODO 4.A (Scenario -- A Shared Interest Rate Across All Accounts):
# write a class SavingsAccount with a class attribute
# interest_rate = 0.02 (a bank-wide rate every account shares by
# default) and __init__(self, owner, balance) storing self.owner =
# owner and self.balance = balance, plus a method apply_interest(self)
# that adds self.balance * SavingsAccount.interest_rate to
# self.balance -- modeling how a bank can change one shared rate and
# have it affect every account that hasn't been individually
# overridden. Create account = SavingsAccount("Dana", 1000), call
# account.apply_interest(), then print account.balance (should be
# 1020.0).


# TODO 4.B (Scenario -- Interview Prep): an interviewer asks you to
# explain the mutable class attribute bug and why it happens. Write a
# function explain_mutable_class_attribute_bug() that returns a
# string explaining that a class attribute is stored once on the
# class itself and shared by every instance that doesn't set its own
# instance attribute of the same name -- which is harmless for
# immutable values like numbers or strings, but dangerous for mutable
# ones like a list or dict, because every instance ends up mutating
# that exact same shared object, so a change made through one
# instance silently shows up on every other instance too; the fix is
# creating that attribute fresh inside __init__ as an instance
# attribute instead of at the class level. Call it and print the
# result.


# ============================================================
# Topic 5: __str__ and __repr__
# ============================================================

# TODO 5.1: Write a class Book with __init__(self, title, author)
# storing both, and a __str__(self) method returning
# f"{self.title} by {self.author}". Create
# book = Book("Dune", "Frank Herbert") and print(book) -- print()
# calls __str__ automatically.


# TODO 5.2: Write a class Point with __init__(self, x, y) storing
# both, and a __repr__(self) method returning
# f"Point({self.x}, {self.y})". Create point = Point(3, 4) and print
# repr(point) -- repr() calls __repr__ automatically.


# TODO 5.3: Write a class Temperature with __init__(self, celsius)
# storing self.celsius = celsius, and both a __str__(self) returning
# f"{self.celsius}°C" and a __repr__(self) returning
# f"Temperature({self.celsius})". Create
# temperature = Temperature(25) and print both str(temperature) and
# repr(temperature) to show they can differ -- __str__ for a
# friendly display, __repr__ for an unambiguous developer-facing one.


# TODO 5.4: Write a class Money with __init__(self, amount, currency)
# storing both, and a __str__(self) method returning
# f"{self.amount:.2f} {self.currency}". Create
# price = Money(19.9, "USD") and print(price) -- should print
# "19.90 USD".


# TODO 5.5 (Debug the Code): this class's __str__ method is supposed
# to let print() show a friendly string, but it's misspelled as
# __string__ instead of __str__ -- Python never calls a method with
# that name automatically, so print(product) falls back to the
# default, unhelpful object repr instead. Fix the method name to
# __str__.
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __string__(self):
        return f"{self.name}: ${self.price}"


product = Product("Widget", 9.99)
print(product)


# TODO 5.A (Scenario -- Friendly Logging Output): write a class
# OrderEvent with __init__(self, order_id, status) storing both, and
# a __str__(self) method returning
# f"Order #{self.order_id} is now {self.status}" -- modeling how a
# real order-tracking system prints a clean, human-readable line to
# its logs every time an order's status changes, instead of an
# unreadable default object repr. Create
# event = OrderEvent(1024, "shipped") and print(event).


# TODO 5.B (Scenario -- Interview Prep): an interviewer asks the
# difference between __str__ and __repr__ and when each is used.
# Write a function explain_str_vs_repr() that returns a string
# explaining that __str__ is meant to produce a readable, user-facing
# description (what print() and str() use), while __repr__ is meant
# to produce an unambiguous, developer-facing description useful for
# debugging (what repr() uses, and what the interactive shell falls
# back on if __str__ isn't defined) -- and that if a class only
# defines __repr__, Python will use it for both, but a class that
# defines both gets to show something friendlier to end users while
# still keeping a precise version available for debugging. Call it
# and print the result.


# ============================================================
# Topic 6: Bringing It Together -- OOP Basics in Production
# ============================================================

# TODO 6.1: Write a class InventoryItem with __init__(self, name,
# quantity, unit_price) storing all three, a method
# total_value(self) that returns self.quantity * self.unit_price,
# and a __str__(self) that returns
# f"{self.name}: {self.quantity} units @ ${self.unit_price:.2f} each".
# Create item = InventoryItem("Widget", 10, 2.5), print(item), then
# print item.total_value() (should be 25.0).


# TODO 6.2: Write a class Task with a class attribute
# next_id = 1 (a shared counter) and __init__(self, description) that
# stores self.id = Task.next_id, self.description = description,
# self.done = False, and then increments Task.next_id by 1 -- so
# every new task automatically gets its own unique, ever-increasing
# id. Also add a method mark_done(self) that sets self.done = True,
# and a __str__(self) returning
# f"Task #{self.id}: {self.description} ({'done' if self.done else 'pending'})".
# Create task_one = Task("Write report") and task_two = Task("Review
# PR"). Call task_one.mark_done(). Print both tasks.


# TODO 6.3: Write a class Playlist with __init__(self, name) storing
# self.name = name and self.songs = [] (a fresh list per instance --
# not a class attribute), a method add_song(self, title) that
# appends title to self.songs, a method total_songs(self) that
# returns len(self.songs), and a __str__(self) returning
# f"{self.name} ({self.total_songs()} songs)". Create
# playlist = Playlist("Road Trip"), add two songs to it with
# add_song(), then print(playlist) and print playlist.songs.


# TODO 6.4: Write a class TemperatureLog with __init__(self, city)
# storing self.city = city and self.readings = [], a method
# add_reading(self, celsius) that appends celsius to self.readings, a
# method average(self) that returns
# round(sum(self.readings) / len(self.readings), 1) if self.readings
# is non-empty, and 0.0 if it's empty (an empty list would otherwise
# raise ZeroDivisionError), and a __str__(self) returning
# f"{self.city}: avg {self.average()}°C over {len(self.readings)} readings".
# Create log = TemperatureLog("Austin"), add readings 30, 32, 28 with
# add_reading(), then print(log).


# TODO 6.5 (Debug the Code): this class models a shared team roster,
# but it defines members = [] as a class attribute instead of an
# instance attribute inside __init__ -- so every separate Team
# instance ends up sharing the exact same underlying list, and
# adding a member to one team shows up on every other team too, the
# same mutable-class-attribute bug from Topic 4. Fix it by moving
# members into __init__ as self.members = [].
class Team:
    members = []

    def __init__(self, name):
        self.name = name

    def add_member(self, member_name):
        self.members.append(member_name)


team_a = Team("Alpha")
team_b = Team("Beta")
team_a.add_member("Priya")
print(team_b.members)


# TODO 6.A (Scenario -- A Small Order-Processing System): write a
# class Order with __init__(self, order_id, customer_name) storing
# both, self.line_items = [] (fresh per instance), and self.status =
# "pending", a method add_line_item(self, product_name, quantity,
# unit_price) that appends a dict {"product": product_name,
# "quantity": quantity, "unit_price": unit_price} to self.line_items,
# a method total(self) that returns
# round(sum(item["quantity"] * item["unit_price"] for item in
# self.line_items), 2), a method mark_shipped(self) that sets
# self.status = "shipped", and a __str__(self) returning
# f"Order #{self.order_id} for {self.customer_name}: {self.status}, total ${self.total():.2f}"
# -- modeling how a real e-commerce backend represents one order as
# one object carrying its own line items, running total, and status
# together. Create order = Order(501, "Dana"), add two line items
# with add_line_item(), call order.mark_shipped(), then print(order).


# TODO 6.B (Scenario -- Interview Prep): an interviewer asks you to
# describe, in your own words, why real production codebases
# organize data and behavior into classes instead of just using
# separate dicts and standalone functions everywhere. Write a
# function explain_oop_basics_production_value() that returns a
# string explaining that bundling related data and the behavior that
# acts on it into one class keeps a program's building blocks
# self-contained and harder to misuse -- a BankAccount object always
# carries its own balance alongside the deposit/withdraw methods that
# know how to change it correctly, instead of a bare balance number
# floating around a codebase next to loose functions that any code
# anywhere could apply incorrectly or forget to call altogether --
# and that this is exactly the same instinct behind grouping a
# person's data in a dict or a file's operations behind a with
# block: keep the data and the rules for changing it safely as close
# together as possible. Call it and print the result.
