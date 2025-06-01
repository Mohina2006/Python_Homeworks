import numpy as np

array = np.random.randint(0, 10000000, (10, 10))  
print("Array:\n", array)

min_val = np.min(array)
max_val = np.max(array)

print("\nMinimum value:", min_val)
print("Maximum value:", max_val)
