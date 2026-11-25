# 21. Write a function to calculate the sum of digits of a number.
def sum_of_digits(number):
    return sum(int(digit) for digit in str(abs(number)))

print("Sum of digits:", sum_of_digits(4827))
