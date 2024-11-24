import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Параметричні рівняння
def x(t):
    return 8 * np.sqrt(2) * (np.cos(t)**3)

def y(t):
    return np.sqrt(2) * (np.sin(t)**3)

# Похідні x та y за параметром t
def dx_dt(t):
    return -24 * np.sqrt(2) * (np.cos(t)**2) * np.sin(t)

def dy_dt(t):
    return 3 * np.sqrt(2) * (np.sin(t)**2) * np.cos(t)

# Врахування обмеження x <= 4
def x_limited(t):
    x_val = 8 * np.sqrt(2) * (np.cos(t)**3)
    return np.minimum(x_val, 4)  # Обмеження x <= 4

# Площа фігури з урахуванням обмеження
def integrand_limited(t):
    x_val = x_limited(t)
    return x_val * dy_dt(t) - y(t) * dx_dt(t)

# Межі інтегрування для повного періоду t
t_min, t_max = 0, 2 * np.pi

# Обчислення площі
area_limited, _ = quad(integrand_limited, t_min, t_max)
area_limited = abs(area_limited) / 2

# Побудова графіка з урахуванням обмеження
t = np.linspace(t_min, t_max, 1000)
x_vals_limited = x_limited(t)
y_vals = y(t)

plt.figure(figsize=(8, 8))
plt.plot(x_vals_limited, y_vals, label="Фігура з обмеженням")
plt.fill(x_vals_limited, y_vals, color='lightcoral', alpha=0.6, label=f"Площа = {area_limited:.2f}")
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
plt.title("Фігура з урахуванням обмеження x ≤ 4")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid()
plt.axis('equal')
plt.show()

# Виведення площі
print(f"Площа фігури з урахуванням обмеження: {area_limited:.2f}")
