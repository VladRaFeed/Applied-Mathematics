import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots(figsize=(10,8))

line, = ax.plot([], [], linewidth=1.5)

colors = ["tomato", "cyan", "magenta", "lime", "yellow", "skyblue", "purple"]

def updateAnim(frame):
    t = np.linspace(-2, 2, 1000)

    x = np.exp(t) * np.cos(t) + (30 - frame % 30 if frame >= 30 else frame) / 3
    y = np.exp(t) * np.sin(t) + np.cos(frame / 5)
    
    line.set_data(x, y)
    line.set_color(np.random.choice(colors)) 
    return line,

animation = FuncAnimation(fig, updateAnim, frames=60, interval=100)

ax.set_xlim(-3, 12)
ax.set_ylim(-1.75, 8)
ax.set_aspect("equal")
animation.save("lab4task1.gif", writer='pillow')    
plt.show()