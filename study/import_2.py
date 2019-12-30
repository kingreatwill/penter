# 导入模块
import sys

import common
# 一个模块只会被导入一次，不管你执行了多少次import。这样可以防止导入模块被一遍又一遍地执行。
# 现在可以调用模块里包含的函数了
common.print_func("Runoob")
common.fib(1000)
print(common.fib2(1000))

# 内置的函数 dir() 可以找到模块内定义的所有名称。以一个字符串列表的形式返回:
# 如果没有给定参数，那么 dir() 函数会罗列出当前定义的所有名称:
print(dir(common))
