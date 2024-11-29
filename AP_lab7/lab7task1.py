from scipy.integrate import quad
import numpy as np
import matplotlib.pyplot as plt
from sympy import *

firstCurve = lambda y: y**2 - 2*y - 2
secondCurve = lambda y: -y 

y = symbols('y')
points = solve(firstCurve(y) - secondCurve(y), y)
y1, y2 = [float(pt) for pt in points]
    
area, _ = quad(lambda y: firstCurve(y) - secondCurve(y), y1, y2)

print(f"Площа фігури: {area:.4f}")

y_vals = np.linspace(y1, y2, 500)
x_vals1 = np.array([firstCurve(y) for y in y_vals])
x_vals2 = np.array([secondCurve(y) for y in y_vals])

plt.figure(figsize=(8, 6))
plt.plot(x_vals1, y_vals, label=r'$x = y^2 - 2y - 2$', color='orange')
plt.plot(x_vals2, y_vals, label=r'$x = -y$', color='lime')

plt.fill_betweenx(y_vals, x_vals1, x_vals2, color='lightblue', alpha=0.5)

plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.axvline(0, color='black', linewidth=0.8, linestyle='--')
plt.legend()
plt.title('Область між кривими')
plt.grid(True)
plt.show()
