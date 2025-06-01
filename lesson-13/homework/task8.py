import numpy as np

# 5x3 matrix (5 rows, 3 columns)
A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12],
    [13, 14, 15]
])

# 3x2 matrix (3 rows, 2 columns)
B = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
])

# Matrix multiplication
C = np.dot(A, B)

print("Matrix A (5x3):\n", A)
print("\nMatrix B (3x2):\n", B)
print("\nProduct C = A x B (5x2):\n", C)
