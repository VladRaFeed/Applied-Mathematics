import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.animation import FuncAnimation


fig=plt.figure(figsize=(12, 9))

ax= fig.add_subplot(111, projection='3d')

x = np.linspace(-30, 30, 1000)
y = np.linspace(-30, 30, 1000)
x,y=np.meshgrid(x,y)
z = (np.sin(np.sqrt(np.pow(x, 2) + np.pow(y, 2)))) / (np.sqrt(np.pow(x, 2) + np.pow(y, 2)))

# myFigure = ax.plot_surface(x, y, z, cmap=cm.Purples, alpha=0.5)

def updateAnim(frame):
    ax.clear()

    xFrame = x + (frame / 2)
    yFrame = y + (frame / 2)

    # if(frame <= 30): 
    #     xFrame = x + (frame / 2)
    # else:
    #     yFrame = y + (frame / 2)

    z = (np.sin(np.sqrt(np.pow(xFrame, 2) + np.pow(yFrame, 2)))) / (np.sqrt(np.pow(xFrame, 2) + np.pow(yFrame, 2)))

    myFigure = ax.plot_surface(xFrame, y, z, cmap=cm.Purples, alpha=0.8)
    ax.set_zlim(-5, 5)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")

animation = FuncAnimation(fig, updateAnim, frames=60, interval=100)

animation.save("lab4task2.gif", writer='pillow')

plt.title("z = sin(sqrt(x**2 + y**2)) / sqrt(x**2 + y**2)")
plt.show()