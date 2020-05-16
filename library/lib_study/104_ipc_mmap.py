"""
class mmap.mmap(fileno, length, tagname=None, access=ACCESS_DEFAULT[, offset])
（ Windows 版本） 映射被文件句柄 fileno 指定的文件的 length 个字节，并创建一个 mmap 对象。如果 length 大于当前文件大小，则文件将扩展为包含 length 个字节。
如果 length 为 0，则映射的最大长度为当前文件大小。如果文件为空， Windows 会引发异常（你无法在Windows上创建空映射）。
如果 tagname 被指定且不是 None ，则是为映射提供标签名称的字符串。 Windows 允许你对同一文件拥有许多不同的映射。如果指定现有标签的名称，则会打开该标签，否则将创建该名称的新标签。
如果省略此参数或设置为 None ，则创建的映射不带名称。避免使用 tag 参数将有助于使代码在Unix和Windows之间可移植。
offset 可以被指定为非负整数偏移量。 mmap 引用将相对于从文件开头的偏移。 offset 默认为0。 offeset 必须是 ALLOCATIONGRANULARITY 的倍数。
引发一个 审计事件 mmap.__new__ 附带参数 fileno, length, access, offset。

class mmap.mmap(fileno, length, flags=MAP_SHARED, prot=PROT_WRITE|PROT_READ, access=ACCESS_DEFAULT[, offset])
(Unix 版本) 映射文件描述符 fileno 指定的文件的 length 个字节，并返回一个 mmap 对象。如果 length 为 0 ，则当调用 mmap 时，映射的最大长度将为文件的当前大小。
"""
import mmap

with mmap.mmap(-1, 13) as mm:
    mm.write(b"Hello world!")

import mmap

# write a simple example file
with open("104_ipc_mmap.txt", "wb") as f:
    f.write(b"Hello Python!\n")

with open("104_ipc_mmap.txt", "r+b") as f:
    print(f.fileno())  # 文件句柄 fileno ,直接分配内存用-1
    # memory-map the file, size 0 means whole file
    mm = mmap.mmap(f.fileno(), 0)
    # read content via standard file methods
    print(mm.readline())  # prints b"Hello Python!\n"
    # read content via slice notation
    print(mm[:5])  # prints b"Hello"
    # update content using slice notation;
    # note that new content must have same size
    mm[6:] = b" world!\n"
    # ... and read again using standard file methods
    mm.seek(0)
    print(mm.readline())  # prints b"Hello  world!\n"
    # close the map
    mm.close()
