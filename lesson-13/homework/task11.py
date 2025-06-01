import numpy as np

# Create a 3x3 matrix
matrix = np.array([
    [4, 2, 1],
    [3, 5, 7],
    [8, 6, 9]
])

# Calculate the determinant
det = np.linalg.det(matrix)

print("Matrix:\n", matrix)
print("\nDeterminant:", round(det))
