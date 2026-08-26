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

- **[Problem Set/tip/tip.py](Week%200/Problem%20Set/tip/tip.py)** - "Tip Calculator": works out how much tip to leave from a bill amount and a tip percentage. Demonstrates:
  - Helper functions that clean up input before converting it: `dollars_to_float()` strips a leading `$` with `.replace("$", "")` before calling `float()`; `percent_to_float()` strips a trailing `%` the same way, then divides by 100 so `"10"` becomes `0.1`
  - Passing the raw string from `input()` straight into a helper function instead of storing it in a variable first
  - Formatted string literals (f-strings): `f"Leave ${tip:.2f}"` embeds the `tip` variable directly inside the string, formatted to two decimal places with the `:.2f` format spec
  - Multiplying two `float` values together to get the tip amount

  The script asks for the cost of the meal (e.g. `$25.00`) and a tip percentage (e.g. `15%`), strips the `$` and `%` symbols, converts both to numbers, and prints how much to leave, rounded to two decimal places.

### Week 1 - Conditionals

Making decisions in code with `if`, `elif`, and `else`.

- **[compare.py](Week%201/compare.py)** - A number comparison program that demonstrates:
  - Reading two separate integer inputs with `int(input(...))`
  - The equality operator `==`
  - Branching with `if` / `else`, where the `else` branch catches every case the `if` didn't

  The script asks for two numbers, `x` and `y`, and prints whether `x` is equal to `y` or not.

- **[grade.py](Week%201/grade.py)** - A letter-grade calculator that demonstrates:
  - Reading a single integer input with `int(input(...))`
  - Comparison operators: `>=`
  - Branching with `if` / `elif` / `elif` / `elif` / `else`, where conditions are checked top to bottom and only the first true one runs - which is why each `elif` only needs to rule out the *next* threshold down, not repeat the ones above it

  The script asks for a numeric score and prints the corresponding letter grade: A (90+), B (80-89), C (70-79), D (60-69), or F (below 60).

- **[parity.py](Week%201/parity.py)** - An even/odd checker that demonstrates:
  - Defining a function that returns a boolean expression directly (`return (n % 2 == 0)`) instead of computing a value first and returning it afterward
  - The modulo operator `%`, which gives the remainder of a division - a number is even exactly when it leaves no remainder after dividing by 2
  - Using a function's return value as the condition of an `if` statement (`if is_even(x):`)

  The script asks for a number and prints whether it's `Even` or `Odd`.

- **[house.py](Week%201/house.py)** - A Hogwarts house sorter that demonstrates:
  - Structural pattern matching with `match` / `case`, an alternative to a long `if` / `elif` chain
  - Matching several possible values in a single `case` with the `|` (or) pattern: `case "Harry" | "Hermione" | "Ron":`
  - The wildcard pattern `case _:`, which matches anything not caught by an earlier `case` - the `match` equivalent of a final `else`

  The script asks for a name and prints "Griffindor" for Harry, Hermione, or Ron, "Slytherin" for Draco, and "Who?" for anyone else.

#### Problem Set 1

Exercises that put the Week 1 concepts into practice.

- **[Problem Set/bank/bank.py](Week%201/Problem%20Set/bank/bank.py)** - "Bank": a teller that greets a customer and quotes a balance based on how they say hello. Demonstrates:
  - Chaining `.lower()` and `.strip()` together on the result of `input()`, so the check that follows doesn't care about capitalization or stray leading/trailing whitespace
  - Slicing a string with `[:5]` to grab just its first 5 characters, so `greeting[:5] == "hello"` matches "hello there" as well as a bare "hello"
  - Indexing a single character out of a string with `[0]`
  - Branching with `if` / `elif` / `else`, where the more specific check (`greeting[:5] == "hello"`) is tested before the looser one (`greeting[0] == "h"`), since `elif` only runs if every check above it was false

  The script asks for a greeting and prints `$0` if it starts with "hello", `$20` if it merely starts with "h" (e.g. "hi"), or `$100` for anything else.

- **[Problem Set/deep/deep.py](Week%201/Problem%20Set/deep/deep.py)** - "Deep Thought": answers the ultimate question, Hitchhiker's-Guide style. Demonstrates:
  - Calling `.lower()` on `input()`'s result so the answer matches regardless of how it was typed
  - `match` / `case` again, this time matching several different spellings of the same answer with `|` ("42", "forty-two", "forty two")
  - The `case _:` wildcard catching every other response

  The script asks for the Answer to the Great Question of Life, the Universe, and Everything, and prints "Yes" if it's some form of "42", or "No" otherwise.

