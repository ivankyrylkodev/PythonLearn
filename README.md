# First Steps in Python

A structured learning path through the fundamentals of Python programming. This repository contains hands-on exercises and projects organized by week.

## Project Structure

### Week 0 - Introduction & Basics

Getting started with Python fundamentals and basic I/O operations.

- **[hello.py](Week%200/hello.py)** - A simple introductory program that demonstrates:
  - Reading user input with `input()`
  - Cleaning up input with `.strip()` (removes leading/trailing whitespace) and `.title()` (capitalizes each word)
  - Splitting a string into parts with `.split(" ")`, using multiple assignment to unpack the result into `first` and `last` variables
  - Formatted output using an f-string (`f"hello, {first}"`)

  This script prompts the user for their full name, normalizes it, splits it into first and last name, and greets the user using just their first name.

## Getting Started

To run any of the Python files:

```bash
python "Week 0/hello.py"
```

When prompted, enter your full name (first and last, separated by a space) to see the greeting.

## Learning Objectives

- Basic Python syntax and structure
- Input/output operations
- String methods (`strip`, `title`, `split`)
- Unpacking values from `split()` into multiple variables
- f-string formatting
