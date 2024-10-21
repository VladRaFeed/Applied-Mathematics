import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

x = np.linspace(-30, 30, 10000)
y = np.linspace(-30, 30, 10000)

x,y=np.meshgrid(x,y)

z = (np.sin(np.sqrt(np.pow(x, 2) + np.pow(y, 2)))) / (np.sqrt(np.pow(x, 2) + np.pow(y, 2)))

fig=plt.figure(figsize=(10, 8))
ax= fig.add_subplot(111, projection='3d')

myFigure = ax.plot_surface(x, y, z, cmap=cm.Purples, alpha=0.5)

ax.set_zlim(-5, 5)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

ax.quiver(0, 0, 0, 30, 0, 0, color='red', arrow_length_ratio=0.1)   
ax.quiver(0, 0, 0, 0, 30, 0, color='red', arrow_length_ratio=0.1) 
ax.quiver(0, 0, 0, 0, 0, 4, color='red', arrow_length_ratio=0.1)

plt.title("z = sin(sqrt(x**2 + y**2)) / sqrt(x**2 + y**2)")
plt.show()