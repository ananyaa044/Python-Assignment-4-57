# 28. Write a function to calculate simple interest using arguments and a return statement.
def simple_interest(principal, rate, time):
    return principal * rate * time / 100

print("Simple interest:", simple_interest(5000, 6, 2))
