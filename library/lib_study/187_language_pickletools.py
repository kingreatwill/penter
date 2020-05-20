# 此模块包含与 pickle 模块内部细节有关的多个常量，一些关于具体实现的详细注释，以及一些能够分析封存数据的有用函数。
# 此模块的内容对需要操作 pickle 的 Python 核心开发者来说很有用处；
# https://docs.python.org/zh-cn/3/library/pickletools.html
import pickle
import pickletools


class Foo:
    attr = 'A class attribute'

picklestring = pickle.dumps(Foo)

pickletools.dis(picklestring)