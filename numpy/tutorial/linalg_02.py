import numpy as np
from sympy import Matrix

A = np.array([[2, 3, 1, 0], [4, -1, 9, 0], [3, 8, -2, 0], [1, -2, 4, 0]])
# 将numpy.array转为sympy.Matrix
MA = Matrix(A)
print(MA.rref()) # 行简化阶梯型

print(MA.LUdecomposition()) # LU 分解
