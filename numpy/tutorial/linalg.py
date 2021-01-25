import numpy as np

# numpy.linalg模块包含线性代数的函数。使用这个模块，可以计算逆矩阵、求特征值、解线性方程组以及求解行列式等。
print("-----逆矩阵---------")
A = np.mat("0 1 2;1 0 3;4 -3 8")
# 逆矩阵
print(np.linalg.inv(A))
print(A * np.linalg.inv(A))
print("-----求解形如 Ax = b 的线性方程组，其中 A 为矩阵，b 为一维或二维的数组，x 是未知变量---------")
B = np.mat("1 -2 1;0 2 -8;-4 5 9")
b = np.array([0, 8, -9])
x = np.linalg.solve(B, b)
print(x)
print(np.dot(B, x))  # 验证
print("-----特征值和特征向量---------")
# 特征值（eigenvalue）即方程 Ax = ax 的根，是一个标量。其中，A 是一个二维矩阵，x 是一个一维向量。特征向量（eigenvector）是关于特征值的向量
# numpy.linalg模块中，eigvals函数可以计算矩阵的特征值，而eig函数可以返回一个包含特征值和对应的特征向量的元组
C = np.mat("3 -2;1 0")
# 调用eigvals函数求解特征值
c0 = np.linalg.eigvals(C)
print(c0)
# 使用eig函数求解特征值和特征向量 (该函数将返回一个元组，按列排放着特征值和对应的特征向量，其中第一列为特征值，第二列为特征向量)
c1, c2 = np.linalg.eig(C)
print(c1, c2)

# 使用dot函数验证求得的解是否正确
for i in range(len(c1)):
    print("left:", np.dot(C, c2[:, i]))
    print("right:", c1[i] * c2[:, i])

I = np.mat("1 0;0 1")
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
print("Sigma:", Sigma)
print("V", V)

# 结果包含等式中左右两端的两个正交矩阵U和V，以及中间的奇异值矩阵Sigma
# 使用diag函数生成完整的奇异值矩阵。将分解出的3个矩阵相乘
print(U * np.diag(Sigma) * V)

print("-----广义逆矩阵---------")
# 使用numpy.linalg模块中的pinv函数进行求解,
# 注：inv函数只接受方阵作为输入矩阵，而pinv函数则没有这个限制
E = np.mat("4 11 14;8 7 -2")
pseudoinv = np.linalg.pinv(E)  # 使用pinv函数计算广义逆矩阵
print(pseudoinv)
# 将原矩阵和得到的广义逆矩阵相乘
print(E * pseudoinv)
print("-----行列式---------")
F = np.mat("3 4;5 6")
print(np.linalg.det(F))
