# 18. Write a function to check whether a number is prime.
def is_prime(number):
    if number < 2:
        return False
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False
    return True

number = 29
print(number, "is prime:", is_prime(number))
