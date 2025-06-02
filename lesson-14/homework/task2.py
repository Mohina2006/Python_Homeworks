import numpy as np

# Define the function
@np.vectorize
def raise_to_power(num, pow):
    return num ** pow

# Arrays
array1 = [2, 3, 4, 5]
array2 = [1, 2, 3, 4]

# Convert to numpy arrays and apply the function
result = raise_to_power(np.array(array1), np.array(array2))

# Print the result
print(*result)
