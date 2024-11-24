from scipy.integrate import quad
import numpy as np
import matplotlib.pyplot as plt
from sympy import *

# Визначаємо функції кривих
def curve1(y):
    return y**2 - 2*y - 2  # x = y^2 - 2y - 2

def curve2(y):
    return -y  # x = -y

# Знаходимо точки перетину кривих (розв'язуємо рівняння y^2 - 2y - 2 = -y)

y = symbols('y')
intersection_points = solve((y**2 - 2*y - 2) - (-y), y)
y1, y2 = [float(pt) for pt in intersection_points]

# Обчислюємо площу між кривими
area, _ = quad(lambda y: curve1(y) - curve2(y), y1, y2)

print(f"Площа фігури: {area:.4f}")

# Побудова графіка
y_vals = np.linspace(y1, y2, 500)
x_vals1 = curve1(y_vals)  # x для кривої 1
x_vals2 = curve2(y_vals)  # x для кривої 2

plt.figure(figsize=(8, 6))
plt.plot(x_vals1, y_vals, label=r'$x = y^2 - 2y - 2$', color='blue')
plt.plot(x_vals2, y_vals, label=r'$x = -y$', color='red')

# Заливка області
plt.fill_betweenx(y_vals, x_vals1, x_vals2, color='lightblue', alpha=0.5)

# Оформлення графіка
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.axvline(0, color='black', linewidth=0.8, linestyle='--')
plt.legend()
plt.title('Область між кривими')
plt.grid(True)
plt.show()
