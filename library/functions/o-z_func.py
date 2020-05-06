# object 是所有类的基类。它具有所有 Python 类实例的通用方法。这个函数不接受任何实参。
# 由于 object 没有 __dict__，因此无法将任意属性赋给 object 的实例。

print(oct(8))
print('%#o' % 10, '%o' % 10)
print(format(10, '#o'), format(10, 'o'))
print(f'{10:#o}', f'{10:o}')

"""
'r'读取（默认）
'w'写入，并先截断文件
'x'排它性创建，如果文件已存在则失败
'a'写入，如果文件存在则在末尾追加
'b'二进制模式
't'文本模式（默认）
'+'打开用于更新（读取与写入）

模式 'w+' 与 'w+b' 将打开文件并清空内容。 模式 'r+' 与 'r+b' 将打开文件并不清空内容。

try:
    f = open('/path/to/file', 'r')
    print(f.read())
finally:
    if f:
        f.close()
"""

f = open('f-n_func.py', encoding='utf-8')
print(f.readline())
f.close()

with open('f-n_func.py', encoding='utf-8') as data_file:
    print(data_file.readline())

"""
ord(c)
对表示单个 Unicode 字符的字符串，返回代表它 Unicode 码点的整数。例如 ord('a') 返回整数 97， ord('€') （欧元符号）返回 8364 。这是 chr() 的逆函数。
"""

print(pow(2, 3))  # 2的3次方
print(pow(2, -3))  # 2的3次方分之一
print(pow(2, 3, 5))  # 2的3次方 取模
"""
math.pow(100, 2) :  10000.0
pow(100, 2) :  10000
math.pow(100, -2) :  0.0001
math.pow(2, 4) :  16.0
math.pow(3, 0) :  1.0
"""
# print(pow(38, -1, mod=97)) #3.8版本 是 38 的倒数对 97 取余:

print("www", "runoob", "com", sep=".")  # 设置间隔符

"""
print 在 Python3.x 是一个函数，但在 Python2.x 版本不是一个函数，只是一个关键字。

语法
以下是 print() 方法的语法:

print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
参数
objects -- 复数，表示可以一次输出多个对象。输出多个对象时，需要用 , 分隔。
sep -- 用来间隔多个对象，默认值是一个空格。
end -- 用来设定以什么结尾。默认值是换行符 \n，我们可以换成其他字符串。
file -- 要写入的文件对象。
flush -- 输出是否被缓存通常决定于 file，但如果 flush 关键字参数为 True，流会被强制刷新。
"""


# class property(fget=None, fset=None, fdel=None, doc=None)
class C(object):
    def __init__(self):
        self._x = None

    def getx(self):
        return self._x

    def setx(self, value):
        print("setx")
        self._x = value

    def delx(self):
        del self._x

    x = property(getx, setx, delx, "I'm the 'x' property.")  # 注释掉 print("setx")不会执行


c = C()
c.x = "123"
print(c.x)


class Parrot:
    def __init__(self):
        self._voltage = 100000

    @property
    def voltage(self):
        print("getx")
        """Get the current voltage."""
        return self._voltage


p = Parrot()
print(p.voltage)


# 等价于上面的class C:例子
class C:
    def __init__(self):
        self._x = None

    @property
    def x(self):
        """I'm the 'x' property."""
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x


print(list(range(10)))
print(list(range(1, 10, 2)))
print(max(list(range(10))))

dict = {'runoob': 'runoob.com', 'google': 'google.com'}
print(repr(dict))

# 字符串
seqString = 'Runoob'
print(list(reversed(seqString)))

# 元组
seqTuple = ('R', 'u', 'n', 'o', 'o', 'b')
print(list(reversed(seqTuple)))

# range
seqRange = range(5, 9)
print(list(reversed(seqRange)))

# 列表
seqList = [1, 2, 4, 3, 5]
print(list(reversed(seqList)))

"""
round(number[, ndigits])
返回 number 舍入到小数点后 ndigits 位精度的值。 如果 ndigits 被省略或为 None，则返回最接近输入值的整数。

对于支持 round() 的内置类型，值会被舍入到最接近的 10 的负 ndigits 次幂的倍数；如果与两个倍数的距离相等，则选择偶数 (因此，round(0.5) 和 round(-0.5) 均为 0 而 round(1.5) 为 2)。 
任何整数值都可作为有效的 ndigits (正数、零或负数)。 如果 ndigits 被省略或为 None 则返回值将为整数。 否则返回值与 number 的类型相同。

对于一般的 Python 对象 number, round 将委托给 number.__round__。

注解 对浮点数执行 round() 的行为可能会令人惊讶：例如，round(2.675, 2) 将给出 2.67 而不是期望的 2.68。 这不算是程序错误：这一结果是由于大多数十进制小数实际上都不能以浮点数精确地表示。 

"""
print(round(0.5))
print(round(1.5))

print(round(2.665, 2))
print(round(2.675, 2))
print(round(2.676, 2))

print(set([1, 2, 3]))

"""
setattr(object, name, value)
此函数与 getattr() 两相对应。 其参数为一个对象、一个字符串和一个任意值。 字符串指定一个现有属性或者新增属性。 
函数会将值赋给该属性，只要对象允许这种操作。 例如，setattr(x, 'foobar', 123) 等价于 x.foobar = 123。
"""

