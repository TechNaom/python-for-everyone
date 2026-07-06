"""
Chapter 16 Practice Bank: Inheritance & Polymorphism
See README.md in this folder for full instructions.
Run this from inside the practice/ folder: python3 starter.py
"""

# ============================================================
# Topic 1: Basic Inheritance
# ============================================================

# TODO 1.1: Write a class Animal with __init__(self, name) storing
# self.name = name, and a method speak(self) that returns
# f"{self.name} makes a sound.". Write a class Dog(Animal) with no
# body other than pass -- showing that Dog automatically gets
# __init__ and speak() from Animal with zero new code. Create
# dog = Dog("Rex") and print dog.speak().


# TODO 1.2: Write a class Vehicle with __init__(self, make, model)
# storing both, and a method description(self) that returns
# f"{self.make} {self.model}". Write a class Car(Vehicle) with no
# body other than pass. Create car = Car("Toyota", "Corolla") and
# print car.description() -- demonstrating a subclass inherits every
# method the parent defines, unchanged, unless it overrides one.


# TODO 1.3: Write a class Employee with __init__(self, name, salary)
# storing both. Write a class Manager(Employee) with no body other
# than pass. Create manager = Manager("Priya", 90000) and print
# manager.name and manager.salary -- showing a subclass automatically
# gets every attribute the parent's __init__ sets, with no extra code
# in the subclass at all.


# TODO 1.4: Write a class Shape with a method area(self) that returns
# 0 (a placeholder base implementation). Write a class Square(Shape)
# with no body other than pass. Create square = Square() and print
# square.area() -- showing the subclass inherits the unmodified
# method exactly as written on the parent.


# TODO 1.5 (Debug the Code): this subclass is supposed to inherit from
# Animal, but the class definition forgot to put Animal in
# parentheses -- class Cat: instead of class Cat(Animal): -- so Cat
# has no relationship to Animal at all, and calling cat.speak() raises
# AttributeError because speak() was never inherited. Fix the class
# definition to class Cat(Animal):.
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."


class Cat:
    pass


cat = Cat("Whiskers")
print(cat.speak())


# TODO 1.A (Scenario -- Modeling a Fleet of Vehicles): a delivery
# company tracks many kinds of vehicles, and a Truck is just a
# Vehicle with no special behavior needed yet. Write a class Vehicle
# with __init__(self, license_plate) storing self.license_plate, and
# a method identify(self) that returns f"Vehicle {self.license_plate}".
# Write a class Truck(Vehicle) with no body other than pass --
# modeling how inheritance lets a new category of object reuse
# everything a more general one already does, with zero duplicated
# code, until the day it actually needs to differ. Create
# truck = Truck("TRK-204") and print truck.identify().


# TODO 1.B (Scenario -- Interview Prep): an interviewer asks you to
# explain, in plain language, what "inheritance" means in
# object-oriented programming and what a subclass gets automatically
# just by inheriting from a parent class. Write a function
# explain_basic_inheritance() that returns a string explaining that
# inheritance lets one class (the subclass, or "child") automatically
# receive every attribute and method defined on another class (the
# superclass, or "parent") without retyping any of that code -- the
# subclass can then add its own new attributes and methods, or
# override an inherited one to behave differently, but anything it
# doesn't touch it gets for free exactly as the parent defined it.
# Call it and print the result.


# ============================================================
# Topic 2: super().__init__()
# ============================================================

# TODO 2.1: Write a class Animal with __init__(self, name) storing
# self.name = name. Write a class Dog(Animal) with
# __init__(self, name, breed) that calls super().__init__(name) to
# reuse the parent's setup, then stores self.breed = breed --
# demonstrating how super().__init__() lets a subclass reuse the
# parent's attribute-setting logic instead of repeating
# self.name = name itself. Create dog = Dog("Rex", "Labrador") and
# print dog.name and dog.breed.


# TODO 2.2: Write a class Person with __init__(self, name) storing
# self.name = name. Write a class Student(Person) with
# __init__(self, name, school) that calls super().__init__(name) and
# then stores self.school = school. Create
# student = Student("Ada", "Central High") and print student.name and
# student.school.


