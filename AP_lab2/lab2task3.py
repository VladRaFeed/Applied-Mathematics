import numpy as np
import matplotlib.pyplot as plt

# x^2+6y^2-6x+12y+13=0, a = 102

# Параметри рівняння еліпса
h = 3  # зсув по осі X
k = -1  # зсув по осі Y
a = np.sqrt(2)  # піввісь по X
b = np.sqrt(1/3)  # піввісь по Y

# Створюємо значення для параметра t
t = np.linspace(0, 2*np.pi, 1000)

# Обчислюємо X та Y координати для еліпса
x_vals = h + a * np.cos(t)
y_vals = k + b * np.sin(t)

plt.figure(figsize=(6,6))
plt.plot(x_vals, y_vals, label='Еліпс', color='magenta')
plt.title('Еліпс')
plt.xlabel('x')
plt.ylabel('y')
plt.text(1, 5, "x^2+6y^2-6x+12y+13=0, a = 102", color="red", rotation=146)
plt.grid()
plt.axhline(0, color="red", linewidth=1, ls = "--")
plt.axvline(0, color="red", linewidth=1, ls = "--")
plt.xlim(-5, 5)
plt.ylim(-5, 10)
plt.legend()
plt.show()