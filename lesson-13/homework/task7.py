import numpy as np

matrix = np.random.rand(5, 5)  # Random floats between 0 and 1
print("Original matrix:\n", matrix)

min_val = matrix.min()
max_val = matrix.max()

normalized_matrix = (matrix - min_val) / (max_val - min_val)
print("\nNormalized matrix:\n", normalized_matrix)