"""
class slice(start, stop[, step])
返回一个表示由 range(start, stop, step) 所指定索引集的 slice 对象。 其中 start 和 step 参数默认为 None。 
切片对象具有仅会返回对应参数值（或其默认值）的只读数据属性 start, stop 和 step。 
它们没有其他的显式功能；不过它们会被 NumPy 以及其他第三方扩展所使用。 切片对象也会在使用扩展索引语法时被生成。 
例如: a[start:stop:step] 或 a[start:stop, i]。 请参阅 itertools.islice() 了解返回迭代器的一种替代版本。
"""
myslice = slice(5)  # 设置截取5个元素的切片
arr = range(10)
print(arr[myslice])  # 截取 5 个元素
print(arr[slice(1, 9, 2)])

"""
sorted(iterable, *, key=None, reverse=False)
根据 iterable 中的项返回一个新的已排序列表。

具有两个可选参数，它们都必须指定为关键字参数。

key 指定带有单个参数的函数，用于从 iterable 的每个元素中提取用于比较的键 (例如 key=str.lower)。 默认值为 None (直接比较元素)。

reverse 为一个布尔值。 如果设为 True，则每个列表元素将按反向顺序比较进行排序。
"""
print(sorted([5, 2, 3, 1, 4], reverse=True))
array = [{"age": 20, "name": "a"}, {"age": 25, "name": "b"}, {"age": 10, "name": "c"}]
array = sorted(array, key=lambda x: x["age"])
print(array)

"""
@staticmethod
将方法转换为静态方法。
静态方法不会接收隐式的第一个参数。要声明一个静态方法，请使用此语法

class C:
    @staticmethod
    def f(arg1, arg2, ...): ...
静态方法的调用可以在类上进行 (例如 C.f()) 也可以在实例上进行 (例如 C().f())。
像所有装饰器一样，也可以像常规函数一样调用 staticmethod ，并对其结果执行某些操作。比如某些情况下需要从类主体引用函数并且您希望避免自动转换为实例方法。对于这些情况，请使用此语法:

class C:
    builtin_open = staticmethod(open)
"""

"""
class str(object='')
class str(object=b'', encoding='utf-8', errors='strict')
返回一个 str 版本的 object 。有关详细信息，请参阅 str() 。
"""

print(sum([1, 2, 3]))

"""
super([type[, object-or-type]])
返回一个代理对象，它会将方法调用委托给 type 的父类或兄弟类。 这对于访问已在类中被重载的继承方法很有用。
class C(B):
    def method(self, arg):
        super().method(arg)    # This does the same thing as:
                               # super(C, self).method(arg)
"""


class A:
    def add(self, x):
        y = x + 1
        print(y)


class B(A):
    def add(self, x):
        super().add(x)


b = B()
b.add(2)  # 3


class FooParent(object):
    def __init__(self):
        self.parent = 'I\'m the parent.'
        print('Parent')

    def bar(self, message):
        print("%s from Parent" % message)


class FooChild(FooParent):
    def __init__(self):
        # super(FooChild,self) 首先找到 FooChild 的父类（就是类 FooParent），然后把类 FooChild 的对象转换为类 FooParent 的对象
        super(FooChild, self).__init__()
        print('Child')

    def bar(self, message):
        super(FooChild, self).bar(message)
        print('Child bar fuction')
        print(self.parent)


if __name__ == '__main__':
    fooChild = FooChild()
    fooChild.bar('HelloWorld')

print(tuple(['Google', 'Taobao', 'Runoob', 'Baidu']))
print(tuple({'www': 123, 'aaa': 234}))  # 将字段转换为元组时，只保留键！

"""
class type(name, bases, dict)
传入一个参数时，返回 object 的类型。 返回值是一个 type 对象，通常与 object.__class__ 所返回的对象相同。

推荐使用 isinstance() 内置函数来检测对象的类型，因为它会考虑子类的情况。

"""

print(vars())

"""
返回一个元组的迭代器，其中的第 i 个元组包含来自每个参数序列或可迭代对象的第 i 个元素。 
当所输入可迭代对象中最短的一个被耗尽时，迭代器将停止迭代。 当只有一个可迭代对象参数时，它将返回一个单元组的迭代器。 不带参数时，它将返回一个空迭代器。

zip() 与 * 运算符相结合可以用来拆解一个列表:
"""

print(list(zip([1, 2, 3], [4, 5, 6]))) # [(1, 4), (2, 5), (3, 6)]

a1, a2 = zip(*zip([1, 2, 3], [4, 5, 6]))  # 与 zip 相反，zip(*) 可理解为解压，返回二维矩阵式
print(list(a1)) # [1, 2, 3]
print(list(a2)) # [4, 5, 6]

a3, a4 = zip(*[(1, 4), (2, 5), (3, 6)])
print(list(a3)) # [1, 2, 3]
print(list(a4)) # [4, 5, 6]


"""
a.py 文件代码：
#!/usr/bin/env python    
#encoding: utf-8  
 
import os  
 
print ('在 a.py 文件中 %s' % id(os))

test.py 文件代码：
#!/usr/bin/env python    
#encoding: utf-8  
 
import sys  
__import__('a')        # 导入 a.py 模块
"""

"""
语句 import spam 的结果将为与以下代码作用相同的字节码:
spam = __import__('spam', globals(), locals(), [], 0)

语句 import spam.ham 的结果将为以下调用:
spam = __import__('spam.ham', globals(), locals(), [], 0)

语句 from spam.ham import eggs, sausage as saus 的结果将为
_temp = __import__('spam.ham', globals(), locals(), ['eggs', 'sausage'], 0)
eggs = _temp.eggs
saus = _temp.sausage
"""