"""

asynchronous context manager -- 异步上下文管理器
此种对象通过定义 __aenter__() 和 __aexit__() 方法来对 async with 语句中的环境进行控制。由 PEP 492 引入。

asynchronous generator -- 异步生成器
返回值为 asynchronous generator iterator 的函数。它与使用 async def 定义的协程函数很相似，不同之处在于它包含 yield 表达式以产生一系列可在 async for 循环中使用的值。

此术语通常是指异步生成器函数，但在某些情况下则可能是指 异步生成器迭代器。如果需要清楚表达具体含义，请使用全称以避免歧义。

一个异步生成器函数可能包含 await 表达式或者 async for 以及 async with 语句。

asynchronous generator iterator -- 异步生成器迭代器
asynchronous generator 函数所创建的对象。

此对象属于 asynchronous iterator，当使用 __anext__() 方法调用时会返回一个可等待对象来执行异步生成器函数的代码直到下一个 yield 表达式。

每个 yield 会临时暂停处理，记住当前位置执行状态 (包括局部变量和挂起的 try 语句)。当该 异步生成器迭代器 与其他 __anext__() 返回的可等待对象有效恢复时，它会从离开位置继续执行。参见 PEP 492 和 PEP 525。

asynchronous iterable -- 异步可迭代对象
可在 async for 语句中被使用的对象。必须通过它的 __aiter__() 方法返回一个 asynchronous iterator。由 PEP 492 引入。


generator -- 生成器
返回一个 generator iterator 的函数。它看起来很像普通函数，不同点在于其包含 yield 表达式以便产生一系列值供给 for-循环使用或是通过 next() 函数逐一获取。

通常是指生成器函数，但在某些情况下也可能是指 生成器迭代器。如果需要清楚表达具体含义，请使用全称以避免歧义。

generator iterator -- 生成器迭代器
generator 函数所创建的对象。

每个 yield 会临时暂停处理，记住当前位置执行状态（包括局部变量和挂起的 try 语句）。当该 生成器迭代器 恢复时，它会从离开位置继续执行（这与每次调用都从新开始的普通函数差别很大）。

generator expression -- 生成器表达式
返回一个迭代器的表达式。 它看起来很像普通表达式后面带有定义了一个循环变量、范围的 for 子句，以及一个可选的 if 子句。 以下复合表达式会为外层函数生成一系列值:


 sum(i*i for i in range(10))         # sum of squares 0, 1, 4, ... 81
285
generic function -- 泛型函数
为不同的类型实现相同操作的多个函数所组成的函数。在调用时会由调度算法来确定应该使用哪个实现。

另请参见 single dispatch 术语表条目、functools.singledispatch() 装饰器以及 PEP 443。

iterator -- 迭代器
用来表示一连串数据流的对象。重复调用迭代器的 __next__() 方法（或将其传给内置函数 next()）将逐个返回流中的项。当没有数据可用时则将引发 StopIteration 异常。到这时迭代器对象中的数据项已耗尽，继续调用其 __next__() 方法只会再次引发 StopIteration 异常。迭代器必须具有 __iter__() 方法用来返回该迭代器对象自身，因此迭代器必定也是可迭代对象，可被用于其他可迭代对象适用的大部分场合。一个显著的例外是那些会多次重复访问迭代项的代码。容器对象（例如 list）在你每次向其传入 iter() 函数或是在 for 循环中使用它时都会产生一个新的迭代器。如果在此情况下你尝试用迭代器则会返回在之前迭代过程中被耗尽的同一迭代器对象，使其看起来就像是一个空容器。

更多信息可查看 迭代器类型。
https://docs.python.org/zh-cn/3/library/stdtypes.html#typeiter

迭代器类型
Python 支持在容器中进行迭代的概念。 这是通过使用两个单独方法来实现的；它们被用于允许用户自定义类对迭代的支持。 将在下文中详细描述的序列总是支持迭代方法。

容器对象要提供迭代支持，必须定义一个方法:

container.__iter__()
返回一个迭代器对象。 该对象需要支持下文所述的迭代器协议。 如果容器支持不同的迭代类型，则可以提供额外的方法来专门地请求不同迭代类型的迭代器。 （支持多种迭代形式的对象的例子有同时支持广度优先和深度优先遍历的树结构。） 此方法对应于 Python/C API 中 Python 对象类型结构体的 tp_iter 槽位。

迭代器对象自身需要支持以下两个方法，它们共同组成了 迭代器协议:

iterator.__iter__()
返回迭代器对象本身。 这是同时允许容器和迭代器配合 for 和 in 语句使用所必须的。 此方法对应于 Python/C API 中 Python 对象类型结构体的 tp_iter 槽位。

iterator.__next__()
从容器中返回下一项。 如果已经没有项可返回，则会引发 StopIteration 异常。 此方法对应于 Python/C API 中 Python 对象类型结构体的 tp_iternext 槽位。

Python 定义了几种迭代器对象以支持对一般和特定序列类型、字典和其他更特别的形式进行迭代。 除了迭代器协议的实现，特定类型的其他性质对迭代操作来说都不重要。

一旦迭代器的 __next__() 方法引发了 StopIteration，它必须一直对后续调用引发同样的异常。 不遵循此行为特性的实现将无法正常使用。

生成器类型
Python 的 generator 提供了一种实现迭代器协议的便捷方式。 如果容器对象 __iter__() 方法被实现为一个生成器，它将自动返回一个迭代器对象（从技术上说是一个生成器对象），该对象提供 __iter__() 和 __next__() 方法。 有关生成器的更多信息可以参阅 yield 表达式的文档。

"""

