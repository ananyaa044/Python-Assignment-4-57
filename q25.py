# 25. Write a function to find the length of a string without using len().
def string_length(text):
    count = 0
    for _ in text:
        count += 1
    return count

print("Length:", string_length("Hello, Python!"))
