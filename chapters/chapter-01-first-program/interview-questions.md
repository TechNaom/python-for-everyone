# Chapter 1 Interview Questions: Your First Python Program

These are the kinds of questions that come up in early screening interviews
and coding bootcamp assessments once someone claims "I know Python basics."
Each includes what a strong answer sounds like, common red flags, and a
natural follow-up an interviewer might ask next.

---

### 1. What does `print()` do, and how is it different from just typing text into your code?

**Strong answer:** `print()` is a function that outputs its argument to the
console/terminal so a human can see it. Text that isn't inside `print()` just
sits in the source code and does nothing when the program runs — Python
doesn't display arbitrary lines of code, only what you explicitly ask it to
output.

**Red flags:** Thinking every line of code "shows up" somewhere automatically,
or confusing `print()` with `return`.

**Follow-up:** "What's the difference between `print()` and `return` in a
function?"

---

### 2. What's the difference between `=` and `==` in Python?

**Strong answer:** `=` is assignment — it stores a value in a variable.
`==` is comparison — it checks whether two values are equal and returns
`True` or `False`. Mixing them up is one of the most common beginner bugs.

**Red flags:** Saying they're "basically the same" or being unable to give an
example of each.

**Follow-up:** "What would `if x = 5:` do in Python?" (Answer: it's a syntax
error — Python doesn't allow assignment inside an `if` condition like that.)

---

### 3. What are the three basic data types you've learned so far, and how do you tell them apart?

**Strong answer:** String (text, always in quotes, e.g. `"hello"`), integer
(whole numbers, no decimal point, e.g. `12`), and float (numbers with a
decimal point, e.g. `4.9`). You can also check a value's type directly with
`type(value)`.

**Red flags:** Not knowing that `"12"` (quoted) is a string even though it
looks numeric.

**Follow-up:** "What would `type("12")` return, and why?"

---

### 4. Why does `print("Age: " + 25)` raise an error, and how do you fix it?

**Strong answer:** `+` means different things for different types — for
numbers it adds, for strings it concatenates. Python won't silently guess
which one you meant when you mix a string and an int, so it raises a
`TypeError`. Fix it by converting the number to a string first:
`print("Age: " + str(25))`.

**Red flags:** Guessing the error is a "syntax error" rather than a type
error, or not knowing `str()` exists.

**Follow-up:** "What's the reverse conversion called, if you have a string
like `"25"` and want it as a number?" (Answer: `int()` or `float()`.)

---

### 5. What does `input()` return, and what type is it always?

**Strong answer:** `input()` displays an optional prompt, pauses execution,
and returns whatever the user typed — always as a **string**, even if they
typed digits. This surprises a lot of beginners: `input("Enter your age: ")`
followed by trying to do math on the result directly will fail unless you
convert it with `int()` first.

**Red flags:** Assuming `input()` automatically knows if the user meant to
type a number.

**Follow-up:** "How would you get a number from the user and immediately add
5 to it?" (Answer: `age = int(input("Age: ")); print(age + 5)`.)

---

### 6. What's a variable, in your own words?

**Strong answer:** A named location that holds a value, which can be read or
changed later in the program. It's a way of giving a piece of data a
memorable label instead of retyping the raw value everywhere.

**Red flags:** Confusing a variable with the value itself (e.g., saying "a
variable is just text") or thinking variable names must match their content's
type in the name.

**Follow-up:** "Can a variable's value change after it's first set? Show me
an example."

---

## Rapid-Fire Q&A

- **Q: What symbol is used for assignment?** A: A single `=`.
- **Q: What wraps text to make it a string?** A: Quotation marks, single or double.
- **Q: Name the two numeric types covered in Chapter 1.** A: int and float.
- **Q: What type does `input()` always return?** A: A string.
- **Q: What function converts a number to a string?** A: `str()`.

## Strategy Tips

- If you're new to interviews: it's completely fine to think out loud
  ("I know `input()` returns a string, so I'd need to convert it before doing
  math") — interviewers are usually evaluating your reasoning, not just your
  final answer.
- If you get a question wrong, don't panic — ask "would it help if I walked
  through a small example?" and write one out. Concrete examples recover a
  lot of partial credit.
