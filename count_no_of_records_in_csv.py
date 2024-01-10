import csv

file_name = "student.csv"

try:
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        row_count = sum(1 for row in reader)
        print(f"Number of records in {file_name}: {row_count}")
except FileNotFoundError:
    print("File not found.")
