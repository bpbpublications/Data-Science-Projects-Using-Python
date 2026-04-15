import numpy as np
arr1 = np.array([11,12,np.nan,14,15])
is_nan_val = np.isnan(arr1)
print("Original Array is:", arr1)
print("Finding a NaN value:", is_nan_val)
