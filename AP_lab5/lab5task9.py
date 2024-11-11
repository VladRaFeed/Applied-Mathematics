from sympy import *

n = Symbol('n')

f = 1 / ((2*n + 5) * (2*n + 7))

ress = summation(f, (n, 1, oo))

if(ress > 0):
    pprint(f'Ряд збіжний, Результат ряду: {ress}')
else:
    print("Ряд розбіжний")

