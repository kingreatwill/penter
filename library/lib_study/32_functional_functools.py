import functools
import statistics

# 3.8 新版功能.
# 将一个类方法转换为特征属性，一次性计算该特征属性的值，然后将其缓存为实例生命周期内的普通属性。 类似于 property() 但增加了缓存功能。
# class DataSet:
#     def __init__(self, sequence_of_numbers):
#         self._data = sequence_of_numbers
#
#     @functools.cached_property
#     def stdev(self):
#         return statistics.stdev(self._data)
#
#     @functools.cached_property
#     def variance(self):
#         return statistics.variance(self._data)
#
#
# ds = DataSet([1, 2, 3, 4, 5, 6])
# print(ds.stdev) #1.8708286933869707

from functools import cmp_to_key


class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        key = cmp_to_key(lambda x, y: int(y) - int(x))
        res = ', '.join(sorted(map(str, nums), key=key))
        return res or '0'


nums = [-1, -2, 3, 4, 9, 2, 3, 4, 5]
s = Solution()
print(map(str, nums))  # 列表不去重
print(s.largestNumber(nums))
nums = {1, 2, 3, 4, 9, 2, 3, 4, 5}
print(map(str, nums))  # 字典会去重
print(s.largestNumber(nums))


# 一个为函数提供缓存功能的装饰器，缓存 maxsize 组传入参数，在下次以相同参数调用时直接返回上一次的结果。用以节约高开销或I/O函数的调用时间。
@functools.lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


print([fib(n) for n in range(16)])
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]

print(fib.cache_info())


# CacheInfo(hits=28, misses=16, maxsize=None, currsize=16)


# @functools.total_ordering
# 给定一个声明一个或多个全比较排序方法的类，这个类装饰器实现剩余的方法。这减轻了指定所有可能的全比较操作的工作。
# 此类必须包含以下方法之一：__lt__() 、__le__()、__gt__() 或 __ge__()。另外，此类必须支持 __eq__() 方法。

@functools.total_ordering
class Student:
    def _is_valid_operand(self, other):
        return (hasattr(other, "lastname") and
                hasattr(other, "firstname"))

    def __eq__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return ((self.lastname.lower(), self.firstname.lower()) ==
                (other.lastname.lower(), other.firstname.lower()))

    def __lt__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return ((self.lastname.lower(), self.firstname.lower()) <
                (other.lastname.lower(), other.firstname.lower()))


# 返回一个新的 部分对象，当被调用时其行为类似于 func 附带位置参数 args 和关键字参数 keywords 被调用。
# 如果为调用提供了更多的参数，它们会被附加到 args。 如果提供了额外的关键字参数，它们会扩展并重载 keywords。
from functools import partial

basetwo = partial(int, base=2)
basetwo.__doc__ = 'Convert base 2 string to an int.'
print(basetwo('10010'))  # 18
print(int('10010', base=2))  # 18


class Cell(object):
    def __init__(self):
        self._alive = False

    @property
    def alive(self):
        return self._alive

    def set_state(self, state):
        self._alive = bool(state)

    set_alive = functools.partialmethod(set_state, True)
    set_dead = functools.partialmethod(set_state, False)


c = Cell()
print(c.alive)  # False

c.set_alive()
print(c.alive)  # True

c.set_dead()
print(c.alive)  # False

# 将两个参数的 function 从左至右积累地应用到 iterable 的条目，以便将该可迭代对象缩减为单一的值。
print(functools.reduce(lambda x, y: x + y, [1, 2, 3, 4, 5]))  # 15  ((((1+2)+3)+4)+5) 的值

"""
@functools.singledispatch
将一个函数转换为 单分派 generic function。
要定义一个泛型函数，应使用 @singledispatch 装饰器进行装饰。 请注意分派是作用于第一个参数的类型，要相应地创建你的函数:
"""
from functools import singledispatch


@singledispatch
def fun(arg, verbose=False):
    if verbose:
        print("Let me just say,", end=" ")
    print(arg)


