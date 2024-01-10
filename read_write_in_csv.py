import csv

# Read from CSV
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Write to CSV
data = [
    ['Name', 'Age'],
    ['Alice', 25],
    ['Bob', 30]
]

with open('new_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
