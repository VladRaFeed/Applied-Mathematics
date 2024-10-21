import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.optimize import fsolve

def f(x, y, z):
    return x**2 + y**2 - z**2 - 6*x - 2*y + 9

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)

x, y = np.meshgrid(x, y)

z = np.zeros_like(x)

for i in range(x.shape[0]):
    for j in range(x.shape[1]):
        initial_num = 0
        z_num = fsolve(f, initial_num, args=(x[i, j], y[i, j]))
        z[i, j] = z_num[0]

ax.plot_surface(x, y, z, cmap='Blues', edgecolor='none')
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.quiver(0, 0, 0, 4, 0, 0, color='red', arrow_length_ratio=0.1)   
ax.quiver(0, 0, 0, 0, 4, 0, color='red', arrow_length_ratio=0.1) 
ax.quiver(0, 0, 0, 0, 0, 4, color='red', arrow_length_ratio=0.1)
plt.title("sqrt(x**2 + y**2 - 6*x - 2*y + 9")
plt.show()