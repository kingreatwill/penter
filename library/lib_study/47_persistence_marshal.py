#  marshal 模块主要是为了支持读写 .pyc 文件形式“伪编译”代码的 Python 模块。
#  因此，Python 维护者保留在必要时以不向下兼容的方式修改 marshal 格式的权利。
#  如果你要序列化和反序列化 Python 对象，请改用 pickle 模块 -- 其执行效率相当，版本独立性有保证，并且 pickle 还支持比 marshal 更多样的对象类型。
# https://docs.python.org/zh-cn/3/library/marshal.html

# 不介绍超级简单.