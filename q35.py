# 35. Write a function that returns both the sum and product of two numbers.
def sum_and_product(first, second):
    return first + second, first * second

total, product = sum_and_product(6, 7)
print("Sum:", total)
print("Product:", product)
