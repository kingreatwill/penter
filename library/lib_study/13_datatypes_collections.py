import collections

# class collections.ChainMap(*maps)
print("-------------class collections.ChainMap(*maps)")
a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
c = collections.ChainMap(a, b)
print(c)
# 如果有重复的键，那么会采用第一个映射中的所对应的值
print(c['z'])
print(len(c))
print(list(c.keys()))
print(list(c.values()))

# 修改映射操作总是会作用在列出的第一个映射结构上，会改变原始的第一个映射结构
# ChainMap使用就是原始字典，因此原始数据修改，ChainMap映射也会改变
c['z'] = 10
print(a)
print(c['z'])

del c['z']
print(a)
print(b)
print(c['z'])  # 4

# merged = dict(b)  # 创建一个新的字典
merged = b.copy()  # 创建一个新的字典
merged.update(a)  # update进入的键值会覆盖原来的键值对
print(merged)  # 这时a,b 和 merged就脱离关系了
"""
1、ChainMap可接受多个映射然后在逻辑上使它们表现为一个单独的映射结构；它只是维护了一个记录底层映射关系的列表，然后去重定义常用的字典操作；
2、如果有重复的键，会采用第一个映射中多对应的值；
3、修改ChainMap映射结构，会同时作用在自己和原始字典结构上；
4、可以使用字典的update()方法，来替代上面的合并方案；但是这就需要创建一个新的字典对象(或者修改原字典，破坏了原始数据)，并且原始字典做了修改，并不会反映到新建的字典上；
5、ChainMap使用的就是原始字典，因此原字典变，它也会改变。
"""
print("-------------")
print(c.maps)
# d.new_child() 调用等价于 ChainMap({}, *d.maps)
new_c = c.new_child()
print(new_c['x'])
new_c['x'] = 20  # 会新增一个，因为 ChainMap({}, *d.maps)中的{}
print(c)
print(new_c)
print(c.parents)  # 属性返回一个新的 ChainMap 包含所有的当前实例的映射，除了第一个
print(new_c.parents)  # d.parents 的引用等价于 ChainMap(*d.maps[1:])

"""
demo1:让用户指定的命令行参数优先于环境变量，优先于默认值的例子

import os, argparse

defaults = {'color': 'red', 'user': 'guest'}

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args()
command_line_args = {k: v for k, v in vars(namespace).items() if v is not None}

combined = ChainMap(command_line_args, os.environ, defaults)
print(combined['color'])
print(combined['user'])


demo2:用 ChainMap 类模拟嵌套上下文的例子
c = ChainMap()        # Create root context
d = c.new_child()     # Create nested child context
e = c.new_child()     # Child of c, independent from d
e.maps[0]             # Current context dictionary -- like Python's locals()
e.maps[-1]            # Root context -- like Python's globals()
e.parents             # Enclosing context chain -- like Python's nonlocals

d['x'] = 1            # Set value in current context
d['x']                # Get first key in the chain of contexts
del d['x']            # Delete from current context
list(d)               # All nested values
k in d                # Check all nested values
len(d)                # Number of nested values
d.items()             # All nested items
dict(d)               # Flatten into a regular dictionary

demo3:ChainMap 类只更新链中的第一个映射，但lookup会搜索整个链。 然而，如果需要深度写和删除，也可以很容易的通过定义一个子类来实现它

class DeepChainMap(ChainMap):
    'Variant of ChainMap that allows direct updates to inner scopes'

    def __setitem__(self, key, value):
        for mapping in self.maps:
            if key in mapping:
                mapping[key] = value
                return
        self.maps[0][key] = value

    def __delitem__(self, key):
        for mapping in self.maps:
            if key in mapping:
                del mapping[key]
                return
        raise KeyError(key)

>>> d = DeepChainMap({'zebra': 'black'}, {'elephant': 'blue'}, {'lion': 'yellow'})
>>> d['lion'] = 'orange'         # update an existing key two levels down
>>> d['snake'] = 'red'           # new keys get added to the topmost dict
>>> del d['elephant']            # remove an existing key one level down
>>> d                            # display result
DeepChainMap({'zebra': 'black', 'snake': 'red'}, {}, {'lion': 'orange'})

"""

print("-------------class collections.Counter([iterable-or-mapping])")

c = collections.Counter()
for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
    c[word] += 1
print(c)
del c["red"]
del c["red0"]
print(c["red0"])
print(c)
c["red0"] += 1
print(c["red0"])

