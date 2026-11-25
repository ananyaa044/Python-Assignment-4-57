# 14. Write a function to find the square and cube of a given number.
def square_and_cube(number):
    return number ** 2, number ** 3

square, cube = square_and_cube(4)
print("Square:", square)
print("Cube:", cube)
