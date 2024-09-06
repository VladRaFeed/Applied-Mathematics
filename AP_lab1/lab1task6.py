import numpy as np

##Варіант №8 Обчисліть площу грані АВС і о б ’єм піраміди А ВСІ) , вершини якої містяться в точках:
##
##  А(0; -3; 5), B(-3; -1; 1), С(2; -5; 2), D(4; 3; 6)
##

A = np.array([0, -3, 5], dtype=np.int16)
B = np.array([-3, -1, 1], dtype=np.int16)
C = np.array([2, -5, 2], dtype=np.int16)
D = np.array([4, 3, 6], dtype=np.int16)

AB = B - A
AC = C - A
AD = D - A

#Sabc

ScalarSum = np.cross(AB, AC)
ress1 = (np.sqrt(np.dot(ScalarSum, ScalarSum))) / 2

print(ress1)

#Vabcd

matrix = np.array([AB, AC, AD])
det = np.floor(np.linalg.det(matrix))
ress2 = np.abs(det) / 6 
print(ress2)