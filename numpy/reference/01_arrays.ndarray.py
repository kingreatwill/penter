# https://numpy.org/doc/stable/reference/arrays.ndarray.html
"""
Array Creation
arange, array, copy, empty, empty_like, eye, fromfile, fromfunction, identity, linspace, logspace, mgrid, ogrid, ones, ones_like, r, zeros, zeros_like

Conversions
ndarray.astype, atleast_1d, atleast_2d, atleast_3d, mat

Manipulations
array_split, column_stack, concatenate, diagonal, dsplit, dstack, hsplit, hstack, ndarray.item, newaxis, ravel, repeat, reshape, resize, squeeze, swapaxes, take, transpose, vsplit, vstack

Questions
all, any, nonzero, where

Ordering
argmax, argmin, argsort, max, min, ptp, searchsorted, sort

Operations
choose, compress, cumprod, cumsum, inner, ndarray.fill, imag, prod, put, putmask, real, sum

Basic Statistics
cov, mean, std, var

Basic Linear Algebra
cross, dot, outer, linalg.svd, vdot

"""
import numpy as np

x = np.array([[1, 2, 3], [4, 5, 6]], np.int32)
print("-----------ndarray attributes")
# Memory layout相关属性
print(x.flags)  # 有关阵列的内存布局的信息。
print(x.shape)
print(x.strides)  # 元组字节，在遍历数组时在每个维度中单步执行。
print(x.ndim)
print(x.data)
print(x.size)
print(x.itemsize)
print(x.nbytes)
print(x.base)  # 如果内存来自其他对象，则使用基对象。
# Data type https://numpy.org/doc/stable/reference/arrays.dtypes.html#arrays-dtypes
print(x.dtype)
# Other 属性
print(x.T)
print(x.real)
print(x.flat)
print(x.imag)
print(x.ctypes)
# Array interface https://numpy.org/doc/stable/reference/arrays.interface.html#arrays-interface
print(x.__array_interface__)
print(x.__array_struct__)

print("-------------ndArray methods")
print(" ---------------转换 methods")
print(x.item(3), x[1, 0])
print(x.tolist())
x.itemset(3, 0)
print(x)
x.itemset((1, 1), 9)
print(x)

print(x.astype(np.float))
print(x.copy())
print(x.view())

print(x.getfield(np.int))
"""
>>> x = np.diag([1.+1.j]*2)
>>> x[1, 1] = 2 + 4.j
>>> x
array([[1.+1.j,  0.+0.j],
       [0.+0.j,  2.+4.j]])
>>> x.getfield(np.float64)
array([[1.,  0.],
       [0.,  2.]])
"""
x.fill(1)
print(x)
print(x.flags)
x.setflags(write=0, align=0)
print(x.flags)

# x.setflags(write=0, align=0) 出错了 write =false了
# x.fill(2)
# print(x)

print(" ---------------形状操纵 methods")
# view相当于传引用，view和原始数据共享一份数据，修改一个会影响另一个。
"""
ndarray.reshape(shape[, order])         Returns an array containing the same data with a new shape.
ndarray.resize(new_shape[, refcheck])   Change shape and size of array in-place.
ndarray.transpose(*axes)                Returns a view of the array with axes transposed.
ndarray.swapaxes(axis1, axis2)          Return a view of the array with axis1 and axis2 interchanged.
ndarray.flatten([order])                Return a copy of the array collapsed into one dimension.
ndarray.ravel([order])                  Return a flattened array.
ndarray.squeeze([axis])                 Remove single-dimensional entries from the shape of a.
转置(transpose)和轴对换(swapaxes)
"""
a = np.array([[1], [4]], np.int32)
print(a.squeeze())
print(a.squeeze(axis=1))
a = np.array([[[0], [1], [2]]])
print(a.squeeze(axis=0))
print("--")
x = np.array([[1, 2, 3]])
print(np.swapaxes(x, 0, 1))
print("--")
x = np.array([[[0, 1], [2, 3]], [[4, 5], [6, 7]]])
print(x, "------", x[0, 1, 1])
# 比如 x[0,1,1]=2 第一维度，1第二维度，1第三维度
x_swap = x.swapaxes(0, 2)  # #就是将第一个维度和第三个维度交换
# 那么x_swap[1,1,0] = 2
print(x_swap, "------", x_swap[1, 1, 0])

print(" -------------------------item 选择和操作 methods")

a = [4, 3, 5, 7, 6, 8]
indices = [0, 1, 4]
print(np.take(a, indices))

a = np.array(a)
print(a[indices])

print(np.take(a, [[0, 1], [2, 3]]))


a = np.arange(5)
np.put(a, [0, 2], [-44, -55])
print(a)

