def unique_vowels(word):
    vowels = set()
    stack = []

    for char in word.lower():
        if char in 'aeiou':
            if char not in vowels:
                vowels.add(char)
                stack.append(char)

    print("Unique vowels in the word:", ", ".join(stack[::-1]))

user_word = input("Enter a word: ")
unique_vowels(user_word)
