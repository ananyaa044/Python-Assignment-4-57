# 22. Write a function to find the largest element in a list.
def largest(numbers):
    if not numbers:
        raise ValueError("The list must not be empty")
    return max(numbers)

print("Largest:", largest([8, 34, 12, 19]))
