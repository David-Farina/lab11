"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
# First example
def square_root(a):
    try:
        return math.sqrt(a)
    except ValueError:
        print("Value cannot be < 0")
        return None

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b): 
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Cannot divide by 0")
        return None

def logarithm(a, b):
    try:
        return math.log(a, b)
    except Exception as e:
        print(e)
        return None

def exponent(a, b):
    return a ** b