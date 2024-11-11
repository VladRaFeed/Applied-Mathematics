from sympy import *

x = symbols('x')

equation = Eq(x**3, -125)

solutions = solve(equation, x)

pprint(solutions)