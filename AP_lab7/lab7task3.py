import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from sympy import symbols, cos, sin, diff, lambdify

t = symbols('t')

x_expr = 8 * np.sqrt(2) * (cos(t)**3)
y_expr = np.sqrt(2) * (sin(t)**3)

dx_dt_expr = diff(x_expr, t)
dy_dt_expr = diff(y_expr, t)

x = lambdify(t, x_expr, 'numpy')
y = lambdify(t, y_expr, 'numpy')
dx_dt = lambdify(t, dx_dt_expr, 'numpy')
dy_dt = lambdify(t, dy_dt_expr, 'numpy')

x_limited = lambda t: np.minimum(x(t), 4)

integrand_limited = lambda t: x_limited(t) * dy_dt(t) - y(t) * dx_dt(t)

t_min, t_max = 0, 2 * np.pi

area_limited, _ = quad(integrand_limited, t_min, t_max)
area_limited = abs(area_limited) / 2

t_vals = np.linspace(t_min, t_max, 1000)
x_vals_limited = np.array([x_limited(ti) for ti in t_vals])
y_vals = np.array([y(ti) for ti in t_vals])

plt.figure(figsize=(8, 8))
plt.plot(x_vals_limited, y_vals, label="Фігура з обмеженням")
plt.fill(x_vals_limited, y_vals, color='tomato', alpha=0.6, label=f"Площа = {area_limited:.2f}")
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
plt.title("Фігура з урахуванням обмеження x ≤ 4")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid()
plt.axis('equal')
plt.show()
print(f"Площа фігури з урахуванням обмеження: {area_limited:.2f}")
