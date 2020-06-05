# https://pandas.pydata.org/docs/user_guide/index.html#user-guide
import numpy as np
import pandas as pd

"""
Numpy 和 Pandas 有什么不同 ¶
如果用 python 的列表和字典来作比较, 那么可以说 Numpy 是列表形式的，没有数值标签，而 Pandas 就是字典形式。
Pandas是基于Numpy构建的，让Numpy为中心的应用变得更加简单。
要使用pandas，首先需要了解他主要两个数据结构：Series和DataFrame。
"""

s = pd.Series([1, 3, 5, np.nan, 6, 8])
# Series的字符串表现形式为：索引在左边，值在右边。由于我们没有为数据指定索引。于是会自动创建一个0到N-1（N为长度）的整数型索引。
print(s)


dates = pd.date_range('20130101', periods=6)
print(dates)

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD')) # ['A','B','C','D']

print(df)
"""
DataFrame是一个表格型的数据结构，它包含有一组有序的列，每列可以是不同的值类型（数值，字符串，布尔值等）。
DataFrame既有行索引也有列索引， 它可以被看做由Series组成的大字典。

我们可以根据每一个不同的索引来挑选数据, 比如挑选 b 的元素:
"""

print(df['B'])

"""
我们在创建一组没有给定行标签和列标签的数据 df1:

df1 = pd.DataFrame(np.arange(12).reshape((3,4)))
print(df1)

```
   0  1   2   3
0  0  1   2   3
1  4  5   6   7
2  8  9  10  11
```
这样,他就会采取默认的从0开始 index. 
"""
'''
还有一种生成 df 的方法, 如下 df2:

"""
     A          B    C  D      E    F
0  1.0 2013-01-02  1.0  3   test  foo
1  1.0 2013-01-02  1.0  3  train  foo
2  1.0 2013-01-02  1.0  3   test  foo
3  1.0 2013-01-02  1.0  3  train  foo
'''
df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20130102'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'foo'})

print(df2)

print(df2.dtypes)

print(df2.index)

print(df2.columns)
print(df2.values)

# 统计
print(df2.describe())

# 对数据的 index 进行排序并输出
print(df2.sort_index(axis=1, ascending=False))

# 对数据 值 排序输出
print(df2.sort_values(by='E'))


import matplotlib.pyplot as plt

# 随机生成1000个数据
data = pd.Series(np.random.randn(1000),index=np.arange(1000))

# 为了方便观看效果, 我们累加这个数据
data = data.cumsum()
# pandas 数据可以直接观看其可视化形式
data.plot()
plt.show()