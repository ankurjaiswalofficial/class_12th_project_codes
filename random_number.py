import random

def generate_lottery_number():
    return random.randint(1, 6)

user_number = int(input("Enter your number (between 1 and 6): "))
lottery_number = generate_lottery_number()

if user_number == lottery_number:
    print(f"Congratulations! You won! Lottery number was {lottery_number}.")
else:
    print(f"Sorry, you didn't win. Lottery number was {lottery_number}.")
