import numpy as np

## Варіант №8
##
##     (2  1  3)
## A = (-3 0 -1)
##     (4  2 -1), f(x) = -2x^2+8x-6

A = np.matrix('2 1 3; -3 0 -1; 4 2 -1', dtype=np.int16)

def f(x):
    print("Функція має вигляд: f(x) = -2x^2+8x-6")
    print("Передана матриця: ")
    print(x)
    print("Розкладемо функцію на дві частини: -2x^2 та 8x-6E")
    print("Перша частина функції з підставленним значенням А, буде дорівнювати:")
    ress1 = (-2 * np.dot(x,x)) 
    print(ress1)
    print("Друга частина буде дорівнювати:")
    ress2 = (8 * x - 6 * np.identity(3, dtype=np.int16))
    print(ress2)
    print("Додамо дві частини функції між собою як задано у прикладі, та отримаємо наступний результат:")
    finalress = ress1 + ress2
    print(finalress)

f(A)