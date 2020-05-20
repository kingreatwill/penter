"""
posix --- 最常见的 POSIX 系统调用  请勿直接导入此模块 而应导入 os 模块
pwd --- 用户密码数据库
spwd --- 针对影子密码数据库的接口，与pwd类似。
grp --- 针对用户组数据库的接口，与pwd类似。
crypt --- 函数可检查Unix密码
termios --- POSIX 风格的 tty 控制
tty --- 终端控制功能
pty --- 伪终端工具
fcntl --- The fcntl and ioctl system calls
pipes --- 终端管道接口
resource --- Resource usage information
nis --- Sun 的 NIS (黄页) 接口
"""


"""
1> tty(终端设备的统称):
       tty一词源于Teletypes，或teletypewriters，原来指的是电传打字机，是通过串行线用打印机键盘通过阅读和发送信息的东西，后来这东西被键盘和显示器取代，所以现在叫终端比较合适。
       终端是一种字符型设备，他有多种类型，通常使用tty来简称各种类型的终端设备。
2> pty（虚拟终端):
       但是假如我们远程telnet到主机或使用xterm时不也需要一个终端交互么？是的，这就是虚拟终端pty(pseudo-tty)
3> pts/ptmx(pts/ptmx结合使用，进而实现pty:
       pts(pseudo-terminal slave)是pty的实现方法，和ptmx(pseudo-terminal master)配合使用实现pty。
"""
import posix

print(posix.environ)

import pwd

print(pwd.getpwuid(0))
print(pwd.getpwnam("root"))
"""
0   pw_name 登录名
1   pw_passwd   密码，可能已经加密
2   pw_uid  用户 ID 数值
3   pw_gid  组 ID 数值
4   pw_gecos    用户名或备注
5   pw_dir  用户主目录
6   pw_shell    用户的命令解释器
"""
print(pwd.getpwall())

import spwd

print(spwd.getspall())
print(spwd.getspnam("root"))

import grp

print(grp.getgrall())
print(grp.getgrnam("root"))
print(grp.getgrgid(1))