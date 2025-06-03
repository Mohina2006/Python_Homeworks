import matplotlib.pyplot as plt
import numpy as np

# Create figure and 3D axis
fig = plt.figure()
ax = plt.axes(projection='3d')

# Generate grid of x and y values
x = np.linspace(-5, 5, 400)
y = np.linspace(-5, 5, 400)
X, Y = np.meshgrid(x, y)  # Creates 2D grid for surface plotting

# Compute Z values from the function
Z = np.cos(X**2 + Y**2)

# Plot the surface
surf = ax.plot_surface(X, Y, Z, cmap='viridis')  

# Add colorbar for reference
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10) #Controls the width-to-height ratio of the colorbar.

# Labels and title
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('f(x, y)')
ax.set_title('3D Surface Plot of $f(x, y) = \cos(x^2 + y^2)$')

# Show the plot
plt.show()
