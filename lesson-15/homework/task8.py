import matplotlib.pyplot as plt
import numpy as np
time_periods = ['T1', 'T2', 'T3', 'T4']
category_A = [10, 15, 20, 25]
category_B = [5, 10, 15, 10]
category_C = [2, 5, 8, 5]
# Plotting the bars
plt.bar(time_periods, category_A, label='Category A', color='skyblue')
plt.bar(time_periods, category_B, bottom=category_A, label='Category B', color='salmon')
# Stack C on top of A + B
bottom_C = np.array(category_A) + np.array(category_B)
plt.bar(time_periods, category_C, bottom=bottom_C, label='Category C', color='lightgreen')

# Add labels and title
plt.title('Stacked Bar Chart of Category Contributions Over Time')
plt.xlabel('Time Periods')
plt.ylabel('Values')

# Add legend to explain color categories
plt.legend()

# Display the chart
plt.show()