c2 = collections.Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])
print(c2)
print(c2.most_common(2))
print(sorted(c2.elements()))  # elements() 方法要求正整数计数。忽略0和负数计数。
"""
统计文本中单词出现10次的单词
import re
words = re.findall(r'\w+', open('hamlet.txt').read().lower())
Counter(words).most_common(10)
"""
c.subtract(['red', 'blue', 'red', 'green', 'blue'])
print(c)

c = collections.Counter(a=4, b=2, c=0, d=-2)
d = collections.Counter(a=1, b=2, c=3, d=4)
c.subtract(d)
print(c)

# 没有实现 print(c.fromkeys(['red', 'blue', 'red', 'green', 'blue']))#NotImplementedError

d.update(a=2, b=2, c=3, d=4)  # 累加
print(d)

# c + d   c - d
# c & d  交集 min(c[x], d[x])
# c | d 并集:  max(c[x], d[x])

c = collections.Counter(a=3, b=1, c=2)
d = collections.Counter(a=1, b=2, d=2)
print(c + d)  # add two counters together:  c[x] + d[x]
print(c - d)  # subtract (keeping only positive counts)
print(c & d)  # intersection:  min(c[x], d[x])
print(c | d)  # union:  max(c[x], d[x])

c = collections.Counter(a=2, b=-4, c=0)
print(+c)  # 移除小于等于0的
print(-c)  # 移除大于等于0的，并且负数变正数

print("-----------------class collections.deque([iterable[, maxlen]]) 双向队列  重点")
# Deque队列是由栈或者queue队列生成的（发音是 “deck”，”double-ended queue”的简称）。Deque 支持线程安全，内存高效添加(append)和弹出(pop)，从两端都可以，两个方向的大概开销都是 O(1) 复杂度。
# 虽然 list 对象也支持类似操作，不过这里优化了定长操作和 pop(0) 和 insert(0, v) 的开销。它们引起 O(n) 内存移动的操作，改变底层数据表达的大小和位置。
# 如果 maxlen 没有指定或者是 None ，deques 可以增长到任意长度。否则，deque就限定到指定最大长度。一旦限定长度的deque满了，当新项加入时，同样数量的项就从另一端弹出。
# 限定长度deque提供类似Unix filter tail 的功能。它们同样可以用与追踪最近的交换和其他数据池活动。

deq = collections.deque()
deq.append(10)
print(deq)
deq.append(11)
print(deq)
deq.appendleft(9)
print(deq)
deq2 = deq.copy()  # 创建一份浅拷贝。
deq.clear()
print(deq)
print(deq2)
print(deq2.count(10))
print(len(deq2))
deq2.extend([12, 13])
print(deq2)
deq2.extendleft([8, 7])  # 注意顺序
print(deq2)
print(deq2.index(8))
deq2.insert(0, 6)
print(deq2)
print(deq2.pop())  # 最右侧的那一个,获取并移除
print(deq2)
print(deq2.popleft())  # 最左侧的那一个,获取并移除
print(deq2)

deq2.remove(10)
print(deq2)

deq2.reverse()
print(deq2)

"""
rotate(n=1)
向右循环移动 n 步。 如果 n 是负数，就向左循环。
如果deque不是空的，向右循环移动一步就等价于 d.appendleft(d.pop()) ， 向左循环一步就等价于 d.append(d.popleft()) 。
"""
print(deq2.rotate(2))
print(deq2)

print(deq2.maxlen)
"""
除了以上操作，deque 还支持迭代、封存、len(d)、reversed(d)、copy.copy(d)、copy.deepcopy(d)、成员检测运算符 in 以及下标引用例如通过 d[0] 访问首个元素等。 
索引访问在两端的复杂度均为 O(1) 但在中间则会低至 O(n)。 如需快速随机访问，请改用列表。
"""

