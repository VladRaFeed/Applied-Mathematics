from sympy import symbols, Eq, Matrix, solve

x, y, z = symbols('x y z')

A = Matrix([
    [2, -1, 3],
    [3, -5, 1],
    [4, -7, 1]
])

det = A.det()

if det == 0:
    print("Визначник матриці дорівнює нулю. Система може не мати єдиного розв'язку.")
else:
    print("Визначник матриці:", det)

eq1 = Eq(2*x - y + 3*z, 9)
eq2 = Eq(3*x - 5*y + z, -4)
eq3 = Eq(4*x - 7*y + z, 5)

solution = solve([eq1, eq2, eq3], (x, y, z))

if not solution:
    print("Система не має розв'язку або має нескінченну кількість розв'язків.")
else:
    print("Розв'язок системи:")
    print(solution)