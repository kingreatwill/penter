import copy
import sys
import types


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


point1 = Point(1, 2)
point2 = eval("{}({}, {})".format("Point", 1, 2))
point3 = globals()["Point"](1, 2)
point4 = locals()["Point"](1, 2)
point5 = getattr(sys.modules[__name__], "Point")(1, 2)
point6 = copy.deepcopy(point1)
point7 = point1.__class__(1, 2)
point8 = type('Point', (Point,), {})(1, 2)
point9 = types.new_class('Point', (Point,), {})(1, 2)
print(point9)
print("------------动态类型创建-types.new_class(name, bases=(), kwds=None, exec_body=None)")


def prepare_class():
    # Basic test of metaclass derivation
    expected_ns = {}

    class A(type):
        def __new__(*args, **kwargs):
            return type.__new__(*args, **kwargs)

        def __prepare__(*args):
            return expected_ns

    B = types.new_class("B", (object,))
    C = types.new_class("C", (object,), {"metaclass": A})

    meta, ns, kwds = types.prepare_class("D", (B, C), {"metaclass": type})
    print(meta is A)
    print(ns is expected_ns)
    print(len(kwds) == 0)


prepare_class()

print(types.resolve_bases([Point, object]))
print("-------------")
print(types.FunctionType)
print(isinstance(prepare_class, types.FunctionType))
print(types.CodeType)
print(types.LambdaType)
print(types.GeneratorType)
print(types.CoroutineType)  # 对象的类型，由 async def 函数创建。
print(types.AsyncGeneratorType)  # asynchronous generator 迭代器对象的类型，由异步生成器函数创建。
print(types.MethodType)
print(types.BuiltinFunctionType)
print(types.BuiltinMethodType)
print(types.WrapperDescriptorType)

print(types.MethodWrapperType)
print(types.MethodDescriptorType)
print(types.ClassMethodDescriptorType)

print(types.FrameType)
print(types.GetSetDescriptorType)
print(types.MemberDescriptorType)
print("-------------")

print("----------class types.CodeType(**kwargs)")
# print(str( b'\x04\x71\x00\x00', "utf-8"))
# co = types.CodeType(0, 0, 0, 0, 0, b'\x04\x71\x00\x00',
#                     (), (), (), '', '', 1, b'')
# exec(co)

print("------------class types.ModuleType(name, doc=None)")

print("------------class types.TracebackType(tb_next, tb_frame, tb_lasti, tb_lineno)")

print("------------class types.MappingProxyType(mapping)")

print("-----------class types.SimpleNamespace")
d = {'a': 1, 'b': 2}
sn = types.SimpleNamespace(**d)  # 这里的**不可以少,表示命名关键字参数
print(sn)
print(sn.a)
print("-----------types.DynamicClassAttribute 在类上访问 __getattr__ 的路由属性")


# Metaclass
class Funny(type):

    def __getattr__(self, value):
        print('search in meta')
        # Normally you would implement here some ifs/elifs or a lookup in a dictionary
        # but I'll just return the attribute
        return Funny.dynprop

    # Metaclasses dynprop:
    dynprop = 'Meta'


class Fun(metaclass=Funny):
    def __init__(self, value):
        self._dynprop = value

    @types.DynamicClassAttribute
    def dynprop(self):
        return self._dynprop


print(Fun.dynprop)
print(Fun('Not-Meta').dynprop)


class Funny(type):
    dynprop = 'Very important meta attribute, do not override'


class Fun(metaclass=Funny):
    def __init__(self, value):
        self._stub = value

    @property
    def dynprop(self):
        return 'Haha, overridden it with {}'.format(self._stub)


print(Fun.dynprop)
print(Fun(2).dynprop)

print("-----------------types.coroutine")
from types import coroutine as t_coroutine
from asyncio import coroutine as a_coroutine, ensure_future, sleep, get_event_loop


@a_coroutine
def a_sleep():
    print("doing something in async")


@t_coroutine
def t_sleep():
    print("doing something in types")


async def start():
    sleep_a = a_sleep()
    sleep_t = t_sleep()
    print("Going down!")


loop = get_event_loop()
loop.run_until_complete(start())

print(isinstance(t_sleep, types.CoroutineType)) # False
print(isinstance(start, types.CoroutineType)) # False
