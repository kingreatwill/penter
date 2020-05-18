
"""
ftp.cwd(path)                           设置FTP当前操作的路径，同linux中的cd
ftp.dir()                               显示目录下所有信息
ftp.nlst()                              获取目录下的文件，显示的是文件名列表
ftp.mkd(directory)                      新建远程目录
ftp.rmd(directory)                          删除远程目录
ftp.rename(old, new)                        将远程文件old重命名为new
ftp.delete(file_name)                       删除远程文件
ftp.storbinary(cmd, fp, bufsize)             上传文件，cmd是一个存储命令，可以为"STOR filename.txt"， fp为类文件对象（有read方法），bufsize设置缓冲大小
ftp.retrbinary(cmd, callback, bufsize)        下载文件，cmd是一个获取命令，可以为"RETR filename.txt"， callback是一个回调函数，用于读取获取到的数据块

"""
from ftplib import FTP
ftp = FTP('ftp.debian.org')     # connect to host, default port
print(ftp.login()   )                  # user anonymous, passwd anonymous@

ftp.cwd('debian')               # change into "debian" directory
print(ftp.retrlines('LIST') )          # list directory contents

# with open('README', 'wb') as fp:
#     ftp.retrbinary('RETR README', fp.write)

ftp.quit()

from ftplib import FTP
with FTP("ftp1.at.proftpd.org") as ftp:
    ftp.login()
    ftp.dir()

print("--------------")
# coding:utf8
from ftplib import FTP


def upload(f, remote_path, local_path):
    fp = open(local_path, "rb")
    buf_size = 1024
    f.storbinary("STOR {}".format(remote_path), fp, buf_size)
    fp.close()


def download(f, remote_path, local_path):
    fp = open(local_path, "wb")
    buf_size = 1024
    f.retrbinary('RETR {}'.format(remote_path), fp.write, buf_size)
    fp.close()


if __name__ == "__main__":
    ftp = FTP()
    ftp.connect("x.x.x.x", 21)      # 第一个参数可以是ftp服务器的ip或者域名，第二个参数为ftp服务器的连接端口，默认为21
    ftp.login("username", "password")     # 匿名登录直接使用ftp.login()
    ftp.cwd("tmp")                # 切换到tmp目录
    upload(ftp, "ftp_a.txt", "a.txt")   # 将当前目录下的a.txt文件上传到ftp服务器的tmp目录，命名为ftp_a.txt
    download(ftp, "ftp_a.txt", "b.txt")  # 将ftp服务器tmp目录下的ftp_a.txt文件下载到当前目录，命名为b.txt
    ftp.quit()