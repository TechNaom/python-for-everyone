"""
Chapter 4 Project: Grade Calculator — reference solution.
"""

# TODO 1: Ask for marks (0-100) in 5 subjects using input(), converting
# each to a float. Store them in five separate variables.
math_marks = float(input("Enter marks in Math: "))
science_marks = float(input("Enter marks in Science: "))
english_marks = float(input("Enter marks in English: "))
history_marks = float(input("Enter marks in History: "))
computer_marks = float(input("Enter marks in Computer Science: "))

# TODO 2: Calculate the average of all five marks.
average = (math_marks + science_marks + english_marks + history_marks + computer_marks) / 5

# TODO 3: Using if/elif/else (ordered correctly!), assign a grade based
# on the scale above and store it in a variable called `grade`.
if average >= 75:
    grade = "A"
elif average >= 60:
    grade = "B"
elif average >= 50:
    grade = "C"
elif average >= 40:
    grade = "D"
else:
    grade = "Fail"

print("=== Report Card ===")
print("Average:", average)
print("Grade:", grade)
