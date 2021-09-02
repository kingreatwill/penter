import numpy as np
#from scipy.linalg import eig
# from sympy import Matrix
#
# print("------------------对角化矩阵-------------------")
# M = Matrix([[0.2,0.7,0.1],[0.01,0.99,0],[0.3,0.3,0.4]])
# P, D = M.diagonalize() # 对角化矩阵
# print(P)
# print("对角矩阵 D：")
# print(D)
# K = Matrix([[1,0,0],[0,0,0],[0,0,0]])
# # K = D的k次方

C = np.mat("0 1;1 0")
c0 = np.linalg.eigvals(C)
print(c0)
c1, c2 = np.linalg.eig(C)

print(c1, c2)