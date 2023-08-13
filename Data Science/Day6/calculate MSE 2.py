import numpy as np
 
O = [7,5,2,0,1,8]
F = [6,5,0,-1,0,7]

MSE = np.square(np.subtract(O,F)).mean()

print(MSE)




 