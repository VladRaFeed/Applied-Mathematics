import numpy as np

## Варіант №8 Знайти ранг матриці:
##
##  ( 3 -1  2  3  5)
##  (-2  1 -1 -2 -3)
##  ( 1  2  1 -1  2)
##  ( 2  2  2  0  4)
##

A = np.matrix('3 -1 2 3 5; -2 1 -1 -2 -3; 1 2 1 -1 2; 2 2 2 0 4', dtype=np.int16)

ress = np.linalg.matrix_rank(A)

print (ress)