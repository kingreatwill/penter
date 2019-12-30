import zlib
# zlib支持通用的数据打包和压缩格式：zlib，gzip，bz2，zipfile，以及 tarfile。


s = b'witch which has which witches wrist watch'
print(len(s))

t = zlib.compress(s)

print(len(t))

print(zlib.decompress(t))

print(zlib.crc32(s))