# 38. Demonstrate local and global variables having the same name.
value = "global value"

def show_values():
    value = "local value"
    print("Inside function:", value)

show_values()
print("Outside function:", value)
