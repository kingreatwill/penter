import os
import sqlite3

# https://docs.python.org/zh-cn/3/library/sqlite3.html
os.remove('example.db')
conn = sqlite3.connect('example.db')
# 你也可以使用 :memory: 来创建一个内存中的数据库
# conn = sqlite3.connect(':memory:')
# 当有了 Connection 对象后，你可以创建一个 Cursor 游标对象，然后调用它的 execute() 方法来执行 SQL 语句：
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE stocks
             (date text, trans text, symbol text, qty real, price real)''')

# Insert a row of data
c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
c.close()

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()

conn = sqlite3.connect('example.db')
cursor = conn.cursor()
# 永远不要这样写！！！
# symbol = 'RHAT'
# cursor.execute("SELECT * FROM stocks WHERE symbol = '%s'" % symbol)
# 这样写才好！！！t = ('RHAT',)
cursor.execute('SELECT * FROM stocks WHERE symbol=?', ('RHAT',))
result = cursor.fetchone()
print(result)

purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
             ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
             ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
             ]
cursor.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)
for row in cursor.execute('SELECT * FROM stocks ORDER BY price'):
    print(row)
cursor.execute('SELECT * FROM stocks ORDER BY price')

print(cursor.fetchall())

cursor.close()
conn.commit()  # 不加commit cursor.executemany 数据不会保存;
# 这个方法提交当前事务。如果没有调用这个方法，那么从上一次提交 commit() 以来所有的变化在其他数据库连接上都是不可见的。
# 如果你往数据库里写了数据，但是又查询不到，请检查是否忘记了调用这个方法。
conn.close()

print("----------------模块函数和常量")
print(sqlite3.version)
print(sqlite3.version_info)  # 模块的版本号，是一个由整数组成的元组。不是 SQLite 库的版本号。
print(sqlite3.sqlite_version)
print(sqlite3.sqlite_version_info)
print(sqlite3.PARSE_DECLTYPES)
print(sqlite3.PARSE_COLNAMES)

print("----------------")
# SQLite 原生只支持5种类型：TEXT，INTEGER，REAL，BLOB 和 NULL。
# 如果你想用其它类型，你必须自己添加相应的支持。使用 detect_types 参数和模块级别的 register_converter() 函数注册**转换器** 可以简单的实现。
# 如果 uri 为真，则 database 被解释为 URI。 它允许您指定选项。 例如，以只读模式打开数据库：
# db = sqlite3.connect('file:path/to/database?mode=ro', uri=True)
# https://www.sqlite.org/uri.html
"""
sqlite3.register_converter(typename, callable)
注册一个回调对象 callable, 用来转换数据库中的字节串为自定的 Python 类型。所有类型为 typename 的数据库的值在转换时，都会调用这个回调对象。
通过指定 connect() 函数的 detect-types 参数来设置类型检测的方式。注意，typename 与查询语句中的类型名进行匹配时不区分大小写。

sqlite3.register_adapter(type, callable)
注册一个回调对象 callable，用来转换自定义Python类型为一个 SQLite 支持的类型。 
这个回调对象 callable 仅接受一个 Python 值作为参数，而且必须返回以下某个类型的值：int，float，str 或 bytes.

sqlite3.complete_statement(sql)
如果字符串 sql 包含一个或多个完整的 SQL 语句（以分号结束）则返回 True。
它不会验证 SQL 语法是否正确，仅会验证字符串字面上是否完整，以及是否以分号结束。

sqlite3.enable_callback_tracebacks(flag)
默认情况下，您不会获得任何用户定义函数中的回溯消息，比如聚合，转换器，授权器回调等。
如果要调试它们，可以设置 flag 参数为 True 并调用此函数。 之后，回调中的回溯信息将会输出到 sys.stderr。 再次使用 False 来禁用该功能。

构建一个 SQLite shell，下面是一个例子：
# A minimal SQLite shell for experiments

import sqlite3

con = sqlite3.connect(":memory:")
con.isolation_level = None
cur = con.cursor()

buffer = ""

print("Enter your SQL commands to execute in sqlite3.")
print("Enter a blank line to exit.")

while True:
    line = input()
    if line == "":
        break
    buffer += line
    if sqlite3.complete_statement(buffer):
        try:
            buffer = buffer.strip()
            cur.execute(buffer)

            if buffer.lstrip().upper().startswith("SELECT"):
                print(cur.fetchall())
        except sqlite3.Error as e:
            print("An error occurred:", e.args[0])
        buffer = ""

con.close()
"""

print(sqlite3.complete_statement("buffer"))  # False
print(sqlite3.complete_statement("buffer;"))  # True


# create_function 可以在sql中执行python函数
# https://docs.python.org/zh-cn/3/library/sqlite3.html#sqlite3.Connection.create_function

# create_aggregate 创建一个自定义的聚合函数。 可以在sql中执行python函数，区别于create_function
# https://docs.python.org/zh-cn/3/library/sqlite3.html#sqlite3.Connection.create_aggregate

# create_collation 使用 name 和 callable 创建排序规则。
# https://docs.python.org/zh-cn/3/library/sqlite3.html#sqlite3.Connection.create_collation



con = sqlite3.connect(":memory:")
con.row_factory = sqlite3.Row

cur = con.cursor()
cur.execute("select 'John' as name, 42 as age")
for row in cur:
    assert row[0] == row["name"]
    assert row["name"] == row["nAmE"]
    assert row[1] == row["age"]
    assert row[1] == row["AgE"]

con.close()