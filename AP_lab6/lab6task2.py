from sympy import *

C1, C2, x = symbols("C1, C2, x")

y = Function("y")(x)

Equantion = Eq(y.diff(x,x)-2*y.diff(x)+2*y, 3*x-2)

#Загальний розв'язок

ress = dsolve(Equantion, y)

#Частковий розв'язок

pprint(ress)

Eq1 = ress.rhs.subs(x, 0)

pprint(Eq1)

Eq2 = ress.rhs.diff(x).subs(x, 0)

pprint(Eq2)

ress2 = solve([Eq1+2, Eq2-2], C1, C2)

pprint(ress2)

ress3 = ress.rhs.subs([(C1, ress2[C1]), (C2, ress2[C2])])

pprint(ress3)

#Графік

plot(ress3, t=(-5,5,100), line_color='red', xlabel="x", ylabel="y", title="Графік часткового розв'язку")