"""
Chapter 16 Practice Bank: Inheritance & Polymorphism -- reference solution.
See README.md in this folder for full instructions.
Run this from inside the practice/ folder: python3 solution.py
"""

# ============================================================
# Topic 1: Basic Inheritance
# ============================================================

# TODO 1.1
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."


class Dog(Animal):
    pass


dog = Dog("Rex")
print(dog.speak())


# TODO 1.2
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def description(self):
        return f"{self.make} {self.model}"


class Car(Vehicle):
    pass


car = Car("Toyota", "Corolla")
print(car.description())


# TODO 1.3
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Manager(Employee):
    pass


manager = Manager("Priya", 90000)
print(manager.name)
print(manager.salary)


# TODO 1.4
class Shape:
    def area(self):
        return 0


class Square(Shape):
    pass


square = Square()
print(square.area())


# TODO 1.5 (Debug the Code)
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."


class Cat(Animal):
    pass


cat = Cat("Whiskers")
print(cat.speak())


# TODO 1.A (Scenario -- Modeling a Fleet of Vehicles)
class Vehicle:
    def __init__(self, license_plate):
        self.license_plate = license_plate

    def identify(self):
        return f"Vehicle {self.license_plate}"


class Truck(Vehicle):
    pass


truck = Truck("TRK-204")
print(truck.identify())


# TODO 1.B (Scenario -- Interview Prep)
def explain_basic_inheritance():
    return (
        "Inheritance lets one class (the subclass, or 'child') "
        "automatically receive every attribute and method defined on "
        "another class (the superclass, or 'parent') without retyping "
        "any of that code. The subclass can then add its own new "
        "attributes and methods, or override an inherited one to behave "
        "differently, but anything it doesn't touch it gets for free "
        "exactly as the parent defined it."
    )


print(explain_basic_inheritance())


# ============================================================
# Topic 2: super().__init__()
# ============================================================

# TODO 2.1
class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed


dog = Dog("Rex", "Labrador")
print(dog.name)
print(dog.breed)


# TODO 2.2
class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def __init__(self, name, school):
        super().__init__(name)
        self.school = school


student = Student("Ada", "Central High")
print(student.name)
print(student.school)


# TODO 2.3
class Shape:
    def __init__(self, color):
        self.color = color


class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height


rectangle = Rectangle("blue", 4, 5)
print(rectangle.color)
print(rectangle.width)
print(rectangle.height)


# TODO 2.4
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model


class Motorcycle(Vehicle):
    def __init__(self, make, model, has_sidecar):
        super().__init__(make, model)
        self.has_sidecar = has_sidecar


motorcycle = Motorcycle("Honda", "Rebel", False)
print(motorcycle.make)
print(motorcycle.model)
print(motorcycle.has_sidecar)


# TODO 2.5 (Debug the Code)
class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed


dog = Dog("Rex", "Labrador")
print(dog.name)
print(dog.breed)


# TODO 2.A (Scenario -- Extending a Base Employee Record)
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Manager(Employee):
    def __init__(self, name, salary, direct_reports):
        super().__init__(name, salary)
        self.direct_reports = direct_reports


manager = Manager("Dana", 95000, 4)
print(manager.name)
print(manager.salary)
print(manager.direct_reports)


# TODO 2.B (Scenario -- Interview Prep)
def explain_super_init_reuse():
    return (
        "super().__init__() calls the parent class's own __init__ so its "
        "setup logic runs exactly once, in exactly one place. If the "
        "parent class's setup ever needs to change (say, adding "
        "validation or a new default), every subclass that calls "
        "super().__init__() picks up that change automatically, whereas "
        "copy-pasted logic in each subclass would have to be found and "
        "updated separately in every single place it was duplicated, "
        "which is exactly the kind of drift inheritance is meant to "
        "prevent."
    )


print(explain_super_init_reuse())


# ============================================================
# Topic 3: Method Overriding
# ============================================================

# TODO 3.1
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."


