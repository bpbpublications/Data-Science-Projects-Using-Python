import numpy as np
# Define two matrices
matrix1 = np.array([[2, 3], [4, 5]])
matrix2 = np.array([[1, 2], [2, 2]])
# Matrix Addition
addition = matrix1 + matrix2
print("Matrix Addition:\n", addition)
# Matrix Subtraction
subtraction = matrix1 - matrix2
print("Matrix Subtraction:\n",subtraction)
# Matrix Multiplication (Dot Product)
matrix_multiply = np.dot(matrix1, matrix2)
print("Matrix Multiplication:\n", matrix_multiply)
# Transpose of a Matrix
transpose = matrix1.T
print("Transpose of matrix1:\n", transpose)
