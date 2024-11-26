import numpy as np
import matplotlib.pyplot as plt

u = np.linspace(-np.pi, np.pi, 100)
v = np.linspace(-np.pi / 2, np.pi / 2, 100)
u, v = np.meshgrid(u, v)

x = np.cos(u) * np.cos(v)
y = np.sin(u) * np.cos(v)
z = np.sin(v)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_wireframe(x, y, z, rstride=5, cstride=3, color='red')
ax.set_xlabel("Вісь X")
ax.set_ylabel("Вісь Y")
ax.set_zlabel("Вісь Z")
ax.set_title("Каркасний тривимірний графік сфери")
fig.text(0.5, 0.05, "Рівняння: x = cos(u)cos(v), y = sin(u)cos(v), z = sin(v)", ha='center', fontsize=10, color='black')

plt.show()