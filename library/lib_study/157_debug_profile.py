# https://docs.python.org/zh-cn/3/library/profile.html
import profile

import re
profile.run('re.compile("foo|bar")')

"""
ncalls
调用次数

tottime
在指定函数中消耗的总时间（不包括调用子函数的时间）

percall
是 tottime 除以 ncalls 的商

cumtime
指定的函数及其所有子函数（从调用到退出）消耗的累积时间。这个数字对于递归函数来说是准确的。

percall
是 cumtime 除以原始调用（次数）的商（即：函数运行一次的平均时间）

filename:lineno(function)
提供相应数据的每个函数
"""