- **[Problem Set/extensions/extensions.py](Week%201/Problem%20Set/extensions/extensions.py)** - "File Extensions": looks at a filename and prints the MIME type that matches its extension. Demonstrates:
  - Chaining `.strip().lower().split(".")` on the result of `input()`, turning the filename into a list of its dot-separated parts in one step
  - Grabbing the last element of that list with `file[len(file) - 1]`, so the extension is found correctly even if the filename itself contains dots (e.g. `my.notes.txt`)
  - `match` / `case` matching several extensions to the same MIME type with `|` (e.g. `case "jpg" | "jpeg":`)
  - `case _:` falling back to the generic `application/octet-stream` type for any unrecognized extension

  The script asks for a filename and prints its MIME type - `image/gif`, `image/jpeg`, `image/png`, `application/pdf`, `text/plain`, or `application/zip` - or `application/octet-stream` if the extension isn't recognized.

- **[Problem Set/interpreter/interpreter.py](Week%201/Problem%20Set/interpreter/interpreter.py)** - "Interpreter": a small four-function calculator that reads and evaluates a whole expression from a single line of input. Demonstrates:
  - Tuple unpacking: `x, symb, y = expression.split(" ")` splits `"3 + 4"` into three separate variables in one line, since `.split(" ")` on a string with two spaces returns a list of exactly three items
  - `match` / `case` branching on the operator symbol (`+`, `-`, `*`, `/`)
  - Converting both operands to `float()` inside each `case`, since splitting a string always produces strings, not numbers
  - `case _:` catching any symbol that isn't a recognized operator

  The script asks for an expression like `3 + 4`, and prints the result of applying the operator to the two numbers, or `Unknown operation` if the symbol isn't `+`, `-`, `*`, or `/`.

- **[Problem Set/meal/meal.py](Week%201/Problem%20Set/meal/meal.py)** - "Meal Time": decides whether a given clock time falls within breakfast, lunch, or dinner. Demonstrates:
  - Splitting work across a `main()` function and a `convert()` helper function, run in that order at the bottom of the file via `if __name__ == "__main__":` - a standard way to mark which function should run when the file is executed directly
  - Converting an `"HH:MM"` string into a single fractional-hour number: `time.split(":")` breaks it into hours and minutes, then `int(time[0]) + int(time[1])/60` combines them (e.g. `"7:30"` becomes `7.5`)
  - Chained comparisons: `7 <= con_time <= 8` reads like the mathematical notation and checks both bounds at once, equivalent to `7 <= con_time and con_time <= 8`
  - An `if` / `elif` chain with no final `else` - if the time doesn't fall in any of the three windows, the script simply prints nothing

  The script asks for the time (e.g. `7:30`), converts it to a fractional hour, and prints `breakfast time`, `lunch time`, or `dinner time` if it falls in the corresponding window - otherwise it prints nothing.

### Week 2 - Loops

Repeating work with `while` and `for` loops.

- **[cat.py](Week%202/cat.py)** - A "meow" printer that demonstrates:
  - An input-validation loop: `while True:` repeats forever until an explicit `break`, which here only fires once the entered number is greater than 0 - so invalid input (zero, negative, or unparseable text) just asks again instead of crashing or continuing with a bad value
  - Splitting the program into three functions - `main()`, `get_number()`, and `meow()` - so reading/validating input is kept separate from acting on it
  - `for _ in range(n):` to repeat an action exactly `n` times; the underscore `_` is a conventional throwaway variable name used when the loop needs a counter to control repetition but never actually uses its value

  The script asks for a positive whole number and prints "meow" that many times, re-prompting if the number entered isn't greater than 0.

