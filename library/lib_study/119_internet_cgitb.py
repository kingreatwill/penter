# https://docs.python.org/zh-cn/3/library/cgitb.html
"""
cgitb模块为Python脚本提供了一个特殊的异常管理器。名字有点误导人，它最初设计是为了以HTML格式展示cgi脚本的大量异常信息。
后来，他扩展为也可以展示纯文本信息。该模块激活后，如果发生了未捕获的异常，将会展示格式化的输出报告。该报告包括源代码每一层的回溯，以及当前执行程序的参数和局部变量。
以及，你可以选择将这些信息存到一个文件里，而不是发送到浏览器。

将下面这行代码加到你的浏览器头部：

import cgitb
cgitb.enable()
两个函数：

cgitb.encable(display=1, logdir=None, context=5, format="html")

display 1，发送至浏览器；0， 不发送
logdir 如果有的话，写到该目录下
context 显示错误代码周围的代码行数
format 是否显示为HTML，除了'html'之外的所有值，都会显示为纯文本
cgitb.handle(info=None)

如果你想用cgitb处理异常，你可以调用这个函数。
info 应当是含有异常类型、异常值和traceback对象的三元组，——如同sys.exc_info()返回的那样。如果不提供info，则从sys.exc_info中获取。
"""