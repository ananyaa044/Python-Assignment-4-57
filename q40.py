# 40. Demonstrate local variables in two functions with the same name.
def first_function():
    message = "Local to the first function"
    print(message)

def second_function():
    message = "Local to the second function"
    print(message)

first_function()
second_function()
