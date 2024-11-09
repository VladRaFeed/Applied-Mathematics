from sympy import *

t, x, y = symbols('t, x, y')

x = pow(E, t)*cos(t)
y = pow(E, t)*sin(t)

diff_x = diff(x, t)
diff_y = diff(y, t)

dydx = diff_y / diff_x

d2yd2x = diff(dydx, t) / diff_x

print("Похідна №1:")
pprint(dydx)
print("Похідна №2:")
pprint(d2yd2x)