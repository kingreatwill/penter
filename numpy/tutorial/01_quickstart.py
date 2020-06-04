# https://numpy.org/doc/stable/user/quickstart.html
import sys

import numpy as np

print("------------基础属性")
a = np.arange(15).reshape(3, 5)
print(a)
"""
[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]]
"""
print(a.data)  # <memory at 0x000001CF2B9E7048>
print(a.shape)  # (3, 5)
print(a.ndim)  # 2
print(a.dtype.name)  # int32
print(a.itemsize)  # 4
print(a.size)  # 15
print(type(a))  # <class 'numpy.ndarray'>
b = np.array([6, 7, 8])
print(b)  # [6 7 8]
print(type(b))  # <class 'numpy.ndarray'>
print("--------------创建数组的方法")

print(np.array([1, 2, 3, 4]))
print(np.array((1, 2, 3, 4)))
print(np.array([(1.5, 2, 3), [4, 5, 6]]))
print(np.array([(1.5, 2, 3), (4, 5, 6)]))

print(np.zeros((3, 4)))

print(np.ones((2, 3, 4), dtype=np.int16))

print(np.empty((2, 3)))

print(np.arange(10, 30, 5))

print(np.linspace(0, 2, 9))  # 9 numbers from 0 to 2
x = np.linspace(0, 2 * np.pi, 10)
print(np.sin(x))

"""
See also
array, zeros, zeros_like, ones, ones_like, empty, empty_like, arange, linspace, 
numpy.random.RandomState.rand, 
numpy.random.RandomState.randn, 
fromfunction, 
fromfile
"""
print("--------------")
print(np.arange(10000))
# [   0    1    2 ... 9997 9998 9999]
# 若要禁用此行为并强制NumPy打印整个数组，可以使用set_printoptions更改打印选项。
# np.set_printoptions(threshold=sys.maxsize)
# 保证所有数据能够显示，而不是用省略号表示，np.inf表示一个足够大的数
#np.set_printoptions(threshold = np.inf)
# 若想不以科学计数显示:
#np.set_printoptions(suppress = True)



a = np.floor(10 * np.random.random((3, 4)))
print(a)

# 是扁平
print(a.ravel())
print(a.flatten())

a.resize((2, 6))
print(a)
# ndarray.shape, reshape, resize, ravel

c = a.view()
print(c)
c[0, 4] = 1234
print(a)

print("-----------Indexing with Arrays of Indices")
a = np.arange(12) ** 2  # the first 12 square numbers
i = np.array([1, 1, 3, 8, 5])  # an array of indices
print(a[i])  # the elements of a at the positions i

j = np.array([[3, 4], [9, 7]])  # a bidimensional array of indices
print(a[j])  # the same shape as j

palette = np.array([[0, 0, 0],  # black
                    [255, 0, 0],  # red
                    [0, 255, 0],  # green
                    [0, 0, 255],  # blue
                    [255, 255, 255]])  # white
image = np.array([[0, 1, 2, 0],  # each value corresponds to a color in the palette
                  [0, 3, 4, 0]])
print(palette[image])  # the (2,4,3) color image
print("-----")
a = np.arange(12).reshape(3, 4)
print(a)

i = np.array([[0, 1],  # indices for the first dim of a
              [1, 2]])
j = np.array([[2, 1],  # indices for the second dim
              [3, 3]])
print("-----")
print(a[i, j])  # i and j must have equal shape
print("-----")
print(a[i, 2])
print("-----")
print(a[:, j])  # i.e., a[ : , j]

a = np.arange(12).reshape(3, 4)
b1 = np.array([False, True, True])  # first dim selection
b2 = np.array([True, False, True, False])  # second dim selection

print(a[b1, :])  # selecting rows

print(a[b1])  # same thing

print(a[:, b2])  # selecting columns

print(a[b1, b2])  # a weird thing to do
