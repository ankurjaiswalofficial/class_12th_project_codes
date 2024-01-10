char = input("Enter a character: ")

if char.isalpha():
    print(char, "is an alphabet.")
elif char.isdigit():
    print(char, "is a digit.")
else:
    print(char, "is another character.")
