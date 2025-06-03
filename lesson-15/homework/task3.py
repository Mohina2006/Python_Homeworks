import matplotlib.pyplot as plt
import numpy as np
# Generate x values
x_full = np.linspace(-5,5,400)
x_positive = np.linspace(0, 5, 400)
# Create a 2x2 grid of subplots
fig, axs = plt.subplots(2, 2, figsize=(12, 8)) #2 rows 2 columns
# Top-left: f(x) = x^3
axs[0,0].plot(x_full, x_full**3, color = 'darkred')
axs[0,0].set_title("f(x) = $x^3$")
axs[0,0].set_xlabel('x')
axs[0, 0].set_ylabel('f(x)')
axs[0,0].grid(True)
# Top - right: f(x) = sin(x)
axs[0,1].plot(x_full, np.sin(x_full), color = 'darkblue')
axs[0,1].set_title("f(x) = $sin(x)$")
axs[0,1].set_xlabel('x')
axs[0,1].set_ylabel('f(x)')
axs[0,1].grid(True)
# Bottom-left:  f(x) = e^x 
axs[1,0].plot(x_full, np.exp(x_full), color = 'darkgreen')
axs[1, 0].set_title('f(x) = $e^x$')
axs[1,0].set_xlabel('x')
axs[1,0].set_ylabel('f(x)')
axs[1,0].grid(True)
# Bottom-right: f(x) = log(x+1)
axs[1, 1].plot(x_positive, np.log(x_positive + 1), color='purple')
axs[1, 1].set_title('f(x) = $\log(x + 1)$')
axs[1, 1].set_xlabel('x')
axs[1, 1].set_ylabel('f(x)')
axs[1, 1].grid(True)
plt.tight_layout()
plt.show()                         