# 33. Write a function that accepts a list as an argument and returns its largest element.
def largest_item(items):
    if not items:
        raise ValueError("The list must not be empty")
    return max(items)

print("Largest:", largest_item([3, 17, 9, 25]))