# TODO 2.3: Write a class Shape with __init__(self, color) storing
# self.color = color. Write a class Rectangle(Shape) with
# __init__(self, color, width, height) that calls
# super().__init__(color) and then stores self.width = width and
# self.height = height. Create
# rectangle = Rectangle("blue", 4, 5) and print rectangle.color,
# rectangle.width, and rectangle.height.


# TODO 2.4: Write a class Vehicle with __init__(self, make, model)
# storing both. Write a class Motorcycle(Vehicle) with
# __init__(self, make, model, has_sidecar) that calls
# super().__init__(make, model) and then stores
# self.has_sidecar = has_sidecar. Create
# motorcycle = Motorcycle("Honda", "Rebel", False) and print
# motorcycle.make, motorcycle.model, and motorcycle.has_sidecar.


# TODO 2.5 (Debug the Code): this subclass __init__ is supposed to
# call super().__init__(name) to reuse the parent's setup and set
# self.name, but it forgot that call entirely -- it only sets
# self.breed, so dog.name raises AttributeError because Animal's
# __init__ never ran. Fix Dog's __init__ to call
# super().__init__(name) before setting self.breed.
class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def __init__(self, name, breed):
        self.breed = breed


dog = Dog("Rex", "Labrador")
print(dog.name)
print(dog.breed)


# TODO 2.A (Scenario -- Extending a Base Employee Record): an HR
# system has a general Employee record, and a Manager is an Employee
# who additionally tracks how many people report to them. Write a
# class Employee with __init__(self, name, salary) storing both.
# Write a class Manager(Employee) with
# __init__(self, name, salary, direct_reports) that calls
# super().__init__(name, salary) and then stores
# self.direct_reports = direct_reports -- modeling how
# super().__init__() lets Manager reuse Employee's setup exactly,
# adding only the one new field a manager actually needs. Create
# manager = Manager("Dana", 95000, 4) and print manager.name,
# manager.salary, and manager.direct_reports.


# TODO 2.B (Scenario -- Interview Prep): an interviewer asks why you'd
# call super().__init__() inside a subclass instead of just
# copy-pasting the parent's attribute-setting lines directly into the
# subclass's own __init__. Write a function
# explain_super_init_reuse() that returns a string explaining that
# super().__init__() calls the parent class's own __init__ so its
# setup logic runs exactly once, in exactly one place -- if the parent
# class's setup ever needs to change (say, adding validation or a new
# default), every subclass that calls super().__init__() picks up that
# change automatically, whereas copy-pasted logic in each subclass
# would have to be found and updated separately in every single place
# it was duplicated, which is exactly the kind of drift inheritance is
# meant to prevent. Call it and print the result.


# ============================================================
# Topic 3: Method Overriding
# ============================================================

# TODO 3.1: Write a class Animal with __init__(self, name) storing
# self.name = name, and a method speak(self) that returns
# f"{self.name} makes a sound.". Write a class Cat(Animal) that
# overrides speak(self) to return f"{self.name} says Meow!" instead --
# completely replacing the parent's version rather than extending it.
# Create cat = Cat("Whiskers") and print cat.speak().


# TODO 3.2: Write a class Shape with __init__(self, name) storing
# self.name = name, and a method describe(self) that returns
# f"This is a {self.name}.". Write a class Circle(Shape) with
# __init__(self, radius) that calls super().__init__("circle") and
# stores self.radius = radius, and an overriding describe(self) that
# calls base = super().describe() to get the parent's version, then
# returns base + f" It has radius {self.radius}." -- extending the
# parent's behavior instead of throwing it away. Create
# circle = Circle(5) and print circle.describe().


# TODO 3.3: Write a class Employee with __init__(self, name) storing
# self.name = name, and a method describe(self) that returns
# f"{self.name} is an employee.". Write a class Manager(Employee) with
# __init__(self, name, team_size) that calls super().__init__(name)
# and stores self.team_size = team_size, and an overriding
# describe(self) that calls base = super().describe(), then returns
# base + f" They manage a team of {self.team_size}.". Create
# manager = Manager("Priya", 6) and print manager.describe().


