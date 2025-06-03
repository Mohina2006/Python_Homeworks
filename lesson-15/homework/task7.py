import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
values = [200, 150, 250, 175, 225]
colors = ['red', 'blue', 'green', 'orange', 'purple']  # Valid color names

# Plot
plt.bar(categories, values, color=colors, width=0.3)

# Customizations
plt.title('Sales Data for Different Products')
plt.xlabel('Product Categories')
plt.ylabel('Sales Values')

# Display
plt.show()
