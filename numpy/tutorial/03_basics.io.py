import numpy as np
from io import StringIO

data = u"1, 2, 3\n4, 5, 6"
a = np.genfromtxt(StringIO(data), delimiter=",")
print(a)
"""
[[1. 2. 3.]
 [4. 5. 6.]]
"""
data = u"  1  2  3\n  4  5 67\n8901234"
a = np.genfromtxt(StringIO(data), delimiter=3)
print(a)
"""
[[  1.   2.   3.]
 [  4.   5.  67.]
 [890. 123.   4.]]
"""

data = u"123456789\n   4  7 9\n   4567 9"
a= np.genfromtxt(StringIO(data), delimiter=(4, 3, 2))
print(a)
"""
[[1234.  567.   89.]
 [   4.    7.    9.]
 [   4.  567.    9.]]
"""


data = u"1, abc , 2\n 3, xxx, 4"
# Without autostrip
a = np.genfromtxt(StringIO(data), delimiter=",", dtype="|U5")
print(a)
"""
[['1' ' abc ' ' 2']
 ['3' ' xxx' ' 4']]
"""

# With autostrip 去掉空格
a = np.genfromtxt(StringIO(data), delimiter=",", dtype="|U5", autostrip=True)
print(a)
"""
[['1' 'abc' '2']
 ['3' 'xxx' '4']]
"""

print(a.dtype) # <U5

data = u"""#
# Skip me !
# Skip me too !
1, 2
3, 4
5, 6 #This is the third line of the data
7, 8
# And here comes the last line
9, 0
"""
a = np.genfromtxt(StringIO(data), comments="#", delimiter=",")
print(a)

data = u"\n".join(str(i) for i in range(10))
np.genfromtxt(StringIO(data),)
# [ 0.,  1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9.]
np.genfromtxt(StringIO(data),skip_header=3, skip_footer=5)
# [ 3.,  4.]

data = u"1 2 3 4\n5 6 7 8"
print(np.genfromtxt(StringIO(data), usecols=(0, -1)))
"""
[[1. 4.]
 [5. 8.]]
"""