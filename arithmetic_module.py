"""Basic arithmetic functions used by q42.py."""

def add(first, second):
    return first + second

def subtract(first, second):
    return first - second

def multiply(first, second):
    return first * second

def divide(first, second):
    if second == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return first / second
