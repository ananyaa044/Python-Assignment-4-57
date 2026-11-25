# 39. Modify a global variable inside a function using the global keyword.
count = 10

def increase_count():
    global count
    count += 1

increase_count()
print("Updated global count:", count)