class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"


cat = Cat("Whiskers")
print(cat.speak())


# TODO 3.2
class Shape:
    def __init__(self, name):
        self.name = name

    def describe(self):
        return f"This is a {self.name}."


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("circle")
        self.radius = radius

    def describe(self):
        base = super().describe()
        return base + f" It has radius {self.radius}."


circle = Circle(5)
print(circle.describe())


# TODO 3.3
class Employee:
    def __init__(self, name):
        self.name = name

    def describe(self):
        return f"{self.name} is an employee."


class Manager(Employee):
    def __init__(self, name, team_size):
        super().__init__(name)
        self.team_size = team_size

    def describe(self):
        base = super().describe()
        return base + f" They manage a team of {self.team_size}."


manager = Manager("Priya", 6)
print(manager.describe())


# TODO 3.4
class Notification:
    def __init__(self, message):
        self.message = message

    def send(self):
        return f"Sending generic notification: {self.message}"


class SMSNotification(Notification):
    def send(self):
        return f"Sending SMS: {self.message}"


sms = SMSNotification("Your code is 4821")
print(sms.send())


# TODO 3.5 (Debug the Code)
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."


class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"


dog = Dog("Rex")
print(dog.speak())


# TODO 3.A (Scenario -- Customizing a Shared Receipt Formatter)
class Receipt:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def format_line(self):
        return f"{self.item}: ${self.price:.2f}"


class DiscountedReceipt(Receipt):
    def __init__(self, item, price, discount_percent):
        super().__init__(item, price)
        self.discount_percent = discount_percent

    def format_line(self):
        base = super().format_line()
        return base + f" ({self.discount_percent}% off)"


receipt = DiscountedReceipt("Headphones", 49.99, 20)
print(receipt.format_line())


# TODO 3.B (Scenario -- Interview Prep)
def explain_overriding_vs_extending():
    return (
        "Overriding simply means a subclass defines a method with the "
        "same name as one on its parent, so calling that method on a "
        "subclass instance runs the subclass's version instead. If the "
        "subclass's version never calls super().method(), the parent's "
        "behavior is fully replaced, but if it does call "
        "super().method() first and builds on the result, the subclass "
        "is extending the parent's behavior rather than discarding it, "
        "which is usually the safer choice when the parent's version "
        "does something still worth keeping."
    )


print(explain_overriding_vs_extending())


# ============================================================
# Topic 4: Polymorphism
# ============================================================

# TODO 4.1
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
    print(animal.speak())


# TODO 4.2
class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        return 0


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("circle")
        self.radius = radius

    def area(self):
        return round(3.14159 * self.radius ** 2, 2)


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("rectangle")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


shapes = [Circle(3), Rectangle(4, 5)]
total = 0
for shape in shapes:
    print(shape.area())
    total += shape.area()
print(total)


# TODO 4.3
class Employee:
    def __init__(self, name):
        self.name = name

    def describe(self):
        return f"{self.name} is an employee."


class Manager(Employee):
    def describe(self):
        return f"{self.name} manages a team."


class Developer(Employee):
    def describe(self):
        return f"{self.name} writes code."


staff = [Manager("Dana"), Developer("Sam")]
for person in staff:
    print(person.describe())


# TODO 4.4
class Notification:
    def __init__(self, message):
        self.message = message

    def send(self):
        return f"Generic: {self.message}"


class EmailNotification(Notification):
    def send(self):
        return f"Email: {self.message}"


class SMSNotification(Notification):
    def send(self):
        return f"SMS: {self.message}"


notifications = [EmailNotification("Welcome!"), SMSNotification("Code: 1234")]
results = []
for n in notifications:
    results.append(n.send())
print(results)


# TODO 4.5 (Debug the Code)
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
    print(animal.speak())


# TODO 4.A (Scenario -- A Payment Processor Supporting Multiple Payment Types)
class Payment:
    def __init__(self, amount):
        self.amount = amount

    def process(self):
        return f"Processing ${self.amount:.2f} generically."


