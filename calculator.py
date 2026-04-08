import math
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
def square_root(a):
    try:
        return math.sqrt(a)
    except ValueError:
        raise ValueError("Value cannot be < 0")

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
        return a/b
    except ZeroDivisionError:
        raise ZeroDivisionError("Divisor cannot be 0")
    
def log(a,b):
    try:
        return math.log(b,a)
    except ValueError as e:
        print(e)
        raise ValueError("Argument must be positive")

def exp(a,b):
    return a**b



