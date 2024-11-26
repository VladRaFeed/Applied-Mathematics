from sympy import *

x, y = symbols('x y')

x_lower = 0
x_upper = 2
y_lower = x / 2 
y_upper = 2 * x 

f = x**2 + 4 * y

integral = integrate(integrate(f, (y, y_lower, y_upper)), (x, x_lower, x_upper))

pprint(integral)

eq_part1 = Eq(y, x / 2)  
eq_part2 = Eq(y, 2 * x) 
vertical_line = Eq(x, 2)  

p = plot_implicit(And(x >= 0, x <= 2, y >= x / 2, y <= 2 * x),
                     line_color='lightblue', show=False, xlabel='x', ylabel='y')
p.xlim = (0,5)
p.ylim = (0,5)

p.extend(plot_implicit(eq_part1, line_color='blue', show=False)) 
p.extend(plot_implicit(eq_part2, line_color='red', show=False))

p.show()
