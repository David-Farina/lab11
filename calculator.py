import math
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
<<<<<<< HEAD
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
=======
def add(a, b):
    a + b
def sub(a,b):
    a - b
def mul(a,b):
    a*b
def div(a,b):
>>>>>>> e7c027bd18dc87710a7f03a9f2395c473b28af66
    try:
        a/b
    except ZeroDivisionError:
        raise ZeroDivisionError
def log(a,b):
    try:
        math.log(b,a)
    except ValueError:
        raise ValueError

def exp(a,b):
    a**b



