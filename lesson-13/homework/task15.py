import numpy as np
# Create a 5x5 random integer matrix
matrix = np.random.randint(0, 10, (5, 5))
print("Matrix:\n", matrix)
# Sum across rows (axis=1)
row_sums = np.sum(matrix, axis=1)
print("\nRow-wise sums:", row_sums)

# Sum across columns (axis=0)
column_sums = np.sum(matrix, axis=0)
print("\nColumn-wise sums:", column_sums)