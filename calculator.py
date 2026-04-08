"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
# First example
def add(a, b): 
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        a/b
    except ZeroDivisionError:
        raise ZeroDivisionError
def log(a,b):
    try:
        return math.log(b,a)
    except ValueError:
        raise ValueError

def exp(a,b):
    return a**b







