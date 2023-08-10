arr = [1,2,3,4,5,6,7,8,9,0]

def sum(n):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] + arr[j] == n:
                print(str(arr[i])+ " " + str(arr[j]))

sum(5)
