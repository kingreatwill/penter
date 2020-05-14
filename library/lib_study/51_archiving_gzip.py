import gzip

# 使用 GZIP 压缩已有的文件示例：
import shutil
with open('51_archiving_gzip.py', 'rb') as f_in:
    with gzip.open('51_archiving_gzip.py.gz', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

# 读取压缩文件示例：
with gzip.open('51_archiving_gzip.py.gz', 'rb') as f:
    file_content = f.read()
    print(file_content)

# 创建GZIP 文件示例：
content = b"Lots of content here"
with gzip.open('51_archiving_gzip.py.gz', 'wb') as f:
    f.write(content)


# 使用 GZIP 压缩二进制字符串示例：
s_in = b"Lots of content here"
s_out = gzip.compress(s_in)

