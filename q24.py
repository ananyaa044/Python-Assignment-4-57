# 24. Write a function to count vowels in a given string.
def count_vowels(text):
    return sum(1 for character in text.lower() if character in "aeiou")

print("Vowel count:", count_vowels("Programming is fun"))
