import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

V = 5
A = np.array([2, 1, -1])
B = np.array([3, 0, 1])
C = np.array([2, -1, 3])
D = np.array([0, 0, 0])

def calculate_volume(y_D):
    D[1] = y_D
    matrix = np.array([
        B - A,
        C - A,
        D - A
    ]).T
    det = np.linalg.det(matrix)
    return abs(det) / 6

y_D_solution = fsolve(lambda y: calculate_volume(y) - V, 0) 
D = np.array([0, y_D_solution[0], 0])

print(D)

points = np.array([A, B, C, D])

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection="3d")

faces = [
    [A, B, C],
    [A, B, D],
    [A, C, D],
    [B, C, D]
]

ax.add_collection3d(Poly3DCollection(faces, alpha=0.5, edgecolor="k"))

ax.scatter(points[:, 0], points[:, 1], points[:, 2], color="red", s=20)
ax.text(*A, "A", color="black")
ax.text(*B, "B", color="black")
ax.text(*C, "C", color="black")
ax.text(*D, "D", color="black")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.show()
