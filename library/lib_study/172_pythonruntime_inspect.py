"""
inspect 模块提供了一些有用的函数帮助获取对象的信息，
例如模块、类、方法、函数、回溯、帧对象以及代码对象。
例如它可以帮助你检查类的内容，获取某个方法的源代码，取得并格式化某个函数的参数列表，或者获取你需要显示的回溯的详细信息。

该模块提供了4种主要的功能：类型检查、获取源代码、检查类与函数、检查解释器的调用堆栈。
# 重点： https://docs.python.org/zh-cn/3/library/inspect.html
"""
import inspect
import types


class Foo(object):
    '''Foo doc'''

    def __init__(self, name):
        self.__name = name

    def getname(self):
        return self.__name


f = Foo("xx")
print(inspect.getdoc(f))
print(inspect.getsourcelines(Foo))
print(inspect.getfile(Foo))

print(inspect.getmembers(Foo, inspect.ismethod))
print(inspect.getmembers(Foo))

print(inspect.getmembers(f, inspect.ismethod))
print(inspect.getmembers(f))

print("------------")


def attr_from_locals(locals_dict):
    self = locals_dict.pop('self')
    args = inspect.getfullargspec(self.__init__.__func__).args[1:]
    for k in args:
        setattr(self, k, locals_dict[k])
    keywords = inspect.getfullargspec(self.__init__.__func__).varkw
    if keywords:
        keywords_dict = locals_dict[keywords]
        for k in keywords_dict:
            setattr(self, k, keywords_dict[k])


class Foo(object):
    def __init__(self, name, **kwargv):
        attr_from_locals(locals())


f = Foo('bar', color='yellow', num=1)
print(f.__dict__)

print("---------")
from inspect import formatargspec, getfullargspec


def f(a: int, b: float):
    pass


# print(formatargspec(*getfullargspec(f)))


print("------")
from inspect import getcallargs


def f2(a, b=1, *pos, **named):
    pass


print(getcallargs(f2, 1, 2, 3) == {'a': 1, 'named': {}, 'b': 2, 'pos': (3,)})

print(getcallargs(f2, a=2, x=4) == {'a': 2, 'named': {'x': 4}, 'b': 1, 'pos': ()})

# inspect.unwrap  在tutorial/17_decorator.py
"""
inspect.iscoroutine(obj) 如果obj是原生协程对象，返回True。
inspect.iscoroutinefunction(obj) 如果obj是原生协程函数，返回True。
inspect.isawaitable(obj) 如果obj是awaitable返回True。
inspect.getcoroutinestate(coro) 返回原生协程对象的当前状态（inspect.getfgeneratorstate(gen)的镜像）。
inspect.getcoroutinelocals(coro) 返回一个原生协程对象的局部变量的映射【译注：变量名->值】（inspect.getgeneratorlocals(gen) 的镜像）。
"""


def gen():
    yield


@types.coroutine
def gen_coro():
    yield


assert not inspect.isawaitable(gen())
assert inspect.isawaitable(gen_coro())


async def agen():
    yield 1


print(inspect.isasyncgenfunction(agen))

print("----------")


def foo(a, b, *, c, d=10):
    pass


sig = inspect.signature(foo)
# 打印所有不带默认值的仅关键字参数：
for param in sig.parameters.values():
    if (param.kind == param.KEYWORD_ONLY and
            param.default is param.empty):
        print('Parameter:', param)
# 打印所有参数的说明 3.8
# for param in sig.parameters.values():
#     print(param.kind.description)
# """
# positional or keyword
# positional or keyword
# keyword-only
# keyword-only
# """

from inspect import Parameter

param = Parameter('foo', Parameter.KEYWORD_ONLY, default=42)
print(str(param))

print(str(param.replace()))  # Will create a shallow copy of 'param'

print(str(param.replace(default=Parameter.empty, annotation='spam')))


def demo(a, *, b):
    print(a, b)


sig = inspect.signature(demo)
ba = sig.bind(10, b=20)
demo(*ba.args, **ba.kwargs)
