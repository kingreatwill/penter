# _*_ coding:utf-8 _*_
import fileinput

# 默认控制台输入
# for line in fileinput.input():
#     print(line)
# UnicodeDecodeError: 'gbk' codec can't decode byte 0xae in position 50: illegal multibyte sequence
# openhook=fileinput.hook_encoded('utf-8')
with fileinput.input(files=('36_filesys_fileinput.py', '35_filesys_os.path.py'),
                     openhook=fileinput.hook_encoded('utf-8')) as f:
    for line in f:
        print(fileinput.filename())
        print(str(fileinput.lineno()) + ":"+line)