"""
demo1:限长deque提供了类似Unix tail 过滤功能
def tail(filename, n=10):
    'Return the last n lines of a file'
    with open(filename) as f:
        return deque(f, n)
        
demo2:另一个用法是维护一个近期添加元素的序列，通过从右边添加和从左边弹出
def moving_average(iterable, n=3):
    # moving_average([40, 30, 50, 46, 39, 44]) --> 40.0 42.0 45.0 43.0
    # http://en.wikipedia.org/wiki/Moving_average
    it = iter(iterable)
    d = deque(itertools.islice(it, n-1))
    d.appendleft(0)
    s = sum(d)
    for elem in it:
        s += elem - d.popleft()
        d.append(elem)
        yield s / n

demo3:一个 轮询调度器 可以通过在 deque 中放入迭代器来实现。值从当前迭代器的位置0被取出并暂存(yield)。 如果这个迭代器消耗完毕，就用 popleft() 将其从对列中移去；否则，就通过 rotate() 将它移到队列的末尾
def roundrobin(*iterables):
    "roundrobin('ABC', 'D', 'EF') --> A D E B F C"
    iterators = deque(map(iter, iterables))
    while iterators:
        try:
            while True:
                yield next(iterators[0])
                iterators.rotate(-1)
        except StopIteration:
            # Remove an exhausted iterator.
            iterators.popleft()

demo4:rotate() 方法提供了一种方式来实现 deque 切片和删除。 例如， 一个纯的Python del d[n] 实现依赖于 rotate() 来定位要弹出的元素
def delete_nth(d, n):
    d.rotate(-n)
    d.popleft()
    d.rotate(n)
要实现 deque 切片， 使用一个类似的方法，应用 rotate() 将目标元素放到左边。通过 popleft() 移去老的条目（entries），通过 extend() 添加新的条目， 然后反向 rotate。这个方法可以最小代价实现命令式的栈操作，诸如 dup, drop, swap, over, pick, rot, 和 roll 。
"""

print("-------------class collections.defaultdict([default_factory[, ...]])")
# 返回一个新的类似字典的对象。 defaultdict 是内置 dict 类的子类。它重载了一个方法并添加了一个可写的实例变量。其余的功能与 dict 类相同，此处不再重复说明。
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
dd = collections.defaultdict(list)  ## 注意是list类型
print(sorted(dd.items()))
for k, v in s:
    dd[k].append(v)

print(sorted(dd.items()))

d = {}
for k, v in s:
    d.setdefault(k, []).append(v)

print(sorted(d.items()))

s = 'mississippi'
d = collections.defaultdict(int)
for k in s:
    d[k] += 1
print(sorted(d.items()))


def constant_factory(value):
    return lambda: value


d = collections.defaultdict(constant_factory('<missing>'))
d.update(name='John', action='ran')
print('%(name)s %(action)s to %(object)s' % d)
print('{name} {action} to {object}'.format(**d))

s = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4), ('red', 1), ('blue', 4)]
d = collections.defaultdict(set)
for k, v in s:
    d[k].add(v)

print(sorted(d.items()))

print("---------------collections.namedtuple(typename, field_names, *, rename=False, defaults=None, module=None) 命名元组")
# Basic example
Point = collections.namedtuple('Point2', ['x', 'y'])
p = Point(11, y=22)  # instantiate with positional or keyword arguments
print(p[0] + p[1])  # indexable like the plain tuple (11, 22)
x, y = p  # unpack like a regular tuple
print(x, y)
print(p.x + p.y)  # fields also accessible by name
print(p)  # readable __repr__ with a name=value style
print(Point._make([11, 22]))  # 创建一个新实例
p = Point(x=11, y=22)
print(dict(p._asdict()))  # 返回一个新的 dict ，它将字段名称映射到它们对应的值：
"""
在 3.1 版更改: 返回一个 OrderedDict 而不是 dict 。
在 3.8 版更改: 返回一个常规 dict 而不是 OrderedDict。 因为自 Python 3.7 起，常规字典已经保证有序。 
如果需要 OrderedDict 的额外特性，推荐的解决方案是将结果转换为需要的类型: OrderedDict(nt._asdict())。
"""
p._replace(x=33)
print(p)
print(p._fields)
print(p._field_defaults)

Account = collections.namedtuple('Account', ['type', 'balance'], defaults=[0])
print(Account._field_defaults)
print(Account('premium'))

d = {'x': 11, 'y': 22}
print(Point(**d))
"""
demo1:命名元组尤其有用于赋值 csv sqlite3 模块返回的元组

EmployeeRecord = namedtuple('EmployeeRecord', 'name, age, title, department, paygrade')

import csv
for emp in map(EmployeeRecord._make, csv.reader(open("employees.csv", "rb"))):
    print(emp.name, emp.title)

import sqlite3
conn = sqlite3.connect('/companydata')
cursor = conn.cursor()
cursor.execute('SELECT name, age, title, department, paygrade FROM employees')
for emp in map(EmployeeRecord._make, cursor.fetchall()):
    print(emp.name, emp.title)

demo2:因为一个命名元组是一个正常的Python类，它可以很容易的通过子类更改功能。这里是如何添加一个计算域和定宽输出打印格式:

>>> class Point(namedtuple('Point', ['x', 'y'])):
...     __slots__ = ()
...     @property
...     def hypot(self):
...         return (self.x ** 2 + self.y ** 2) ** 0.5
...     def __str__(self):
...         return 'Point: x=%6.3f  y=%6.3f  hypot=%6.3f' % (self.x, self.y, self.hypot)

>>> for p in Point(3, 4), Point(14, 5/7):
...     print(p)
Point: x= 3.000  y= 4.000  hypot= 5.000
Point: x=14.000  y= 0.714  hypot=14.018

"""
Point3D = collections.namedtuple('Point3D', Point._fields + ('z',))
print(Point3D(1, 2, 3))
# 文档字符串可以自定义，通过直接赋值给 __doc__ 属性:
Book = collections.namedtuple('Book', ['id', 'title', 'authors'])
Book.__doc__ += ': Hardcover book in active collection'
Book.id.__doc__ = '13-digit ISBN'
Book.title.__doc__ = 'Title of first printing'
Book.authors.__doc__ = 'List of authors sorted by last name'

