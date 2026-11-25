# 50. Create a simple package with two modules and import functions from both modules.
from basic_package.greetings import greet
from basic_package.calculations import add

greet("Ananya")
print("Sum:", add(12, 8))
