from sympy import *
from sympy.plotting import plot

x = symbols('x')
PI = pi

f = Piecewise((0, (x >= -PI) & (x < 0)), (x - 2, (x > 0) & (x <= PI)))

fourier = fourier_series(f, (x, -PI, PI))

p1 = plot(f, (x, -PI, PI), show=False, line_color='blue', label='f(x)')
p2 = plot(fourier.truncate(n=20), (x, -PI, PI), show=False, line_color='pink', label='Сума ряду Фур\'є')
p1.extend(p2)

p1.title = "f(x) та Сума ряду Фур'є для f(x)"
p1.xlabel = "x"
p1.ylabel = "Значення"
p1.show()
