"""
Chapter 14 Exercises: OOP Basics — reference solution.
Run this from inside the exercises/ folder: python3 solution.py
"""

# TODO 1: Write a class Book with an __init__ that takes title and
# author and stores them as instance attributes. Create two Book
# objects with different titles/authors and print each one's title
# and author.
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

book1 = Book("Dune", "Frank Herbert")
book2 = Book("Foundation", "Isaac Asimov")
print(book1.title, "-", book1.author)
print(book2.title, "-", book2.author)


# TODO 2: Write a class Movie whose __init__ takes title, year, and
# rating, storing all three as instance attributes. Create a Movie
# object for "Arrival", 2016, 8.0 and print its three attributes.
class Movie:
    def __init__(self, title, year, rating):
        self.title = title
        self.year = year
        self.rating = rating

movie = Movie("Arrival", 2016, 8.0)
print(movie.title, movie.year, movie.rating)


# TODO 3: Write a class Counter whose __init__ takes no arguments
# (besides self) and sets an instance attribute count to 0. Give it an
# instance method increment(self, amount=1) that adds amount to
# self.count. Create a Counter, call increment() once with no argument
# and once with 5, then print count.
class Counter:
    def __init__(self):
        self.count = 0

    def increment(self, amount=1):
        self.count += amount

counter = Counter()
counter.increment()
counter.increment(5)
print(counter.count)


# TODO 4: Write a class Employee with a class attribute
# company_name = "Acme Corp", and an __init__ that takes name and
# salary and stores them as instance attributes. Create two Employee
# objects and print each one's company_name, name, and salary to show
# company_name is shared while name/salary are not.
class Employee:
    company_name = "Acme Corp"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

emp1 = Employee("Alice", 60000)
emp2 = Employee("Bob", 55000)
print(emp1.company_name, emp1.name, emp1.salary)
print(emp2.company_name, emp2.name, emp2.salary)


# TODO 5: Write a class Playlist whose __init__ takes owner and sets
# self.owner, and sets self.songs to a new empty list created inside
# __init__ (not a class attribute). Give it an instance method
# add_song(self, song) that appends to self.songs. Create two Playlist
# objects, add a different song to each, then print both owners and
# their song lists to show they stay independent.
class Playlist:
    def __init__(self, owner):
        self.owner = owner
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

playlist1 = Playlist("Alice")
playlist2 = Playlist("Bob")
playlist1.add_song("Clair de Lune")
playlist2.add_song("Bohemian Rhapsody")
print(playlist1.owner, "->", playlist1.songs)
print(playlist2.owner, "->", playlist2.songs)


# TODO 6: Write a class Product with an __init__ that takes name and
# price, and a __str__ that returns f"{self.name}: ${self.price:.2f}".
# Create a Product for "Notebook", 2.5 and print() it directly to show
# __str__ is used automatically.
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: ${self.price:.2f}"

product = Product("Notebook", 2.5)
print(product)


# TODO 7 (Debug the Code): this Timer class's tick method is missing
# self as its first parameter, so calling timer.tick() raises a
# TypeError. Find and fix the method definition.
# Bug: def tick(): has no self, so it can't take the automatically
# passed-in object, and it also can't see self.seconds. Fix: add self
# as the first parameter.
class Timer:
    def __init__(self):
        self.seconds = 0

    def tick(self):
        self.seconds += 1

timer = Timer()
timer.tick()
timer.tick()
print(timer.seconds)


# TODO 8 (Debug the Code): this Team class declares members = [] as a
# class attribute, so every Team object ends up sharing and mutating
# the exact same list. Find and fix it so each Team gets its own
# independent members list, set up inside __init__.
# Bug: members = [] at the class level is one list shared by every
# Team instance. Fix: move it into __init__ as self.members = [], so
# each instance gets its own fresh list.
class Team:
    def __init__(self, name):
        self.name = name
        self.members = []

    def add_member(self, member):
        self.members.append(member)

team1 = Team("Falcons")
team2 = Team("Hawks")
team1.add_member("Alice")
team2.add_member("Bob")
print(team1.name, "->", team1.members)
print(team2.name, "->", team2.members)
