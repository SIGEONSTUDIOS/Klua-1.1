import time
import random
import webbrowser
import platform
import colorama
from colorama import Fore, Back, Style
from PIL import Image
import winsound
import os
import sys

#klua dependendents #todo start to create dependancys
#import var_storage status: exists but doesnt work
#import kprint ---- status: exists but doesnt work

os.chdir(os.path.dirname(os.path.abspath(__file__)))
colorama.init()

#todo removed modules = {} since not needed 
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

def make(name, value, debug): #variable creation #todo make it so debug_false isnt required
    try:
        if debug == "debug_true":
            if isinstance(value, bool):
                print("value is a boolean -DEBUG")
                print("var =",value, "name =",name, "-DEBUG")
                variables[name] = bool(value)
            elif isinstance(value, int):
                print("value is an integretor -DEBUG")
                print("var =",value, "name =",name, "-DEBUG")
                variables[name] = value
            elif isinstance(value, str):
                print("value is a string -DEBUG")
                print("var =",value, "name =",name, "-DEBUG")
                variables[name] = str(value)
        else:
            variables[name] = value
        return variables[name]
    except Exception as error:
        print("Klua Error:", error)

def kprint(text, debug): #output #todo make it so debug_false isnt required
    try:
        try:
            if debug == "debug_true":
                print("debug_true flag active -DEBUG")
                if isinstance(text, int):
                    print("text is an integretor -DEBUG")
                    if text in variables:
                        print("integretor is a var -DEBUG")
                        print(variables[text])
                    else:
                        print("integretor isnt a var -DEBUG",)
                        print(text)
                elif isinstance(text, str):
                    print("text is a string -DEBUG")
                    if text in variables:
                        print("string is an var -DEBUG")
                        print("var contains", variables[text], "-DEBUG")
                        print(variables[text])
                    else:
                        print("string isnt a var -DEBUG")
                        print(text)
            elif debug == "debug_false":
                if isinstance(text, int):
                    if text in variables:
                        print(variables[text])
                    else:
                        print(text)
                elif isinstance(text, str):
                    if text in variables:
                        print(variables[text])
                    else:
                        print(text)
        except Exception as error:
            print("klua error", error)
    except Exception as error:
        print("klua error", error)




        











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
        elif action == "processor":
            return platform.processor()
    except Exception as error:
        print("Klua Error:",error)







            
                
# WRITE CODE UNDER ME \/
