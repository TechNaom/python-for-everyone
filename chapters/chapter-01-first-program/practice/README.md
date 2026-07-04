# Chapter 1 Practice Bank: Your First Python Program

A deeper set of practice problems, organized by topic, on top of the
main `exercises/` folder — including scenario-based problems written
in the same style you'll see in real interviews. Uses only what
Chapter 1 covered: `print()`, variables, basic types (string/int/float),
`input()`, and string concatenation with `+` and `str()`.

## How to run

```bash
python3 starter.py
```

## Topic 1: `print()`

1. Print `"Hello, World!"` on one line, then print your own name on the next line.
2. Print a 3-line shipping label — name, street address, city + zip.
3. Print a decorative header: a line of dashes, a title, another line of dashes.
4. Print `"Loading..."` three times, each in its own `print()` call, and explain in a comment why they land on separate lines.
5. Print a 2-line "Welcome" banner using symbols of your choice.
6. **Scenario — Internal Tool:** print a 2-line startup banner for a CLI script.
7. **Scenario — Interview Prep:** prove that `print()` always starts a new line after each call.

## Topic 2: Variables

1. Store your name, age, and height in three variables and print each.
2. Create `score = 10`, print it, reassign to `20`, print again.
3. Create two variables and print them in reverse order to show a variable is just a label.
4. Create `balance = 100` and reassign it three times like a running total, printing after each change.
5. Copy one variable's value into a second variable and print both.
6. **Scenario — Click Counter:** simulate 3 button clicks by reassigning a counter variable and printing after each one.
7. **Scenario — Debug the Code (Interview Prep):** fix code that prints a bank balance *before* a deposit is added instead of after.

## Topic 3: Basic Types (string / int / float)

1. Create one variable of each type for a product listing and print each with a label.
2. Join a string label with an int using `str()`.
3. **Debug the Code:** fix a `TypeError` caused by joining a string directly with an int.
4. Build a one-line "ID card" sentence joining a string, an int, and a float.
5. Store the same number as an int and as a float, and print both to see the difference.
6. **Scenario — Till Receipt:** print a receipt line like `Coffee - $4.50`.
7. **Scenario — Interview Prep:** explain (in a comment) why `"Age: " + 30` crashes but `"Age: " + str(30)` doesn't.

## Topic 4: `input()`

1. Ask for the user's name and print a personalized greeting.
2. Ask two questions with two `input()` calls and combine both answers in one sentence.
3. Ask for the user's age as text and build a sentence with it.
4. **Debug the Code:** fix a `TypeError` caused by joining `input()` text with an `int` variable directly.
5. Ask two more questions and combine both answers into one sentence.
6. **Scenario — Mini Mad Libs:** ask for a noun and an adjective, print a silly sentence combining them.
7. **Scenario — Interview Prep:** prove that `input()` always returns a string, no matter what's typed.

## Checking your work

Compare your output against `solution.py`. Your exact wording doesn't
need to match — the goal is that your program runs without errors and
does what each TODO asks.
