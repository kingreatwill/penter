import fibo
# import fibo as fib
"""
注解 出于效率的考虑，每个模块在每个解释器会话中只被导入一次。因此，如果你更改了你的模块，则必须重新启动解释器， 
或者，如果它只是一个要交互式地测试的模块，请使用 importlib.reload()，例如 import importlib; importlib.reload(modulename)
"""
fibo.fib(1000)
fibo.fib2(100)
print(fibo.__name__)

# from fibo import fib, fib2
# # from fibo import * #这会调入所有非以下划线（_）开头的名称
# # from fibo import fib as fibonacci
# fib(500)
# fib2(100)

"""
当一个名为 spam 的模块被导入的时候，解释器首先寻找具有该名称的内置模块。如果没有找到，然后解释器从 sys.path 变量给出的目录列表里寻找名为 spam.py 的文件。sys.path 初始有这些目录地址:

包含输入脚本的目录（或者未指定文件时的当前目录）。

PYTHONPATH （一个包含目录名称的列表，它和shell变量 PATH 有一样的语法）。https://docs.python.org/zh-cn/3/using/cmdline.html#envvar-PYTHONPATH

取决于安装的默认设置
"""

import sys
print(sys.path)

"""
为了加速模块载入，Python在 __pycache__ 目录里缓存了每个模块的编译后版本，名称为 module.version.pyc ，其中名称中的版本字段对编译文件的格式进行编码； 它一般使用Python版本号。例如，在CPython版本3.3中，spam.py的编译版本将被缓存为 __pycache__/spam.cpython-33.pyc。此命名约定允许来自不同发行版和不同版本的Python的已编译模块共存。

Python根据编译版本检查源的修改日期，以查看它是否已过期并需要重新编译。这是一个完全自动化的过程。此外，编译的模块与平台无关，因此可以在具有不同体系结构的系统之间共享相同的库。

Python在两种情况下不会检查缓存。首先，对于从命令行直接载入的模块，它从来都是重新编译并且不存储编译结果；其次，如果没有源模块，它不会检查缓存。为了支持无源文件（仅编译）发行版本， 编译模块必须是在源目录下，并且绝对不能有源模块。

给专业人士的一些小建议:

你可以在Python命令中使用 -O 或者 -OO 开关， 以减小编译后模块的大小。 -O 开关去除断言语句，-OO 开关同时去除断言语句和 __doc__ 字符串。由于有些程序可能依赖于这些，你应当只在清楚自己在做什么时才使用这个选项。“优化过的”模块有一个 opt- 标签并且通常小些。将来的发行版本或许会更改优化的效果。

一个从 .pyc 文件读出的程序并不会比它从 .py 读出时运行的更快，.pyc 文件唯一快的地方在于载入速度。

compileall 模块可以为一个目录下的所有模块创建.pyc文件。

关于这个过程，PEP 3147 中有更多细节，包括一个决策流程图。
"""

# winreg只在Windows下提供
# winreg --- Windows 注册表访问
# https://docs.python.org/zh-cn/3/library/winreg.html#module-winreg



"""
当导入这个包时，Python搜索 sys.path 里的目录，查找包的子目录。
必须要有 __init__.py 文件才能让 Python 将包含该文件的目录当作包。 
这样可以防止具有通常名称例如 string 的目录在无意中隐藏稍后在模块搜索路径上出现的有效模块。 
在最简单的情况下，__init__.py 可以只是一个空文件，但它也可以执行包的初始化代码或设置 __all__ 变量

包的用户可以从包中导入单个模块，例如:

import sound.effects.echo
这会加载子模块 sound.effects.echo 。但引用它时必须使用它的全名。

sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)
导入子模块的另一种方法是

from sound.effects import echo
这也会加载子模块 echo ，并使其在没有包前缀的情况下可用，因此可以按如下方式使用:

echo.echofilter(input, output, delay=0.7, atten=4)
另一种形式是直接导入所需的函数或变量:

from sound.effects.echo import echofilter
同样，这也会加载子模块 echo，但这会使其函数 echofilter() 直接可用:

echofilter(input, output, delay=0.7, atten=4)
请注意，当使用 from package import item 时，item可以是包的子模块（或子包），也可以是包中定义的其他名称，如函数，类或变量。 import 语句首先测试是否在包中定义了item；如果没有，它假定它是一个模块并尝试加载它。如果找不到它，则引发 ImportError 异常。

相反，当使用 import item.subitem.subsubitem 这样的语法时，除了最后一项之外的每一项都必须是一个包；最后一项可以是模块或包，但不能是前一项中定义的类或函数或变量。
"""
