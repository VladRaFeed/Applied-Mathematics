from sympy import *

x = Symbol('x')

f = 1 / (2*x**2+x+2)

partialF = apart(f, x)

integ = Integral(f)

ress = integ.doit()

# pprint(integ)
# ress = integrate(partialF, x)

pprint(ress)

# Інтегрування напряму робиться тому що, розкласти знаменик виділенням повного
# квадрату - не можливо, так як дискримінант = -15 і треба робити обрахунки 
# через комплексні числа, тому робиться інтегрування на пряму.