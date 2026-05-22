def is_palindrome(text):
    new_text = text.replace(" ", "").lower()
    return new_text == new_text[::-1]

word = input("Enter a word or phrase: ")

if is_palindrome(word):
    print("Palindrome")
else:
    print("Not a palindrome")
