import struct

# 格式符”i”表示转换为int占4位   h表示short占2位  b表示 signed char占1位  !网络=大端   > 大端   < 小端  如果第一个字符（@，=<，>!）不是其中之一，则假定为 '@'
# 下面的意思1占4位  2占2位  3占1位
buffer = struct.pack("ihb", 1, 2, 3)
print(repr(buffer))


print(struct.unpack("ihb", buffer))
# data from a sequence, network byteorder
data = [1, 2, 3]
buffer = struct.pack("!ihb", *data)
print(repr(struct.pack(">ihb", *data)))
print(repr(buffer))

print(repr(struct.pack("=ihb", *data)))
print(repr(struct.pack("@ihb", *data)))

print(struct.unpack("!ihb", buffer))

print(struct.calcsize('hhl'))
print(struct.calcsize('ihb'))
