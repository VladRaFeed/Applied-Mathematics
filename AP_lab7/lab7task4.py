import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

y = lambda x: (np.exp(2 * x) + np.exp(-2 * x)) / 2 
dydx = lambda x: (2 * np.exp(2 * x) - 2 * np.exp(-2 * x)) / 2
areaLen = lambda x: np.sqrt(1 + dydx(x)**2)  

x_min, x_max = 0, 2

length, _ = quad(areaLen, x_min, x_max)

x_vals = np.linspace(x_min, x_max, 500)
y_vals = np.array([y(xi) for xi in x_vals])

plt.figure(figsize=(8, 6))
plt.plot(x_vals, y_vals, label=r'$y(x) = \frac{e^{2x} + e^{-2x}}{2}$', color='lightblue')
plt.fill_between(x_vals, 0, y_vals, color='gray', alpha=0.5, label='Область під кривою')
plt.title("Графік функції та довжина кривої")
plt.xlabel("x")
plt.ylabel("y")
plt.axhline(0, color='black', linewidth=0.8, linestyle="--")
plt.axvline(0, color='black', linewidth=0.8, linestyle="--")
plt.legend()
plt.grid()

plt.show()

print(f"Довжина дуги: {length:.4f}")
