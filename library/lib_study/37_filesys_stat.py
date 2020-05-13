import os
import stat

# https://docs.python.org/zh-cn/3/library/stat.html
#  os.stat(), os.fstat() 和 os.lstat()
# # 打开文件
# fd = os.open( "foo.txt", os.O_RDWR|os.O_CREAT )
# # 获取元组
# info = os.fstat(fd)

mode_dir = os.stat("./").st_mode
mode_file = os.stat("37_filesys_stat.py").st_mode
print(mode_dir, mode_file)
print(stat.S_ISDIR(mode_dir))
print(stat.S_ISDIR(mode_file))
print(stat.filemode(mode_dir))
print(stat.filemode(mode_file))
