import pickle

def update_marks(roll_number, new_marks):
    try:
        with open('students_marks.bin', 'rb+') as file:
            while True:
                pos = file.tell()
                data = pickle.load(file)
                if data['roll_number'] == roll_number:
                    data['marks'] = new_marks
                    file.seek(pos)
                    pickle.dump(data, file)
                    print("Marks updated successfully.")
                    return
    except EOFError:
        print("Roll number not found.")

roll_to_update = int(input("Enter roll number to update marks: "))
new_marks = float(input("Enter new marks: "))
update_marks(roll_to_update, new_marks)
