#sndhdr --- 推测声音文件的类型  https://docs.python.org/zh-cn/3/library/sndhdr.html#module-sndhdr
import sndhdr

print(sndhdr.what("E:/linux/emacs-26.3-x86_64/lib/python2.7/test/audiodata/pluck-pcm8.wav"))

print(sndhdr.whathdr("E:/linux/emacs-26.3-x86_64/lib/python2.7/test/audiodata/pluck-pcm8.wav"))