from sympy import *

x, y, z = symbols('x, y, z')

M1 = {x: 1, y: 1, z: 1}
M2 = {x: 0, y: 1, z: 2}

u = atan(x+(y**2*z))

gradientU = [diff(u, initial_symb) for initial_symb in (x, y, z)]

gradientWithM1 = [grad.subs(M1) for grad in gradientU]
gradientWithM2 = [grad.subs(M2) for grad in gradientU]

scalar = sum(grad1 * grad2 for grad1, grad2 in zip(gradientWithM1, gradientWithM2))

normGradientM1 = sqrt(sum(gradient**2 for gradient in gradientWithM1))
normGradientM2 = sqrt(sum(gradient**2 for gradient in gradientWithM2))

gradientCos = scalar / (normGradientM1 * normGradientM2)

angle = acos(gradientCos)

pprint(angle)