print("--------------------class collections.OrderedDict([items])")
"""
有序词典就像常规词典一样，但有一些与排序操作相关的额外功能。由于内置的 dict 类获得了记住插入顺序的能力（在 Python 3.7 中保证了这种新行为），它们变得不那么重要了。
一些与 dict 的不同仍然存在：
常规的 dict 被设计为非常擅长映射操作。 跟踪插入顺序是次要的。
OrderedDict 旨在擅长重新排序操作。 空间效率、迭代速度和更新操作的性能是次要的。
算法上， OrderedDict 可以比 dict 更好地处理频繁的重新排序操作。 这使其适用于跟踪最近的访问（例如在 LRU cache 中）。
对于 OrderedDict ，相等操作检查匹配顺序。
OrderedDict 类的 popitem() 方法有不同的签名。它接受一个可选参数来指定弹出哪个元素。
OrderedDict 类有一个 move_to_end() 方法，可以有效地将元素移动到任一端。
Python 3.8之前， dict 缺少 __reversed__() 方法。
"""

od = collections.OrderedDict([{"a": 1, "b": 2}, {"c": 3, "d": 4}])
print(od)
print(dict(od))
print(od["a"])
"""
popitem(last=True)
有序字典的 popitem() 方法移除并返回一个 (key, value) 键值对。 如果 last 值为真，则按 LIFO 后进先出的顺序返回键值对，否则就按 FIFO 先进先出的顺序返回键值对。
"""
print(od.popitem())
print(od)

d = collections.OrderedDict.fromkeys('abcde')
print(d)
d.move_to_end('b')
print(''.join(d.keys()))
d.move_to_end('b', last=False)
print(''.join(d.keys()))

"""
demo1:创建记住键值 最后 插入顺序的有序字典变体很简单。 如果新条目覆盖现有条目，则原始插入位置将更改并移至末尾:
class LastUpdatedOrderedDict(OrderedDict):
    'Store items in the order the keys were last added'

    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        self.move_to_end(key)

demo2:一个 OrderedDict 对于实现 functools.lru_cache() 的变体也很有用:
class LRU(OrderedDict):
    'Limit size, evicting the least recently looked-up key when full'

    def __init__(self, maxsize=128, /, *args, **kwds):
        self.maxsize = maxsize
        super().__init__(*args, **kwds)

    def __getitem__(self, key):
        value = super().__getitem__(key)
        self.move_to_end(key)
        return value

    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        if len(self) > self.maxsize:
            oldest = next(iter(self))
            del self[oldest]
"""


class LRU(collections.OrderedDict):
    'Limit size, evicting the least recently looked-up key when full'

    def __init__(self, maxsize=128, *args, **kwds):
        self.maxsize = maxsize
        super().__init__(*args, **kwds)

    def __getitem__(self, key):
        value = super().__getitem__(key)
        self.move_to_end(key)
        return value

    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        if len(self) > self.maxsize:
            oldest = next(iter(self))
            del self[oldest]


lru = LRU(2)
lru["a"] = 10
print(lru)
lru["b"] = 11
print(lru)
lru["c"] = 12
print(lru)

print("-----------------------class collections.UserDict([initialdata])")

ud = collections.UserDict({"a": 1, "b": 2})
print(ud["a"])
print(ud.data)

print("-----------------------class collections.UserList([list])")

ul = collections.UserList([{"a": 1, "b": 2}, {"c": 3, "d": 4}])

print(ul.data)
ul.append({"a": 1, "b": 2})
print(ul.data)

print("-----------------class collections.UserString(seq)")
us = collections.UserString([{"a": 1, "b": 2}, {"c": 3, "d": 4}])

print(us.data)
print(us.upper())