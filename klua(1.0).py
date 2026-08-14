import time
import random
import webbrowser
import platform
import colorama
from colorama import Fore, Back, Style
colorama.init()

modules = {}
variables = {}
functions = {}

def do(name, code): 
    functions[name] = code

def run(name):
    if name in functions:
        functions[name]()
    else:
        print("Klua Error: Function not found")




def get(name, text): #input
    variables[name] = input(text)
    return variables[name]

def make(name, value): #variable creation
    try:
        if isinstance(value, bool):
            variables[name] = bool(value)
        elif isinstance(value, int):
            variables[name] = value
        elif isinstance(value, str):
            variables[name] = str(value)
        else:
            variables[name] = value
        return variables[name]
    except Exception as error:
        print("Klua Error:", error)

def kprint(text): #output
    try:
        if isinstance(text, int):
            print(text)
        elif text in variables:
            print(variables[text])
        else:
            print(text)
    except Exception as error:
        print("Klua Error:", error)


    except Exception as error:
        print("Klua Error:", error)


def condition(condition): #conditions
    return eval(condition, {}, variables)


def math(operator, name, amount): #math
    try:
        if operator == "add":
            if name in variables:
                variables[name] += amount
                return variables[name]
            else:
                print("Klua error: Variable not found")
        elif operator == "minus":
            if name in variables:
                variables[name] -= amount
                return variables[name]
            else:
                print("Klua error: Variable not found")
    except Exception as error:
        print("Klua error:", error)


def wait(amount): #waiting
    try:
        if isinstance(amount, bool):
            print("Klua error: amount must be a number not a boolean")
        elif isinstance(amount, int):
            time.sleep(amount)
        elif isinstance(amount, str):
            print("Klua error: amount must be a number not a string")
        elif isinstance(amount, float):
            print("Klua Warning: we dont support floats yet!")
    except Exception as error:
        print("Klua error:",error)


def roll(name, min, max):
    try:
        if isinstance(min, int) and isinstance(max, int):
            variables[name] = random.randint(min, max)
            return variables[name]
        else:
            print("Klua error: min and max must be numbers")
    except Exception as error:
        print("Klua error:", error)

def pick(name, options):
    variables[name] = random.choice(options)

def delete(name):
    try:
        if name in variables:
            del variables[name]
        else:
            print("Klua Error: variable not found")
    except Exception as error:
        print("Klua Error:", error)

def found(name):
    try:
        return name in variables
    except Exception as error:
        print("Klua Error:", error)

def clear():
    variables.clear()

def search(url):
    try:
        webbrowser.open(url)
    except Exception as error:
        print("Klua error:",error)

def PLT_show(action):
    try:
        if action == "system":
            return platform.system()
        elif action == "procceser":
            return platform.processor()
    except Exception as error:
        print("Klua Error:",error)


                
# WRITE CODE UNDER ME \/
