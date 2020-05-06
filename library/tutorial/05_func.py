# def 函数
def demo():
    print("demo")


i = 5


def f(arg=i):  # 默认值只会执行一次
    print(arg)


i = 6
f()  # 5

"""
重要警告： 默认值只会执行一次。这条规则在默认值为可变对象（列表、字典以及大多数类实例）时很重要。比如，下面的函数会存储在后续调用中传递给它的参数:
也就是当默认值是可以改变的参数，那么会传递下去
"""


def f(a, L=[]):
    L.append(a)
    return L


print(f(1))
print(f(2))
print(f(3))
"""
[1]
[1, 2]
[1, 2, 3]

如果你不想要在后续调用之间共享默认值，你可以这样写这个函数:
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L
"""

# 函数参数 以及默认值
"""
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response') # 抛出异常
        print(reminder)


ask_ok('Do you really want to quit?')
ask_ok('Do you really want to quit?', 2)
ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')
ask_ok('OK to overwrite the file?', reminder='Come on, only yes or no!')
"""
"""
只给出必需的参数：ask_ok('Do you really want to quit?')
给出一个可选的参数：ask_ok('OK to overwrite the file?', 2)
或者给出所有的参数：ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')
"""


# 关键字参数

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


# 当存在一个形式为 **name 的最后一个形参时，它会接收一个字典
# *name，接收一个包含除了与已有形参列表以外的位置参数的 元组 的形参  组合使用 (*name 必须出现在 **name 之前。)
"""
complex(real=3, imag=5)
complex(**{'real': 3, 'imag': 5})

complex(3, 5)
complex(*(3, 5))
"""


def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])


cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

# 特殊参数
"""
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
      -----------    ----------     ----------
        |             |                  |
        |        Positional or keyword   |
        |                                - Keyword only
         -- Positional only
在这里 / 和 * 是可选的。 如果使用这些符号则表明可以通过何种形参将参数值传递给函数：仅限位置、位置或关键字，以及仅限关键字。 关键字形参也被称为命名形参。

3.8

def standard_arg(arg):
    print(arg)

def pos_only_arg(arg, /):
    print(arg)

def kwd_only_arg(*, arg):
    print(arg)

def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)
"""

"""
最后，请考虑这个函数定义，它的位置参数 name 和 **kwds 之间由于存在关键字名称 name 而可能产生潜在冲突:

def foo(name, **kwds):
    return 'name' in kwds
任何调用都不可能让它返回 True，因为关键字 'name' 将总是绑定到第一个形参。 例如:

但使用 / (仅限位置参数) 就可能做到，因为它允许 name 作为位置参数，也允许 'name' 作为关键字参数的关键字名称:
def foo(name, /, **kwds):
    return 'name' in kwds
>>> foo(1, **{'name': 2})
True
"""

"""
一般来说，这些 可变参数 将在形式参数列表的末尾，因为它们收集传递给函数的所有剩余输入参数。出现在 *args 参数之后的任何形式参数都是 ‘仅关键字参数’，也就是说它们只能作为关键字参数而不能是位置参数。:
def concat(*args, sep="/"):
    return sep.join(args)
"""

# 解包参数列表
print(list(range(*[3, 6])))


def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")


d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)


# lambda
# 使用一个lambda表达式来返回一个函数
def make_incrementor(n):
    return lambda x: x + n


f = make_incrementor(42)
print(f(0))
print(f(1))

# 传递一个小函数作为参数
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)


# 文档字符串
def my_function():
    """Do nothing, but document it.

    No, really, it doesn't do anything.
    """
    pass

print(my_function.__doc__)

## 函数标注
"""
只是用作提示，不会报错

函数标注通常用于 类型提示：例如以下函数预期接受两个 int 参数并预期返回一个 int 值:

def sum_two_numbers(a: int, b: int) -> int:
   return a + b

函数标注 以字典的形式存放在函数的 __annotations__ 属性中

"""
def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs

f('spam')

