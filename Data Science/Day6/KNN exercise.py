import math

C = [7,7,3,1,3]
W = [70,40,40,40,70]
H = ["BAD","BAD","GOOD","GOOD","BAD"]

newList=[]

newC = int(input("Enter new cigrattes: "))
newW = int(input("Enter new Weigth: "))


for i in range(len(C)):
    D = math.sqrt((newC -C[i])**2 + (newW - W[i])**2)
    newList.append(D)
    
    
print(newList)    
print("min is: ",min(newList))

R = newList.index(min(newList))

print("The result: ",H[R])




