from sympy import *

x, y = symbols('x y')

z = 2*x - y + 1/x*(y+log(x) + 1)

diffX = diff(z, x)
diffY = diff(z, y)

ress = solve([diffX, diffY], [x, y])

diffX2 = diff(diffX, x)
diffY2 = diff(diffY, y)
diffXY2 = diff(diffX, y)

subNums = {x: ress[0][0], y: ress[0][1]}
A = diffX2.subs(subNums)
B = diffXY2.subs(subNums)
C = diffY2.subs(subNums)

result = (A, B, C)

D = result[0] * result[2] - result[1]**2

if(D > 0):
    if(result[0] > 0):
        print(f"Точка з координатами {ress} - точка мінімуму")
    if(result[0] < 0):
        print(f"Точка з координатами {ress} - точка максимуму")
else:
    print("Екстремум відсутній")