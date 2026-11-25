# 32. Write a function to demonstrate variable-length arguments using *args.
def add_all(*args):
    return sum(args)

print("Sum:", add_all(2, 4, 6, 8))
