# 所有内置函数是在builtins包下
# import builtins
# dir(builtins)

print(abs(-1))
"""
返回一个数的绝对值。 参数可以是一个整数或浮点数。 如果参数是一个复数，则返回它的模。 
如果 x 定义了 __abs__()，则 abs(x) 将返回 x.__abs__()。
"""

print(all(['a', 'b', 'c', 'd']))
print(all(['a', 'b', '', 'd']))  # 列表list，存在一个为空的元素
print(any(['a', 'b', '', 'd']))
"""
all(iterable)
如果 iterable 的所有元素为真（或迭代器为空），返回 True 。等价于:
def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True

any(iterable)
如果 iterable 的任一元素为真则返回 True。 如果迭代器为空，返回 False。 等价于:

def any(iterable):
    for element in iterable:
        if element:
            return True
    return False
"""

print(ascii('1aA你好，'))
print(repr('1aA你好，'))

"""
repr(object)
返回包含一个对象的可打印表示形式的字符串。 对于许多类型来说，该函数会尝试返回的字符串将会与该对象被传递给 eval() 时所生成的对象具有相同的值，
在其他情况下表示形式会是一个括在尖括号中的字符串，其中包含对象类型的名称与通常包括对象名称和地址的附加信息。 
类可以通过定义 __repr__() 方法来控制此函数为它的实例所返回的内容(是不是想tostring)。
"""

print(bin(3))
"""
bin(x)
如果 x 不是 Python 的 int 对象，那它需要定义 __index__() 方法返回一个整数

如果不一定需要前缀“0b”，还可以使用如下的方法。
"""
print(format(14, '#b'), format(14, 'b'))
print(f'{14:#b}', f'{14:b}')

print(bool(0), bool(1), bool(''), bool(), bool("s"), bool)
# False True False False True <class 'bool'>

# breakpoint() # https://docs.python.org/zh-cn/3.9/library/functions.html#breakpoint
# 进入pdb调试 https://docs.python.org/zh-cn/3.9/library/pdb.html#module-pdb

# 不明白什么用处？？
print(bytearray(255))

a = b"abc"
b = a.replace(b"a", b"f")
print(type(b))

print(callable(1))
"""
callable(object)
如果参数 object 是可调用的就返回 True，否则返回 False。 如果返回 True，调用仍可能失败，但如果返回 False，则调用 object 将肯定不会成功。
 请注意类是可调用的（调用类将返回一个新的实例）；如果实例所属的类有 __call__() 则它就是可调用的。
"""

print(chr(8364))  # 返回 Unicode 码位为整数 i 的字符的字符串格式。
print(chr(97))
"""
这是 ord() 的逆函数。
实参的合法范围是 0 到 1,114,111（16 进制表示是 0x10FFFF）。如果 i 超过这个范围，会触发 ValueError 异常。
"""
print(ord('a'))

"""
@classmethod
https://docs.python.org/zh-cn/3.9/library/functions.html#classmethod

compile
https://docs.python.org/zh-cn/3.9/library/functions.html#compile
"""
print(exec("print(1)"))
print(eval("print(1)"))

print(complex('1+2j'))
"""
对于一个普通 Python 对象 x，complex(x) 会委托给 x.__complex__()。 如果 __complex__() 未定义则将回退至 __float__()。 如果 __float__() 未定义则将回退至 __index__()。
字符串在 + 或 - 的周围必须不能有空格
"""

"""
delattr(object, name)
setattr() 相关的函数。实参是一个对象和一个字符串。该字符串必须是对象的某个属性。如果对象允许，该函数将删除指定的属性。例如 delattr(x, 'foobar') 等价于 del x.foobar 。
"""

a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})
f = dict({'one': 1, 'three': 3}, two=2)
print(a == b == c == d == e == f)

print(dir())
import struct

print(dir(struct))


class Shape:
    def __dir__(self):
        return ['area', 'perimeter', 'location']


s = Shape()
print(dir(s))
"""
如果没有实参，则返回当前本地作用域中的名称列表。如果有实参，它会尝试返回该对象的有效属性列表。

如果对象有一个名为 __dir__() 的方法，那么该方法将被调用，并且必须返回一个属性列表。这允许实现自定义 __getattr__() 或 __getattribute__() 函数的对象能够自定义 dir() 来报告它们的属性。

如果对象不提供 __dir__()，这个函数会尝试从对象已定义的 __dict__ 属性和类型对象收集信息。结果列表并不总是完整的，如果对象有自定义 __getattr__()，那结果可能不准确。

默认的 dir() 机制对不同类型的对象行为不同，它会试图返回最相关而不是最全的信息：

如果对象是模块对象，则列表包含模块的属性名称。

如果对象是类型或类对象，则列表包含它们的属性名称，并且递归查找所有基类的属性。

否则，列表包含对象的属性名称，它的类属性名称，并且递归查找它的类的所有基类的属性。
"""
y, z = divmod(7, 3)
print(y, z)

"""
它将两个（非复数）数字作为实参，并在执行整数除法时返回一对商和余数。对于混合操作数类型，适用双目算术运算符的规则。
对于整数，结果和 (a // b, a % b) 一致。
对于浮点数，结果是 (q, a % b) ，q 通常是 math.floor(a / b) 但可能会比 1 小。
在任何情况下， q * b + a % b 和 a 基本相等；如果 a % b 非零，它的符号和 b 一样，并且 0 <= abs(a % b) < abs(b) 。
"""

x = 1
x = eval('x+1')
print(x)

exec('x=x+1')  # 返回None;
print(x)
