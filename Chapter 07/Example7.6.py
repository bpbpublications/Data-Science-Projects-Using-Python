import numpy as np
var1 = np.arange(1,10,1)
print("Elements of array:",var1)
var2 = var1[np.array([3,1,2,-1,-2])]
print("Fetching the elements using indexing",var2)
