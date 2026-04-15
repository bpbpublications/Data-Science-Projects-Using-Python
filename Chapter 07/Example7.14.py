import numpy as np
arr1 = np.array([12,22,3,22,14,14,25])
unique_values,count_value = np.unique(arr1,return_counts=True)
print("Unique elements:", unique_values)
print("Counts:", count_value)
