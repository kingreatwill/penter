import os
import sys

print("----------------------")
print(os.name)  # 以下名称目前已注册: 'posix', 'nt', 'java'
#print(os.uname()) # 可用性: 较新的 Unix 版本。
print(sys.platform)
print("----------------------进程参数")
# print(os.ctermid()) # 可用性: Unix。
"""
os.getegid()
返回当前进程的有效组ID。对应当前进程执行文件的 "set id" 位。
可用性: Unix。

os.geteuid()
返回当前进程的有效用户ID。
可用性: Unix。

os.getgid()
返回当前进程的实际组ID。
可用性: Unix。

os.getgrouplist(user, group)
返回该用户所在的组 ID 列表。可能 group 参数没有在返回的列表中，实际上用户应该也是属于该 group。
group 参数一般可以从储存账户信息的密码记录文件中找到。
可用性: Unix。

os.getgroups()¶
返回当前进程对应的组ID列表
可用性: Unix。

os.getpgid(pid)
根据进程id pid 返回进程的组 ID 列表。如果 pid 为 0，则返回当前进程的进程组 ID 列表
可用性: Unix。

os.getpgrp()
返回当时进程组的ID
可用性: Unix。

os.getpriority(which, who)
获取程序调度优先级。which 参数值可以是 PRIO_PROCESS，PRIO_PGRP，或 PRIO_USER 中的一个，
who 是相对于 which (PRIO_PROCESS 的进程标识符，PRIO_PGRP 的进程组标识符和 PRIO_USER 的用户ID)。
当 who 为 0 时（分别）表示调用的进程，调用进程的进程组或调用进程所属的真实用户 ID。
可用性: Unix。

os.PRIO_PROCESS
os.PRIO_PGRP
os.PRIO_USER
函数 getpriority() 和 setpriority() 的参数。
可用性: Unix。

os.getresuid()
返回一个由 (ruid, euid, suid) 所组成的元组，分别表示当前进程的真实用户ID，有效用户ID和甲暂存用户ID。
可用性: Unix。


os.getresgid()
返回一个由 (rgid, egid, sgid) 所组成的元组，分别表示当前进程的真实组ID，有效组ID和暂存组ID。
可用性: Unix。


os.getuid()
返回当前进程的真实用户ID。
可用性: Unix。

os.initgroups(username, gid)
调用系统 initgroups()，使用指定用户所在的所有值来初始化组访问列表，包括指定的组ID。
可用性: Unix。

os.setegid(egid)
设置当前进程的有效组ID。
可用性: Unix。

os.seteuid(euid)
设置当前进程的有效用户ID。
可用性: Unix。

os.setgid(gid)
设置当前进程的组ID。
可用性: Unix。

os.setgroups(groups)¶
将 group 参数值设置为与当进程相关联的附加组ID列表。group 参数必须为一个序列，每个元素应为每个组的数字ID。该操作通常只适用于超级用户。
可用性: Unix。

os.setpgrp()
根据已实现的版本（如果有）来调用系统 setpgrp() 或 setpgrp(0, 0) 。相关说明，请参考 Unix 手册。
可用性: Unix。

os.setpgid(pid, pgrp)
使用系统调用 setpgid()，将 pid 对应进程的组ID设置为 pgrp。相关说明，请参考 Unix 手册。
可用性: Unix。

os.setpriority(which, who, priority)
设置程序调度优先级。 which 的值为 PRIO_PROCESS, PRIO_PGRP 或 PRIO_USER 之一，而 who 会相对于 which (PRIO_PROCESS 的进程标识符, 
PRIO_PGRP 的进程组标识符和 PRIO_USER 的用户 ID) 被解析。 who 值为零 (分别) 表示调用进程，调用进程的进程组或调用进程的真实用户 ID。 
priority 是范围在 -20 至 19 的值。 默认优先级为 0；较小的优先级数值会更优先被调度。
可用性: Unix。

os.setregid(rgid, egid)
设置当前进程的真实和有效组ID。
可用性: Unix。

os.setresgid(rgid, egid, sgid)
设置当前进程的真实，有效和暂存组ID。
可用性: Unix。

os.setresuid(ruid, euid, suid)
设置当前进程的真实，有效和暂存用户ID。
可用性: Unix。


os.setreuid(ruid, euid)
设置当前进程的真实和有效用户ID。
可用性: Unix。

os.getsid(pid)
调用系统调用 getsid()。相关说明，请参考 Unix 手册。
可用性: Unix。

os.setsid()
使用系统调用 getsid()。相关说明，请参考 Unix 手册。
可用性: Unix。

os.setuid(uid)
设置当前进程的用户ID。
可用性: Unix。
"""
print(os.environ)
print(os.getcwd())
# 改变当前工作目录到指定的路径。
# os.chdir("D:/")
# print(os.getcwd())
# fchdir通过文件描述符改变当前工作目录。
# 打开新目录 "/tmp"
# fd = os.open( "/tmp", os.O_RDONLY )
# # 使用 os.fchdir() 方法修改到新目录
# os.fchdir(fd)
# os.close( fd )


import pathlib

print(os.fsencode("D:/sfdsf/123.g"))
print(os.fsdecode(os.fsencode("D:/sfdsf/123.g")))
print(os.fspath(pathlib.Path("D:/sfdsf/123.g")))

print(os.getenv("PaTh"))
print(os.get_exec_path())
print(os.getlogin())
print(os.getpid())
print(os.getppid())


# print(os.putenv("key", "value"))
# print(os.getenv("key"))
print("------------文件")
# fd = os.open( "foo.txt", os.O_RDWR|os.O_CREAT )
# print(os.fstat(fd))
# os.close(fd)
print (os.getcwd())#获得当前目录
print (os.path.abspath('.'))#获得当前工作目录
print (os.path.abspath('..'))#获得当前工作目录的父目录
print (os.path.abspath(os.curdir))#获得当前工作目录
print(sys.argv[0])#当前脚本的位置
print(pathlib.Path().absolute())

print("---------")

for root, dirs, files in os.walk(os.getcwd()):
    print(root)
    print(dirs)
    for single_file in files:
        print(single_file)

print("------------")
print(os.times())
#os.execl("/usr/bin/python ", "python ", 'test.py ', 'i ')
