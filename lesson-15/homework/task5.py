import matplotlib.pyplot as plt
import numpy as np
data = np.random.normal(loc=0, scale=1, size=1000) # mean = 0, sd = 1
plt.hist(data, bins=30, alpha=0.7, color='steelblue', edgecolor='black') # alpha sets transparency, bins divide axis by 30 equal width bars
plt.title('Histogram of Normally Distributed Data (mean=0, std=1)')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.grid(True)
plt.tight_layout()
plt.show()

