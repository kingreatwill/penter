# 在 python 用 import 或者 from...import 来导入相应的模块。
#
# 将整个模块(somemodule)导入，格式为： import somemodule
#
# 从某个模块中导入某个函数,格式为： from somemodule import somefunction
#
# 从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc
#
# 将某个模块中的全部函数导入，格式为： from somemodule import *

import sys
print('\n python 路径为',sys.path)

from sys import path  #  导入特定的成员
print('path:',path) # 因为已经导入path成员，所以此处引用时不需要加sys.path
# sys.path 包含了一个 Python 解释器自动查找所需模块的路径的列表。

from sys import *  #  导入所有的成员
print('argv:',argv) # 因为已经导入所有的成员，所以此处引用时不需要加sys.argv