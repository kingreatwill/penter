# Python 字节码反汇编器
# https://docs.python.org/zh-cn/3/library/dis.html
import dis


def myfunc(alist):
    return len(alist)
# 显示 myfunc() 的反汇编
dis.dis(myfunc)

print("------------")
bytecode = dis.Bytecode(myfunc)
print(bytecode.dis())
for instr in bytecode:
    print(instr.opname)

print(dis.opname)
print(dis.opmap)