import numpy as np
from sympy import Matrix

A = np.array([[2, 3, 1, 0], [4, -1, 9, 0], [3, 8, -2, 0], [1, -2, 4, 0]])
# 将numpy.array转为sympy.Matrix
MA = Matrix(A)
print("------------------行简化阶梯型-------------------")
print(MA.rref()) # 行简化阶梯型


print("------------------对角化矩阵-------------------")
M = Matrix([[3,-2,4,-2],[5,3,-3,-2],[5,-2,2,-2],[5,-2,-3,3]])
P, D = M.diagonalize() # 对角化矩阵
print(P)
print("对角矩阵 D：")
print(D)

print("------------------LU 分解-------------------")
print(MA.LUdecomposition()) # LU 分解
from scipy.linalg import lu
B = np.array([[2, 5, 8, 7], [5, 2, 2, 8], [7, 5, 6, 6], [5, 4, 4, 8]])
p, l, u = lu(B)

print("------------------QR 分解-------------------")
print(MA.QRdecomposition()) # QR 分解
# (把矩阵分解成一个正交矩阵与一个上三角矩阵的积 ,Q 是正交矩阵（意味着 QTQ = I）而 R 是上三角矩阵,此外，原矩阵A不必为正方矩阵； 如果矩阵A大小为n*m，则矩阵Q大小为n*m，矩阵R大小为m*m。)

