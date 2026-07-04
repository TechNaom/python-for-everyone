"""
Chapter 1 Exercises: Your First Python Program — reference solution.
"""

# TODO 1: Print a greeting of your choice.
print("Hello there! Welcome to Python.")


# TODO 2: Create three variables — city (string), favorite_number (int),
# and temperature_today (float) — then print all three.
city = "Hyderabad"
favorite_number = 7
temperature_today = 31.5
print(city)
print(favorite_number)
print(temperature_today)


# TODO 3: Ask the user for their favorite color with input(), store it,
# then print a sentence that includes their answer.
favorite_color = input("What's your favorite color? ")
print("Nice choice — " + favorite_color + " is a great color!")


# TODO 4: Fix the TypeError below using str().
visits = 5
print("You've visited this page " + str(visits) + " times.")
