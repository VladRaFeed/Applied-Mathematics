from sympy import *

x = Symbol('x')

y = x**2 / (x**2 - 1)

plot(y, title="Графік кривої", xlabel="x", ylabel="y", legend=True, xlim=(-10, 10), ylim=(-10,10), line_color="yellow")