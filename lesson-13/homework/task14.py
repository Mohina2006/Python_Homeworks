import numpy as np

# Define a 3x3 matrix A
A = np.array([
    [3, 1, -1],
    [2, 4, 1],
    [1, -2, 5]
])

# Define a 3x1 vector b
b = np.array([[4], [1], [1]])

# Solve for x in Ax = b
x = np.linalg.solve(A, b)

print("Solution vector x:\n", x)