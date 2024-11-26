import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.1, 5, 500)

y = (-5 * np.cos(10 * x) * np.sin(3 * x)) / (x ** x)

plt.plot(x, y, label=r'$Y(x) = \frac{-5 \cdot \cos(10x) \cdot \sin(3x)}{x^x}$', color='green', linewidth=2)

plt.title('Графік функції Y(x)', fontsize=15)

plt.xlabel('x', fontsize=12, color='blue')
plt.ylabel('Y(x)', fontsize=12, color='blue')

plt.legend()

plt.grid(True)

plt.show()