@fun.register
def _(arg: int, verbose=False):
    if verbose:
        print("Strength in numbers, eh?", end=" ")
    print(arg)


@fun.register
def _(arg: list, verbose=False):
    if verbose:
        print("Enumerate this:")
    for i, elem in enumerate(arg):
        print(i, elem)


@fun.register(complex)
def _(arg, verbose=False):
    if verbose:
        print("Better than complicated.", end=" ")
    print(arg.real, arg.imag)


fun(132, True)
print(fun.registry.keys())
print(fun.registry[int])

# class functools.singledispatchmethod(func)
# 将一个方法转换为 单分派 generic function。
# 3.8 新版功能.
# class Negator:
#     @functools.singledispatchmethod
#     def neg(self, arg):
#         raise NotImplementedError("Cannot negate a")
#
#     @neg.register
#     def _(self, arg: int):
#         return -arg
#
#     @neg.register
#     def _(self, arg: bool):
#         return not arg
#
# print(Negator().neg(1))


"""
functools.update_wrapper(wrapper, wrapped, assigned=WRAPPER_ASSIGNMENTS, updated=WRAPPER_UPDATES)
更新一个 wrapper 函数以使其类似于 wrapped 函数。 
可选参数为指明原函数的哪些属性要直接被赋值给 wrapper 函数的匹配属性的元组，并且这些 wrapper 函数的属性将使用原函数的对应属性来更新。
 这些参数的默认值是模块级常量 WRAPPER_ASSIGNMENTS (它将被赋值给 wrapper 函数的 __module__, __name__, __qualname__, __annotations__ 和 __doc__ 即文档字符串) 以及 WRAPPER_UPDATES (它将更新 wrapper 函数的 __dict__ 即实例字典)。
"""


def wrap(func):
    def call_it(*args, **kwargs):
        """wrap func: call_it"""
        print('before call')
        return func(*args, **kwargs)

    return call_it


@wrap
def hello():
    """say hello"""
    print("hello world")


from functools import update_wrapper


def wrap2(func):
    def call_it(*args, **kwargs):
        """wrap func: call_it2"""
        print('before call')
        return func(*args, **kwargs)

    return update_wrapper(call_it, func)


@wrap2
def hello2():
    """test hello"""
    print('hello world2')


if __name__ == '__main__':
    hello()
    print(hello.__name__)  # call_it  而不是输出hello
    print(hello.__doc__)  # wrap func: call_it 而不是 say hello
    print()
    hello2()
    print(hello2.__name__)  # hello2  这才是想要的
    print(hello2.__doc__)  # test hello 这才是想要的

"""
@functools.wraps(wrapped, assigned=WRAPPER_ASSIGNMENTS, updated=WRAPPER_UPDATES)
这是一个便捷函数，用于在定义包装器函数时发起调用 update_wrapper() 作为函数装饰器。 
它等价于 partial(update_wrapper, wrapped=wrapped, assigned=assigned, updated=updated)。
"""
from functools import wraps


def my_decorator(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        print('Calling decorated function')
        return f(*args, **kwds)

    return wrapper


@my_decorator
def example():
    """Docstring"""
    print('Called example function')


example()
# Calling decorated function
# Called example function
print(example.__name__)  # example
print(example.__doc__)  # Docstring

"""
partial 对象¶
partial 对象是由 partial() 创建的可调用对象。 它们具有三个只读属性：

partial.func
一个可调用对象或函数。 对 partial 对象的调用将被转发给 func 并附带新的参数和关键字。

partial.args
最左边的位置参数将放置在提供给 partial 对象调用的位置参数之前。

partial.keywords
当调用 partial 对象时将要提供的关键字参数。

partial 对象与 function 对象的类似之处在于它们都是可调用、可弱引用的对象并可拥有属性。 
但两者也存在一些重要的区别。 例如前者不会自动创建 __name__ 和 __doc__ 属性。 而且，在类中定义的 partial 对象的行为类似于静态方法，并且不会在实例属性查找期间转换为绑定方法。
"""
