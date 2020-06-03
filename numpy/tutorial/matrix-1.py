# matrix类是numpy中的一个过时的类，可能会在未来被移除。
import numpy as np
# 总结Numpy中matrix和ndarray的区别    https://blog.csdn.net/wzyaiwl/article/details/90552935

# matrix有两种构造方式，从第二种我们看到和一般的数组类型一模一样，在这里我们就能窥到matrix其实就是继承了ndarray，基于ndarray。拿matrix进行线性代数运算是因为它有很多方便的函数。
a = np.matrix('1 2; 3 4')
print(a)

print(np.matrix([[1, 2], [3, 4]]))
"""
matrix.T     transpose：返回矩阵的转置矩阵
matrix.H     hermitian (conjugate) transpose：返回复数矩阵的共轭元素矩阵
matrix.I     inverse：返回矩阵a逆矩阵
matrix.A     base array：返回矩阵基于的数组<br>matrix.AI　　 flattened ndarray: 返回展平的数组
"""
print(a.T)
print(a.H)
print(a.I)
print(a.A)

print("--------")
a1 = np.array([[1, 2], [3, 4]])

# 生成martix对象使用的是np.mat()方法
# np.mat([[1,2],[5,7]])
# np.mat(((1,2),(5,7),(7,9)))
# np.mat(np.array(((1,2),(5,7),(7,9))))
# np.mat("1,2,3;4,5,6")

# 生成ndarray对象
# 该对象生成的方式很多，如np.zeros()、np.empty()、np.ones()、np.array()等等

"""
两个对象之间的相互转化
对于两个对象之间的相互转化，在两个对象的生成中就讲过了。这里再次总结下。

从array()函数到mat()函数用np.asmatrix()或np.mat()
从mat()函数到array()函数用np.asarray()
"""

print(a1.T)  # 只有T
# ndarray类型同样能方便地进行转置和求逆
# matrix.I
a1_I = np.linalg.inv(a1)
print(a1_I)
# matrix.H
print(a1.transpose())
# matrix.A 就是a1本身
