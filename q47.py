# 47. Use the random module to generate five random integers.
import random

for index in range(5):
    print(f"Random integer {index + 1}:", random.randint(1, 100))
