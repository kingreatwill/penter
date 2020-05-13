# _*_ coding:utf-8 _*_
# https://docs.python.org/zh-cn/3/library/pickle.html
import copyreg
import io
import os
import pickle

# 用处： 可以吧训练好的数据进行dump到file，其它机器直接load运行！！！
print("------------------常量")
# 整数，可用的最高 协议版本,3.8 是5
print(pickle.HIGHEST_PROTOCOL)

# 整数，用于 pickle 数据的默认 协议版本  3.8是4
print(pickle.DEFAULT_PROTOCOL)


class A:
    i = 99

    def print(self):
        print(A.i)


# pickle.dump(obj, file)
# 将对象 obj 封存以后的对象写入已打开的 file object file。它等同于 Pickler(file, protocol).dump(obj)。

A.i = 100
a = A()
a.print()  # 100

# 将 obj 封存以后的对象作为 bytes 类型直接返回，而不是将其写入到文件。
abys = pickle.dumps(a)
A.i = 101
pickle.loads(abys).print()  # 101

with open('xx.txt', 'wb+') as f:
    # f = os.open("xx.txt",os.O_RDWR|os.O_CREAT)
    pickle.dump(a, f)
    f.seek(0)
    pickle.load(f).print()

"""
下列类型可以被封存：
None、True 和 False
整数、浮点数、复数
str、byte、bytearray
只包含可封存对象的集合，包括 tuple、list、set 和 dict
定义在模块最外层的函数（使用 def 定义，lambda 函数则不可以）
定义在模块最外层的内置函数
定义在模块最外层的类
某些类实例，这些类的 __dict__ 属性值或 __getstate__() 函数的返回值可以被封存（详情参阅 封存类实例 这一段）。
"""
print("----------------")


# 处理有状态的对象
# 下面的示例展示了如何修改类在封存时的行为。其中 TextReader 类打开了一个文本文件，每次调用其 readline() 方法则返回行号和该行的字符。
# 在封存这个 TextReader 的实例时，除了 文件对象，其他属性都会被保存。 当解封实例时，需要重新打开文件，然后从上次的位置开始继续读取。
# 实现这些功能需要实现 __setstate__() 和 __getstate__() 方法。
class TextReader:
    """Print and number lines in a text file."""

    def __init__(self, filename):
        self.filename = filename
        self.file = open(filename, encoding="utf-8")
        self.lineno = 0

    def readline(self):
        self.lineno += 1
        line = self.file.readline()
        if not line:
            return None
        if line.endswith('\n'):
            line = line[:-1]
        return "%i: %s" % (self.lineno, line)

    def __getstate__(self):
        # Copy the object's state from self.__dict__ which contains
        # all our instance attributes. Always use the dict.copy()
        # method to avoid modifying the original state.
        state = self.__dict__.copy()
        # Remove the unpicklable entries.
        del state['file']
        return state

    def __setstate__(self, state):
        # Restore instance attributes (i.e., filename and lineno).
        self.__dict__.update(state)
        # Restore the previously opened file's state. To do so, we need to
        # reopen it and read from it until the line count is restored.
        file = open(self.filename, encoding="utf-8")
        for _ in range(self.lineno):
            file.readline()
        # Finally, save the file.
        self.file = file


reader = TextReader("44_persistence_pickle.py")
print(reader.readline())
print(reader.readline())
new_reader = pickle.loads(pickle.dumps(reader))
print(new_reader.readline())

print("=----------------")
# Simple example presenting how persistent ID can be used to pickle
# external objects by reference.

import pickle
import sqlite3
from collections import namedtuple

# Simple class representing a record in our database.
MemoRecord = namedtuple("MemoRecord", "key, task")


class DBPickler(pickle.Pickler):

    def persistent_id(self, obj):
        # Instead of pickling MemoRecord as a regular class instance, we emit a
        # persistent ID.
        if isinstance(obj, MemoRecord):
            # Here, our persistent ID is simply a tuple, containing a tag and a
            # key, which refers to a specific record in the database.
            return ("MemoRecord", obj.key)
        else:
            # If obj does not have a persistent ID, return None. This means obj
            # needs to be pickled as usual.
            return None


class DBUnpickler(pickle.Unpickler):

    def __init__(self, file, connection):
        super().__init__(file)
        self.connection = connection

    def persistent_load(self, pid):
        # This method is invoked whenever a persistent ID is encountered.
        # Here, pid is the tuple returned by DBPickler.
        cursor = self.connection.cursor()
        type_tag, key_id = pid
        if type_tag == "MemoRecord":
            # Fetch the referenced record from the database and return it.
            cursor.execute("SELECT * FROM memos WHERE key=?", (str(key_id),))
            key, task = cursor.fetchone()
            return MemoRecord(key, task)
        else:
            # Always raises an error if you cannot return the correct object.
            # Otherwise, the unpickler will think None is the object referenced
            # by the persistent ID.
            raise pickle.UnpicklingError("unsupported persistent object")


def main():
    import io
    import pprint

    # Initialize and populate our database.
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE memos(key INTEGER PRIMARY KEY, task TEXT)")
    tasks = (
        'give food to fish',
        'prepare group meeting',
        'fight with a zebra',
    )
    for task in tasks:
        cursor.execute("INSERT INTO memos VALUES(NULL, ?)", (task,))

    # Fetch the records to be pickled.
    cursor.execute("SELECT * FROM memos")
    memos = [MemoRecord(key, task) for key, task in cursor]
    # Save the records using our custom DBPickler.
    file = io.BytesIO()
    DBPickler(file).dump(memos)

    print("Pickled records:")
    pprint.pprint(memos)

    # Update a record, just for good measure.
    cursor.execute("UPDATE memos SET task='learn italian' WHERE key=1")

    # Load the records from the pickle data stream.
    file.seek(0)
    memos = DBUnpickler(file, conn).load()

    print("Unpickled records:")
    pprint.pprint(memos)


if __name__ == '__main__':
    main()
