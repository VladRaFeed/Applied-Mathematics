from sympy import *

t = Symbol("t")

x = Function("x")(t)
y = Function("y")(t)

eq = (Eq(Derivative(x, t), 2*x+y+t-2), Eq(Derivative(y,t), 3*x+4*y+3))

ress = dsolve(eq)

pprint(ress)