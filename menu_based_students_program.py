import pickle

def insert_record():
    try:
        roll_number = int(input("Enter roll number: "))
        name = input("Enter name: ")
        marks = float(input("Enter marks: "))

        with open('students_data.bin', 'ab') as file:
            data = {'roll_number': roll_number, 'name': name, 'marks': marks}
            pickle.dump(data, file)
            print("Record inserted successfully.")
    except ValueError:
        print("Invalid input. Roll number should be integer and marks should be a float.")

def read_record():
    try:
        with open('students_data.bin', 'rb') as file:
            while True:
                try:
                    data = pickle.load(file)
                    print("Roll Number:", data['roll_number'])
                    print("Name:", data['name'])
                    print("Marks:", data['marks'])
                    print()
                except EOFError:
                    break
    except FileNotFoundError:
        print("File not found.")

def update_record():
    try:
        roll_number = int(input("Enter roll number to update: "))
        new_marks = float(input("Enter new marks: "))
        updated = False

        with open('students_data.bin', 'rb+') as file:
            while True:
                try:
                    pos = file.tell()
                    data = pickle.load(file)
                    if data['roll_number'] == roll_number:
                        data['marks'] = new_marks
                        file.seek(pos)
                        pickle.dump(data, file)
                        print("Marks updated successfully.")
                        updated = True
                        break
                except EOFError:
                    break
            
        if not updated:
            print("Roll number not found.")
    except ValueError:
        print("Invalid input. Roll number should be integer and marks should be a float.")

def search_record():
    try:
        roll_number = int(input("Enter roll number to search: "))
        found = False

        with open('students_data.bin', 'rb') as file:
            while True:
                try:
                    data = pickle.load(file)
                    if data['roll_number'] == roll_number:
                        print("Roll Number:", data['roll_number'])
                        print("Name:", data['name'])
                        print("Marks:", data['marks'])
                        print()
                        found = True
                        break
                except EOFError:
                    break

        if not found:
            print("Roll number not found.")
    except ValueError:
        print("Invalid input. Roll number should be integer.")

def delete_record():
    try:
        roll_number = int(input("Enter roll number to delete: "))
        deleted = False

        with open('students_data.bin', 'rb') as file:
            temp_data = []
            try:
                while True:
                    data = pickle.load(file)
                    if data['roll_number'] != roll_number:
                        temp_data.append(data)
                    else:
                        deleted = True
            except EOFError:
                pass

        if deleted:
            with open('students_data.bin', 'wb') as file:
                for data in temp_data:
                    pickle.dump(data, file)
            print("Record deleted successfully.")
        else:
            print("Roll number not found.")
    except ValueError:
        print("Invalid input. Roll number should be integer.")

while True:
    print("\nMenu:")
    print("1. Insert a record")
    print("2. Read a record")
    print("3. Update a record")
    print("4. Search a record")
    print("5. Delete a record")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        insert_record()
    elif choice == 2:
        read_record()
    elif choice == 3:
        update_record()
    elif choice == 4:
        search_record()
    elif choice == 5:
        delete_record()
    elif choice == 6:
        break
    else:
        print("Invalid choice. Please enter a valid option.")
