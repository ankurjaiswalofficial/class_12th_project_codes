file_name = input("Enter the file name: ")

try:
    with open(file_name, 'r') as file:
        print("File position:", file.tell())
        file.seek(10)  # Reset file position to byte 10
        print("File position after seeking:", file.tell())
except FileNotFoundError:
    print("File not found.")
