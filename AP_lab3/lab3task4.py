import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)

z = np.sqrt(x**2 + y**2 - 6*x - 2*y + 9)
z[np.isnan(z)] = 0

ax.plot_surface(x, y, z, cmap='Blues', edgecolor='none')
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.quiver(0, 0, 0, 4, 0, 0, color='red', arrow_length_ratio=0.1)   
ax.quiver(0, 0, 0, 0, 4, 0, color='red', arrow_length_ratio=0.1) 
ax.quiver(0, 0, 0, 0, 0, 8, color='red', arrow_length_ratio=0.1)
plt.title("sqrt(x**2 + y**2 - 6*x - 2*y + 9")
plt.show()