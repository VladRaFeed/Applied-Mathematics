
from sympy import *
from sympy.plotting import *

x, y, z = symbols('x y z')

eq = Eq(x**2 + y**2 - z**2 - 6*x - 2*y - 2*z + 9, 0)

solutions = solve(eq, z)

g = plot3d(
    solutions[0], (x, -10, 10), (y, -10, 10), show=False, line_color="blue"
)
g.extend(
    plot3d(
        solutions[1], (x, -10, 10), (y, -10, 10), show=False, line_color="red"
    )
)

g[0].surface_color = lambda x, y: sin(x)
g[1].surface_color = lambda x, y: cos(y)

g.show()
