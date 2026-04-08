"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
def add(a, b): 
    pass
def add(a, b):
    a + b
def sub(a,b):
    a - b
def mul(a,b):
    a*b
def div(a,b):
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


