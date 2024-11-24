from sympy import *

x = Symbol('x')

y = Function('y')

Eqauntion = Eq(y(x).diff(x,x)-3*y(x).diff(x)+2*y(x), 2*x*exp(x))

pprint(Eqauntion)

ress = dsolve(Eqauntion, y(x))

pprint(ress)