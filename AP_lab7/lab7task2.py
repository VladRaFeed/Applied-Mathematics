import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Функція p(φ) у полярних координатах
def polar_function(phi):
    return 2 - np.sin(phi)

# Функція для обчислення площі через інтеграл
def area_integrand(phi):
    r = polar_function(phi)
    return 0.5 * r**2

# Межі інтегрування (φ від 0 до 2π)
phi_min, phi_max = 0, 2 * np.pi

# Обчислення площі фігури
area, _ = quad(area_integrand, phi_min, phi_max)

# Побудова графіка фігури
phi_vals = np.linspace(0, 2 * np.pi, 1000)
r_vals = polar_function(phi_vals)

# Переводимо у декартову систему координат для побудови
x_vals = r_vals * np.cos(phi_vals)
y_vals = r_vals * np.sin(phi_vals)

# Візуалізація
plt.figure(figsize=(6, 6))
plt.fill(x_vals, y_vals, color='magenta', alpha=0.3, label="Фігура")
plt.plot(x_vals, y_vals, color='purple', linewidth=2, label="Контур")

plt.title("Фігура в полярній системі координат")
plt.grid(True)
plt.legend()
plt.show()

print(area)
