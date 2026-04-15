import numpy as np
# Create a NumPy array
arr = np.array([20, 25, 30, 45, 55])
# Boolean condition: Find elements greater than or equal to 25
check = arr >= 25
# Use the condition to index the array
arr1 = arr[check]
print("Original Array:", arr)
print("Conditional array (array >= 25):", check)
print("Filtered Array:", arr1)
