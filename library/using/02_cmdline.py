# python [-bBdEhiIOqsSuvVWx?] [-c command | -m module-name | script | - ] [args]

# https://docs.python.org/zh-cn/3/using/cmdline.html
"""
-c <command>
执行 command 中的 Python 代码。 command 可以为一条或以换行符分隔的多条语句，其中前导空格像在普通模块代码中一样具有作用。

如果给出此选项，sys.argv 的首个元素将为 "-c" 并且当前目录将被加入 sys.path 的开头（以允许该目录中的模块作为最高层级模块被导入）。

使用 command 参数会引发 审计事件 cpython.run_command 。

-m <module-name>
在 sys.path 中搜索指定名称的模块并将其内容作为 __main__ 模块来执行。

由于该参数为 module 名称，你不应给出文件扩展名 (.py)。 模块名称应为绝对有效的 Python 模块名称，但具体实现可能并不总是强制要求这一点（例如它可能允许你使用包含连字符的名称）。

包名称（包括命名空间包）也允许使用。 当所提供的是包名称而非普通模块名称时，解释器将把 <pkg>.__main__ 作为主模块来执行。 此行为特意被设计为与作为脚本参数传递给解释器的目录和 zip 文件的处理方式类似。

注解 此选项不适用于内置模块和以 C 编写的扩展模块，因为它们并没有对应的 Python 模块文件。 但是它仍然适用于预编译的模块，即使没有可用的初始源文件。
如果给出此选项，sys.argv 的首个元素将为模块文件的完整路径 (在定位模块文件期间，首个元素将设为 "-m")。 与 -c 选项一样，当前目录将被加入 sys.path 的开头。

-I 选项可用来在隔离模式下运行脚本，此模式中 sys.path 既不包含当前目录也不包含用户的 site-packages 目录。 所有 PYTHON* 环境变量也会被忽略。

许多标准库模块都包含作为脚本执行时会被发起调用的代码。 其中的一个例子是 timeit 模块:

python -m timeit -s 'setup here' 'benchmarked code here'
python -m timeit -h # for details

runpy.run_module()
Python 代码可以直接使用的等效功能
"""