def is_perfect(num):
    sum_factors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_factors += i
    return sum_factors == num

number = int(input("Enter a number: "))
if is_perfect(number):
    print(number, "is a perfect number.")
else:
    print(number, "is not a perfect number.")
