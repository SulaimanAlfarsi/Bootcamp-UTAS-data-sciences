
def oddEven(n):
    if s%2 == 0:
        return "Even"
    else:
        return "Odd"
    
s=int(input("Enter a Number: "))
print(oddEven(s))

print("_________________________________________________________________________")

n=int(input("Enter a Number: "))
OddEven = lambda n:(n%2 and 'odd' or 'even')

print(OddEven(n))