# TODO 3.4: Write a class Notification with __init__(self, message)
# storing self.message = message, and a method send(self) that
# returns f"Sending generic notification: {self.message}". Write a
# class SMSNotification(Notification) that overrides send(self) to
# return f"Sending SMS: {self.message}" instead. Create
# sms = SMSNotification("Your code is 4821") and print sms.send().


# TODO 3.5 (Debug the Code): this subclass is supposed to override
# Animal's speak method, but it misspells the method name as
# spaek(self) -- so instead of overriding speak(), it accidentally
# defines an unrelated new method, and calling dog.speak() still runs
# Animal's original version ("Rex makes a sound.") instead of the
# intended "Rex says Woof!". Fix the method name from spaek to speak.
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."


class Dog(Animal):
    def spaek(self):
        return f"{self.name} says Woof!"


dog = Dog("Rex")
print(dog.speak())


# TODO 3.A (Scenario -- Customizing a Shared Receipt Formatter): a
# store's checkout system formats a normal receipt line one way, but a
# discounted receipt needs to show the same line plus a discount note.
# Write a class Receipt with __init__(self, item, price) storing both,
# and a method format_line(self) that returns
# f"{self.item}: ${self.price:.2f}". Write a class
# DiscountedReceipt(Receipt) with
# __init__(self, item, price, discount_percent) that calls
# super().__init__(item, price) and stores
# self.discount_percent = discount_percent, and an overriding
# format_line(self) that calls base = super().format_line(), then
# returns base + f" ({self.discount_percent}% off)" -- modeling how a
# real receipt formatter extends the shared base format instead of
# reimplementing it from scratch. Create
# receipt = DiscountedReceipt("Headphones", 49.99, 20) and print
# receipt.format_line().


# TODO 3.B (Scenario -- Interview Prep): an interviewer asks you to
# explain the difference between a subclass that overrides a method by
# completely replacing it, versus one that overrides a method by
# extending it with super(). Write a function
# explain_overriding_vs_extending() that returns a string explaining
# that overriding simply means a subclass defines a method with the
# same name as one on its parent, so calling that method on a subclass
# instance runs the subclass's version instead -- if the subclass's
# version never calls super().method(), the parent's behavior is fully
# replaced, but if it does call super().method() first and builds on
# the result, the subclass is extending the parent's behavior rather
# than discarding it, which is usually the safer choice when the
# parent's version does something still worth keeping. Call it and
# print the result.


# ============================================================
# Topic 4: Polymorphism
# ============================================================

# TODO 4.1: Write a class Animal with __init__(self, name) storing
# self.name = name, and a method speak(self) that returns
# f"{self.name} makes a sound.". Write a class Dog(Animal) overriding
# speak(self) to return f"{self.name} says Woof!", and a class
# Cat(Animal) overriding speak(self) to return
# f"{self.name} says Meow!". Create
# animals = [Dog("Rex"), Cat("Whiskers")], then loop over animals and
# print animal.speak() for each -- calling the exact same method name
# on every item without ever checking what type each one is; each
# object already knows which version of speak() to run.


# TODO 4.2: Write a class Shape with __init__(self, name) storing
# self.name = name, and a method area(self) that returns 0. Write a
# class Circle(Shape) with __init__(self, radius) calling
# super().__init__("circle") and storing self.radius = radius, with
# an overriding area(self) returning
# round(3.14159 * self.radius ** 2, 2). Write a class Rectangle(Shape)
# with __init__(self, width, height) calling
# super().__init__("rectangle") and storing self.width and
# self.height, with an overriding area(self) returning
# self.width * self.height. Create
# shapes = [Circle(3), Rectangle(4, 5)], then loop over shapes,
# printing each shape.area(), and print the sum of all their areas
# using a total computed in the same loop.


# TODO 4.3: Write a class Employee with __init__(self, name) storing
# self.name = name, and a method describe(self) that returns
# f"{self.name} is an employee.". Write a class Manager(Employee)
# overriding describe(self) to return f"{self.name} manages a team.",
# and a class Developer(Employee) overriding describe(self) to return
# f"{self.name} writes code.". Create
# staff = [Manager("Dana"), Developer("Sam")], then loop over staff
# and print person.describe() for each.


