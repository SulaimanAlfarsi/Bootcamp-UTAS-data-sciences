def is_even(L):
    evenList = []
    for num in L:
        if num % 2 == 0:
            evenList.append(num)
    return evenList

n = int(input("How many numbers: "))
numbers = []
for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

even_numbers = is_even(numbers)
print("All Numbers: ",numbers)
print("Even numbers:", even_numbers)

evenUsingfilter = list(filter(lambda n: n%2==0,numbers))

print("filter numbers: ",evenUsingfilter)


mapRuselt = list(map(lambda e : e*2 , evenUsingfilter))
print("map: ",mapRuselt)
