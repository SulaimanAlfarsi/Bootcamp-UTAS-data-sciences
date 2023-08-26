
S = input("Enter a string: ")

char_count = {}


for char in S:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1


for char in S:
    if char_count[char] == 1:
        result = char
        break
else:
    result = '&'

# Print the result
print("The first non-repetend letter:", result)
