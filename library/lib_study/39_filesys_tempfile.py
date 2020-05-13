# 该模块用于创建临时文件和目录，它可以跨平台使用。
# TemporaryFile、NamedTemporaryFile、TemporaryDirectory 和 SpooledTemporaryFile 是带有自动清理功能的高级接口，
# 可用作上下文管理器。mkstemp() 和 mkdtemp() 是低级函数，使用完毕需手动清理。
# https://docs.python.org/zh-cn/3/library/tempfile.html
import tempfile

fp = tempfile.TemporaryFile()
fp.write(b'Hello world!')

fp.seek(0)
print(fp.read())
fp.close()

with tempfile.TemporaryFile() as fp:
    fp.write(b'Hello world!')
    fp.seek(0)
    print(fp.read())


with tempfile.TemporaryDirectory() as tmpdirname:
    print('created temporary directory', tmpdirname)