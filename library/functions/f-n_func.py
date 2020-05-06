print(filter(lambda x: x >= 2, [1, 2, 3]))  # 返回迭代器
print(list(filter(lambda x: x >= 2, [1, 2, 3])))

print(float('+1.23'))
print(float('   -12345\n'))
print(float('-Infinity'))
# 如果 __float__() 未定义则回退至 __index__()。

# https://docs.python.org/zh-cn/3.9/library/string.html#formatspec
print(format(255, '#x'), format(255, 'x'), format(255, 'X'))
# str.format
print('{} {}'.format('a', 'b'))
print('{0} {1}'.format('a', 'b'))
print('{0}{0} {1}'.format('a', 'b'))
print("{:.2f}".format(3.1415926))  # 保留小数点后两位
print("{:+.2f}".format(3.1415926))  # 带符号保留小数点后两位
print("{:.0f}".format(3.1415926))  # 不带小数
print("{:0>2d}".format(3))  # 数字补零 (填充左边, 宽度为2)
print("{:x<4d}".format(3))  # 数字补x (填充右边, 宽度为4)

print("{:>10d}".format(13))  # 右对齐 (默认, 宽度为10)
print("{:<10d}".format(13))  # 左对齐 (宽度为10)
print("{:^10d}".format(13))  # 中间对齐 (宽度为10)

print("13".rjust(10))
print("13".ljust(10))
print("13".center(10))


print("{:,}".format(1000000))  # 以逗号分隔的数字格式
print("{:.2e}".format(1000000))  # 指数记法
print("{:.2%}".format(0.25))  # 百分比格式 25.00%
print("{:.0%}".format(0.25))  # 百分比格式 25%

# b、d、o、x 分别是二进制、十进制、八进制、十六进制。
print('{:b}'.format(11))
print('{:d}'.format(11))
print('{:o}'.format(11))
print('{:x}'.format(11))
print('{:#x}'.format(11))
print('{:#X}'.format(11))

print("name：{name}, 地址 {url}".format(name="xxx", url="www.xxx.com"))
# 通过字典设置参数
site = {"name": "xxx", "url": "www.xxx.com"}
print("name：{name}, 地址 {url}".format(**site))
# 通过列表索引设置参数
my_list = ['xxx', 'www.xxx.com']
print("name：{0[0]}, 地址 {0[1]}".format(my_list))  # "0" 是必须的

print(frozenset([1, 1, 3]))

"""
getattr(object, name[, default])
返回对象命名属性的值。name 必须是字符串。如果该字符串是对象的属性之一，则返回该属性的值。例如， getattr(x, 'foobar') 等同于 x.foobar。
如果指定的属性不存在，且提供了 default 值，则返回它，否则触发 AttributeError。

hasattr(object, name)
该实参是一个对象和一个字符串。如果字符串是对象的属性之一的名称，则返回 True，否则返回 False。（此功能是通过调用 getattr(object, name) 看是否有 AttributeError 异常来实现的。）
"""

print(globals())
"""
dir()
1、dir()作用在实例上时，显示实例变量还有在实例变量所在类及所有它的基类中定义的方法和属性
2、dir()作用在类上时，显示类及所有它的基类中__dict__的内容，不包括元类
3、dir()作用在模块上时，显示模块的__dict__的内容
4、dir()不带参数时显示调用者的局部变量，等价于locals()，但返回的不是字典

vars()
给定的对象必须参数必须有一个__dict__属性，作用在对象上时，返回__dict__字典中的内容，如果没有参数，等价于locals()

locals()
局部变量，只读

globals()
全局变量，非只读
"""

print(hash("123"))
"""
hash(object)
返回该对象的哈希值（如果它有的话）。哈希值是整数。它们在字典查找元素时用来快速比较字典的键。相同大小的数字变量有相同的哈希值（即使它们类型不同，如 1 和 1.0）。

注解 如果对象实现了自己的 __hash__() 方法，请注意，hash() 根据机器的字长来截断返回值。另请参阅 __hash__()。
"""

# help('str')             # 查看 str 数据类型的帮助
# help('sys')             # 查看 sys 模块的帮助
# a = [1,2,3]
# help(a)                 # 查看列表 list 帮助信息
# help(a.append)          # 显示list的append方法的帮助

