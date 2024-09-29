import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2 * np.pi, 1000) # ф

a = 2.5
b = 1

p = a / (1 + b * np.sin(t))

plt.figure(figsize=(6,6))
plt.polar(t, p)
plt.title("Крива у полярній системі координат яка задана рівнянням")
plt.grid(True)
plt.legend()

x = p * np.cos(t)
y = p * np.sin(t)
plt.figure(figsize=(6,6))
plt.plot(x, y)
plt.title("Крива в декатровій системі координат")
plt.xlabel("x")
plt.ylabel("y")
plt.axhline(0, color="red", linewidth=1, ls = "--")
plt.axvline(0, color="red", linewidth=1, ls = "--")
plt.axis("equal")
plt.grid()
plt.legend()
plt.show()