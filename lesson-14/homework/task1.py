import numpy as np
@np.vectorize

def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

fahrenheit_values = np.array([32, 68, 100, 212, 77])
celsius_values = fahrenheit_to_celsius(fahrenheit_values)
print(*np.round(celsius_values, 2))