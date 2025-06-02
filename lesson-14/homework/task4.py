import numpy as np
arr1 = np.array([
    [10, -2, 3],
    [-2, 8, -1],
    [3, -1, 6]
    ])
arr2 = np.array([12, -5, 15])
print(*np.linalg.solve(arr1, arr2))