file_name = input("Enter the file name: ")

try:
    with open(file_name, 'r') as file:
        content = file.read()
        vowel_count = sum(1 for char in content if char.lower() in 'aeiou')
        print("Number of vowels in the file:", vowel_count)
except FileNotFoundError:
    print("File not found.")
