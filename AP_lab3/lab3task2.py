import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arrow

n = 8
figure, ax = plt.subplots(figsize=(10, 8))

degrees = np.linspace(0, 2 * np.pi, n, endpoint=False)

x = np.cos(degrees) * 5
y = np.sin(degrees) * 5

# -1(left) +1(right)
dx = np.roll(x, -1) - x
dy = np.roll(y, -1) - y

for i in range(n):
    arrow = Arrow(x[i], y[i], dx[i], dy[i], width=1.5, color='magenta')
    ax.add_patch(arrow)

ax.text(-1.5, -0.4, f"n = {n}", color='#FFF', fontsize=24, bbox=dict(facecolor="#000"))

ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_aspect("equal")
ax.set_xlabel("x")
ax.set_ylabel("y")

plt.title("Task 2")
plt.grid(True)
plt.show()
