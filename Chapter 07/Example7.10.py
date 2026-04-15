import numpy as np
var2 = np.array([[32, 21, 15], [11, 4, 64]])
sort = np.sort(var2, axis=1)  # Sort row-wise
print("Sorted row-wise elements in 2-D array",sort)
