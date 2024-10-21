import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

num_of_columns = 12

height1 = np.random.rand(num_of_columns)
height2 = np.random.rand(num_of_columns)
height3 = np.random.rand(num_of_columns)
colors1 = cm.Blues(np.linspace(0.1, 0.8, num_of_columns))
colors2 = cm.Purples(np.linspace(0.1, 0.8, num_of_columns))
colors3 = cm.Reds(np.linspace(0.1, 0.8, num_of_columns))
variable_y_positions = np.linspace(0.05, 1, num_of_columns)

ax.bar(np.arange(num_of_columns), height1, zs=np.arange(num_of_columns), zdir='x', color=colors1)
ax.bar(np.arange(num_of_columns), height2, zs=np.arange(num_of_columns), zdir='x', color=colors2)
ax.bar(np.arange(num_of_columns), height3, zs = variable_y_positions, zdir='y', color=colors3)

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

plt.title("Просторові стовпчаті графіки")
plt.show()