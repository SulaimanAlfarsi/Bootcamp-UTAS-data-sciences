import numpy as np

L1 = [7,8,6,100,7,9]

print(L1)
    
avg = np.average(L1)
print("Average: ",avg)
print("____________________________\n")

std=np.std(L1)
print("Standard deviation: ",std)
print("____________________________\n")


for i in L1:
    z = (i - avg) / std
    print(z," of ",i)
    
print("____________________________\n")
S1=set(L1)
print(S1)
print(type(S1))

print("____________________________\n")
L1=list(S1)
print(L1)
print(type(L1))


print("____________________________\n")

L2 = [85,94,26,46,47,3,5,47,5,43]

min1=min(L2)
max1 =max(L2)

for i in L2:
    x=(i-min1)/(max1-min1)
    print(i,x)
print("Minimum: ",min1)
print("Maximum: ",max1)
print(len(L2))





