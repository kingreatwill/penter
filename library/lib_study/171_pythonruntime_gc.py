import gc
"""
垃圾回收器把所有对象分类为三代,取决于对象幸存于多少次垃圾回收。
新创建的对象会被放在最年轻代（第 0 代）。
如果一个对象幸存于一次垃圾回收，则该对象会被放入下一代。
第 2 代是最老的一代，因此这一代的对象幸存于垃圾回收后，仍会留在第 2 代。
为了判定何时需要进行垃圾回收，垃圾回收器会跟踪上一次回收后，分配和释放的对象的数目。
当分配对象的数量减去释放对象的数量大于阈值 threshold0 时，回收器开始进行垃圾回收。
起初只有第 0 代会被检查。当上一次第 1 代被检查后，第 0 代被检查的次数多于阈值 threshold1 时，第 1 代也会被检查。
相似的， threshold2 设置了触发第 2 代被垃圾回收的第 1 代被垃圾回收的次数。
"""
# sys.getrefcount(t)    #sys.getrefcount函数用来查看一个对象有几个引用
"""
# gc.set_debug(gc.DEBUG_LEAK)
gc.DEBUG_STATS
在回收完成后打印统计信息。当回收频率设置较高时，这些信息会比较有用。

gc.DEBUG_COLLECTABLE
当发现可回收对象时打印信息。

gc.DEBUG_UNCOLLECTABLE
打印找到的不可回收对象的信息（指不能被回收器回收的不可达对象）。这些对象会被添加到 garbage 列表中。

在 3.2 版更改: 当 interpreter shutdown 时，即解释器关闭时，若 garbage 列表中存在对象，这些对象也会被打印输出。

gc.DEBUG_SAVEALL
设置后，所有回收器找到的不可达对象会被添加进 garbage 而不是直接被释放。这在调试一个内存泄漏的程序时会很有用。

gc.DEBUG_LEAK
调试内存泄漏的程序时，使回收器打印信息的调试标识位。（等价于 DEBUG_COLLECTABLE | DEBUG_UNCOLLECTABLE | DEBUG_SAVEALL ）。
"""



print(gc.get_stats())
"""
collections 是该代被回收的次数；
collected 是该代中被回收的对象总数；
uncollectable 是在这一代中被发现无法收集的对象总数 （因此被移动到 garbage 列表中）。
"""

print(gc.get_count())


print(gc.is_tracked("a"))
print(gc.is_tracked([]))

print("-------------")
debug = gc.get_debug()
print(debug)
#gc.set_debug(debug | gc.DEBUG_SAVEALL)

"""
gc.disable()关闭自动的垃圾回收，改为手动；

gc.get_count()查看0、1、2代的数量(创建的对象数量-销毁的对象数量)

gc.get_threshold()查看0、1、2代的阈值

gc.collect(*args, **kwargs)手动执行垃圾回收，参数可以为0、1、2，表示回收指定代的垃圾；没有参数，表示0、1、2代全部回收，返回不可达的对象数量，不可达的对象也是要被清楚的对象，会被标记清除

gc.set_debug(DEBUG_COLLECTABLE|DEBUG_LEAK|DEBUG_SAVEALL|DEBUG_STATS|DEBUG_UNCOLLECTABLE) 把所有的debug开关打开。估计后端的C语音是根据8个bit位来判断debug开关功能的。
"""

print("------------")


class A():
  def __init__(self):
    pass
  def __del__(self):
    pass

class B():
  def __init__(self):
    pass
  def __del__(self):
    pass

a = A()
b = B()
a._b = b
b._a = a
del a
del b

print(gc.collect())
print(gc.garbage)