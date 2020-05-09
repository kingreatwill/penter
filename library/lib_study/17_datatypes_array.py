# 高效的数值数组
import array

# https://docs.python.org/zh-cn/3/library/array.html

print(array.typecodes) # 包含所有可用类型码的字符串。

a = array.array('f')
a.append(1)
print(a)

a = array.array('B') # 0-255
a.append(255)
print(a)

print(a.typecode)
print(a.itemsize)

"""
array('l')
array('u', 'hello \u2641')
array('l', [1, 2, 3, 4, 5])
array('d', [1.0, 2.0, 3.14])
"""



