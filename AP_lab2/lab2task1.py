import numpy as np
import matplotlib.pyplot as plt

plt.title("Параметричне рівняння")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.axhline(0, color="red", linewidth=2, ls = "solid")
plt.axvline(0, color="red", linewidth=2, ls = "solid")
t = np.linspace(-2.321, 2.321) 
x = np.exp(t) * np.cos(t)
y = np.exp(t) * np.sin(t)
plt.plot(x, y, "g", label="y = e^t*sin(t), x = e^t*cos(t)", linewidth=2)
plt.legend()
plt.show()  # Отображает график