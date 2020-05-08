
# readline模块定义了一系列函数用来读写Python解释器中历史命令，并提供自动补全命令功能。这个模块可以通过relcompleter模块直接调用，模块中的设置会影响解释器中的交互提示，以及内置函数raw_input()和input()提供的提示。
# https://pypi.org/project/readline/
# http://gnuwin32.sourceforge.net/packages/readline.htm
# 没有这个模块？？？
# 1.安装readline
# cmd命令行，就会自动安装readline模块
#
# pip install pyreadline
import os
"""
>>> import rlcompleter
>>> import readline
>>> readline.parse_and_bind("tab: complete")
>>> readline. <TAB PRESSED>
readline.__doc__          readline.get_line_buffer(  readline.read_init_file(
readline.__file__         readline.insert_text(      readline.set_completer(
readline.__name__         readline.parse_and_bind(
>>> readline.
搞了半天原来只在交互环境中存在.
"""

