# First Steps in Python

A structured learning path through the fundamentals of Python programming. This repository contains hands-on exercises and projects organized by week.

## Project Structure

### Week 0 - Introduction & Basics

Getting started with Python fundamentals: functions, input/output, and basic arithmetic.

- **[hello.py](Week%200/hello.py)** - A simple greeting program that demonstrates:
  - Defining and calling functions with `def`
  - Reading user input with `input()`
  - Default parameter values (`def hello(to="world")`) - if `hello()` is called without an argument, it falls back to `"world"`
  - Passing a variable from one function into another
  - Printing multiple values with `print()` by separating them with a comma

  The script asks for the user's name, then passes it to a `hello()` function that prints a greeting. `main()` is defined first but called last, after `hello()` has been defined, so that the file reads top-down like a table of contents while still running correctly (Python only needs a function to exist by the time it's *called*, not by the time it's *defined above*).

- **[calculator.py](Week%200/calculator.py)** - A simple calculator that demonstrates:
  - Converting input from a string to an integer with `int()`, since `input()` always returns text
  - Defining a function that takes a parameter and returns a value (`def square(n): return pow(n, 2)`)
  - Using the built-in `pow()` function to raise a number to a power
  - Passing the result of one function call directly into another (`square(x)` inside `print()`)

  The script asks the user for a number, squares it, and prints the result.

#### Problem Set 0

Exercises that put the Week 0 concepts into practice.

- **[Problem Set/Indoor Voice/indoor.py](Week%200/Problem%20Set/Indoor%20Voice/indoor.py)** - "Indoor Voice": converts shouted (all-caps) text into a normal, quiet sentence. Demonstrates:
  - Reading a full line of text with `input()`
  - String methods: `.lower()` converts every character in a string to lowercase
  - Chaining a method call directly onto the result of `input()`, then passing that straight into `print()`, without storing an intermediate variable

  The script reads a line of text and prints it back entirely in lowercase, so an ALL-CAPS "outdoor voice" sentence reads as a calm "indoor voice" one.

- **[Problem Set/playback/playback.py](Week%200/Problem%20Set/playback/playback.py)** - "Playback": simulates a slow, drawn-out way of speaking. Demonstrates:
  - String methods: `.replace(old, new)` swaps every occurrence of one substring for another
  - Using a space `" "` as the substring to search for, so the replacement happens between every word

  The script reads a line of text and prints it back with every space replaced by `"..."`, so "hello there" becomes "hello...there" - as if the sentence were being read out slowly.

- **[Problem Set/faces/faces.py](Week%200/Problem%20Set/faces/faces.py)** - "Faces": converts text emoticons into emoji. Demonstrates:
  - Chaining two `.replace()` calls back-to-back on the same string, so the second replacement runs on the output of the first
  - Using emoji characters directly as string literals in Python source code

  The script reads a line of text and prints it back with every `:)` swapped for 🙂 and every `:(` swapped for 🙁.

- **[Problem Set/einstein/einstein.py](Week%200/Problem%20Set/einstein/einstein.py)** - "Einstein": calculates energy from mass using Einstein's mass-energy equivalence formula, E = mc². Demonstrates:
  - Converting input to an integer with `int()` inline, directly inside a larger expression, instead of storing it in a separate variable first
  - The exponentiation operator `**` (here, squaring the speed of light, `299792458 ** 2`)
  - Operator precedence: `**` binds tighter than `*`, so `int(m) * 299792458 ** 2` squares the speed of light first, then multiplies by the mass

  The script reads a mass in kilograms, multiplies it by the speed of light in meters per second squared, and prints the resulting energy in joules.

## Getting Started

To run any of the Python files, use `python` followed by the path in quotes (the quotes matter because the folder names contain spaces):

```bash
python "Week 0/hello.py"
python "Week 0/calculator.py"
python "Week 0/Problem Set/Indoor Voice/indoor.py"
python "Week 0/Problem Set/playback/playback.py"
python "Week 0/Problem Set/faces/faces.py"
python "Week 0/Problem Set/einstein/einstein.py"
```

- `hello.py` will prompt for your name and print a greeting.
- `calculator.py` will prompt for a number and print its square.
- `indoor.py` will prompt for a line of text and print it back in lowercase.
- `playback.py` will prompt for a line of text and print it back with spaces replaced by `"..."`.
- `faces.py` will prompt for a line of text and print it back with `:)` and `:(` replaced by emoji.
- `einstein.py` will prompt for a mass (in kg) and print the equivalent energy (in joules).

## Learning Objectives

- Basic Python syntax and structure
- Defining and calling functions, including functions with default parameter values
- Input/output operations, including converting input strings to numbers
- Returning values from functions vs. printing directly
- Using built-in functions like `pow()`, and the equivalent `**` exponentiation operator
- Working with string methods like `.lower()` and `.replace()`, including chaining multiple method calls together
- Operator precedence in arithmetic expressions
