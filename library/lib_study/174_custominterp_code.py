# 如果你想要一个支持附加一些特殊功能到 Python 语言的 Python 解释器，你应该看看 code 模块。 （ codeop 模块是低层级的，用于支持编译可能不完整的 Python 代码块。）

# py_compile 模块
import code
# ``compile_command`` 与内建 ``compile`` 函数行为相似, 但它会通过测试来保证你传递的是一个完成的 Python 语句.
code.compile_command("print(2)")



ii = code.InteractiveInterpreter()
ii.runsource("print(1)")


# console = code.InteractiveConsole()
# console.interact()