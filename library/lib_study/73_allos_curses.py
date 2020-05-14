# 终端字符单元显示的处理

import locale, curses, curses.textpad, curses.ascii, curses.panel

locale.setlocale(locale.LC_ALL, '')
code = locale.getpreferredencoding()
print(code)
# CHCP 65001 显示中文
