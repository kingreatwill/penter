"""
对 uuencode 文件进行编码与解码 https://docs.python.org/zh-cn/3/library/uu.html


uu.encode(in_file, out_file, name=None, mode=None, *, backtick=False)
使用 uuencode 将 in_file 文件编码为 out_file 文件。 经过 uuencoded 编码的文件将具有指定 name 和 mode 作为解码该文件默认结果的标头。 默认值会相应地从 in_file 或 '-' 以及 0o666 中提取。 如果 backtick 为真值，零会用 '`' 而不是空格来表示。

在 3.7 版更改: 增加 backtick 参数

uu.decode(in_file, out_file=None, mode=None, quiet=False)
调用此函数会解码 uuencod 编码的 in_file 文件并将结果放入 out_file 文件。 如果 out_file 是一个路径名称，mode 会在必须创建文件时用于设置权限位。 out_file 和 mode 的默认值会从 uuencode 标头中提取。 但是，如果标头中指定的文件已存在，则会引发 uu.Error。

如果输入由不正确的 uuencode 编码器生成，decode() 可能会打印一条警告到标准错误 ，这样 Python 可以从该错误中恢复。 将 quiet 设为真值可以屏蔽此警告。
"""