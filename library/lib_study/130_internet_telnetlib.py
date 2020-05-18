"""
Telnet协议是TCP/IP协议族中的一员，是Internet远程登录服务的标准协议和主要方式。
它为用户提供了在本地计算机上完成远程主机工作的能力。
在终端使用者的电脑上使用telnet程序，用它连接到服务器。终端使用者可以在telnet程序中输入命令，这些命令会在服务器上运行，就像直接在服务器的控制台上输入一样。
可以在本地就能控制服务器。要开始一个telnet会话，必须输入用户名和密码来登录服务器。Telnet是常用的远程控制Web服务器的方法。
"""

"""
一、linux服务端：
安装软件：
yum  -y  install  telnet-server  xinetd

创建用户：（默认只能是普通用户登录）如需开启root用户登录，请参考下面的方法：vi /etc/pam.d/login   #auth requiredpam_securetty.so将这一行加上注释。
useradd  telu
passwd  telu

启动服务：
systemctl  start  xinetd
systemctl  enable xinetd
systemctl  start  telnet.socket
systemctl  enable telnet.socket

测试：
netstat  -nutlp  |  grep  23

二、windows服务器开启telnet服务
"""

# from telnetlib import Telnet
# with Telnet('192.168.110.216', 23) as tn:
#     tn.interact()

import getpass
import telnetlib

HOST = '192.168.110.216'
user = "telu"  # input("Enter your remote account: ")
password = "123456"  # "getpass.getpass()"

tn = telnetlib.Telnet(HOST)

tn.read_until(b"login: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"cd /\n")
tn.write(b"ls\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))
