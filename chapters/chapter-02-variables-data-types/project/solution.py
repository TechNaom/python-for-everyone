"""
Chapter 2 Project: Everyday Unit Converter — reference solution.
"""

# TODO 1: Ask for a temperature in Celsius using input(), convert it to a
# float, then calculate and print the Fahrenheit and Kelvin equivalents.
celsius = float(input("Enter a temperature in Celsius: "))
fahrenheit = celsius * 9 / 5 + 32
kelvin = celsius + 273.15

# TODO 2: Ask for a distance in kilometers, convert to float, then
# calculate and print the equivalent in miles.
kilometers = float(input("Enter a distance in kilometers: "))
miles = kilometers * 0.621371

# TODO 3: Ask for a weight in kilograms, convert to float, then calculate
# and print the equivalent in pounds.
kilograms = float(input("Enter a weight in kilograms: "))
pounds = kilograms * 2.20462

print("=== Conversion Summary ===")
print(str(celsius) + " C is " + str(fahrenheit) + " F and " + str(kelvin) + " K")
print(str(kilometers) + " km is " + str(miles) + " miles")
print(str(kilograms) + " kg is " + str(pounds) + " lb")