# TODO 4.4: Write a class Notification with __init__(self, message)
# storing self.message = message, and a method send(self) that
# returns f"Generic: {self.message}". Write a class
# EmailNotification(Notification) overriding send(self) to return
# f"Email: {self.message}", and a class SMSNotification(Notification)
# overriding send(self) to return f"SMS: {self.message}". Create
# notifications = [EmailNotification("Welcome!"), SMSNotification("Code: 1234")],
# then loop over notifications, collecting each n.send() into a list
# called results, and print results.


# TODO 4.5 (Debug the Code): this loop is supposed to demonstrate
# polymorphism by calling speak() the same way on every animal, but it
# defeats the entire point by checking each animal's type first with
# an if/elif chain (isinstance(animal, Dog) ... elif
# isinstance(animal, Cat) ...) and calling a differently-named method
# on each branch instead of just calling animal.speak() once, the same
# way, for every item. Fix the loop body to simply call and print
# animal.speak() for every animal, deleting the if/elif type-checking
# entirely.
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."


class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"


class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"


animals = [Dog("Rex"), Cat("Whiskers")]
for animal in animals:
    if isinstance(animal, Dog):
        print(animal.speak())
    elif isinstance(animal, Cat):
        print(animal.speak())


# TODO 4.A (Scenario -- A Payment Processor Supporting Multiple
# Payment Types): a checkout system needs to process a mixed cart of
# payment methods without a giant if/elif chain checking which kind
# each one is. Write a class Payment with __init__(self, amount)
# storing self.amount = amount, and a method process(self) that
# returns f"Processing ${self.amount:.2f} generically.". Write a class
# CardPayment(Payment) overriding process(self) to return
# f"Charging ${self.amount:.2f} to card.", and a class
# PayPalPayment(Payment) overriding process(self) to return
# f"Sending ${self.amount:.2f} via PayPal.". Create
# payments = [CardPayment(50), PayPalPayment(30)], then loop over
# payments, collecting each payment.process() into a list called
# results, and print results -- modeling how a real payment pipeline
# processes every payment type through the identical call, letting
# each class supply its own behavior.


# TODO 4.B (Scenario -- Interview Prep): an interviewer asks why
# polymorphism is considered better design than writing an if/elif
# chain that checks each object's type before deciding what to do with
# it. Write a function explain_polymorphism_benefit() that returns a
# string explaining that polymorphism means calling the exact same
# method name on a collection of different objects and letting each
# object's own class decide what actually happens, instead of the
# calling code needing to know every possible type up front and branch
# on it -- this matters in practice because adding a brand-new subclass
# later (a new payment type, a new notification channel) requires zero
# changes to the code that loops over and calls the shared method,
# whereas an if/elif chain would need a new branch added to it every
# single time a new type is introduced, which is a maintenance burden
# and an easy place to forget a case. Call it and print the result.


# ============================================================
# Topic 5: isinstance() vs type()
# ============================================================

# TODO 5.1: Write a class Animal with __init__(self, name) storing
# self.name = name. Write a class Dog(Animal) with no body other than
# pass. Create dog = Dog("Rex"), then print isinstance(dog, Animal)
# (should be True, since Dog is a subclass of Animal) and
# print type(dog) == Animal (should be False, since type() checks the
# exact class, and dog's exact type is Dog, not Animal).


# TODO 5.2: Write a class Shape with no body other than pass. Write a
# class Circle(Shape) with no body other than pass. Create
# shapes = [Circle(), Shape(), Circle()], then loop over shapes and
# count how many satisfy isinstance(shape, Circle), printing the
# count (should be 2) -- showing isinstance() as the safe way to check
# membership in a mixed list of related types.


# TODO 5.3: Write a class Vehicle with no body other than pass. Write
# a class Car(Vehicle) with no body other than pass. Create
# car = Car(), then print isinstance(car, Car) (True),
# print isinstance(car, Vehicle) (True, since Car IS-A Vehicle), and
# print type(car) == Vehicle (False, since type() only matches the
# exact class Car, not its parent Vehicle).


