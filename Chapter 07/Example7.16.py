import numpy as np
arr1 = np.array([10,15,25,35,40])
result = np.where(arr1>20,"Greater","Less")
print("Original Array is:",arr1)
print("Result after condition is:",result)
