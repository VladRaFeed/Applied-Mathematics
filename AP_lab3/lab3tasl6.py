import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

fig=plt.figure(figsize=(10, 8))
ax1 = fig.add_subplot(131, projection='3d')
ax2 = fig.add_subplot(132, projection='3d')
ax3 = fig.add_subplot(133, polar=True)

x = np.linspace(-30, 30, 10000)
y = np.linspace(-30, 30, 10000)

x,y=np.meshgrid(x,y)

z = (np.sin(np.sqrt(np.pow(x, 2) + np.pow(y, 2)))) / (np.sqrt(np.pow(x, 2) + np.pow(y, 2)))

myFigure = ax1.plot_surface(x, y, z, cmap=cm.Purples)

ax1.set_zlim(-5, 5)
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.set_zlabel("z")

ax1.quiver(0, 0, 0, 30, 0, 0, color='red', arrow_length_ratio=0.1)   
ax1.quiver(0, 0, 0, 0, 30, 0, color='red', arrow_length_ratio=0.1) 
ax1.quiver(0, 0, 0, 0, 0, 4, color='red', arrow_length_ratio=0.1)
ax1.set_title('sin(sqrt(x^2 + y^2)) / sqrt(x^2 + y^2)')

# --------------------------------------------------------------------------

x2 = np.linspace(-5, 5, 100)
y2 = np.linspace(-5, 5, 100)
x2, y2 = np.meshgrid(x2, y2)

z2 = np.sqrt(x2**2 + y2**2 - 6*x2 - 2*y2 + 9)
z2[np.isnan(z2)] = 0

ax2.plot_surface(x2, y2, z2, cmap='Blues', edgecolor='none')
ax2.set_xlabel("x")
ax2.set_ylabel("y")
ax2.set_zlabel("z")
ax2.quiver(0, 0, 0, 4, 0, 0, color='red', arrow_length_ratio=0.1)   
ax2.quiver(0, 0, 0, 0, 4, 0, color='red', arrow_length_ratio=0.1) 
ax2.quiver(0, 0, 0, 0, 0, 8, color='red', arrow_length_ratio=0.1)
ax2.set_title('sqrt(x^2 + y^2 - 6*x - 2y + 9)')

# --------------------------------------------------------------------------

t = np.linspace(0, 2 * np.pi, 100)
f = 3 * np.sin(4 * t)
ax3.plot(t, f, color = 'r')
ax3.fill(t, f, 'b', alpha=0.5)
ax3.set_title('3sin4f')

plt.show()