# TODO 5.4: Write a class Employee with __init__(self, name) storing
# self.name = name. Write a class Manager(Employee) with no body other
# than pass. Create
# staff = [Employee("Sam"), Manager("Dana"), Employee("Ada"), Manager("Priya")],
# then build a list managers_only containing every entry in staff for
# which isinstance(person, Manager) is True (using a list
# comprehension or a loop with .append), and print
# [person.name for person in managers_only].


# TODO 5.5 (Debug the Code): this code is supposed to check whether
# vehicle belongs to the Vehicle family (including any subclass like
# Car), but it uses type(vehicle) == Vehicle, which only matches
# objects whose EXACT type is Vehicle -- since vehicle is actually a
# Car (a subclass), type(vehicle) == Vehicle evaluates to False even
# though a Car clearly IS a Vehicle, so the check wrongly reports
# "False" for something that should count as a Vehicle. Fix the check
# to use isinstance(vehicle, Vehicle) instead, which correctly
# accounts for subclasses.
class Vehicle:
    pass


class Car(Vehicle):
    pass


vehicle = Car()
print(type(vehicle) == Vehicle)


# TODO 5.A (Scenario -- Validating Mixed Input Before Processing): a
# billing system receives a list that might contain a base Payment or
# any of its subclasses, and needs a validation helper that accepts
# all of them safely. Write a class Payment with no body other than
# pass. Write a class CardPayment(Payment) with no body other than
# pass. Write a function is_valid_payment(item) that returns
# isinstance(item, Payment) -- modeling how real validation code
# should accept any subclass of the expected type, not just the exact
# base class. Create
# items = [Payment(), CardPayment(), "not a payment", 42], then print
# [is_valid_payment(item) for item in items] (should be
# [True, True, False, False]).


# TODO 5.B (Scenario -- Interview Prep): an interviewer asks when
# you'd reach for isinstance() instead of type(), and why isinstance()
# is usually considered the safer default. Write a function
# explain_isinstance_vs_type() that returns a string explaining that
# type(obj) == SomeClass only matches when obj's exact class is
# SomeClass, ignoring inheritance entirely, while
# isinstance(obj, SomeClass) returns True for an instance of SomeClass
# OR any of its subclasses -- since polymorphic code is usually meant
# to treat every subclass as a valid member of its parent's family
# (any Dog or Cat should count as an Animal), isinstance() is almost
# always the safer and more correct choice, and type() is reserved for
# the rarer case where you deliberately need to exclude subclasses and
# match one exact class only. Call it and print the result.


# ============================================================
# Topic 6: Bringing It Together -- Inheritance & Polymorphism in
# Production
# ============================================================

# TODO 6.1: Write a class Shape with __init__(self, name) storing
# self.name = name, and a method area(self) that returns 0. Write a
# class Rectangle(Shape) with __init__(self, width, height) calling
# super().__init__("rectangle"), storing self.width and self.height,
# and an overriding area(self) returning self.width * self.height.
# Write a class Circle(Shape) with __init__(self, radius) calling
# super().__init__("circle"), storing self.radius, and an overriding
# area(self) returning round(3.14159 * self.radius ** 2, 2). Create
# shapes = [Rectangle(4, 5), Circle(3)], loop over shapes summing
# shape.area() for each into total_area, and print total_area.


# TODO 6.2: Write a class Employee with __init__(self, name) storing
# self.name = name, and a method describe(self) that returns
# f"{self.name} is an employee.". Write a class Manager(Employee) with
# __init__(self, name, team_size) calling super().__init__(name),
# storing self.team_size, and an overriding describe(self) that
# extends the parent's version with super().describe() plus
# f" They manage {self.team_size} people.". Write a class
# Developer(Employee) with __init__(self, name, language) calling
# super().__init__(name), storing self.language, and an overriding
# describe(self) that extends the parent's version plus
# f" They write {self.language}.". Create
# staff = [Manager("Dana", 5), Developer("Sam", "Python")], build
# managers_only = [person for person in staff if isinstance(person, Manager)],
# and print [person.describe() for person in staff] followed by
# len(managers_only).


