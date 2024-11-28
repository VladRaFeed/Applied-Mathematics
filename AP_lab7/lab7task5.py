import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt

dx_dt = lambda t: (np.cos(t) / (1 + np.sin(t))) - (np.sin(t) / np.cos(t))
dy_dt = lambda t: (-np.sin(t) / (1 - np.cos(t))) - (np.cos(t) / np.sin(t))
arc_length = lambda t: np.sqrt(dx_dt(t)**2 + dy_dt(t)**2)

t_min = np.pi / 6
t_max = np.pi / 3

length, _ = quad(arc_length, t_min, t_max)

t_values = np.linspace(t_min, t_max, 500)
x_values = np.log(1 + np.sin(t_values)) - np.log(np.cos(t_values))
y_values = np.log(1 - np.cos(t_values)) - np.log(np.sin(t_values))

plt.figure(figsize=(8, 6))
plt.plot(x_values, y_values, label="Параметрична крива", color="red")
# plt.fill_between(x_values, 0, y_values, color='lightblue', alpha=0.5, label='Область під кривою')
plt.xlabel("x")
plt.ylabel("y")
plt.title("Графік параметричної кривої")
plt.legend()
plt.grid(True)
plt.show()

print(f"Довжина кривої: {length:.4f}")