- **[hogwarts.py](Week%202/hogwarts.py)** - A student roster printer that demonstrates:
  - A list of dictionaries, `students = [{"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"}, ...]`, where each item bundles several related values under named keys instead of just one value per position
  - `for student in students:` looping directly over the *items* of a list, rather than over its indices, since each iteration doesn't need to know its position
  - Indexing into a dictionary with a string key, `student["name"]`, instead of an integer position
  - The `sep` keyword argument to `print()`: `print(a, b, c, sep=", ")` joins the values with `", "` instead of `print()`'s default single space
  - Using `None` as a dictionary value to represent "no data" - Draco's `"patronus"` is `None` because he doesn't have one, and `print()` displays it as the literal text `None`

  The script loops over the `students` list and, for each student, prints their name, house, and patronus (or `None` if they don't have one), separated by commas.

- **[mario.py](Week%202/mario.py)** - A solid square drawn out of `#` characters, demonstrating:
  - Splitting drawing logic across three functions - `main()`, `print_square(size)`, and `print_row(width)` - where each function calls the next, so `main()` doesn't need to know how a row is actually drawn
  - `for i in range(size):` used purely to repeat an action `size` times; like the `_` convention seen in `cat.py`, the loop variable `i` is never read inside the loop body
  - The string repetition operator `*`: `"#" * width` builds a row by repeating the single-character string `"#"` `width` times, rather than looping over individual characters

  The script prints a 3x3 square of `#` characters, one row per line.

#### Problem Set 2

Exercises that put the Week 2 concepts into practice.

- **[Problem Set/camel/camel.py](Week%202/Problem%20Set/camel/camel.py)** - "camelCase": converts a camelCase-formatted word or sentence into snake_case. Demonstrates:
  - Iterating directly over the characters of a string with `for letter in words:`, rather than looping over its indices
  - The string method `.isupper()`, which checks whether a single character is an uppercase letter
  - Reassigning the loop variable (`words`) from inside the loop body: `for letter in words:` grabs its sequence of characters from the original string before the loop starts, so reassigning `words` partway through doesn't change which letters get visited next - it only affects what the final `return words` sends back
  - Building the replacement text inline with `"_" + letter.lower()`, then passing it straight into `.replace(letter, ...)`, which swaps every occurrence of that character in the string, not just the one at the current position

  The script asks for a camelCase word or sentence and prints it converted to snake_case, with each uppercase letter replaced by an underscore followed by its lowercase form (e.g. `helloWorld` becomes `hello_world`).

- **[Problem Set/coke/coke.py](Week%202/Problem%20Set/coke/coke.py)** - "Vending Machine": accepts coins one at a time until a $0.50 balance is met, then prints any change owed. Demonstrates:
  - A `while` loop whose condition depends on a running total (`while insert_coin < 50:`), so it keeps looping until enough has been inserted
  - Combining multiple equality checks with `or` (`add_coin == 5 or add_coin == 10 or add_coin == 25`) to accept any of several valid coin values
  - The `continue` statement, which jumps straight back to the top of the loop - here, skipping the running total's update whenever an invalid coin value is entered, so the next iteration just re-prompts
  - The augmented assignment operator `+=` to add each accepted coin onto the running total

  The script repeatedly prints how much is still due and asks for a coin (5, 10, or 25 cents), ignoring any other amount, until 50 cents has been inserted, then prints the change owed.

- **[Problem Set/twttr/twttr.py](Week%202/Problem%20Set/twttr/twttr.py)** - "twttr": strips every vowel out of a line of text, the way Twitter's early name dropped its vowels. Demonstrates:
  - Iterating over the *original* characters of a string with `for letter in input_text:`, even though `input_text` is reassigned inside the loop body - the loop already captured its sequence of characters before the first reassignment happened, the same behavior noted in `camel.py`
  - The `in` operator to test membership in a string: `letter.lower() in "aeiou"` checks whether a single character appears anywhere in the string `"aeiou"`
  - Calling `.lower()` only to *check* whether a letter is a vowel, while leaving the original-case `letter` untouched, so `.replace(letter, "")` removes the exact character (uppercase or lowercase) that was actually found
  - `.replace(letter, "")` removing every occurrence of that character from the current string in one call, not just the one at the current loop position

  The script asks for a line of text and prints it back with every vowel (`a`, `e`, `i`, `o`, `u`, in either case) removed - e.g. `"twitter"` becomes `"twttr"`.

## Getting Started

To run any of the Python files, use `python` followed by the path in quotes (the quotes matter because the folder names contain spaces):

```bash
python "Week 0/hello.py"
python "Week 0/calculator.py"
python "Week 0/Problem Set/Indoor Voice/indoor.py"
python "Week 0/Problem Set/playback/playback.py"
python "Week 0/Problem Set/faces/faces.py"
python "Week 0/Problem Set/einstein/einstein.py"
python "Week 0/Problem Set/tip/tip.py"
python "Week 1/compare.py"
python "Week 1/grade.py"
python "Week 1/house.py"
python "Week 1/parity.py"
python "Week 1/Problem Set/bank/bank.py"
python "Week 1/Problem Set/deep/deep.py"
python "Week 1/Problem Set/extensions/extensions.py"
python "Week 1/Problem Set/interpreter/interpreter.py"
python "Week 1/Problem Set/meal/meal.py"
python "Week 2/cat.py"
python "Week 2/hogwarts.py"
python "Week 2/mario.py"
python "Week 2/Problem Set/camel/camel.py"
python "Week 2/Problem Set/coke/coke.py"
python "Week 2/Problem Set/twttr/twttr.py"
```

- `hello.py` will prompt for your name and print a greeting.
- `calculator.py` will prompt for a number and print its square.
- `indoor.py` will prompt for a line of text and print it back in lowercase.
- `playback.py` will prompt for a line of text and print it back with spaces replaced by `"..."`.
- `faces.py` will prompt for a line of text and print it back with `:)` and `:(` replaced by emoji.
- `einstein.py` will prompt for a mass (in kg) and print the equivalent energy (in joules).
- `tip.py` will prompt for a meal cost and a tip percentage, then print how much tip to leave.
- `compare.py` will prompt for two numbers, `x` and `y`, and print whether `x` is equal to `y` or not.
- `grade.py` will prompt for a score and print the corresponding letter grade.
- `house.py` will prompt for a name and print the matching Hogwarts house, or `Who?` if it doesn't recognize the name.
- `parity.py` will prompt for a number and print whether it's `Even` or `Odd`.
- `bank.py` will prompt for a greeting and print `$0`, `$20`, or `$100` depending on how it starts.
- `deep.py` will prompt for the Answer to the Great Question of Life, the Universe, and Everything and print `Yes` or `No`.
- `extensions.py` will prompt for a filename and print its MIME type based on the extension.
- `interpreter.py` will prompt for an expression (e.g. `3 + 4`) and print the result.
- `meal.py` will prompt for a time (e.g. `7:30`) and print whether it's breakfast, lunch, or dinner time.
- `cat.py` will prompt for a positive number and print "meow" that many times.
- `hogwarts.py` will print each student's name, house, and patronus from a hardcoded list.
- `mario.py` will print a 3x3 square made of `#` characters.
- `camel.py` will prompt for a camelCase word or sentence and print it converted to snake_case.
- `coke.py` will repeatedly prompt for a coin (5, 10, or 25) until 50 cents has been inserted, then print the change owed.
- `twttr.py` will prompt for a line of text and print it back with every vowel removed.

## Learning Objectives

- Basic Python syntax and structure
- Defining and calling functions, including functions with default parameter values
- Input/output operations, including converting input strings to numbers
- Returning values from functions vs. printing directly
- Using built-in functions like `pow()`, and the equivalent `**` exponentiation operator
- Working with string methods like `.lower()` and `.replace()`, including chaining multiple method calls together
- Operator precedence in arithmetic expressions
- Converting strings to `float` values, and cleaning up input (stripping symbols like `$` and `%`) before converting it
- Formatting output with f-strings, including format specs like `:.2f` for two decimal places
- Comparison operators (`==`, `>=`) and branching with `if` / `elif` / `else`
- Structural pattern matching with `match` / `case`, including combining values with `|` and the `case _:` wildcard
- The modulo operator `%` and returning boolean expressions directly from a function
- String slicing (`[:5]`) and indexing (`[0]`) to inspect part of a string
- Ordering `if` / `elif` checks from most to least specific
- Tuple unpacking to split one string into several variables at once (`x, symb, y = expression.split(" ")`)
- Chained comparisons (`7 <= con_time <= 8`) as a shorthand for combining two bounds with `and`
- Splitting work between a `main()` function and helper functions, run via `if __name__ == "__main__":`
- Indexing from the end of a list with `list[len(list) - 1]` to handle inputs of varying length (e.g. filenames with extra dots)
- Input-validation loops with `while True:` and `break`, so invalid input is silently re-prompted instead of crashing the program
- Repeating an action a fixed number of times with `for _ in range(n):`, using `_` as a throwaway variable when the loop counter's value isn't needed
- List literals and looping over list indices with `for i in range(len(list)):`, then indexing with `list[i]` to access each item
- Lists of dictionaries for grouping several related values together, and looping directly over a list's items with `for item in list:` when position doesn't matter
- Indexing a dictionary by string key (`d["key"]`) instead of an integer position, and using `None` to represent a missing or absent value
- Customizing `print()`'s separator between multiple values with the `sep` keyword argument
- Splitting a task across multiple functions that call one another (e.g. `main()` -> `print_square()` -> `print_row()`), and building a repeated string with the `*` operator (`"#" * width`)
- Iterating directly over the characters of a string with `for letter in string:`, and checking a character's case with `.isupper()`
- Understanding that a `for` loop captures its sequence of items up front, so reassigning the variable it's looping over from inside the loop body doesn't change which items get visited next
- Writing a `while` loop whose condition depends on a running total that's updated inside the loop body
- Combining several equality checks with `or`, and using `continue` to skip the rest of a loop iteration and jump back to the condition
- The `in` operator for checking whether a value appears within a string (membership testing)
