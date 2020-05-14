#!/usr/bin/env python
# -*- coding: utf-8 -*-
# http://www.zlib.net/
# https://www.cnblogs.com/ygbh/p/12082799.html
import zlib
import binascii

original_data = b'This is the original text.'
print('源始数据:长度 : {},内容 : {}'.format(len(original_data), original_data))

#压缩数据
compressed_data = zlib.compress(original_data)
print('压缩的数据:长度 : {},内容 : {}'.format(len(compressed_data), binascii.hexlify(compressed_data))) #binascii.hexlify主要作用是将字节类转为16进制显示

#解压数据
decompress_data = zlib.decompress(compressed_data)
print('压缩的数据:长度 : {},内容 : {}'.format(len(decompress_data), decompress_data))


template = '{:>15}  {:>15}'
print(template.format('原始长度', '压缩长度'))
print(template.format('-' * 25, '-' * 25))

for i in range(5):
    data = original_data * i #数据倍增
    compressed = zlib.compress(data) #压缩数据
    highlight = '*' if len(data) < len(compressed) else '' #三目运算法，如果原始数据长度小于压缩的长度就显示*
    print(template.format(len(data), len(compressed)), highlight)


# zlib增量压缩与解压
compressor = zlib.compressobj(1)
with open('50_archiving_zlib.py', 'rb') as input:
    while True:
        block = input.read(64)  # 每次读取64个字节
        if not block:
            break
        compressed = compressor.compress(block)
        if compressed:
            print('压缩数据: {}'.format(
                binascii.hexlify(compressed)))
        else:
            print('数据缓存中...')
    remaining = compressor.flush()  # 刷新返回压缩的数据
    print('Flushed: {}'.format(binascii.hexlify(remaining)))

#一次性解压数据，需要注意的是增量压缩，默认会把zlib压缩的头部信息去除，所以解压时需要带上789c
zlib_head = binascii.unhexlify('789c')
decompress_data = zlib.decompress(zlib_head + remaining)
print(decompress_data)