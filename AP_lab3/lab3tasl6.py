import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from scipy.optimize import fsolve


fig=plt.figure(figsize=(10, 8))
ax1 = fig.add_subplot(131, projection='3d')
ax2 = fig.add_subplot(132, projection='3d')
ax3 = fig.add_subplot(133, polar=True)

x = np.linspace(-30, 30, 10000)
y = np.linspace(-30, 30, 10000)

x,y=np.meshgrid(x,y)

z = (np.sin(np.sqrt(np.pow(x, 2) + np.pow(y, 2)))) / (np.sqrt(np.pow(x, 2) + np.pow(y, 2)))

myFigure = ax1.plot_wireframe(x, y, z, cmap=cm.Purples, alpha=0.3)

ax1.set_zlim(-5, 5)
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.set_zlabel("z")

ax1.quiver(0, 0, 0, 30, 0, 0, color='red', arrow_length_ratio=0.1)   
ax1.quiver(0, 0, 0, 0, 30, 0, color='red', arrow_length_ratio=0.1) 
ax1.quiver(0, 0, 0, 0, 0, 4, color='red', arrow_length_ratio=0.1)
ax1.set_title('sin(sqrt(x^2 + y^2)) / sqrt(x^2 + y^2)', fontsize=10)

# --------------------------------------------------------------------------

def f(x, y, z):
    return x**2 + y**2 - z**2 - 6*x - 2*y + 9

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)

x, y = np.meshgrid(x, y)

z = np.zeros_like(x)

for i in range(x.shape[0]):
    for j in range(x.shape[1]):
        initial_num = 0
        z_num = fsolve(f, initial_num, args=(x[i, j], y[i, j]))
        z[i, j] = z_num[0]

ax2.scatter(x, y, z, cmap='Blues', edgecolor='none', alpha=0.3)
ax2.set_xlabel("x")
ax2.set_ylabel("y")
ax2.set_zlabel("z")
ax2.quiver(0, 0, 0, 4, 0, 0, color='red', arrow_length_ratio=0.1)   
ax2.quiver(0, 0, 0, 0, 4, 0, color='red', arrow_length_ratio=0.1) 
ax2.quiver(0, 0, 0, 0, 0, 4, color='red', arrow_length_ratio=0.1)
ax2.set_title('sqrt(x^2 + y^2 - 6*x - 2y + 9)', fontsize=10)

# --------------------------------------------------------------------------

t = np.linspace(0, 2 * np.pi, 100)
f = 3 * np.sin(4 * t)
ax3.plot(t, f, color = 'r')
ax3.fill(t, f, 'b', alpha=0.5)
ax3.set_title('3sin4f')

plt.show()