# 提供迭代支持，必须定义一个方法: __iter__()
# 迭代器有两个基本的方法：iter() 和 next()。
list = [1, 2, 3, 4]
it = iter(list)  # 创建迭代器对象
print(next(it))  # 输出迭代器的下一个元素
print(next(it))  # 输出迭代器的下一个元素
print(next(it))  # 输出迭代器的下一个元素
print(next(it))  # 输出迭代器的下一个元素
# 出错 (next(it))   # 输出迭代器的下一个元素

it = iter(list)  # 创建迭代器对象
for x in it:
    print(x, end=" ")

it = iter(list)  # 创建迭代器对象
while True:
    try:
        print(next(it))
    except StopIteration:
        break


# 创建一个迭代器实现两个方法 __iter__() 与 __next__()
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))

# StopIteration
# StopIteration 异常用于标识迭代的完成，防止出现无限循环的情况，在 __next__() 方法中我们可以设置在完成指定循环次数后触发 StopIteration 异常来结束迭代。
class MyNumbers2:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myclass = MyNumbers2()
myiter = iter(myclass)
for x in myiter:
    print(x)

# 再看class range(object)就很容易理解了

# 生成器  generator
# 在 Python 中，使用了 yield 的函数被称为生成器（generator）。
#
# 跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。
# 在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回 yield 的值, 并在下一次执行 next() 方法时从当前位置继续运行。
# 生成器是一种特殊的迭代器
# 斐波那契数列
import sys

def fibonacci(n):  # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1


f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成

while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        break


def foo():
    print("starting...")
    while True:
        res = yield 4
        print("res:",res)
g = foo()
print(next(g))
print("*"*20)
print(g.send(7))

"""
（1）什么是可迭代对象？ 可迭代对象要么实现了能返回迭代器的 iter 方法，要么实现了 getitem 方法而且其参数是从零开始的索引。

（2）什么是迭代器？ 迭代器是这样的对象：实现了无参数的 next 方法，返回下一个元素，如果没有元素了，那么抛出 StopIteration 异常；并且实现iter 方法，返回迭代器本身。

（3）什么是生成器？ 生成器是带有 yield 关键字的函数。调用生成器函数时，会返回一个生成器对象。

（4）什么是生成器表达式？ 生成器表达式是创建生成器的简洁句法，这样无需先定义函数再调用。
"""

# 可迭代对象
class Eg1:
    def __init__(self,text):
        self.text = text
        self.sub_text = text.split(' ')

    def __getitem__(self, item):
        return self.sub_text[item]

o1 = Eg1('Hello sdfds xxx.')
for i in o1:
    print(i)

#生成器

class Eg3:
    def __init__(self,text):
        self.text = text
        self.sub_text = text.split(' ')

    def __iter__(self):
        for item in self.sub_text:
            yield item

o3 = Eg3('Hello sdfds xxx.')

for i in o3:
    print(i)

#生成器表达式

class Eg4:
    def __init__(self,text):
        self.text = text
        self.sub_text = text.split(' ')

    def __iter__(self):
        yield from self.sub_text

o4 = Eg4('Hello sdfds xxx.')
for i in o4:
    print(i)

