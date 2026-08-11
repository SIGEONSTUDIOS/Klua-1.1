# Klua-1.0 SDK

Klua is a Python-powered scripting language focused on simplicity, readability, and game development.

This SDK contains the built-in functions available in Klua.

support me by gifting something to me via my withlist i beg
https://store.steampowered.com/wishlist/profiles/76561199813570330/
---

# Variables

## `make(name, value)`

Creates a variable.

```text
make("score", 100)
make("name", "Ron")
make("playing", true)
```

Supported values include:

* `int` — numbers
* `str` — text
* `bool` — `true` or `false`

---

## `get(name, text)`

Gets input from the user and stores it in a variable.

```text
get("name", "What is your name? ")
```

`name` is the variable that stores the input.

`text` is the message shown to the user.

---

## `delete(name)`

Deletes a variable.

```text
delete("score")
```

If the variable does not exist, Klua returns:

```text
Klua Error: variable not found
```

---

## `found(name)`

Checks whether a variable exists.

```text
found("score")
```

Returns `true` if the variable exists and `false` if it does not.

---

## `clear()`

Deletes all currently stored variables.

```text
clear()
```

---

# Output

## `kprint(text)`

Prints text or the value of a variable.

```text
kprint("Hello World")
```

If a variable exists with that name:

```text
make("name", "Ron")
kprint("name")
```

Output:

```text
Ron
```

If the variable does not exist, Klua prints the text itself.

```text
kprint("Hello")
```

Output:

```text
Hello
```

---

# Input

## `get(name, text)`

Gets user input and stores it in `name`.

```text
get("username", "Enter your username: ")
kprint("username")
```

---

# Functions

## `do(name, code)`

Registers a Python function under a Klua name.

The Python function must already exist.

```python
def hello():
    print("Hello!")

do("hello", "hello")
```

The first `hello` is the Klua function name.

The second `hello` is the Python function name.

---

## `run(name)`

Runs a function registered with `do()`.

```text
run("hello")
```

If the function does not exist:

```text
Klua Error: Function not found
```

---

# Conditions

## `condition(condition)`

Evaluates a condition using the current Klua variables.

```text
make("score", 10)
condition("score == 10")
```

Variables can be used directly inside the condition.

For strings, quotes are required:

```text
make("name", "Ron")
condition("name == 'Ron'")
```

Currently, invalid Python expressions may produce a Python traceback instead of a Klua error.

---

# Math

## `math(operator, name, amount)`

Performs mathematical operations on an existing variable.

Currently supported operators:

* `"add"`
* `"minus"`

### Add

```text
make("score", 5)
math("add", "score", 5)
```

`score` is now:

```text
10
```

### Minus

```text
math("minus", "score", 3)
```

`score` is now:

```text
7
```

If the variable does not exist:

```text
Klua error: Variable not found
```

---

# Random

## `roll(name, min, max)`

Generates a random integer between `min` and `max` and stores it in `name`.

```text
roll("number", 1, 10)
kprint("number")
```

The result could be any integer from `1` to `10`.

Both `min` and `max` must be integers.

---

## `pick(name, options)`

Randomly chooses one item from a list and stores it in `name`.

```text
pick("weapon", ["sword", "bow", "axe"])
kprint("weapon")
```

Possible results:

```text
sword
bow
axe
```

`pick()` uses Python's `random.choice()` internally.

---

# Timing

## `wait(amount)`

Pauses the program for a specified number of seconds.

```text
wait(2)
```

This pauses execution for 2 seconds.

Currently supported:

* `int`

Floats are not currently supported.

Using a boolean or string produces a Klua error.

---

# Web

## `search(url)`

Opens a URL using the system's default web browser.

```text
search("https://example.com")
```

---

# Platform

## `PLT_show(action)`

Gets information about the current platform.

Currently supported actions:

### `system`

```text
PLT_show("system")
```

Returns the operating system.

Example:

```text
Windows
```

### `processor`

```text
PLT_show("processor")
```

Returns information about the system processor.

---

# Terminal Colors

Klua has Colorama built in.

Colorama is initialized automatically when the Klua runtime starts.

The following Colorama components are available internally:

```python
Fore
Back
Style
```

This allows Klua to support colored terminal output without requiring the user to manually install and initialize Colorama.

---

# Runtime Storage

Klua internally uses three dictionaries:

```python
modules = {}
variables = {}
functions = {}
```

### `variables`

Stores Klua variables.

### `functions`

Stores functions registered through `do()`.

### `modules`

Stores loaded Klua modules.

---

# Quick Reference

| Function      | Purpose                    |
| ------------- | -------------------------- |
| `make()`      | Create a variable          |
| `get()`       | Get user input             |
| `kprint()`    | Print output               |
| `do()`        | Register a function        |
| `run()`       | Run a function             |
| `condition()` | Evaluate a condition       |
| `math()`      | Add or subtract            |
| `wait()`      | Pause execution            |
| `roll()`      | Generate a random number   |
| `pick()`      | Randomly choose an option  |
| `delete()`    | Delete a variable          |
| `found()`     | Check if a variable exists |
| `clear()`     | Delete all variables       |
| `search()`    | Open a URL                 |
| `PLT_show()`  | Get platform information   |

---

# Example

A small Klua program can combine multiple SDK functions:

```text
make("score", 0)

get("name", "What is your name? ")

kprint("name")

math("add", "score", 10)

pick("reward", ["Sword", "Bow", "Axe"])

kprint("reward")
kprint("score")

wait(2)

delete("score")
```

Klua is designed to keep common programming tasks simple while still being powered by Python underneath.

7. 

