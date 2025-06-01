import numpy as np

# Define matrix A (3x4)
A = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])

# Define matrix B (4x3)
B = np.array([
    [2, 3, 4],
    [5, 6, 7],
    [8, 9, 10],
    [11, 12, 13]
])

# Compute the matrix product A·B (result will be 3x3)
result = np.dot(A, B)

print("Matrix A (3x4):\n", A)
print("\nMatrix B (4x3):\n", B)
print("\nMatrix product A · B (3x3):\n", result)
