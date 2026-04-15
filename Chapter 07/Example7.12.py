import numpy as np
# 2D array with shape (2, 3)
arr2 = np.array([[11, 10, 20],
                  [20, 30, 30]])
# 1D array with shape (3,)
arr1 = np.array([1, 2, 3])
# Broadcasting: add arr1 to each row of arr2
result = arr2 + arr1
print("Original 2D array:\n", arr2)
print("1D array:\n", arr1)
print("Result after broadcasting:\n", result)
