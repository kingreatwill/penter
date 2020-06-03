import time
# https://morvanzhou.github.io/tutorials/data-manipulation/np-pd/2-7-np-split/
import numpy as np

# numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)
"""
参数说明：

名称	描述
object	数组或嵌套的数列
dtype	数组元素的数据类型，可选
copy	对象是否需要复制，可选
order	创建数组的样式，C为行方向，F为列方向，A为任意方向（默认）
subok	默认返回一个与基类类型一致的数组
ndmin	指定生成数组的最小维度
"""
a = np.array([1, 2, 3])
print(a)

a = np.array([[1, 2], [3, 4]])
print(a)

# 最小维度
a = np.array([1, 2, 3, 4, 5], ndmin=3)
print(a)
print(a.ndim, a.shape, a.size)

# dtype 参数

a = np.array([1, 2, 3], dtype=complex)
print(a)
a2 = np.array([1, 2, 3], dtype=np.complex)
print(a2)
print("----------------索引")
A = np.arange(3,15).reshape((3,4))
print(A[2])
# [11 12 13 14]
print(A[1][1])      # 8
print(A[1, 1])      # 8
print(A[1, 1:3])    # [8 9]
# 使变平
print(A.flatten())
# array([3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
print(list(A.flat))
# list([3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
print("----------------基础属性")
"""
ndim：维度
shape：行数和列数
size：元素个数
dtype:
itemsize:每个元素的大小，float64 的为8  complex32 的为4
data: 
"""
array = np.array([[1, 2, 3], [2, 3, 4]])  # 列表转化为矩阵
print('number of dim:', array.ndim)  # 维度
# number of dim: 2

print('shape :', array.shape)  # 行数和列数
# shape : (2, 3)

print('size:', array.size)  # 元素个数
# size: 6

print("---------创建array")
"""
array：创建数组
dtype：指定数据类型
zeros：创建数据全为0
ones：创建数据全为1
empty：创建数据接近0
arrange：按指定范围创建数据
linspace：创建线段
"""
a = np.zeros((3, 4))  # 数据全为0，3行4列
print(a)

a = np.ones((3, 4), dtype=np.int)  # 数据为1，3行4列
print(a)

# 创建全空数组, 其实每个值都是接近于零的数:
# a = np.empty((3,4)) # 数据为empty，3行4列
print("--")
print(np.empty((3, 4)))
print(np.empty((3, 4), dtype=int))
print(np.empty((3, 4), dtype=np.int))
print("--")
"""
对 np.empty 的理解有点小问题，np.empty 分配指定的数组空间后不初始化，
所以，np.empty 后打印出来的东西每次不一定是一样的，而并不是接近于 0 的数字，
这个方法最大的好处就是速度快，因为少了初始化空间的操作
"""

a = np.arange(10, 20, 2)  # 10-19 的数据，2步长
print(a)

# 使用 reshape 改变数据的形状
a = np.arange(12).reshape((3, 4))  # 3行4列，0到11
print(a)

# 用 linspace 创建线段型数据:
a = np.linspace(1, 10, 20)  # 开始端1，结束端10，且分割成20个数据，生成线段
print(a)

print("---------numpy 的几种基本运算")
a = np.array([10, 20, 30, 40])  # array([10, 20, 30, 40])
b = np.arange(4)  # array([0, 1, 2, 3])

c = a - b  # array([10, 19, 28, 37])
print(c)
c = a + b  # array([10, 21, 32, 43])
print(c)
c = a * b  # array([  0,  20,  60, 120])
print(c)
c = b ** 2  # array([0, 1, 4, 9])
print(c)

# 数学函数
c = 10 * np.sin(a)
# array([-5.44021111,  9.12945251, -9.88031624,  7.4511316 ])
print(c)

# 返回的是一个bool类型的矩阵
print(b < 3)
# array([ True,  True,  True, False], dtype=bool)

print(b == 3)
# [False False False  True]

# 多维操作
a = np.array([[1, 1], [0, 1]])
b = np.arange(4).reshape((2, 2))

print(a)
# array([[1, 1],
#       [0, 1]])

print(b)
# array([[0, 1],
#       [2, 3]])

# 矩阵乘法
c_dot = np.dot(a, b)
print(c_dot)
# array([[2, 4],
#       [2, 3]])
c_dot_2 = a.dot(b)
# array([[2, 4],
#       [2, 3]])

