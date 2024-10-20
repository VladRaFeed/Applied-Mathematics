import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

def solve_functions(x):
    ress = (np.pow(x, 3) - 1) - (np.sin(x-3))
    return ress


# Створюємо значення для параметра t
t = np.linspace(-3, 2*np.pi, 1000)

f1 = np.pow(t, 3) - 1
f2 = np.sin(t-3)

plt.figure(figsize=(10,10))

plt.subplot(1, 2, 1)
plt.plot(t, f1, label="x^3-1", color="brown", lw=1)
plt.title("x^3 - 1")
plt.xlabel("x")
plt.ylabel("y")
plt.xlim(-10, 10)
plt.ylim(-30, 30)
plt.grid()
plt.axhline(0, color="red", linewidth=1, ls = "--")
plt.axvline(0, color="red", linewidth=1, ls = "--")
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(t, f2, label="sin(x-3)", color="red", lw=1)
plt.title("sin(x-3)")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.axhline(0, color="red", linewidth=1, ls = "--")
plt.axvline(0, color="red", linewidth=1, ls = "--")
plt.legend()
plt.axis("equal")

plt.figure(figsize=(6,6))

plt.plot(t, f1, label="x^3-1", color="brown", lw=0.5)
plt.plot(t, f2, label="sin(x-3)", color="red", lw=2)
plt.title("Два графіки у одній площині координат")
plt.xlabel("x")
plt.ylabel("y")
# plt.xlim(-10, 10)
# plt.ylim(-5, 5)
plt.grid()
plt.axhline(0, color="red", linewidth=1, ls = "--")
plt.axvline(0, color="red", linewidth=1, ls = "--")
plt.legend()

x_dot = fsolve(solve_functions, 1)
print(x_dot)
y_dot = solve_functions(x_dot[0])

plt.scatter(x_dot[0], y_dot, marker=',', color="magenta", s=70, label="Точка перетину")

plt.show()