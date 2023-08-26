def get_largest_number(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

largest_number = get_largest_number(num1, num2, num3)
print("The largest number is:", largest_number)

