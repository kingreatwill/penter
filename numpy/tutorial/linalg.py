import numpy as np

# numpy.linalg模块包含线性代数的函数。使用这个模块，可以计算逆矩阵、求特征值、解线性方程组以及求解行列式等。
print("-----逆矩阵---------")
A = np.mat("0 1 2;1 0 3;4 -3 8")
# 逆矩阵（非奇异矩阵才有逆矩阵）
print(np.linalg.inv(A))
print(A * np.linalg.inv(A))
print("-----求解形如 Ax = b 的线性方程组，其中 A 为矩阵，b 为一维或二维的数组，x 是未知变量---------")
B = np.mat("1 -2 1;0 2 -8;-4 5 9")
b = np.array([0, 8, -9])
x = np.linalg.solve(B, b)
print(x)
print(np.dot(B, x))  # 验证
print("-----LU分解(还有个LDU分解)---------")
# 数值分析实验之矩阵的LU分解及在解线性方程组中的应用 https://www.cnblogs.com/ynly/p/12879529.html
def decA(A):
    A = np.array(A)
    n = len(A)
    L = np.zeros((n, n))
    U = np.zeros((n, n))
    U[0, :] = A[0, :]
    L[:, 0] = A[:, 0] / U[0, 0]
    for i in range(n):
        L[i, i] = 1
    for row in range(n - 1):
        flag = 1
        for col in range(row, n - 1):
            U[row + 1, col + 1] = A[row + 1, col + 1] - np.dot(L[row + 1, :], U[:, col + 1])  # 计算U矩阵非零元素
            if (row + 2 < n) & (flag == 1):  # 计算L矩阵非零元素
                for k in range(1, row + 2):
                    L[row + 2, k] = (A[row + 2, k] - np.dot(L[row + 2, :], U[:, k])) / U[k, k]
            flag += 1
    print("U = ", U)
    print("L = ", L)


A = [[10, 7, 8, 7],
     [7, 5, 6, 5],
     [8, 6, 10, 9],
     [7, 5, 9, 10]]
decA(A)
print("-----特征值和特征向量---------")
'''
Ax = ax
A是n阶方阵，x是n*1的列向量（！=0），a是一个数字(可以等于0)

a 就是A的特征值，x是a的特征向量

Ax = ax这个过程，可以看成是线性替换，从方阵到数字，相当于空间转换

解题思路：
ax - Ax = 0
aEx - Ax = 0
aEx - Ax = 0
(aE - A)x = 0
-> 相当于求非零解  也就是(行列式)|aE - A| = 0

性质：
n个特征值相加=主对角元素相加
n个特征值相乘=|A|(A的行列式)
'''
# 特征值（eigenvalue）即方程 Ax = ax 的根，是一个标量。其中，A 是一个二维矩阵，x 是一个一维向量。特征向量（eigenvector）是关于特征值的向量
# numpy.linalg模块中，eigvals函数可以计算矩阵的特征值，而eig函数可以返回一个包含特征值和对应的特征向量的元组
C = np.mat("3 -2;1 0")
# 调用eigvals函数求解特征值
c0 = np.linalg.eigvals(C)
print(c0)  # [2. 1.] 结果可能是多个（或者说一定是n个，n是A方阵的阶数，重根就是解出来的特征值有相等的）
# 使用eig函数求解特征值和特征向量 (该函数将返回一个元组，按列排放着特征值和对应的特征向量，其中第一列为特征值，第二列为特征向量)
c1, c2 = np.linalg.eig(C)
print(c1, c2)

# 使用dot函数验证求得的解是否正确
for i in range(len(c1)):
    print("left:", np.dot(C, c2[:, i]))
    print("right:", c1[i] * c2[:, i])

I = np.mat("1 0;0 1")  # I 或者E是 单位向量
# 验证  det(A - 特征值@I) = 0  ;其中I是单位向量
print(np.linalg.det(C - np.dot(c1[0], I)))
print(np.linalg.det(C - np.dot(c1[1], I)))

print("-----奇异值分解---------")
# SVD（Singular Value Decomposition，奇异值分解）是一种因子分解运算，将一个矩阵分解为3个矩阵的乘积
# numpy.linalg模块中的svd函数可以对矩阵进行奇异值分解。该函数返回3个矩阵——
# U、Sigma和V，其中U和V是正交矩阵，Sigma包含输入矩阵的奇异值。
D = np.mat("4 11 14;8 7 -2")
U, Sigma, V = np.linalg.svd(D, full_matrices=False)
print("U:", U)
print("Sigma:", Sigma) #Sigma是奇异值组成的对角矩阵， 奇异值越大的时候，代表的信息越多 ，注意：linalg为了节省空间，对角矩阵以一维向量返回
print("V", V)

print("Sigma 矩阵:", np.diag(Sigma))

# 结果包含等式中左右两端的两个正交矩阵U和V，以及中间的奇异值矩阵Sigma
# 使用diag函数生成完整的奇异值矩阵。将分解出的3个矩阵相乘
print(U * np.diag(Sigma) * V)

print("-----广义逆矩阵---------")
"""
伪逆矩阵：
伪逆矩阵是逆矩阵的广义形式。由于奇异矩阵或非方阵的矩阵不存在逆矩阵，但在matlab里可以用函数pinv(A)求其伪逆矩阵

若A不是方阵，或者|A|=0，那么只能求A的伪逆，所谓伪逆是通过SVD计算出来的；
"""
print("广义逆矩阵-右逆:")
# 使用numpy.linalg模块中的pinv函数进行求解,
# 注：inv函数只接受方阵作为输入矩阵，而pinv函数则没有这个限制
E = np.mat("4 11 14;8 7 -2")
pseudoinv = np.linalg.pinv(E)  # 使用pinv函数计算广义逆矩阵
print(pseudoinv)
# 将原矩阵和得到的广义逆矩阵相乘
print(E * pseudoinv)
"""
E = np.mat("4 11 14;8 7 -2")
E 2*3

pseudoinv = pinv(E) =（E的转置*E）的逆*E的转置

行满秩，所以pseudoinv也称为右逆；
列满秩，则是左逆，如下
"""
print("广义逆矩阵-左逆:")
A = np.mat("4 8;11 7;14 -2")
A_1 = np.linalg.pinv(A)
print(A_1)
print(A_1*A)
print("-----行列式---------")
F = np.mat("3 4;5 6")
print(np.linalg.det(F))
