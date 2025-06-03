import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-10,10,400)
f = x ** 2 - 4 * x + 4
plt.figure(figsize=(8,5))
plt.plot(x,f, label = '$f(x)=x^2-4x+4$', color = 'green')
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Plot of $f(x) = x^2 - 4x + 4$")
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)  # x-axis
plt.axvline(0, color='black', linewidth=0.5)  # y-axis
plt.legend()
plt.show()
