import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import Arc, Arrow, Polygon, Wedge, Rectangle

figure, ax = plt.subplots(figsize=(10, 8))

arrow = Arrow(1, -2, 20, 5, width=1.5, color='magenta')
ax.add_patch(arrow)

semicircle = Arc((0, 20), 10, 10, theta1=180, theta2=0, color='c', lw=2)
ax.add_patch(semicircle)

triangle = Polygon([(16, 12), (21, 25), (12, 21)], closed=True, facecolor='aqua', lw=2)
ax.add_patch(triangle)

rhomb = Polygon([[-8, 16], [-4, 10], [-8, 4], [-12, 10]], closed=True, facecolor='blue', lw=2)
ax.add_patch(rhomb)

rectangle = Rectangle((4, -15), 10, 5, facecolor='green', lw=2)
ax.add_patch(rectangle)

sector = Wedge(center=(-15, 2), r=6, theta1=60, theta2=310, color='tomato', lw=2)
ax.add_patch(sector)

ax.set_xlim(-30, 30)
ax.set_ylim(-30, 30)
ax.set_aspect("equal")
ax.set_xlabel("x")
ax.set_ylabel("y")

plt.title("Task 1")
plt.grid(True)
plt.show()