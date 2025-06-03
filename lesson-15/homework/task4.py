import matplotlib.pyplot as plt
import numpy as np
# Generate 100 random points
x = np.random.uniform(0, 10, 100)
y = np.random.uniform(0, 10, 100)
colors = np.random.rand(100)  # Random values for coloring
markers = ['o', 's', '^', 'x', '*']  # Different marker types
marker_choices = np.random.choice(markers, 100)
fig, ax = plt.subplots()
for m in markers:
    idx = marker_choices == m
    ax.scatter(x[idx], y[idx], marker = m, label = f"Marker: {m}", c = colors[idx], cmap = "viridis")
ax.set_title('Scatter Plot of 100 Random Points')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.grid(True)
ax.legend(loc='upper right', bbox_to_anchor=(1.2, 1))
plt.tight_layout()
plt.show()