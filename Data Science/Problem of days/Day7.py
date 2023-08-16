list1 = [16, 17, 4, 3, 5, 2]
leaders = []

max_right = list1[-1]  
leaders.append(max_right)

for i in range(len(list1) - 2, -1, -1):
    if list1[i] >= max_right:
        max_right = list1[i]
        leaders.append(max_right)

leaders.reverse()

print(leaders)
