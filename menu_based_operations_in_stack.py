stack = []

def push(item):
    stack.append(item)
    print(f"Pushed '{item}' onto the stack.")

def pop():
    if not is_empty():
        return stack.pop()
    return "Stack is empty"

def display():
    if not is_empty():
        print("Stack Contents:")
        for item in reversed(stack):
            print(item)
    else:
        print("Stack is empty")

def is_empty():
    return len(stack) == 0

# Menu-driven program
while True:
    print("\nMenu:")
    print("1. PUSH")
    print("2. POP")
    print("3. DISPLAY")
    print("4. EXIT")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        item = input("Enter item to push: ")
        push(item)
    elif choice == 2:
        print("Popped item:", pop())
    elif choice == 3:
        display()
    elif choice == 4:
        break
    else:
        print("Invalid choice. Please enter a valid option.")
