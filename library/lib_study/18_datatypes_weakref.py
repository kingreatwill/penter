# 弱引用
# 几个内建类型如 list 和 dict 不直接支持弱引用，但可以通过子类化添加支持:
import gc
import weakref

print(weakref.ReferenceType)
print(weakref.ProxyType)
print(weakref.CallableProxyType)
print(weakref.ProxyTypes)
print("------------------")
import weakref


class Object:
    pass


o = Object()
r = weakref.ref(o)
o2 = r()
print(o is o2)


# python中的垃圾回收机制是简单的基于引用计数规则的

class Dict(dict):
    pass


obj = Dict(red=1, green=2, blue=3)  # this object is weak referenceable

print(obj)

# class weakref.ref(object[, callback])
# 返回对 对象 的弱引用。如果原始对象仍然存活，则可以通过调用引用对象来检索原始对象；如果引用的原始对象不再存在，则调用引用对象将得到 None 。
# 如果提供了 回调 而且值不是 None ，并且返回的弱引用对象仍然存活，则在对象即将终结时将调用回调;弱引用对象将作为回调的唯一参数传递；指示物将不再可用。
# d = {"red": 1, "green": 2, "blue": 3}
wd = weakref.ref(obj)  # 不能用于list 和 dict

# 如果 object 可哈希，则弱引用也为 hashable。
print(wd())  # 我们使用 weakref.ref() 创建弱引用，每次使用时都需要形如这样 xx() 来获取
# 如果一个对象只剩下一个弱引用，那么它是可以被垃圾回收的
# weakref.proxy() #  Proxy 对象不是 hashable 对象，无论被引用对象是否可哈希
p = weakref.proxy(obj)
print(p)


# 对 weakref 的一点理解
class Node(object):
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.children = []

    def add_child(self, child):
        self.children.append(child)
        child.parent = self

    def __del__(self):
        print('__del__')


n = Node(0)
del n  # __del__

n1 = Node(1)
n2 = Node(2)
n1.add_child(n2)
del n1  # no output  没有执行def __del__(self): 原因是python的垃圾回收仅仅是基于引用计数，而在树形结构中父子节点之间相互存在引用关系,所以造成死锁,不会真的删除对象实例。
print(n2.parent)  ## <__main__.Node at 0x7fd87ad5c250>
# 双亲节点的指针指向孩子节点，孩子节点又指向双亲节点。这构成了循环引用，所以每个对象的引用计数都不可能变成 0
gc.collect()  # 手动gc
print(n2.parent)  ## <__main__.Node at 0x7fd87ad5c250>
del n2  # no output
gc.collect()  # 只有删除n1和n2再次GC才会触发 def __del__(self):方法，但是这样写不友好

print("-------------------")
import weakref


class Node(object):

    def __init__(self, data):
        self.data = data
        self._parent = None
        self.children = []

    @property
    def parent(self):
        return None if self._parent is None else self._parent()

    @parent.setter
    def parent(self, node):
        self._parent = weakref.ref(node, callback)

    def add_child(self, child):
        self.children.append(child)
        child.parent = self


def callback(ref):
    print('__del__', ref)


n1 = Node(0)
n2 = Node(2)
print(n1, n2)

# <__main__.Node object at 0x7fb0c2750c10> <__main__.Node object at 0x7fb0c2750d10>
n1.add_child(n2)
print(weakref.getweakrefcount(n1))
print(weakref.getweakrefcount(n2))
print(weakref.getweakrefs(n1))
del n1


# __del__ <weakref at 0x7fb0c26e75d0; dead>

class DemoClass:
    def __init__(self, name):
        self.name = name


print("----------------class weakref.WeakKeyDictionary([dict])")
n = DemoClass("name")
a = DemoClass("age")
keyd = weakref.WeakKeyDictionary({n: "xxx", a: 2})
print(keyd[n])
for k, v in keyd.items():
    print(k, v)
del n
for k, v in keyd.items():
    print(k, v)
print(keyd.keyrefs())  # 返回包含对键的弱引用的可迭代对象。
print("----------------class weakref.WeakValueDictionary([dict])")