a = np.random.random((2, 4))
print(a)
# array([[ 0.94692159,  0.20821798,  0.35339414,  0.2805278 ],
#       [ 0.04836775,  0.04023552,  0.44091941,  0.21665268]])
np.sum(a)  # 4.4043622002745959
np.min(a)  # 0.23651223533671784
np.max(a)  # 0.90438450240606416

print("a =", a)
# a = [[ 0.23651224  0.41900661  0.84869417  0.46456022]
# [ 0.60771087  0.9043845   0.36603285  0.55746074]]

"""
如果你需要对行或者列进行查找运算，就需要在上述代码中为 axis 进行赋值。 
当axis的值为0的时候，将会以列作为查找单元， 当axis的值为1的时候，将会以行作为查找单元。
"""
print("sum =", np.sum(a, axis=1))
# sum = [ 1.96877324  2.43558896]

print("min =", np.min(a, axis=0))
# min = [ 0.23651224  0.41900661  0.36603285  0.46456022]

print("max =", np.max(a, axis=1))
# max = [ 0.84869417  0.9043845 ]


A = np.arange(2, 14).reshape((3, 4))

# array([[ 2, 3, 4, 5]
#        [ 6, 7, 8, 9]
#        [10,11,12,13]])

print(np.argmin(A))  # 0
print(np.argmax(A))  # 11
# 其中的 argmin() 和 argmax() 两个函数分别对应着求矩阵中最小元素和最大元素的索引。
# 相应的，在矩阵的12个元素中，最小值即2，对应索引0，最大值为13，对应索引为11。

# 均值
print(np.mean(A))  # 7.5 均值，通常指算术平均，也可以是几何平均
print(np.average(A))  # 7.5 均值，通常指算术平均
print(A.mean())  # 7.5

# 中位数
print(np.median(A))  # 7.5 (7+8/2) 中间值
print(np.median(np.array([1, 4, 5, 6])))  # 4.5

# 累加函数
print(np.cumsum(A))
# [2 5 9 14 20 27 35 44 54 65 77 90]

# 累差运算函数
print(np.diff(A))
# 该函数计算的便是每一行中后一项与前一项之差
# 故一个3行4列矩阵通过函数计算得到的矩阵便是3行3列的矩阵



print(print(np.nonzero(A)))
# (array([0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2], dtype=int64), array([0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3], dtype=int64))
# 这个函数将所有非零元素的行与列坐标分割开，重构成两个分别关于行和列的矩阵。


A = np.arange(14,2, -1).reshape((3,4))

# array([[14, 13, 12, 11],
#       [10,  9,  8,  7],
#       [ 6,  5,  4,  3]])

print(np.sort(A))

# array([[11,12,13,14]
#        [ 7, 8, 9,10]
#        [ 3, 4, 5, 6]])


# 矩阵的转置有两种表示方法：
print(np.transpose(A))
print(A.T)

# array([[14,10, 6]
#        [13, 9, 5]
#        [12, 8, 4]
#        [11, 7, 3]])
# array([[14,10, 6]
#        [13, 9, 5]
#        [12, 8, 4]
#        [11, 7, 3]])

print(A)
# array([[14,13,12,11]
#        [10, 9, 8, 7]
#        [ 6, 5, 4, 3]])

print(np.clip(A,5,9))
# array([[ 9, 9, 9, 9]
#        [ 9, 9, 8, 7]
#        [ 6, 5, 5, 5]])

"""
这个函数的格式是clip(Array,Array_min,Array_max)，
顾名思义，Array指的是将要被执行用的矩阵，
而后面的最小值最大值则用于让函数判断矩阵中元素是否有比最小值小的或者比最大值大的元素，
并将这些指定的元素转换为最小值或者最大值。
"""

# 在 Numpy 中, 创建 2D Array 的默认方式是 “C-type” 以 row 为主在内存中排列,
# 而如果是 “Fortran” 的方式创建的, 就是以 column 为主在内存中排列.

col_major = np.zeros((10,10), order='C')    # C-type
row_major = np.zeros((10,10), order='F')    # Fortran


a = np.zeros((200, 200), order='C')
b = np.zeros((200, 200), order='F')
N = 9999

def f1(a):
    for _ in range(N):
        np.concatenate((a, a), axis=0)

