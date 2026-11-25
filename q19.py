# 19. Write a function to check whether a string is a palindrome.
def is_palindrome(text):
    return text == text[::-1]

word = "level"
print(word, "is palindrome:", is_palindrome(word))
