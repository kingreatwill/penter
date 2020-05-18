import chunk
# chunk 分块；Read IFF chunked data
#  Audio Interchange File Format (AIFF/AIFF-C) and the Real Media File Format (RMFF)
# 也可以读取wave文件？
with open("E:/linux/emacs-26.3-x86_64/lib/python2.7/test/audiodata/pluck-pcm8.wav","rb") as f:
    c = chunk.Chunk(f)
    print(c.getname())