def f2(b):
    for _ in range(N):
        np.concatenate((b, b), axis=0)

t0 = time.time()
f1(a)
t1 = time.time()
f2(b)
t2 = time.time()

print((t1-t0)/N)     # 0.000040
print((t2-t1)/N)     # 0.000070

# https://morvanzhou.github.io/tutorials/data-manipulation/np-pd/4-1-speed-up-numpy/

print("-------Numpy array 合并")
A = np.array([1, 1, 1])
B = np.array([2, 2, 2])

# 上下合并
print(np.vstack((A, B)))  # vertical stack
"""
[[1,1,1]
 [2,2,2]]
"""
# 左右合并
D = np.hstack((A,B))       # horizontal stack
print(D)
# [1,1,1,2,2,2]


# np.newaxis() 新轴
print(A[np.newaxis,:])
# [[1 1 1]]

print(A[:,np.newaxis])
"""
[[1]
[1]
[1]]
"""

A = np.array([1, 1, 1])[:, np.newaxis]
B = np.array([2, 2, 2])[:, np.newaxis]

C = np.vstack((A, B))  # vertical stack
D = np.hstack((A, B))  # horizontal stack
print(C)
"""
[[1]
 [1]
 [1]
 [2]
 [2]
 [2]]
"""
print(D)
"""
[[1 2]
[1 2]
[1 2]]
"""

# np.concatenate() 使(成串地)连结[衔接]起来

C = np.concatenate((A,B,B,A),axis=0)
print(C)
"""
array([[1],
       [1],
       [1],
       [2],
       [2],
       [2],
       [2],
       [2],
       [2],
       [1],
       [1],
       [1]])
"""

D = np.concatenate((A,B,B,A),axis=1)

print(D)
"""
array([[1, 2, 2, 1],
       [1, 2, 2, 1],
       [1, 2, 2, 1]])
"""
# axis参数很好的控制了矩阵的纵向或是横向打印，相比较vstack和hstack函数显得更加方便。

print("----------------Numpy array 分割")
A = np.arange(12).reshape((3, 4))
print(A)
"""
array([[ 0,  1,  2,  3],
    [ 4,  5,  6,  7],
    [ 8,  9, 10, 11]])
"""
# 纵向分割
print(np.split(A, 2, axis=1))
"""
[array([[0, 1],
        [4, 5],
        [8, 9]]), array([[ 2,  3],
        [ 6,  7],
        [10, 11]])]
"""
# 横向分割
print(np.split(A, 3, axis=0))

# [array([[0, 1, 2, 3]]), array([[4, 5, 6, 7]]), array([[ 8,  9, 10, 11]])]
"""
范例的Array只有4列，只能等量对分，因此输入以上程序代码后Python就会报错。

print(np.split(A, 3, axis=1))
or print(np.split(A, 4, axis=0)) 只有3行 分四个
# ValueError: array split does not result in an equal division
为了解决这种情况, 我们会有下面这种方式.
"""
# 不等量的分割
print(np.array_split(A, 3, axis=1))
"""
[array([[0, 1],
        [4, 5],
        [8, 9]]), array([[ 2],
        [ 6],
        [10]]), array([[ 3],
        [ 7],
        [11]])]
"""

print(np.vsplit(A, 3)) #等于 print(np.split(A, 3, axis=0))
# [array([[0, 1, 2, 3]]), array([[4, 5, 6, 7]]), array([[ 8,  9, 10, 11]])]

print(np.hsplit(A, 2)) #等于 print(np.split(A, 2, axis=1))
"""
[array([[0, 1],
       [4, 5],
       [8, 9]]), array([[ 2,  3],
        [ 6,  7],
        [10, 11]])]
"""
print("--------Numpy copy & deep copy")
a = np.arange(4)
# array([0, 1, 2, 3])

b = a
c = a
d = b
a[0] = 11
print(a)
# array([11,  1,  2,  3])
# 改变a的第一个值，b、c、d的第一个值也会同时改变。同样更改d的值，a、b、c也会改变。
# b is a  # True
# c is a  # True
# d is a  # True

b = a.copy()    # deep copy
print(b)        # array([11, 22, 33,  3])
a[3] = 44
print(a)        # array([11, 22, 33, 44])
print(b)        # array([11, 22, 33,  3])