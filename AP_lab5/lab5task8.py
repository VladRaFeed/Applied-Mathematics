from sympy import *

# Оголошення змінних
x = symbols('x')
PI = pi

# Опис функції
f = Piecewise((0, (x >= -PI) & (x < 0)), (x - 2, (x > 0) & (x <= PI)))
pprint(f)

# Обчислення коефіцієнтів ряду Фур'є
a0 = integrate(f, (x, -PI, PI)) / (2 * PI)
a_n = lambda n: integrate(f * cos(n * pi * x / PI), (x, -PI, PI)) / PI
b_n = lambda n: integrate(f * sin(n * pi * x / PI), (x, -PI, PI)) / PI

# Реконструкція ряду Фур'є до певної кількості членів
N = 20  # Кількість членів
fourier_series = a0 + sum(a_n(n) * cos(n * pi * x / PI) + b_n(n) * sin(n * pi * x / PI) for n in range(1, N + 1))

# Побудова графіка
plot(fourier_series, (x, -PI, PI), title="Сума ряду Фур'є для f(x)", ylabel="Сума ряду Фур'є", xlabel="x", line_color="pink")
