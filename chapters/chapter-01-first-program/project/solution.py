"""
Chapter 1 Project: Personal Greeting Generator — reference solution.
"""

# TODO 1: Ask for the person's name using input(), store it in a variable.
name = input("What's your name? ")

# TODO 2: Ask for their favorite animal.
animal = input("What's your favorite animal? ")

# TODO 3: Ask for their favorite food.
food = input("What's your favorite food? ")

# TODO 4: Ask for a number from 1 to 100.
number = input("Pick a number from 1 to 100: ")

# TODO 5: Print a personalized greeting using all four answers.
print("=== Your Personalized Greeting ===")
print("Dear " + name + ",")
print("")
print("Congratulations! You have been officially named")
print("Grand Ambassador of " + animal + "s, Protector of " + food + ",")
print("and Keeper of the Sacred Number " + number + ".")
print("")
print("May your day be as wonderful as you are.")
