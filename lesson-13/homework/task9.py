import numpy as np

# Create two 3x3 matrices explicitly
M1 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

M2 = np.array([
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
])

# Compute their dot product (real matrix product)
result = np.dot(M1, M2)

print("Matrix M1:\n", M1)
print("\nMatrix M2:\n", M2)
print("\nDot product (Matrix multiplication) M1 x M2:\n", result)