# TODO 6.3: Write a class Notification with __init__(self, message)
# storing self.message = message, and a method send(self) that
# returns f"Generic: {self.message}". Write a class
# EmailNotification(Notification) with __init__(self, message, address)
# calling super().__init__(message), storing self.address, and an
# overriding send(self) returning
# f"Email to {self.address}: {self.message}". Write a class
# SMSNotification(Notification) with __init__(self, message, phone)
# calling super().__init__(message), storing self.phone, and an
# overriding send(self) returning
# f"SMS to {self.phone}: {self.message}". Create
# notifications = [EmailNotification("Hi", "a@example.com"), SMSNotification("Hi", "555-0100")],
# loop over notifications collecting each n.send() into a list
# results, and print results.


# TODO 6.4: Write a class Vehicle with __init__(self, make) storing
# self.make = make, and a method describe(self) that returns
# f"A {self.make} vehicle.". Write a class Car(Vehicle) with
# __init__(self, make, doors) calling super().__init__(make), storing
# self.doors, and an overriding describe(self) extending the parent's
# version plus f" It has {self.doors} doors.". Write a class
# Truck(Vehicle) with __init__(self, make, payload_capacity) calling
# super().__init__(make), storing self.payload_capacity, and an
# overriding describe(self) extending the parent's version plus
# f" It can carry {self.payload_capacity} lbs.". Create
# fleet = [Car("Honda", 4), Truck("Ford", 2000)], build
# trucks_only = [v for v in fleet if isinstance(v, Truck)], and print
# [v.describe() for v in fleet] followed by len(trucks_only).


# TODO 6.5 (Debug the Code): this subclass is supposed to extend
# Shape's describe() method (adding its own radius detail on top of
# the parent's message) but its overriding describe() completely
# skips calling super().describe(), silently dropping the shared
# "This is a shape." message the rest of the codebase expects every
# describe() call to include -- circle.describe() only prints the
# radius detail with no base message at all. Fix Circle's describe()
# to build base = super().describe() first, then return
# base + f" It has radius {self.radius}." instead of returning just
# the radius detail on its own.
class Shape:
    def describe(self):
        return "This is a shape."


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def describe(self):
        return f" It has radius {self.radius}."


circle = Circle(5)
print(circle.describe())


# TODO 6.A (Scenario -- A Small Media Library): a media library
# catalogs different kinds of items, each needing its own summary
# format, but the library's report-printing code should treat every
# item the same way. Write a class MediaItem with __init__(self, title)
# storing self.title = title, and a method summary(self) that returns
# f"{self.title}". Write a class Book(MediaItem) with
# __init__(self, title, author) calling super().__init__(title),
# storing self.author, and an overriding summary(self) that extends
# the parent's version with super().summary() plus
# f" by {self.author}". Write a class Movie(MediaItem) with
# __init__(self, title, director) calling super().__init__(title),
# storing self.director, and an overriding summary(self) that extends
# the parent's version plus f" directed by {self.director}". Create
# library = [Book("Dune", "Frank Herbert"), Movie("Arrival", "Denis Villeneuve")],
# loop over library collecting each item.summary() into a list
# report, and print report.


# TODO 6.B (Scenario -- Interview Prep): an interviewer asks you to
# describe a real system where inheritance was clearly the right tool,
# and a case where composition -- giving a class an instance of
# another class as an attribute, instead of inheriting from it --
# would have been the better choice. Write a function
# explain_inheritance_vs_composition() that returns a string
# explaining that inheritance fits an "IS-A" relationship where every
# subclass genuinely is a more specific version of the parent sharing
# its whole behavior (a Manager IS-A Employee, a Car IS-A Vehicle),
# while composition fits a "HAS-A" relationship where one class simply
# needs to use another's functionality without being that kind of
# thing itself (a Car HAS-A Engine, but a Car being forced to inherit
# from Engine would be backwards and would drag in unrelated Engine
# behavior the Car doesn't want); reaching for inheritance just to
# reuse a few convenient methods, when the relationship isn't really
# IS-A, tends to produce a fragile, tangled class hierarchy, which is
# why "favor composition over inheritance" is common real-world
# advice once a hierarchy starts feeling forced. Call it and print the
# result.
