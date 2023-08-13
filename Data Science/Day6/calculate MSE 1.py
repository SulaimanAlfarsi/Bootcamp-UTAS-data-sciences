O = [7,5,2,0,1,8]
F = [6,5,0,-1,0,7]

x=0
for i in range(len(O)):
    x+=((F[i]-O[i])**2)
    print(x)
    
MSE = x /(len(O))

print(MSE)
    
