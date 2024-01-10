def is_armstrong(num):
    order = len(str(num))
    temp = num
    sum_armstrong = 0
    while temp > 0:
        digit = temp % 10
        sum_armstrong += digit ** order
        temp //= 10
    return sum_armstrong == num

number = int(input("Enter a number: "))
if is_armstrong(number):
    print(number, "is an Armstrong number.")
else:
    print(number, "is not an Armstrong number.")
