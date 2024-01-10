file_name = input("Enter the file name: ")

try:
    with open(file_name, 'r') as file:
        content = file.read()
        capitalized_content = content.capitalize()
    
    with open(file_name, 'w') as file:
        file.write(capitalized_content)
        print("First letter capitalized in the file.")
except FileNotFoundError:
    print("File not found.")