class CardPayment(Payment):
    def process(self):
        return f"Charging ${self.amount:.2f} to card."


class PayPalPayment(Payment):
    def process(self):
        return f"Sending ${self.amount:.2f} via PayPal."


payments = [CardPayment(50), PayPalPayment(30)]
results = []
for payment in payments:
    results.append(payment.process())
print(results)


# TODO 4.B (Scenario -- Interview Prep)
def explain_polymorphism_benefit():
    return (
        "Polymorphism means calling the exact same method name on a "
        "collection of different objects and letting each object's own "
        "class decide what actually happens, instead of the calling "
        "code needing to know every possible type up front and branch "
        "on it. This matters in practice because adding a brand-new "
        "subclass later (a new payment type, a new notification "
        "channel) requires zero changes to the code that loops over and "
        "calls the shared method, whereas an if/elif chain would need a "
        "new branch added to it every single time a new type is "
        "introduced, which is a maintenance burden and an easy place to "
        "forget a case."
    )


print(explain_polymorphism_benefit())


# ============================================================
# Topic 5: isinstance() vs type()
# ============================================================

# TODO 5.1
class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    pass


dog = Dog("Rex")
print(isinstance(dog, Animal))
print(type(dog) == Animal)


# TODO 5.2
class Shape:
    pass


class Circle(Shape):
    pass


shapes = [Circle(), Shape(), Circle()]
count = 0
for shape in shapes:
    if isinstance(shape, Circle):
        count += 1
print(count)


# TODO 5.3
class Vehicle:
    pass


class Car(Vehicle):
    pass


car = Car()
print(isinstance(car, Car))
print(isinstance(car, Vehicle))
print(type(car) == Vehicle)


# TODO 5.4
class Employee:
    def __init__(self, name):
        self.name = name


class Manager(Employee):
    pass


staff = [Employee("Sam"), Manager("Dana"), Employee("Ada"), Manager("Priya")]
managers_only = [person for person in staff if isinstance(person, Manager)]
print([person.name for person in managers_only])


# TODO 5.5 (Debug the Code)
class Vehicle:
    pass


class Car(Vehicle):
    pass


vehicle = Car()
print(isinstance(vehicle, Vehicle))


# TODO 5.A (Scenario -- Validating Mixed Input Before Processing)
class Payment:
    pass


class CardPayment(Payment):
    pass


def is_valid_payment(item):
    return isinstance(item, Payment)


items = [Payment(), CardPayment(), "not a payment", 42]
print([is_valid_payment(item) for item in items])


# TODO 5.B (Scenario -- Interview Prep)
def explain_isinstance_vs_type():
    return (
        "type(obj) == SomeClass only matches when obj's exact class is "
        "SomeClass, ignoring inheritance entirely, while "
        "isinstance(obj, SomeClass) returns True for an instance of "
        "SomeClass OR any of its subclasses. Since polymorphic code is "
        "usually meant to treat every subclass as a valid member of its "
        "parent's family (any Dog or Cat should count as an Animal), "
        "isinstance() is almost always the safer and more correct "
        "choice, and type() is reserved for the rarer case where you "
        "deliberately need to exclude subclasses and match one exact "
        "class only."
    )


print(explain_isinstance_vs_type())


# ============================================================
# Topic 6: Bringing It Together -- Inheritance & Polymorphism in
# Production
# ============================================================

# TODO 6.1
class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        return 0


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("rectangle")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("circle")
        self.radius = radius

    def area(self):
        return round(3.14159 * self.radius ** 2, 2)


shapes = [Rectangle(4, 5), Circle(3)]
total_area = 0
for shape in shapes:
    total_area += shape.area()
print(total_area)


# TODO 6.2
class Employee:
    def __init__(self, name):
        self.name = name

    def describe(self):
        return f"{self.name} is an employee."


