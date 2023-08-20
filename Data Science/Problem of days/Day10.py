
A = 2
B = 5
array = [1, 4, 5, 2, 7, 8, 3]

found_element_in_range = False
for num in array:
    if A <= num <= B:
        found_element_in_range = True
    
if found_element_in_range:
    print("yes")
else:
    print("no")
