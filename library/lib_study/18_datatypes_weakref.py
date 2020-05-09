# 弱引用
# 几个内建类型如 list 和 dict 不直接支持弱引用，但可以通过子类化添加支持:
import weakref
# python中的垃圾回收机制是简单的基于引用计数规则的

class Dict(dict):
    pass


obj = Dict(red=1, green=2, blue=3)  # this object is weak referenceable

print(obj)

# class weakref.ref(object[, callback])
# 返回对 对象 的弱引用。如果原始对象仍然存活，则可以通过调用引用对象来检索原始对象；如果引用的原始对象不再存在，则调用引用对象将得到 None 。
# 如果提供了 回调 而且值不是 None ，并且返回的弱引用对象仍然存活，则在对象即将终结时将调用回调;弱引用对象将作为回调的唯一参数传递；指示物将不再可用。
# d = {"red": 1, "green": 2, "blue": 3}
wd = weakref.ref(obj) # 不能用于list 和 dict
# 如果 object 可哈希，则弱引用也为 hashable。
print(wd)

weakref.proxy() #  Proxy 对象不是 hashable 对象，无论被引用对象是否可哈希


