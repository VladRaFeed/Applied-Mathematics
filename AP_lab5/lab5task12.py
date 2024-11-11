from sympy import *
import matplotlib.pyplot as plt

x, y = symbols('x,y')

eq1 = Eq(y**2 - 4*x, 4)
eq2 = Eq(x, 3 - 3/7*sqrt(49-y**2))

p1 = plot_implicit(eq1, (x, -5, 5), (y, -5, 5), show=False, line_color="lime")
p2 = plot_implicit(eq2, (x, -5, 5), (y, -5, 5), show=False, line_color="red")

p1.extend(p2)
p1.show()
