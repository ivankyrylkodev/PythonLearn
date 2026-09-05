# First Steps in Python

A structured learning path through Python fundamentals: hands-on exercises organized by week.

## Project Structure

### Week 0 - Introduction & Basics

Functions, input/output, and basic arithmetic.

- **[hello.py](Week%200/hello.py)** - Greeting program. Demonstrates `def`, `input()`, a default parameter (`def hello(to="world")`), passing a variable between functions, and printing multiple values with a comma. Asks for a name and greets it; `main()` is defined first but called last, so the file reads top-down while still working (Python only needs a function to exist by the time it's called).

- **[calculator.py](Week%200/calculator.py)** - Squares a number. Demonstrates `int()` conversion (since `input()` returns text), a function that takes a parameter and returns a value, `pow()`, and passing one function's result into another. Asks for a number and prints its square.

#### Problem Set 0

- **[Problem Set/Indoor Voice/indoor.py](Week%200/Problem%20Set/Indoor%20Voice/indoor.py)** - "Indoor Voice". Demonstrates `input()` and `.lower()`, chained directly into `print()` with no intermediate variable. Prints a line of text back in lowercase.

- **[Problem Set/playback/playback.py](Week%200/Problem%20Set/playback/playback.py)** - "Playback". Demonstrates `.replace(old, new)`, here replacing every space so words are separated by `"..."`. Turns "hello there" into "hello...there".

- **[Problem Set/faces/faces.py](Week%200/Problem%20Set/faces/faces.py)** - "Faces". Demonstrates chaining two `.replace()` calls back-to-back, and emoji as string literals. Swaps every `:)` for 🙂 and `:(` for 🙁.

- **[Problem Set/einstein/einstein.py](Week%200/Problem%20Set/einstein/einstein.py)** - "Einstein" (E = mc²). Demonstrates `int()` used inline inside a larger expression, the `**` operator, and operator precedence (`**` binds tighter than `*`, so the speed of light is squared before multiplying by mass). Prints energy in joules from a mass in kg.

- **[Problem Set/tip/tip.py](Week%200/Problem%20Set/tip/tip.py)** - "Tip Calculator". Demonstrates helper functions that clean input before converting (`dollars_to_float()` strips `$`, `percent_to_float()` strips `%` and divides by 100), passing a raw string straight into a helper, and f-strings with a format spec (`f"Leave ${tip:.2f}"`). Asks for a meal cost and tip percent, prints the tip owed.

### Week 1 - Conditionals

Branching with `if`, `elif`, and `else`.

- **[compare.py](Week%201/compare.py)** - Demonstrates `int(input(...))`, `==`, and `if`/`else`. Prints whether two numbers are equal.

- **[grade.py](Week%201/grade.py)** - Demonstrates `>=` and an `if`/`elif`/`elif`/`elif`/`else` chain, where each branch only needs to rule out the next threshold down since conditions run top to bottom. Prints a letter grade (A 90+, B 80-89, C 70-79, D 60-69, F below 60).

- **[parity.py](Week%201/parity.py)** - Demonstrates returning a boolean expression directly (`return (n % 2 == 0)`), the modulo operator `%`, and using a function's return value as an `if` condition. Prints `Even` or `Odd`.

- **[house.py](Week%201/house.py)** - Hogwarts sorter. Demonstrates `match`/`case`, matching multiple values with `|` (`case "Harry" | "Hermione" | "Ron":`), and the `case _:` wildcard (match's version of `else`). Prints a house name or `Who?`.

#### Problem Set 1

- **[Problem Set/bank/bank.py](Week%201/Problem%20Set/bank/bank.py)** - "Bank". Demonstrates chaining `.lower().strip()`, slicing (`[:5]`), indexing (`[0]`), and ordering `if`/`elif`/`else` from more to less specific. Prints `$0` for a greeting starting "hello", `$20` for just "h", `$100` otherwise.

- **[Problem Set/deep/deep.py](Week%201/Problem%20Set/deep/deep.py)** - "Deep Thought". Demonstrates `.lower()` on input, and `match`/`case` matching several spellings ("42", "forty-two", "forty two") with `|`. Prints `Yes` for any form of 42, else `No`.

- **[Problem Set/extensions/extensions.py](Week%201/Problem%20Set/extensions/extensions.py)** - "File Extensions". Demonstrates chaining `.strip().lower().split(".")`, grabbing the last list element with `file[len(file) - 1]` (so extra dots in a filename don't break it), and `match`/`case` with `|` and a `case _:` fallback. Prints the MIME type for a filename's extension, or `application/octet-stream`.

- **[Problem Set/interpreter/interpreter.py](Week%201/Problem%20Set/interpreter/interpreter.py)** - "Interpreter". Demonstrates tuple unpacking (`x, symb, y = expression.split(" ")`), `match`/`case` on an operator symbol, converting operands to `float()` per case, and `case _:`. Evaluates `3 + 4`-style expressions, or prints `Unknown operation`.

- **[Problem Set/meal/meal.py](Week%201/Problem%20Set/meal/meal.py)** - "Meal Time". Demonstrates splitting work between `main()` and a `convert()` helper via `if __name__ == "__main__":`, converting `"HH:MM"` to a fractional hour, chained comparisons (`7 <= con_time <= 8`), and an `if`/`elif` chain with no `else` (prints nothing if no window matches). Prints `breakfast time`, `lunch time`, or `dinner time`.

### Week 2 - Loops

Repeating work with `while` and `for`.

- **[cat.py](Week%202/cat.py)** - Demonstrates an input-validation loop (`while True:` plus `break`), splitting work across `main()`/`get_number()`/`meow()`, and `for _ in range(n):` with `_` as a throwaway variable. Prints "meow" `n` times, re-prompting until `n > 0`.

- **[hogwarts.py](Week%202/hogwarts.py)** - Demonstrates a list of dictionaries, looping directly over items (not indices) with `for student in students:`, string-key dictionary indexing, the `sep` argument to `print()`, and `None` for missing data. Prints each student's name, house, and patronus.

- **[mario.py](Week%202/mario.py)** - Demonstrates splitting logic across `main()`/`print_square(size)`/`print_row(width)`, `for i in range(size):` with an unused loop variable, and the string repetition operator (`"#" * width`). Prints a 3x3 square of `#`.

#### Problem Set 2

- **[Problem Set/camel/camel.py](Week%202/Problem%20Set/camel/camel.py)** - "camelCase" to snake_case. Demonstrates iterating over string characters directly, `.isupper()`, and that a `for` loop captures its sequence up front - reassigning the loop variable (`words`) inside the loop doesn't change what gets visited next. Turns `helloWorld` into `hello_world`.

- **[Problem Set/coke/coke.py](Week%202/Problem%20Set/coke/coke.py)** - "Vending Machine". Demonstrates a `while` loop driven by a running total, combining equality checks with `or`, `continue` to skip an invalid coin's update, and `+=`. Accepts 5/10/25-cent coins until 50 cents is reached, then prints change owed.

- **[Problem Set/nutrition/nutrition.py](Week%202/Problem%20Set/nutrition/nutrition.py)** - "Nutrition Facts". Demonstrates a list of dictionaries as a lookup table, looping over items to compare a key, `break` on match, and nested double-quoted f-string keys (`f"Calories: {fruit["calories"]}"`, Python 3.12+). Prints a fruit's calories, or nothing if not found.

- **[Problem Set/plates/plates.py](Week%202/Problem%20Set/plates/plates.py)** - "Vanity Plates". Demonstrates looping over indices with `range(len(s))` to compare neighboring characters, `.isnumeric()`, and a negative-indexing quirk: on `i == 0`, `s[i-1]` becomes `s[-1]` (the last character), so the first comparison unintentionally checks first against last. Also layers independent rules that each `return False` immediately, with `return True` only at the end. Prints `Valid`/`Invalid` per DMV-style plate rules.

- **[Problem Set/twttr/twttr.py](Week%202/Problem%20Set/twttr/twttr.py)** - "twttr". Demonstrates iterating over a string's original characters even after it's reassigned mid-loop (same captured-sequence behavior as `camel.py`), the `in` membership operator, and checking `.lower()` while replacing the original-case character. Strips vowels: `"twitter"` becomes `"twttr"`.

### Week 3 - Exceptions

Handling errors with `try`/`except` instead of crashing.

- **[hello.py](Week%203/hello.py)** - Simplest possible program: prints `hello, world`.

- **[number.py](Week%203/number.py)** - Demonstrates a `get_int(prompt)` helper, wrapping a risky conversion in `try`, catching a specific type with `except ValueError:`, returning from inside `try` to both produce a value and exit a `while True:` loop, and `except ValueError: pass` to silently re-prompt. Keeps asking until a valid integer is entered, then prints it.

#### Problem Set 3

- **[Problem Set/fuel/fuel.py](Week%203/Problem%20Set/fuel/fuel.py)** - "Fuel Gauge". Demonstrates tuple unpacking a split fraction (`x, y = input(...).split("/")`), validating with a chained `or` and `pass` inside a `try`, catching two exception types at once (`except (ValueError, ZeroDivisionError):`), and truncating a division to a whole-number percentage. Prints `E` (≤1%), `F` (≥99%), or a percentage.

- **[Problem Set/grocery/grocery.py](Week%203/Problem%20Set/grocery/grocery.py)** - "Grocery List". Demonstrates a dictionary used as a counter (increment or initialize on `if item in groc:`), catching `EOFError` (raised when `input()` has no more data, e.g. Ctrl+D) as the loop's only exit, `.strip().upper()` normalization, and `sorted()` for alphabetical output. Tallies items typed until end-of-input, e.g. `2 APPLE`.

- **[Problem Set/outdated/outdated.py](Week%203/Problem%20Set/outdated/outdated.py)** - "Outdated" date converter. Demonstrates a month-name list used both to validate and, via `.index()`, convert to a number; branching on `"/" in user_date`; tuple unpacking twice over for each format; a shared day-count validity check (treats February as always 28 days, so `2/29/2024` is rejected even in a leap year); and zero-padding with `:02`. Converts `8/1/2023` or `August 1, 2023` to `2023-08-01`.

- **[Problem Set/taqueria/taqueria.py](Week%203/Problem%20Set/taqueria/taqueria.py)** - "Taqueria" order total. Demonstrates a dictionary as a price lookup table, `.strip().title()` to match case-sensitive keys, letting a missing key raise `KeyError` naturally instead of checking membership first, `except KeyError: pass` to ignore unknown items, and `except EOFError: break`. Prints a running total after each valid item until input ends.

### Week 4 - Libraries

Using Python's standard library and command-line arguments instead of writing everything from scratch.

- **[average.py](Week%204/average.py)** - Demonstrates `import statistics` and `statistics.mean()`. Prints the average of `[100, 90]`.

- **[generate.py](Week%204/generate.py)** - Demonstrates `import random` and `random.shuffle()`, which shuffles a list in place (no return value) rather than returning a new one. Shuffles `["jack", "queen", "king"]` and prints them in random order.

- **[name.py](Week%204/name.py)** - Demonstrates `import sys` and `sys.argv` for command-line arguments, `sys.exit(message)` as a one-line "print and quit" for the missing-argument case, and slicing `sys.argv[1:-1]` to loop over multiple names - note this drops the *last* argument, so `python name.py David` (only one name) prints nothing, while `python name.py David Alice` greets only David. Run with one or more names; with none, prints `Too few arguments` and exits.

- **[itunes.py](Week%204/itunes.py)** - "iTunes Search". Demonstrates a third-party package (`import requests`, installed via `pip install requests` - unlike `statistics`/`random`/`sys`, which ship with Python) used to call a web API, building a URL by string concatenation with `sys.argv[1]`, `response.json()` to parse the JSON response body, and looping over a list of dicts (`o["results"]`) to pull one field (`trackName`) out of each. Exits silently (`sys.exit()` with no message) unless given exactly one argument. Run as `python itunes.py "Taylor Swift"` to print matching track names from the iTunes Search API.

- **[sayings.py](Week%204/sayings.py)** - Demonstrates a module written to be imported rather than run directly: plain `hello()`/`goodbye()` helper functions plus a `main()` guarded by `if __name__ == "__main__":`, so running this file directly calls both, while importing it elsewhere (as `say.py` does) runs neither automatically. Run directly, prints `hello, world` and `goodbye, world`.

- **[say.py](Week%204/say.py)** - Demonstrates importing one specific name out of a local module (`from sayings import goodbye`) rather than the whole module, and `sys.argv` for a single command-line argument. Run as `python say.py David` to print `goodbye, David`.

#### Problem Set 4

- **[Problem Set/emojize/emojize.py](Week%204/Problem%20Set/emojize/emojize.py)** - "Emojize". Demonstrates a third-party package beyond `requests` (`import emoji`, installed via `pip install emoji`), and `emoji.emojize(text, language="alias")` to convert a `:shorthand:` code into its emoji character. Prompts for text like `:thumbs_up:` and prints the emoji it represents.

- **[Problem Set/adieu/adieu.py](Week%204/Problem%20Set/adieu/adieu.py)** - "Adieu, Adieu". Demonstrates the third-party `inflect` package (`pip install inflect`), building an `inflect.engine()` once and reusing it, collecting values into a list inside a `try`/`except EOFError:` loop, and `p.join(names)` to grammatically join a list with commas and "and" (handles 0, 1, 2, or many names correctly, unlike manual `", ".join()`). Reads names until Ctrl+D, then prints `Adieu, adieu, to ...` followed by the joined list.

- **[Problem Set/figlet/figlet.py](Week%204/Problem%20Set/figlet/figlet.py)** - "Figlet". Demonstrates the third-party `pyfiglet` package (`pip install pyfiglet`), branching on `len(sys.argv)` to support both a zero-argument and a `-f`/`-font FONT`-flagged form, validating the flag name and that the requested font is a member of `pyfiglet.Figlet().getFonts()` before using it, `random.choice()` to pick a font when none is specified, and `sys.exit("Invalid usage")` for malformed arguments. Prints the input text as ASCII art in the chosen (or random) font.

- **[Problem Set/bitcoin/bitcoin.py](Week%204/Problem%20Set/bitcoin/bitcoin.py)** - "Bitcoin Price". Demonstrates calling a live REST API with `requests.get()`, pulling a nested field out of the response (`o["data"]["priceUsd"]`), multiplying it by a command-line argument, and formatting the result with both a thousands separator and four decimal places (`f"${result:,.4f}"`). Also demonstrates catching `requests.RequestException` (network/API failures) separately from `ValueError` (a non-numeric argument) - note the file also does `import json` but never uses it, since `response.json()` is a method `requests` provides, not the `json` module. Run as `python bitcoin.py 1.5` to print the current USD value of 1.5 bitcoin.

- **[Problem Set/game/game.py](Week%204/Problem%20Set/game/game.py)** - "Guess the Number". Demonstrates two separate input-validation loops built the same way (`while True:` + `try`/`except ValueError:`, with `raise ValueError` used to manually reject an in-range-but-invalid number like a negative level) but exited two different ways - `break` once a valid level is read, `continue` to silently re-prompt after an invalid guess. Picks a random integer from 1 to the chosen level with `random.randint()`, then loops on guesses printing `Too small!`/`Too large!` until the guess matches, then `Just right!`.

- **[Problem Set/professor/professor.py](Week%204/Problem%20Set/professor/professor.py)** - "Little Professor". Demonstrates splitting work across `main()`, `get_level()`, and `generate_integer(level)`; scaling the difficulty of two random addends by level by using it as an exponent (`random.randint(1, 10 ** level)`); a nested `for i in range(3):` giving three attempts per question; `print(..., end="")` to keep the running `a + b = ` prompt on one line across retries; and checking `i == 2` to reveal the correct answer only after the final wrong attempt. Asks ten addition questions and prints a score out of 10, printing `EEE` for each wrong or non-numeric answer.

### Week 5 - Unit Testing

Testing code with `pytest` instead of only checking it by eye.

- **[calculator.py](Week%205/calculator.py)** - Same `square()` program as [Week 0's calculator.py](Week%200/calculator.py), moved here so it has something to be tested against. Demonstrates nothing new by itself - the point is what's tested alongside it.

- **[test_calculator.py](Week%205/test_calculator.py)** - Demonstrates a `pytest` test file: importing a function to test with `from calculator import square` (rather than running `calculator.py` directly), naming a test function `test_square` so `pytest` discovers it automatically, and `assert` statements checking several cases in one test (a positive number, a negative number, and zero) to confirm squaring works and that a negative input still returns a positive result. Run with `pytest test_calculator.py` from inside `Week 5/`; no output means every `assert` passed.

## Getting Started

Run any file with `python` and its quoted path (folder names contain spaces):

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
python "Week 2/Problem Set/nutrition/nutrition.py"
python "Week 2/Problem Set/plates/plates.py"
python "Week 2/Problem Set/twttr/twttr.py"
python "Week 3/hello.py"
python "Week 3/number.py"
python "Week 3/Problem Set/fuel/fuel.py"
python "Week 3/Problem Set/grocery/grocery.py"
python "Week 3/Problem Set/outdated/outdated.py"
python "Week 3/Problem Set/taqueria/taqueria.py"
python "Week 4/average.py"
python "Week 4/generate.py"
python "Week 4/name.py" David
python "Week 4/itunes.py" "Taylor Swift"
python "Week 4/sayings.py"
python "Week 4/say.py" David
python "Week 4/Problem Set/emojize/emojize.py"
python "Week 4/Problem Set/adieu/adieu.py"
python "Week 4/Problem Set/figlet/figlet.py"
python "Week 4/Problem Set/bitcoin/bitcoin.py" 1.5
python "Week 4/Problem Set/game/game.py"
python "Week 4/Problem Set/professor/professor.py"
python "Week 5/calculator.py"
```

`test_calculator.py` needs `pytest` installed first: `pip install pytest`. Run it (from inside `Week 5/`, since it imports `calculator` by module name) with:

```bash
cd "Week 5"
pytest test_calculator.py
```

`itunes.py` and `bitcoin.py` need `requests` installed first: `pip install requests`. `emojize.py` needs `emoji` installed first: `pip install emoji`. `adieu.py` needs `inflect` installed first: `pip install inflect`. `figlet.py` needs `pyfiglet` installed first: `pip install pyfiglet`.

- `hello.py` (Week 0) - prompts for a name, prints a greeting.
- `calculator.py` - prompts for a number, prints its square.
- `indoor.py` - lowercases a line of text.
- `playback.py` - replaces spaces with `"..."`.
- `faces.py` - replaces `:)`/`:(` with emoji.
- `einstein.py` - mass (kg) to energy (joules).
- `tip.py` - meal cost + tip % to tip owed.
- `compare.py` - are `x` and `y` equal?
- `grade.py` - score to letter grade.
- `house.py` - name to Hogwarts house, or `Who?`.
- `parity.py` - `Even` or `Odd`.
- `bank.py` - greeting to `$0`/`$20`/`$100`.
- `deep.py` - is the answer 42? `Yes`/`No`.
- `extensions.py` - filename to MIME type.
- `interpreter.py` - evaluates `3 + 4`-style expressions.
- `meal.py` - time to breakfast/lunch/dinner.
- `cat.py` - prints "meow" `n` times.
- `hogwarts.py` - prints the student roster.
- `mario.py` - prints a 3x3 `#` square.
- `camel.py` - camelCase to snake_case.
- `coke.py` - accepts coins, prints change owed.
- `nutrition.py` - fruit to calorie count.
- `plates.py` - `Valid`/`Invalid` license plate.
- `twttr.py` - strips vowels from text.
- `hello.py` (Week 3) - prints `hello, world`.
- `number.py` - re-prompts until a valid integer, then prints it.
- `fuel.py` - fraction to `E`/`F`/percentage.
- `grocery.py` - tallies items until Ctrl+D.
- `outdated.py` - date to `YYYY-MM-DD`.
- `taqueria.py` - running order total until Ctrl+D.
- `average.py` - prints the average of `[100, 90]`.
- `generate.py` - shuffles and prints three cards.
- `name.py` - greets names passed as command-line arguments (drops the last one - see note above).
- `itunes.py` - prints iTunes song titles matching a search term.
- `sayings.py` - prints `hello, world` and `goodbye, world` when run directly.
- `say.py` - prints `goodbye, <name>` for a name passed as a command-line argument.
- `emojize.py` - converts a `:shorthand:` code (e.g. `:thumbs_up:`) to its emoji.
- `adieu.py` - farewells a list of names typed until Ctrl+D.
- `figlet.py` - prints input text as ASCII art, in a chosen or random font.
- `bitcoin.py` - USD value of a bitcoin amount, via a live price API.
- `game.py` - number-guessing game at a player-chosen difficulty.
- `professor.py` - "Little Professor" addition quiz, three tries per question, score out of 10.
- `calculator.py` (Week 5) - prompts for a number, prints its square (same as Week 0's, kept here for `test_calculator.py` to test).
- `test_calculator.py` - `pytest` test suite for `square()`; run with `pytest`, prints nothing on success.

## Learning Objectives

- Basic syntax, functions (`def`), default parameters, and I/O with `input()`/`print()`
- Converting input strings to `int`/`float`, and returning vs. printing values
- `pow()` and `**`, and operator precedence
- String methods (`.lower()`, `.replace()`, `.strip()`, `.upper()`, `.title()`, `.isupper()`, `.isnumeric()`) and chaining them
- Cleaning input (stripping symbols) before conversion; f-strings and format specs (`:.2f`, `:02`)
- Comparison operators and `if`/`elif`/`else`, ordered most- to least-specific
- `match`/`case`, combining values with `|`, and the `case _:` wildcard
- Modulo (`%`), boolean expressions returned directly, string slicing/indexing (`[:5]`, `[0]`, `[-1]`)
- Tuple unpacking (`x, y = s.split(...)`) and chained comparisons (`a <= x <= b`)
- `main()` plus helpers, run via `if __name__ == "__main__":`
- Input-validation loops (`while True:` + `break`), and `for _ in range(n):` with `_` as a throwaway variable
- Looping over list/string items vs. indices; `list[len(list) - 1]` and `range(len(s))` for neighbor comparisons
- Lists of dictionaries and dictionaries as flat lookup tables/counters; string-key indexing and `None` for missing data
- `print()`'s `sep` argument; building repeated strings with `*`
- A `for` loop capturing its sequence up front, so reassigning the loop variable mid-loop doesn't change iteration
- Running totals with `+=`; combining checks with `or`; `continue` vs. `break`
- Nested double-quoted f-string keys (Python 3.12+); the `in` membership operator
- Negative-indexing pitfalls (`s[-1]`) from unguarded first iterations
- Chaining independent validity rules that each `return False` immediately
- `try`/`except`, catching specific/multiple exception types (`except (A, B):`), and `except ...: pass` to silently retry
- `EOFError` for end-of-input as a loop's exit condition; `KeyError` from a missing dict key driving control flow instead of a membership check first
- Reusing a list to both validate membership and convert via `.index()`
- Importing standard library modules (`import statistics`, `import random`, `import sys`) instead of hand-rolling functionality
- In-place mutation (`random.shuffle()`) vs. functions that return a new value
- Command-line arguments via `sys.argv`, slicing `sys.argv[1:-1]` to loop over several, and `sys.exit(message)` to print and quit in one line
- Third-party packages (`pip install requests`) vs. the standard library
- Calling a web API with `requests.get()` and parsing the JSON response with `response.json()`
- Writing a module meant to be imported (`sayings.py`), guarding its demo code with `if __name__ == "__main__":` so importing it doesn't run that code
- Importing one specific name from a local module (`from sayings import goodbye`) instead of the whole module
- Grammatically joining a list of varying length with `inflect.engine().join()` instead of manual comma-handling
- Branching on `len(sys.argv)` to support multiple valid call forms, validating a flag plus its value against an allowed set, and `random.choice()` to pick from a list
- Catching a library-specific exception (`requests.RequestException`) separately from a built-in one (`ValueError`), and formatting numbers with a thousands separator (`:,.4f`)
- `raise`-ing an exception manually so an existing `except` block also catches an otherwise-valid value that fails an extra check (e.g. a negative number)
- Retrying a fixed number of attempts with a nested `for i in range(3):`, using `end=""` to build a prompt across retries and revealing an answer only after the last attempt
- Writing automated tests with `pytest`: importing the function under test, naming test functions `test_*` for auto-discovery, and `assert` to check several cases (including edge cases like `0` and negative numbers) in one test
