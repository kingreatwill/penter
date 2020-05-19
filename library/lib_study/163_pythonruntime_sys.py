import sys

# https://www.jianshu.com/p/5ef7183ade1b
# print(sys.abiflags) linux

# 153_debug_audit_events.py
# def audit_hook(event,args):
#   print(event)
# sys.addaudithook(audit_hook)
# print('test')

print(sys.argv)

print(sys.base_exec_prefix)
print(sys.base_prefix)

print(sys.exec_prefix)  # 虚拟环境
print(sys.prefix)  # 虚拟环境

# 本地字节顺序的指示符。在大端序（最高有效位优先）操作系统上值为 'big' ，在小端序（最低有效位优先）操作系统上为 'little' 。
# 字节存放顺序：大尾，小尾  http://blog.sina.com.cn/s/blog_6277623c0102vntv.html
print(sys.byteorder)

# 包含了所有的被编译进 Python 解释器的模块
print(sys.builtin_module_names)

sys.call_tracing(print, (1,))


def mrintArgs(*args):  # 创建方法，收集参数。
    print(list(args))


sys.call_tracing(mrintArgs, (1, 2, 3, 4))

print(sys.copyright)

sys._clear_type_cache()

print(sys._current_frames())

# sys.breakpointhook()

# 打印CPython内存分配器状态的低级信息到stderr。
# sys._debugmallocstats()

# Windows可用
print(sys.dllhandle)
print("-----------------")
# def audit_hook2(event,args):
#   if event in ['test']:
#     print('event:'+event)
#     print(args)
# sys.addaudithook(audit_hook2)
# sys.audit('test','Hello World!')
# """
# 输出：
# event:test
# ('Hello World!',)
# """
# sys.displayhook('test')

# 如果值为True，导入源模块时python将不会写入.pyc文件。
# 如果这是True，Python就不会试图在源模块的导入中编写.pyc文件。这个值最初根据-B命令行选项和PYTHONDONTWRITEBYTECODE环境变量设置为True或False，但是您可以自己设置它来控制字节码文件的生成。
print(sys.dont_write_bytecode)

# print(sys.pycache_prefix)


# def new_excepthook(type, value, traceback):  # 创建一个新的异常处置方法
#     print(type, '+', value, '+', traceback)
#
#
# sys.excepthook = new_excepthook  # 用新的方法替代默认的方法
# print(a)  # 故意触发一个异常，不抛出错误，只打印,错误后的代码同样不会执行

print("------------")
# 此函数返回三个值的元组，这些值提供有关当前正在处理的异常的信息。
print(sys.exc_info())
try:
    1 / 0  # 故意触发一个异常
except Exception as e:
    info = sys.exc_info()  # 返回异常信息
    print(info)

print(sys.exec_prefix)
print(sys.executable)

print(sys.flags)
print(sys.float_info)
print(sys.float_info.dig)

s = '3.14159265358979'  # decimal string with 15 significant digits
print(format(float(s), '.15g'))  # convert to float and back -> same value
s = '9876543211234567'  # 16 significant digits is too many!
print(format(float(s), '.16g'))  # conversion changes value

print(sys.float_repr_style)

# 返回解释器当前分配的内存块数，而不考虑其大小。
print(sys.getallocatedblocks())

# 3.2版后已移除: Use getswitchinterval() instead.
# setcheckinterval().
# print(sys.getcheckinterval())
# 返回解释器的“线程切换间隔。
print(sys.getswitchinterval())  # setswitchinterval().

print(sys.getdefaultencoding())
print(sys.getfilesystemencoding())
print(sys.getfilesystemencodeerrors())


# 返回<object>的引用次数。
# 引用次数会比期望值值多一个，因为它包含getrefcount()参数的临时引用。
class Test():
    pass


t = Test()
print(sys.getrefcount(t))  # t 本身是Test,所以被引用了一次。

