import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Функція, яка задає криву
def y(x):
    return (np.exp(2*x) + np.exp(-2*x)) / 2

# Похідна функції y(x)
def dydx(x):
    return (2 * np.exp(2*x) - 2 * np.exp(-2*x)) / 2

# Формула для обчислення довжини дуги
def arc_length_integrand(x):
    return np.sqrt(1 + dydx(x)**2)

# Межі інтегрування
x_min, x_max = 0, 2

# Обчислення довжини дуги
length, _ = quad(arc_length_integrand, x_min, x_max)

# Генерація даних для графіку
x_vals = np.linspace(x_min, x_max, 500)
y_vals = y(x_vals)

# Відображення графіку
plt.figure(figsize=(8, 6))
plt.plot(x_vals, y_vals, label='y(x) = (e^(2x) + e^(-2x)) / 2', color='blue')
plt.fill_between(x_vals, 0, y_vals, color='lightblue', alpha=0.5, label='Area under the curve')
plt.title("Графік функції та довжина кривої")
plt.xlabel("x")
plt.ylabel("y")
plt.axhline(0, color='black', linewidth=0.8, linestyle="--")
plt.axvline(0, color='black', linewidth=0.8, linestyle="--")
plt.legend()
plt.grid()

# Виведення результату
plt.show()

print(length)
