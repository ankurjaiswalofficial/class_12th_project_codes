def is_palindrome(string):
    string = string.lower()
    left = 0
    right = len(string) - 1
    while right > left:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True

word = input("Enter a string: ")
if is_palindrome(word):
    print(word, "is a palindrome.")
else:
    print(word, "is not a palindrome.")
