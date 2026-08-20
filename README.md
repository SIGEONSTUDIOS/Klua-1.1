
##FILES

Renderer.py beta
AudioEngine.py beta
klua.py stable v1.2


## I tried to access cpu temps
but its hard to code it
# Klua 1.1 SDK Documentation

## Introduction

Klua is a lightweight Python-powered scripting SDK designed for simplicity, readability, and rapid development. Klua 1.1 introduces improved debugging support, variable management, functions, conditions, randomization, and utility features.

---

# Variables

## Create a Variable

```python
make("username", "Player")
```

Supported types:

```python
make("name", "Steve")
make("health", 100)
make("alive", True)
```

## Get User Input

```python
get("name", "Enter your name: ")
```

Example:

```text
Enter your name: Steve
```

## Delete a Variable

```python
delete("name")
```

## Check if a Variable Exists

```python
found("name")
```

Returns:

```python
True
```

or

```python
False
```

## Clear All Variables

```python
clear()
```

---

# Output

## Print Text

```python
kprint("Hello World")
```

Output:

```text
Hello World
```

## Print a Variable

```python
make("coins", 50)
kprint("coins")
```

Output:

```text
50
```

---

# Functions

## Create a Function

```python
def hello():
    print("Hello!")

do("hello", hello)
```

## Run a Function

```python
run("hello")
```

Output:

```text
Hello!
```

---

# Conditions

## Evaluate a Condition

```python
make("money", 100)

if condition("'money' >= 50"):
    print("Purchase successful")
    you HAVE to put '' if its string
```

Output:

```text
Purchase successful
```

Examples:

```python
condition("health <= 0")
condition("coins > 100")
condition("name == 'Steve'")
condition("alive == True")
```

---

# Math

## Add

```python
make("score", 10)

math("add", "score", 5)
```

## Subtract

```python
math("minus", "score", 3)
```

---

# Waiting

## Pause Execution

```python
wait(5)
```

Pauses execution for 5 seconds.

---

# Random Numbers

## Roll a Random Number

```python
roll("dice", 1, 6)

kprint("dice")
```

Possible output:

```text
4
```

## Pick a Random Option

```python
pick("weapon", ["Sword", "Bow", "Gun"])

kprint("weapon")
```

Possible output:

```text
Bow
```

---

# Web Browser

## Open a Website

```python
search("https://github.com")
```

This opens the user's default web browser.

---

# Platform Information

## Operating System

```python
PLT_show("system")
```

Example output:

```text
Windows
```

## Processor

```python
PLT_show("processor")
```

---

# Debugging

Klua 1.1 includes debugging support for variable creation and output functions.

Enable debugging:

```python
make("health", 100, "debug_true")
kprint("health", "debug_true")
```

Disable debugging:

```python
make("health", 100, "debug_false")
kprint("health", "debug_false")
```

---

# Error Handling

Klua automatically catches many runtime errors and displays them as:

```text
Klua Error: <error message>
```

Example:

```python
delete("unknown_variable")
```

Output:

```text
Klua Error: variable not found
```

---

# Klua 1.1 Feature List

* Variables
* User Input
* Output System
* Functions
* Conditions
* Math Operations
* Wait System
* Random Numbers
* Random Selection
* Variable Management
* Web Browser Support
* Platform Information
* Debugging System
* Error Handling

---

Created by SIGEON STUDIOS

Version: Klua 1.1
