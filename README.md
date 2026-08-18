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

## Getting Started

To run any of the Python files, use `python` followed by the path in quotes (the quotes matter because the folder name contains a space):

```bash
python "Week 0/hello.py"
python "Week 0/calculator.py"
```

- `hello.py` will prompt for your name and print a greeting.
- `calculator.py` will prompt for a number and print its square.

## Learning Objectives

- Basic Python syntax and structure
- Defining and calling functions, including functions with default parameter values
- Input/output operations, including converting input strings to numbers
- Returning values from functions vs. printing directly
- Using built-in functions like `pow()`
