import numpy as np
arr1 = np.array([
    [4, 5, 6],
    [3, -1, 1],
    [2, 1, -2]
    ])
arr2 = np.array([7, 4, 5])
print(*np.linalg.solve(arr1, arr2))