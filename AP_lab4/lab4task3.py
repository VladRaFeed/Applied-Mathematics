import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})

def updateAnim(frame):
    ax.clear()
    t = np.linspace(0, 2 * np.pi * (frame / 50 if frame < 50 else 1), 100)
    f = 3 * np.sin(4 * t + (frame - 50 if frame >= 50 else 0))  
    line, = ax.plot(t, f, color='black')
    ax.fill(t, f, color='blue', alpha=0.3)
    ax.set_title(f"r = 4 cos(3 * phi * {(frame / 50 if frame < 50 else 1)}) Frame: {frame}")
    return line,

animation = FuncAnimation(fig, updateAnim, frames=100, interval=100)

animation.save("lab4task3.gif", writer='pillow')
plt.show()