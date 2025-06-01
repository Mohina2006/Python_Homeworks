import numpy as np

# Create a 3x3 random matrix
matrix = np.random.randint(0, 1000, (3, 3))

# Create a 3-element column vector (shape: 3x1)
column_vector = np.random.randint(0, 1000, (3, 1))

# Compute the matrix-vector product
result = np.dot(matrix, column_vector)

print("Matrix (3x3):\n", matrix)
print("\nColumn vector (3x1):\n", column_vector)
print("\nMatrix-vector product (3x1):\n", result)
