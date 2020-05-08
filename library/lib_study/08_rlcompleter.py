# rlcompeleter 通过补全有效的 Python 标识符和关键字定义了一个适用于 readline 模块的补全函数。
# rlcompleter 模块是为了使用 Python 的 交互模式 而设计的。 除非 Python 是通过 -S 选项运行, 这个模块总是自动地被导入且配置 (参见 Readline configuration)。
import rlcompleter
"""
>>> import rlcompleter
>>> import readline
>>> readline.parse_and_bind("tab: complete")
>>> readline. <TAB PRESSED>
readline.__doc__          readline.get_line_buffer(  readline.read_init_file(
readline.__file__         readline.insert_text(      readline.set_completer(
readline.__name__         readline.parse_and_bind(
>>> readline.
"""