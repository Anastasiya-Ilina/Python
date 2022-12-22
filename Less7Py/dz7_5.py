import numpy as np
import random as rn

A = np.array([[rn.randint(-100, 100), rn.randint(-100, 100), rn.randint(-100, 100)],
             [rn.randint(-100, 100), rn.randint(-100, 100), rn.randint(-100, 100)],
             [rn.randint(-100, 100), rn.randint(-100, 100), rn.randint(-100, 100)]])

print('Исходная матрица\n', A)
print('Транспонированная матрица\n', A.T)
