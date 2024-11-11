from sympy import *
from sympy.plotting import *

x, y, z = symbols('x y z')

eq = Eq(x**2+y**2-z**2-6*x-2*y-2*z+9, 0)

solution = solve(eq, z)

g = plot3d(solution, (x, -10, 10), (y, -10, 10), show=False)
g[0].surface_color = lambda x, y: sin(x)
g.show()