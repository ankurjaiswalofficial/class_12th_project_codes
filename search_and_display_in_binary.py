import pickle

def search_roll_number(roll_number):
    try:
        with open('students_data.bin', 'rb') as file:
            while True:
                data = pickle.load(file)
                if data['roll_number'] == roll_number:
                    print("Name:", data['name'])
                    return
    except EOFError:
        print("Roll number not found.")

roll_to_search = int(input("Enter roll number to search: "))
search_roll_number(roll_to_search)
