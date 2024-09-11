import sympy as sm

##Варіант №8 Обчисліть:
##
## a) (3a+2b)*(-a+3b), в) |2a+3b|, якщо |a| = 4√2, |b| = 3, φ = Р/4
##

a = sm.Symbol('a')
b = sm.Symbol('b')

x = sm.expand((3*a + 2*b)*(-1*a + 3*b))

x = x.evalf(subs = {a**2: 32, b**2: 9, a*b: ((4 * sm.sqrt(2))*3*sm.cos((sm.pi/4)))})

print(x)

y = sm.expand(sm.sqrt((2*a + 3*b)**2))

print(y)

y = y.evalf(subs = {a**2: 32, b**2: 9, a*b: ((4*sm.sqrt(2)*3*sm.cos(sm.pi/4)))})

print(y)