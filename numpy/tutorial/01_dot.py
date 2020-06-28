import numpy as np
# 矩阵乘法的几何意义 https://zhuanlan.zhihu.com/p/64606322
# 矩阵乘法  矩阵积 点积  matrix product
a = np.array([[4, 5], [6, 7]])
b = np.arange(4).reshape((2, 2))
print(a)
# [[4 5]
#  [6 7]]
print(b)
# [[0 1]
#  [2 3]]
# 矩阵乘法
c_dot = np.dot(a,b)
print(c_dot)
# [[10 19]
#  [14 27]]
c_dot_2 = a.dot(b)
# [[10 19]
#  [14 27]]
print(a @ b)

print(a * b)
"""
a1,1 * b1,1 + a1,2 * b2,1 + a1,n * bn,1  ,  a1,1 * b1,2 + a1,2 * b2,2 + a1,n * bn,2
a2,1 * b1,1 + a2,2 * b2,1 + a2,n * bn,1  ,  a2,1 * b1,2 + a2,2 * b2,2 + a2,n * bn,2
= A 的行数 ，B的列数
= [
[4*0+5*2,4*1+5*3],
[6*0+7*2,6*1+7*3]
]
"""