print(hex(255))
# 将整数转换为以“0x”为前缀的小写十六进制字符串。如果 x 不是 Python int 对象，则必须定义返回整数的 __index__() 方法

print('%#x' % 255, '%x' % 255, '%X' % 255)  # 老语法
print(format(255, '#x'), format(255, 'x'), format(255, 'X'))
print(f'{255:#x}', f'{255:x}', f'{255:X}')

print(id(1))

# s = input('--> ')
# print(type(s)) # <class 'str'>
# print(s)


print(int(2))
print(int("10", 2))
"""
class int(x, base=10)
返回一个基于数字或字符串 x 构造的整数对象，或者在未给出参数时返回 0。 如果 x 定义了 __int__()，int(x) 将返回 x.__int__()。 如果 x 定义了 __index__()，它将返回 x.__index__()。 如果 x 定义了 __trunc__()，它将返回 x.__trunc__()。 对于浮点数，它将向零舍入。

如果 x 不是数字，或者有 base 参数，x 必须是字符串、bytes、表示进制为 base 的 整数字面值 的 bytearray 实例。
该文字前可以有 + 或 - （中间不能有空格），前后可以有空格。一个进制为 n 的数字包含 0 到 n-1 的数，其中 a 到 z （或 A 到 Z ）表示 10 到 35。默认的 base 为 10 ，
允许的进制有 0、2-36。2、8、16 进制的数字可以在代码中用 0b/0B 、 0o/0O 、 0x/0X 前缀来表示。
进制为 0 将安照代码的字面量来精确解释，最后的结果会是 2、8、10、16 进制中的一个。所以 int('010', 0) 是非法的，但 int('010') 和 int('010', 8) 是合法的。
"""

"""
isinstance(object, classinfo)
如果参数 object 是参数 classinfo 的实例或者是其 (直接、间接或 虚拟) 子类则返回 True。 如果 object 不是给定类型的对象，函数将总是返回 False。 
如果 classinfo 是类型对象元组（或由其他此类元组递归组成的元组），那么如果 object 是其中任何一个类型的实例就返回 True。 
如果 classinfo 既不是类型，也不是类型元组或类型元组的元组，则将引发 TypeError 异常。

class A:
    pass
 
class B(A):
    pass
 
isinstance(A(), A)    # returns True
type(A()) == A        # returns True
isinstance(B(), A)    # returns True
type(B()) == A        # returns False
print(issubclass(B,A))    # 返回 True

issubclass(class, classinfo)
如果 class 是 classinfo 的 (直接、间接或 虚拟) 子类则返回 True。 类会被视作其自身的子类。 
classinfo 也以是类对象的元组，在此情况下 classinfo 中的每个条目都将被检查。 在任何其他情况下，都将引发 TypeError 异常。
"""
a = 2
print(isinstance(a, int))
print(isinstance(a, (str, int, list)))  # 是元组中的一个返回 True

lst = [1, 2, 3]
for i in iter(lst):
    print(i)

print(len("123你好"))

print(list(filter(lambda x: x >= 2, [1, 2, 3])))

aTuple = (123, 'Google', 'Runoob', 'Taobao')
list1 = list(aTuple)
print("列表元素 : ", list1)

str = "Hello World"
list2 = list(str)
print("列表元素 : ", list2)

print(locals())

mm = map(lambda x: x ** 2, [1, 2, 3, 4, 5])
print(mm)  # 使用 lambda 匿名函数 返回迭代器
print(list(mm))
print(map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])) # 提供了两个列表，对相同位置的列表数据进行相加 返回迭代器
print(list(map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])))

print(max(80, 100, 1000))
print(max([1, 2, 3, 4, 5]))
#print(list([1, 2, 3, 4, 5]))# 错误的

print(min(80, 100, 1000))
print(min([1, 2, 3, 4, 5]))

print(memoryview(bytearray("abcefg", 'utf-8')))

# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
        print(x)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break

it = iter([1, 2, 5, 4, 3])
while True:
    x = next(it, 'a') # 如果传入第二个参数, 获取最后一个元素之后, 下一次next返回该默认值, 而不会抛出 StopIteration:
    print(x)
    if x == 'a':
        break

