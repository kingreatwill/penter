# 重点：https://docs.python.org/zh-cn/3/library/importlib.html
"""
importlib 包的目的有两个。 第一个目的是在 Python 源代码中提供 import 语句的实现（并且因此而扩展 __import__() 函数）。
这提供了一个可移植到任何 Python 解释器的 import 实现。 相比使用 Python 以外的编程语言实现方式，这一实现更加易于理解。

第二个目的是实现 import 的部分被公开在这个包中，使得用户更容易创建他们自己的自定义对象 (通常被称为 importer) 来参与到导入过程中。
"""
# tutorial/06_module.py
import importlib

c = importlib.import_module("176_modules")
c.demo()

# import importlib.util
# spec = importlib.util.spec_from_file_location('my_module', '/paht/to/my_module')
# module = importlib.util.module_from_spec(spec)
# spec.loader.exec_module(module)
#
# import importlib.machinery, importlib.util
# loader = importlib.machinery.SourceFileLoader('my_module', '/path/to/my_module')
# spec = importlib.util.spec_from_loader(loader.name, loader)
# my_module = importlib.util.module_from_spec(spec)
# loader.exec_module(my_module)

# import importlib.util
# import sys
#
# # For illustrative purposes.
# name = 'itertools'
#
# if name in sys.modules:
#     print(f"{name!r} already in sys.modules")
# elif (spec := importlib.util.find_spec(name)) is not None:
#     # If you chose to perform the actual import ...
#     module = importlib.util.module_from_spec(spec)
#     sys.modules[name] = module
#     spec.loader.exec_module(module)
#     print(f"{name!r} has been imported")
# else:
#     print(f"can't find the {name!r} module")


import importlib.util
import sys

# For illustrative purposes.
import tokenize
file_path = tokenize.__file__
module_name = tokenize.__name__

spec = importlib.util.spec_from_file_location(module_name, file_path)
module = importlib.util.module_from_spec(spec)
sys.modules[module_name] = module
spec.loader.exec_module(module)