from sympy import *

t = Symbol('t')

x = t**2 - 4*t
y = ln(t) + sqrt(t)

plot = plot_parametric((x, y, (t, 0.1, 5)), xlabel='x', ylabel='y', title='Параметрично задана крива', line_color="magenta", show=False)
plot.show()