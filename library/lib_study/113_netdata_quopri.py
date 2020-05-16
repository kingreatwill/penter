"""
quopri.decode(input, output, header=False)
解码 input 文件的内容并将已解码二进制数据结果写入 output 文件。 input 和 output 必须为 二进制文件对象。 如果提供了可选参数 header 且为真值，下划线将被解码为空格。 此函数可用于解码“Q”编码的头数据，具体描述见 RFC 1522: "MIME (Multipurpose Internet Mail Extensions) Part Two: Message Header Extensions for Non-ASCII Text"。

quopri.encode(input, output, quotetabs, header=False)
编码 input 文件的内容并将转换后可打印的数据结果写入 output 文件。 input 和 output 必须为 二进制文件对象. quotetabs 是一个非可选的旗标，它控制是否要编码内嵌的空格与制表符；当为真值时将编码此类内嵌空白符，当为假值时则保持原样不进行编码。 请注意出现在行尾的空格与制表符总是会被编码，具体描述见 RFC 1521。 header 旗标控制空格符是否要编码为下划线，具体描述见 RFC 1522。

quopri.decodestring(s, header=False)
类似 decode()，区别在于它接受一个源 bytes 并返回对应的已解码 bytes。

quopri.encodestring(s, quotetabs=False, header=False)
类型 encode()，区别在于它接受一个源 bytes 并返回对应的已编码 bytes。 在默认情况下，它会发送 False 值给 encode() 函数的 quotetabs 形参。
"""
import quopri

s = quopri.encodestring(b"sdfdsf")
print(s)
d = quopri.decodestring(s)
print(d)