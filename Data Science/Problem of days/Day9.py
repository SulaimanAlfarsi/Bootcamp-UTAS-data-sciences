S = input("Enter a string: ")

lowerCount = 0
upperCount = 0
result = 0

for char in S:
    if char.islower():
        lowerCount += 1
    else:
        upperCount += 1
    
    if lowerCount == upperCount:
        result += 1

print("Number of substrings with equal lowercase and uppercase:", result)
