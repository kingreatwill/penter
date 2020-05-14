import xdrlib

# 编码与解码 XDR数据

p = xdrlib.Packer()
try:
    p.pack_double(8.01) # 将数据打包为 XDR 表示形式
except xdrlib.ConversionError as instance:
    print('packing the double failed:', instance.msg)

data = p.get_buffer()
up = xdrlib.Unpacker(data)

print(up.unpack_double())