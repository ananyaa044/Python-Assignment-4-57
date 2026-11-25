# 34. Write a function that accepts a string and returns uppercase and lowercase character counts.
def count_case(text):
    uppercase = sum(1 for character in text if character.isupper())
    lowercase = sum(1 for character in text if character.islower())
    return uppercase, lowercase

upper_count, lower_count = count_case("Hello Python 3!")
print("Uppercase:", upper_count)
print("Lowercase:", lower_count)
