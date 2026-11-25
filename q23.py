# 23. Write a function to calculate the average of a list of numbers.
def average(numbers):
    if not numbers:
        raise ValueError("The list must not be empty")
    return sum(numbers) / len(numbers)

print("Average:", average([10, 20, 30, 40]))
