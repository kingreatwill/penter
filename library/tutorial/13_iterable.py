"""

Python中 list，truple，str，dict这些都可以被迭代，但他们并不是迭代器。为什么？

因为和迭代器相比有一个很大的不同，list/truple/map/dict这些数据的大小是确定的，也就是说有多少事可知的。但迭代器不是，迭代器不知道要执行多少次，所以可以理解为不知道有多少个元素，每调用一次next()，就会往下走一步，是惰性的。

"""
import types
from collections.abc import Iterable, Iterator
# 可迭代对象
class Eg1:
    def __init__(self, text):
        self.text = text
        self.sub_text = text.split(' ')

    def __getitem__(self, item):
        return self.sub_text[item]


o1 = Eg1('Hello sdfds xxx.')
# 判断是不是可以迭代，用Iterable


print(isinstance({}, Iterable))  # True
print(isinstance((), Iterable))  # True
print(isinstance(o1, Iterable))  # False 可以for循环啊
print(isinstance((x for x in range(10)), Iterable))  # True
print(isinstance(range(10), Iterable))  # True
print("----------------")
print(isinstance({}, Iterator))  # False
print(isinstance((), Iterator))  # False
print(isinstance(o1, Iterator))  # False
print(isinstance((x for x in range(10)), Iterator))  # True
print(isinstance(range(10), Iterator))  # False
print(isinstance((x for x in range(10)), types.GeneratorType))  # True
print(isinstance(range(10), types.GeneratorType))  # False
# 凡是可以next()的，都是Iterator
"""
如果这个答案有什么地方不对的话，以文档为准。iterable，根据文档中的定义，指的是那些可以把自己的成员一个一个返回（或者说遍历自己的成员）的一类对象（这里的成员不是类成员的那种成员，而更类似于元素）。
只要有__iter__()或者__getitem__()（类似于operator[]）定义的对象都是iterable。
一个iterator对象就是我们所谓的迭代器，你可以把它传给next()或者调用它的__next__()来获得下一个元素。按照Python的要求，iterator的__iter__()应当返回其自身，因此iterator也是一个Iterable。
一般而言你不需要直接操作iterator，for循环会帮你搞定的。

iterable -- 可迭代对象
能够逐一返回其成员项的对象。
可迭代对象的例子包括所有序列类型（例如 list、str 和 tuple）以及某些非序列类型例如 dict、文件对象 以及定义了 __iter__() 方法或是实现了 Sequence 语义的 __getitem__() 方法的任意自定义类对象。

可迭代对象被可用于 for 循环以及许多其他需要一个序列的地方（zip()、map() ...）。
当一个可迭代对象作为参数传给内置函数 iter() 时，它会返回该对象的迭代器。这种迭代器适用于对值集合的一次性遍历。
在使用可迭代对象时，你通常不需要调用 iter() 或者自己处理迭代器对象。for 语句会为你自动处理那些操作，创建一个临时的未命名变量用来在循环期间保存迭代器。
参见 iterator、sequence 以及 generator。

iterator -- 迭代器
用来表示一连串数据流的对象。重复调用迭代器的 __next__() 方法（或将其传给内置函数 next()）将逐个返回流中的项。
当没有数据可用时则将引发 StopIteration 异常。到这时迭代器对象中的数据项已耗尽，继续调用其 __next__() 方法只会再次引发 StopIteration 异常。
迭代器必须具有 __iter__() 方法用来返回该迭代器对象自身，因此迭代器必定也是可迭代对象，可被用于其他可迭代对象适用的大部分场合。
一个显著的例外是那些会多次重复访问迭代项的代码。
容器对象（例如 list）在你每次向其传入 iter() 函数或是在 for 循环中使用它时都会产生一个新的迭代器。如果在此情况下你尝试用迭代器则会返回在之前迭代过程中被耗尽的同一迭代器对象，使其看起来就像是一个空容器。

更多信息可查看 迭代器类型。

sequence -- 序列
一种 iterable，它支持通过 __getitem__() 特殊方法来使用整数索引进行高效的元素访问，并定义了一个返回序列长度的 __len__() 方法。
内置的序列类型有 list、str、tuple 和 bytes。注意虽然 dict 也支持 __getitem__() 和 __len__()，但它被认为属于映射而非序列，因为它查找时使用任意的 immutable 键而非整数。

collections.abc.Sequence 抽象基类定义了一个更丰富的接口，它超越了 __getitem__() 和 __len__()，添加了 count(), index(), __contains__() 和 __reversed__() 。 
可以使用 register() 显式注册实现此扩展接口的类型。

"""