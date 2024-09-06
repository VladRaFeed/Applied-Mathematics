import numpy as np
import math

## Варіант №8 Розв'язати систему а) Матричним методом б) за формулами Крамера:
##
## {x1  + 2x2 - 2x3  = -3
## {2x1 + x2  +  3x4  = 8
## {3x1 - 4x2 + x3    = 5
##

A = np.array([[1, 2, -2], [2, 1, 3], [3, -4, 1]], dtype=np.int16)
B = np.array([-3, 8, 5], dtype=np.int16)


## Матричний метод

def MatrixMethod(mtrx1, mtrx2):
    ress = np.linalg.solve(mtrx1, mtrx2)
    print(ress)

# MatrixMethod(A, B)

## за формулами Крамера

def CramersFormuls(mtrx1, mtrx2):
    det = np.ceil(np.linalg.det(mtrx1)).astype(int)
    helpMatrix1 = mtrx1.copy()
    helpMatrix2 = mtrx1.copy()
    helpMatrix3 = mtrx1.copy()
    helpMatrix1[:, 0] = mtrx2
    helpMatrix2[:, 1] = mtrx2
    helpMatrix3[:, 2] = mtrx2
    det1 = np.ceil(np.linalg.det(helpMatrix1)).astype(int)
    det2 = np.floor(np.linalg.det(helpMatrix2)).astype(int)
    det3 = np.floor(np.linalg.det(helpMatrix3)).astype(int)
    x1 = np.ceil(det1 / det).astype(int)
    x2 = np.ceil(det2 / det).astype(int)
    x3 = np.ceil(det3 / det).astype(int)
    print(x1)
    print(x2)
    print(x3)

# CramersFormuls(A, B)