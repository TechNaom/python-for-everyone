"""
Chapter 16 Exercises: Inheritance & Polymorphism
See README.md in this folder for full instructions.
Run this from inside the exercises/ folder: python3 starter.py
"""

# TODO 1: Write a class Animal whose __init__ takes name and stores it
# as self.name. Give it a method speak(self) that returns
# f"{self.name} makes a sound." Write a subclass Dog(Animal) with an
# empty body (just pass). Create a Dog named "Rex" and print the
# result of calling speak() on it, then print rex.name.


# TODO 2: Write a class Employee whose __init__ takes name and salary,
# storing both as instance attributes. Write a subclass Manager(Employee)
# whose __init__ takes name, salary, and team_size, calls
# super().__init__(name, salary) to reuse the parent's setup, then
# stores team_size as its own attribute. Create a Manager named "Priya"
# with salary 90000 and team_size 5, then print her name, salary, and
# team_size.


# TODO 3: Write a class Shape with a method area(self) that returns 0.
# Write a subclass Square(Shape) whose __init__ takes side and stores
# it as self.side, and that overrides area(self) to return
# self.side ** 2. Create a Square with side 4 and print the result of
# calling area() on it.


# TODO 4: Write a class Employee with __init__ taking name and salary,
# and a method pay_summary(self) that returns
# f"{self.name} earns {self.salary}". Write a subclass Manager(Employee)
# whose __init__ takes name, salary, and bonus, calls
# super().__init__(name, salary), and stores bonus. Override
# pay_summary(self) to call super().pay_summary() and append
# f" plus a bonus of {self.bonus}" to the result. Create a Manager
# named "Sam" with salary 70000 and bonus 5000, then print the result
# of calling pay_summary() on it.


# TODO 5: Write a class Shape with a method area(self) that returns 0.
# Write two subclasses: Square(Shape), whose __init__ takes side and
# overrides area(self) to return side ** 2, and Circle(Shape), whose
# __init__ takes radius and overrides area(self) to return
# round(3.14159 * radius ** 2, 2). Put one Square(side=3) and one
# Circle(radius=2) into a list, loop over the list, and print the
# result of calling area() on each one -- no if/elif type-checking.


# TODO 6: Write a class Employee with __init__ taking name and salary.
# Write a subclass Manager(Employee) with no extra __init__ (just
# inherits Employee's). Create one Employee named "Alex" with salary
# 55000 and one Manager named "Jordan" with salary 85000. Print, for
# each of the two objects: whether isinstance(obj, Employee) is True,
# and whether type(obj) == Employee is True. (Print four lines total,
# two per object.)


# TODO 7 (Debug the Code): this Car class forgets to call
# super().__init__() in its own __init__, so the parent Vehicle's
# setup never runs and car.make/car.model are never actually set --
# accessing them raises an AttributeError. Find and fix it.
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        self.num_doors = num_doors

car = Car("Honda", "Civic", 4)
print(car.make, car.model, car.num_doors)


# TODO 8 (Debug the Code): this code loops over a mixed list of Car and
# Motorcycle objects and tries to print a description for each, but
# instead of relying on each subclass's own overridden describe(), it
# checks type(vehicle) == Car and hardcodes the Car-only message for
# every object -- so the Motorcycle object gets the wrong description
# printed, and describe() is never even called. Find and fix it so the
# loop calls vehicle.describe() on every object and lets polymorphism
# pick the right version automatically.
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def describe(self):
        return f"{self.make} {self.model} is a generic vehicle."

class Car(Vehicle):
    def describe(self):
        return f"{self.make} {self.model} is a car."

class Motorcycle(Vehicle):
    def describe(self):
        return f"{self.make} {self.model} is a motorcycle."

vehicles = [Car("Toyota", "Corolla"), Motorcycle("Harley-Davidson", "Iron 883")]
for vehicle in vehicles:
    if type(vehicle) == Car:
        print(f"{vehicle.make} {vehicle.model} is a car.")
