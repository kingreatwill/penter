# list
squares = [1, 4, 9, 16, 25]

newlist = squares[-3:]

newlist2 = squares + [36, 49, 64, 81, 100]
newlist2.append(2)
# append 等价于 newlist2[len(newlist2):]=[2]
newlist2.extend([1, 2, 3])
# 相当于 a[len(a):] = iterable

print(newlist2)
newlist2[2:5] = []
print(newlist2)
newlist2[2:5] = ['C', 'D', 'E']
print(newlist2)

del newlist2[0]

del newlist2[:]

"""
list.append(x)
在列表的末尾添加一个元素。相当于 a[len(a):] = [x] 。

list.extend(iterable)
使用可迭代对象中的所有元素来扩展列表。相当于 a[len(a):] = iterable 。

list.insert(i, x)
在给定的位置插入一个元素。第一个参数是要插入的元素的索引，所以 a.insert(0, x) 插入列表头部， a.insert(len(a), x) 等同于 a.append(x) 。

list.remove(x)
移除列表中第一个值为 x 的元素。如果没有这样的元素，则抛出 ValueError 异常。

list.pop([i])
删除列表中给定位置的元素并返回它。如果没有给定位置，a.pop() 将会删除并返回列表中的最后一个元素。（ 方法签名中 i 两边的方括号表示这个参数是可选的，而不是要你输入方括号。你会在 Python 参考库中经常看到这种表示方法)。

list.clear()
删除列表中所有的元素。相当于 del a[:] 。

list.index(x[, start[, end]])
返回列表中第一个值为 x 的元素的从零开始的索引。如果没有这样的元素将会抛出 ValueError 异常。

可选参数 start 和 end 是切片符号，用于将搜索限制为列表的特定子序列。返回的索引是相对于整个序列的开始计算的，而不是 start 参数。

list.count(x)
返回元素 x 在列表中出现的次数。

list.sort(key=None, reverse=False)
对列表中的元素进行排序（参数可用于自定义排序，解释请参见 sorted()）。

list.reverse()
反转列表中的元素。

list.copy()
返回列表的一个浅拷贝。相当于 a[:] 。
"""

"""
你可能已经注意到，像 insert ，remove 或者 sort 方法，只修改列表，没有打印出返回值——它们返回默认值 None 。这是Python中所有可变数据结构的设计原则。
你可能会注意到的另一件事是并非所有数据或可以排序或比较。 例如，[None, 'hello', 10] 就不可排序，因为整数不能与字符串比较，而 None 不能与其他类型比较。 
并且还存在一些没有定义顺序关系的类型。 例如，3+4j < 5+7j 就不是一个合法的比较。
"""

# 列表作为栈使用 append() pop()
# 列表作为队列使用
"""
列表也可以用作队列，其中先添加的元素被最先取出 (“先进先出”)；
然而列表用作这个目的相当低效。因为在列表的末尾添加和弹出元素非常快，但是在列表的开头插入或弹出元素却很慢 (因为所有的其他元素都必须移动一位)。
若要实现一个队列， collections.deque 被设计用于快速地从两端操作。例如
>>> from collections import deque
>>> queue = deque(["Eric", "John", "Michael"])
>>> queue.append("Terry")           # Terry arrives
>>> queue.append("Graham")          # Graham arrives
>>> queue.popleft()                 # The first to arrive now leaves
'Eric'
>>> queue.popleft()                 # The second to arrive now leaves
'John'
>>> queue                           # Remaining queue in order of arrival
deque(['Michael', 'Terry', 'Graham'])
"""

# 列表推导式
squares = []
for x in range(10):
    squares.append(x ** 2)

print(x)  # 9 注意这里创建（或被重写）的名为 x 的变量在for循环后仍然存在。

squares1 = list(map(lambda x: x ** 2, range(10)))
# 等价
squares2 = [x ** 2 for x in range(10)]

# 列表推导式 if
print([(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y])

# 嵌套的列表推导式
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
print([[row[i] for row in matrix] for i in range(4)])

print(list(zip(*matrix)))

# tuple元组  不可变
t = 12345, 54321, 'hello!'
x, y, z = t
print(t[0])
print(x)
t1 = (12345, 54321, 'hello!')

t2 = t, (1, 2, 3, 4, 5)
print(t2)
t3 = t, 1, 2, 3, 4, 5
print(t3)
t4 = *t, 1, 2, 3, 4, 5
print(t4)

# set
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
a = set('abracadabra')
b = set('alacazam')
print(a - b)  # 差集
print(a | b)  # 合集
print(a & b)  # 交集
print(a ^ b)  # 合集 - 交集

a = {x for x in 'abracadabra' if x not in 'abc'}
# 要创建一个空集合你只能用 set() 而不能用 {}，因为后者是创建一个空字典


# dic
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
del tel['sape']
tel['irv'] = 4127
print(tel)
print(dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]))
print(dict(sape=4139, guido=4127, jack=4098))
print({x: x ** 2 for x in (2, 4, 6)})

for k, v in tel.items():
    print(k, v)

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

print((1, 2, 3) < (1, 2, 4))
print([1, 2, 3] < [1, 2, 4])
print('ABC' < 'C' < 'Pascal' < 'Python')
print((1, 2, 3, 4) < (1, 2, 4))
print((1, 2) < (1, 2, -1))
print((1, 2, 3) == (1.0, 2.0, 3.0))
print((1, 2, ('aa', 'ab')) < (1, 2, ('abc', 'a'), 4))
