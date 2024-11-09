from sympy import *

x = Symbol('x')

firstEquation = ((sqrt(1 + asin(x))) - (sqrt(1 - sin(x)))) / tan(x)
secondEquation = (pow(E, x) - E + log(2 - x**2)) / (2*x**2 - 3*x + 1)

ress1 = limit(firstEquation, x, 0)
ress2 = limit(secondEquation, x, 1)

pprint(Limit(firstEquation, x, 0))
print("Розв'язок:")
pprint(ress1)
pprint(Limit(secondEquation, x, 1))
print("Розв'язок:")
pprint(ress2)