import numpy as np

## Варіант №8 Розв'яжіть матричні рівняння
##                 (4 3 6)      (2  0)
## x * a =  b, a = (5 4 7), b = (3  1) 
##                 (6 5 7)      (3 -4)

A = np.matrix('4 3 6; 5 4 7; 6 5 7', dtype=np.int16)
B = np.matrix('2 0; 3 1; 3 -4', dtype=np.int16)

# print(A)
# print(B)

inversemtA = np.linalg.inv(A)

ress = np.dot(inversemtA, B)

print(ress)