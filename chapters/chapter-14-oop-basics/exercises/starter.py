"""
Chapter 14 Exercises: OOP Basics
See README.md in this folder for full instructions.
Run this from inside the exercises/ folder: python3 starter.py
"""

# TODO 1: Write a class Book with an __init__ that takes title and
# author and stores them as instance attributes. Create two Book
# objects with different titles/authors and print each one's title
# and author.


# TODO 2: Write a class Movie whose __init__ takes title, year, and
# rating, storing all three as instance attributes. Create a Movie
# object for "Arrival", 2016, 8.0 and print its three attributes.


# TODO 3: Write a class Counter whose __init__ takes no arguments
# (besides self) and sets an instance attribute count to 0. Give it an
# instance method increment(self, amount=1) that adds amount to
# self.count. Create a Counter, call increment() once with no argument
# and once with 5, then print count.


# TODO 4: Write a class Employee with a class attribute
# company_name = "Acme Corp", and an __init__ that takes name and
# salary and stores them as instance attributes. Create two Employee
# objects and print each one's company_name, name, and salary to show
# company_name is shared while name/salary are not.


# TODO 5: Write a class Playlist whose __init__ takes owner and sets
# self.owner, and sets self.songs to a new empty list created inside
# __init__ (not a class attribute). Give it an instance method
# add_song(self, song) that appends to self.songs. Create two Playlist
# objects, add a different song to each, then print both owners and
# their song lists to show they stay independent.


# TODO 6: Write a class Product with an __init__ that takes name and
# price, and a __str__ that returns f"{self.name}: ${self.price:.2f}".
# Create a Product for "Notebook", 2.5 and print() it directly to show
# __str__ is used automatically.


# TODO 7 (Debug the Code): this Timer class's tick method is missing
# self as its first parameter, so calling timer.tick() raises a
# TypeError. Find and fix the method definition.
class Timer:
    def __init__(self):
        self.seconds = 0

    def tick():
        self.seconds += 1

timer = Timer()
timer.tick()
timer.tick()
print(timer.seconds)


# TODO 8 (Debug the Code): this Team class declares members = [] as a
# class attribute, so every Team object ends up sharing and mutating
# the exact same list. Find and fix it so each Team gets its own
# independent members list, set up inside __init__.
class Team:
    members = []

    def __init__(self, name):
        self.name = name

    def add_member(self, member):
        self.members.append(member)

team1 = Team("Falcons")
team2 = Team("Hawks")
team1.add_member("Alice")
team2.add_member("Bob")
print(team1.name, "->", team1.members)
print(team2.name, "->", team2.members)
