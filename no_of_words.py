file_name = input("Enter the file name: ")

try:
    with open(file_name, 'r') as file:
        content = file.read()
        words = content.split()
        word_count = len(words)
        print("Number of words in the file:", word_count)
except FileNotFoundError:
    print("File not found.")
