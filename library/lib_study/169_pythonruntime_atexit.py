import atexit # 有点像defer

# 在正常的程序终止时 (举例来说, 当调用了 sys.exit() 或是主模块的执行完成时), 所有注册过的函数都会以后进先出的顺序执行.
# 这样做是假定更底层的模块通常会比高层模块更早引入, 因此需要更晚清理.
atexit.register(print, 1)
atexit.register(print, 2)

# try:
#     with open("counterfile") as infile:
#         _count = int(infile.read())
# except FileNotFoundError:
#     _count = 0
#
# def incrcounter(n):
#     global _count
#     _count = _count + n
#
# def savecounter():
#     with open("counterfile", "w") as outfile:
#         outfile.write("%d" % _count)
#
# import atexit
# atexit.register(savecounter)

import atexit

# 只有在函数不需要任何参数调用时才能工作.
@atexit.register
def goodbye():
    print("You are now leaving the Python sector.")
