# ctypes 是 Python 的外部函数库。它提供了与 C 兼容的数据类型，并允许调用 DLL 或共享库中的函数。
# 可使用该模块以纯 Python 形式对这些库进行封装。

from ctypes import *
print(windll.kernel32)

print(cdll.msvcrt)

libc = cdll.msvcrt
print(libc)

# 调用函数
print(libc.time(None))
print(hex(windll.kernel32.GetModuleHandleA(None)))

# 类型
i = c_int(42)
print(i)

print(i.value)

i.value = -99
print(i.value)