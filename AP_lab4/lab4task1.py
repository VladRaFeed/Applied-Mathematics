import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots(figsize=(6,6))

line, = ax.plot([], [], linewidth=2)
colors = ["tomato", "cyan", "magenta", "lime", "yellow", "skyblue", "purple"]

def update(frame):
    t = np.linspace(-2, 2, 1000)

    x = np.exp(t) * np.cos(t)
    y = np.exp(t) * np.sin(t)

    x += (30 - frame % 30 if frame >= 30 else frame) / 3

    y += np.cos(frame / 10)
    
    line.set_data(x, y)
    line.set_color(colors[frame % len(colors)]) 
    return line,

animation = FuncAnimation(fig, update, frames=60, interval=100)

animation.save("lab4task1.gif", writer='pillow')
ax.set_xlim(-3, 12)
ax.set_ylim(-1.75, 8)
ax.set_aspect("equal")
plt.show()