print(sys.getrecursionlimit())  # setrecursionlimit().
print(sys.getsizeof(t))

print(sys._getframe(0))
print("---------------------")


def test(*args):
    print("args=" + str(list(args)))


# sys.setprofile(test)
#
# print(sys.getprofile())


print("---------------------")

# sys.settrace(test)
print("xxxxxxxxxxxxxxxx", sys.gettrace())

print(sys.getwindowsversion())


def firstiter():
    print('from firstiter.')


def finalizer():
    print('from finalizer.')


sys.set_asyncgen_hooks(firstiter, finalizer)
print(sys.get_asyncgen_hooks())

print(sys.get_coroutine_origin_tracking_depth())

print(sys.hash_info)

print(sys.hexversion)
print(sys.implementation)

print(sys.int_info)

print(sys.__interactivehook__)

s1 = sys.intern('hello!哈哈')
s2 = 'hello!哈哈'
s3 = ('hello!哈哈')
print(s1 == s2)
print(s1 is s3)
print(sys.is_finalizing())

# 最大的Int值。32位平台是2**31 - 1。64位平台是2**63 - 1。
print(sys.maxsize)

# unicode字符的最大代码点。
print(sys.maxunicode)
print(chr(sys.maxunicode))
# 1114111 (0x10FFFF in hexadecimal).
# print(chr(sys.maxunicode +1))

print(sys.meta_path)

print(sys.modules)
import timeit
print(sys.modules["timeit"])

# 字符串列表，用于指定模块的搜索路径。 从环境变量PYTHONPATH初始化，再加上与安装有关的默认值。
print(sys.path)
import os

print(os.getenv("PYTHONPATH"))

print(sys.path_hooks)

print(sys.path_importer_cache)

print(sys.platform)

# 只有在命令行里才有
# print(sys.ps1)
# print(sys.ps2)

print(sys.getfilesystemencoding())
print(sys.getfilesystemencodeerrors())
sys._enablelegacywindowsfsencoding()
print(sys.getfilesystemencoding())
print(sys.getfilesystemencodeerrors())


# input1 = sys.stdin.readline()
# print(input1)
sb = sys.stdout.buffer.write(b'abcxx')
print(sb)

output = sys.stdout.write
output('Hello World\n')
# err = sys.stderr.write
# err('WARNING: something bad occur!')
# 'nt': Windows 线程、'pthread': POSIX 线程、'solaris': Solaris 线程
# 锁实现的名称：'semaphore': 锁使用信号量、'mutex+cond': 锁使用互斥和条件变量、None 如果此信息未知
print(sys.thread_info)

# 默认值为 1000 .当设置为 0 或者更少，抑制所有的回溯信息，只打印异常类型和值。
# print(sys.tracebacklimit)

# import contextlib
# @contextlib.contextmanager
# def throw_unraisable_exceptions():
#     unraisable = None
#     old_hook = sys.unraisablehook
#
#     def hook(exc):
#         nonlocal unraisable
#         unraisable = exc
#
#     sys.unraisablehook = hook
#     try:
#         yield
#         if unraisable is not None:
#             raise unraisable
#     finally:
#         unraisable = None
#         sys.unraisablehook = old_hook
#
#
# try:
#     with throw_unraisable_exceptions():
#         1/0
# except Exception as e:
#     ... # the exception is now here

print(sys.version)
print(sys.api_version)
print(sys.version_info)
print(sys.warnoptions)
print(sys.winver)

# 通过 -X 命令行选项传递的各种实现特定标志的字典。
# 如果显式给定，则选项名要么映射到它们的值，要么映射到 True。
print(sys._xoptions)

"""
python -Xa=b -Xc 163_pythonruntime_sys.py
or 
$ ./python -Xa=b -Xc
Python 3.2a3+ (py3k, Oct 16 2010, 20:14:50)
[GCC 4.4.3] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import sys
>>> sys._xoptions
{'a': 'b', 'c': True}
"""