import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

polarF = lambda phi: 2 - np.sin(phi)
areaI = lambda phi: 0.5 * (polarF(phi))**2

phi_min, phi_max = 0, 2 * np.pi

area, _ = quad(areaI, phi_min, phi_max)

phi_vals = np.linspace(0, 2 * np.pi, 1000)
r_vals = np.array([polarF(phi) for phi in phi_vals])

x_vals = r_vals * np.cos(phi_vals)
y_vals = r_vals * np.sin(phi_vals)

plt.figure(figsize=(6, 6))
plt.fill(x_vals, y_vals, color='magenta', alpha=0.3, label="Фігура")
plt.plot(x_vals, y_vals, color='purple', linewidth=2, label="Контур")
plt.title("Фігура в полярній системі координат")
plt.grid(True)
plt.legend()
plt.show()

print(f"Площа фігури: {area:.4f}")
