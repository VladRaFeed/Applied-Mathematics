from sympy import *

x = Symbol('x')

ress = factor(2*x**3 - 7*x**2 + 8*x - 3)

pprint(ress)