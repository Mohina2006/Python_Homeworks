import matplotlib.pyplot as plt
import numpy as np
# Define x values from 0 to 2π
x = np.linspace(0, np.pi * 2, 400)
# Compute y values for sine and cosine
y_sin = np.sin(x)
y_cos = np.cos(x)
plt.figure(figsize=(10, 3))
#Plot sine function with a red dashed line and circle markers
plt.plot(x, y_sin, 'g--o', label = 'sin(x)', markevery = 30)
plt.plot(x, y_cos, 'b-s', label='cos(x)', markevery=30)
plt.xlabel('x (radians)')
plt.ylabel("Function value")
plt.title("Plot of sin(x) and cos(x)")
plt.legend()
plt.grid(True)
plt.show()