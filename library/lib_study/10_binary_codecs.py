# 编解码器注册和相关基类
import codecs

# 编码转换时，通常需要以unicode作为中间编码，即先将其他编码的字符串解码（decode）成unicode，再从unicode编码（encode）成另一种编码。
# Unicode 是「字符集」 U+ 0000 ~ U+10FFFF
# UTF-8 是「编码规则」
# str 这个类是用来存储Unicode字符串的，而 bytes 和 bytearray 这两个类是用来存储二进制数据的。

# Unicode 字符集为每一个字符分配一个码位，例如「知」的码位是 30693，记作 U+77E5（30693 的十六进制为 0x77E5）。
# UTF-8 顾名思义，是一套以 8 位为一个编码单位的可变长编码。会将一个码位编码为 1 到 4 个字节：
#U+ 0000 ~ U+  007F: 0XXXXXXX
#U+ 0080 ~ U+  07FF: 110XXXXX 10XXXXXX
#U+ 0800 ~ U+  FFFF: 1110XXXX 10XXXXXX 10XXXXXX
#U+10000 ~ U+10FFFF: 11110XXX 10XXXXXX 10XXXXXX 10XXXXXX
# 根据上表中的编码规则，之前的「知」字的码位 U+77E5 属于第三行的范围：
"""
       7    7    E    5    
    0111 0111 1110 0101    二进制的 77E5
--------------------------
    0111   011111   100101 二进制的 77E5
1110XXXX 10XXXXXX 10XXXXXX 模版（上表第三行）
11100111 10011111 10100101 代入模版
   E   7    9   F    A   5
"""
# 这就是将 U+77E5 按照 UTF-8 编码为字节序列 E79FA5 的过程。反之亦然。
# print(codecs.encode("知", encoding='utf-8')) # b'\xe7\x9f\xa5'

import sys
print(sys.getdefaultencoding())
print(sys.getfilesystemencoding())

# 编码 https://docs.python.org/zh-cn/3/library/codecs.html#standard-encodings 查看有哪些编码
print(codecs.encode("你好一", encoding='utf-8'))
print(codecs.encode("你好一", encoding='utf-16'))
# print(codecs.encode("你好一", encoding='ascii')) # 出错
print(codecs.encode("abc", encoding='ascii'))
print(codecs.encode("abc/."))
print(codecs.encode("你好一", encoding='ANSI')) # ANSI在不同语言中有不同的具体标准，在简体中文系统下，ANSI 编码代表 GB2312 编码，在日文操作系统下，ANSI 编码代表 JIS 编码。
print(codecs.encode("你好一", encoding='GB2312'))
print(codecs.encode("你好一", encoding='BIG5'))
print(codecs.encode("你好一", encoding='GBK')) # GBK 是 GB2312的扩展 ,除了兼容GB2312外，它还能显示繁体中文，还有日文的假名。
print(codecs.encode("にほんご", encoding='GB2312'))

print(len("中"))
print("你好".encode('gb2312') )   # 将gb2312编码的字符串转换成unicode编码
print(b'\xc4\xe3\xba\xc3\xd2\xbb'.decode('gb2312') )   # 将unicode编码的字符串转换成gb2312编码



print(codecs.lookup("GB2312"))

# codecs.CodecInfo(encode, decode, streamreader=None, streamwriter=None, incrementalencoder=None, incrementaldecoder=None, name=None)

codescInfo0 = codecs.CodecInfo(codecs.getencoder("GB2312"),codecs.getdecoder("utf-8"))
print(codescInfo0.encode("你好"))
print(codescInfo0.decode(b'\xe4\xbd\xa0\xe5\xa5\xbd\xe4\xb8\x80'))


codescInfo = codecs.lookup("GB2312")
print(codescInfo.encode("你好"))


print(codecs.getencoder("GB2312"))

print(codecs.lookup_error('strict')) # 'ignore' 'replace'

# class codecs.Codec

cc = codecs.Codec()


