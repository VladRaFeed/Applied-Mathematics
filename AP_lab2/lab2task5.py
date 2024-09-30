import matplotlib.pyplot as plt
import numpy as np

# Створюємо значення для параметра x
x = np.linspace(-2, 2 * np.pi, 1000)

# Для еліпса: (27x^2/28) + (9y^2/7) = 1
y1_positive = np.sqrt((7/9) * (1 - (27/28) * x**2))  # верхня частина еліпса
y1_negative = -np.sqrt((7/9) * (1 - (27/28) * x**2))  # нижня частина еліпса

# Для прямої: 3x - y + 5 = 0  =>  y = 3x + 5
y2 = 3 * x + 5

# Створюємо графіки
plt.figure(figsize=(10, 5))

# Графік еліпса
plt.subplot(1, 3, 1)
plt.plot(x, y1_positive, label='(27x^2/28) + (9y^2/7) = 1', color='magenta')
plt.plot(x, y1_negative, color='magenta')  # нижня частина еліпса
plt.xlabel('x')
plt.ylabel('y')
plt.title('Графік: (27x^2/28) + (9y^2/7) = 1')
plt.legend()
plt.grid(True)
plt.axhline(0, color='red', linewidth=0.5, ls="--")
plt.axvline(0, color='red', linewidth=0.5, ls="--")

# Графік прямої
plt.subplot(1, 3, 2)
plt.plot(x, y2, label='3x - y + 5 = 0', color='yellow')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Графік: 3x - y + 5 = 0')
plt.legend()
plt.grid(True)
plt.axhline(0, color='red', linewidth=0.5, ls="--")
plt.axvline(0, color='red', linewidth=0.5, ls="--")

# Обидва графіки
plt.subplot(1, 3, 3)
plt.plot(x, y1_positive, label='(27x^2/28) + (9y^2/7) = 1', color='magenta', linewidth=1)
plt.plot(x, y1_negative, color='magenta', linewidth=1)  # нижня частина еліпса
plt.plot(x, y2, label='3x - y + 5 = 0', color='yellow')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Графік еліпса та лінії')
plt.legend()
plt.grid(True)
plt.axhline(0, color='red', linewidth=0.5, ls="--")
plt.axvline(0, color='red', linewidth=0.5, ls="--")

plt.tight_layout()
plt.show()