n = DemoClass("name")
a = DemoClass("age")
keyd = weakref.WeakValueDictionary({"name": n, "age": a})
print(keyd["name"])
for k, v in keyd.items():
    print(k, v)
del n
for k, v in keyd.items():
    print(k, v)
print(keyd.valuerefs())
print("----------------class weakref.WeakSet([elements])")

n = DemoClass("name")
a = DemoClass("age")
keyd = weakref.WeakSet({n, a})
for k in keyd:
    print(k)
del n
for k in keyd:
    print(k)

print("----------------class weakref.WeakMethod(method)")


class C:
    def method(self):
        print("method called!")


c = C()
r = weakref.WeakMethod(c.method)

print(r())  # <bound method C.method of <__main__.C object at 0x0000022E4789BB48>>
r()()  # method called!
del c
print(r())  # None
print("---------------class weakref.finalize(obj, func, *args, **kwargs)")
import weakref


class Object:
    pass


kenny = Object()
f = weakref.finalize(kenny, print, "You killed Kenny!")
# print(f.detach()) # (<__main__.Object object at 0x000002221F7B0A88>, <built-in function print>, ('You killed Kenny!',), {})
print(
    f.peek())  # (<__main__.Object object at 0x000002858FFB4B88>, <built-in function print>, ('You killed Kenny!',), {})
print(f.alive)  # True
# del kenny # "You killed Kenny!"
f()  # You killed Kenny!   直接调用相当于del kenny
print(f.peek())  # None
# print(f.detach()) # None
print(f.alive)  # False
"""
detach()
如果 self 为存活状态则将其标记为已死亡，并返回元组 (obj, func, args, kwargs)。 如果 self 已死亡则返 None。
peek()
如果 self 为存活状态则返回元组 (obj, func, args, kwargs)。 如果 self 已死亡则返回 None。
"""

'''
这个例子演示了如何将 ref 的一个子类用于存储有关对象的附加信息并在引用被访问时影响其所返回的值:

import weakref

class ExtendedRef(weakref.ref):
    def __init__(self, ob, callback=None, /, **annotations):
        super(ExtendedRef, self).__init__(ob, callback)
        self.__counter = 0
        for k, v in annotations.items():
            setattr(self, k, v)

    def __call__(self):
        """Return a pair containing the referent and the number of
        times the reference has been called.
        """
        ob = super(ExtendedRef, self).__call__()
        if ob is not None:
            self.__counter += 1
            ob = (ob, self.__counter)
        return ob

这个简单的例子演示了一个应用如何使用对象 ID 来提取之前出现过的对象。 然后对象的 ID 可以在其它数据结构中使用，而无须强制对象保持存活，但处于存活状态的对象也仍然可以通过 ID 来提取。

import weakref

_id2obj_dict = weakref.WeakValueDictionary()

def remember(obj):
    oid = id(obj)
    _id2obj_dict[oid] = obj
    return oid

def id2obj(oid):
    return _id2obj_dict[oid]
    
除非你将 atexit 属性设为 False，否则终结器在程序退出时如果仍然存活就将被调用。 例如

>>> obj = Object()
>>> weakref.finalize(obj, print, "obj dead or exiting")
<finalize object at ...; for 'Object' at ...>
>>> exit()
obj dead or exiting
'''


class TempDir:
    def __init__(self):
        self.name = "tempfile.mkdtemp()"

    def remove(self):
        if self.name is not None:
            print("remove", self.name)
            self.name = None

    @property
    def removed(self):
        print("removed", self.name)
        return self.name is None

    def __del__(self):
        print("__del__", self.name) # 程序退出或者del时执行
        self.remove()

print("-------------")
t = TempDir()
print(t.removed)
print("-------------")



class TempDir2:
    def __init__(self):
        self.name = "tempfile.mkdtemp()"
        self._finalizer = weakref.finalize(self, print, "_finalizer", self.name) # 程序退出或者del时执行

    def remove(self):
        self._finalizer()

    @property
    def removed(self):
        return not self._finalizer.alive

t2 = TempDir2()
del t2
print("-------------对象被作为垃圾回收，对象的 remove() 方法被调用，或程序退出。")

