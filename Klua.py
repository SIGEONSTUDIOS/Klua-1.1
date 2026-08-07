import time


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
            variables[name] = int(value)
        else:
            variables[name] = value
        return variables[name]
    except Exception as error:
        print("Klua Error:", error)


def kprint(text): #output
    try:
        if text in variables:
            print(variables[text])
        else:
            print(text)
    except Exception as error:
        print("Klua Error:", error)
        

def condition(condition): #conditions
    return eval(condition, {}, variables)


def math(operator, name, amount): #math
    try:
        if operator == "add":
            if name in variables:
                variables[name] += amount
            else:
                print("Klua error: Variable not found")
        elif operator == "minus":
            if name in variables:
                variables[name] -= amount
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
    except Exception as error:
        print("Klua error:",error)