class Manager(Employee):
    def __init__(self, name, team_size):
        super().__init__(name)
        self.team_size = team_size

    def describe(self):
        base = super().describe()
        return base + f" They manage {self.team_size} people."


class Developer(Employee):
    def __init__(self, name, language):
        super().__init__(name)
        self.language = language

    def describe(self):
        base = super().describe()
        return base + f" They write {self.language}."


staff = [Manager("Dana", 5), Developer("Sam", "Python")]
managers_only = [person for person in staff if isinstance(person, Manager)]
print([person.describe() for person in staff])
print(len(managers_only))


# TODO 6.3
class Notification:
    def __init__(self, message):
        self.message = message

    def send(self):
        return f"Generic: {self.message}"


class EmailNotification(Notification):
    def __init__(self, message, address):
        super().__init__(message)
        self.address = address

    def send(self):
        return f"Email to {self.address}: {self.message}"


class SMSNotification(Notification):
    def __init__(self, message, phone):
        super().__init__(message)
        self.phone = phone

    def send(self):
        return f"SMS to {self.phone}: {self.message}"


notifications = [
    EmailNotification("Hi", "a@example.com"),
    SMSNotification("Hi", "555-0100"),
]
results = []
for n in notifications:
    results.append(n.send())
print(results)


# TODO 6.4
class Vehicle:
    def __init__(self, make):
        self.make = make

    def describe(self):
        return f"A {self.make} vehicle."


class Car(Vehicle):
    def __init__(self, make, doors):
        super().__init__(make)
        self.doors = doors

    def describe(self):
        base = super().describe()
        return base + f" It has {self.doors} doors."


class Truck(Vehicle):
    def __init__(self, make, payload_capacity):
        super().__init__(make)
        self.payload_capacity = payload_capacity

    def describe(self):
        base = super().describe()
        return base + f" It can carry {self.payload_capacity} lbs."


fleet = [Car("Honda", 4), Truck("Ford", 2000)]
trucks_only = [v for v in fleet if isinstance(v, Truck)]
print([v.describe() for v in fleet])
print(len(trucks_only))


# TODO 6.5 (Debug the Code)
class Shape:
    def describe(self):
        return "This is a shape."


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def describe(self):
        base = super().describe()
        return base + f" It has radius {self.radius}."


circle = Circle(5)
print(circle.describe())


# TODO 6.A (Scenario -- A Small Media Library)
class MediaItem:
    def __init__(self, title):
        self.title = title

    def summary(self):
        return f"{self.title}"


class Book(MediaItem):
    def __init__(self, title, author):
        super().__init__(title)
        self.author = author

    def summary(self):
        base = super().summary()
        return base + f" by {self.author}"


class Movie(MediaItem):
    def __init__(self, title, director):
        super().__init__(title)
        self.director = director

    def summary(self):
        base = super().summary()
        return base + f" directed by {self.director}"


library = [Book("Dune", "Frank Herbert"), Movie("Arrival", "Denis Villeneuve")]
report = []
for item in library:
    report.append(item.summary())
print(report)


# TODO 6.B (Scenario -- Interview Prep)
def explain_inheritance_vs_composition():
    return (
        "Inheritance fits an 'IS-A' relationship where every subclass "
        "genuinely is a more specific version of the parent sharing its "
        "whole behavior (a Manager IS-A Employee, a Car IS-A Vehicle), "
        "while composition fits a 'HAS-A' relationship where one class "
        "simply needs to use another's functionality without being that "
        "kind of thing itself (a Car HAS-A Engine, but a Car being "
        "forced to inherit from Engine would be backwards and would "
        "drag in unrelated Engine behavior the Car doesn't want). "
        "Reaching for inheritance just to reuse a few convenient "
        "methods, when the relationship isn't really IS-A, tends to "
        "produce a fragile, tangled class hierarchy, which is why "
        "'favor composition over inheritance' is common real-world "
        "advice once a hierarchy starts feeling forced."
    )


print(explain_inheritance_vs_composition())
