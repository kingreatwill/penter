import os
import tarfile
# https://docs.python.org/zh-cn/3/library/tarfile.html

# tar = tarfile.open("sample.tar.gz")
# tar.extractall()
# tar.close()

# 压缩
tar = tarfile.open('your.tar', 'w')  # 创建一个压缩包
tar.add('/Users/wupeiqi/PycharmProjects/bbs2.log', arcname='bbs2.log')  # 将文件添加到压缩包并命名
tar.add('/Users/wupeiqi/PycharmProjects/cmdb.log', arcname='cmdb.log')  #
tar.close()  # 关闭压缩包

# 解压
tar = tarfile.open('your.tar', 'r')  # 打开一个压缩包
tar.extractall()  # 解压包内所有文件（可设置解压地址）
tar.close()  # 关闭压缩包

# 压缩某个目录下所有文件
def compress_file(tarfilename, dirname):    # tarfilename是压缩包名字，dirname是要打包的目录
    if os.path.isfile(dirname):
        with tarfile.open(tarfilename, 'w') as tar:
            tar.add(dirname)
    else:
        with tarfile.open(tarfilename, 'w') as tar:
            for root, dirs, files in os.walk(dirname):
                for single_file in files:
                    # if single_file != tarfilename:
                    filepath = os.path.join(root, single_file)
                    tar.add(filepath)

compress_file('test.tar', 'test.txt')
compress_file('t.tar', '.')


def addfile(tarfilename, dirname):    # tarfilename是压缩包名字，dirname是要打包的目录
    if os.path.isfile(dirname):
        with tarfile.open(tarfilename, 'a') as tar:
            tar.add(dirname)
    else:
        with tarfile.open(tarfilename, 'a') as tar:
            for root, dirs, files in os.walk(dirname):
                for single_file in files:
                    # if single_file != tarfilename:
                    filepath = os.path.join(root, single_file)
                    tar.add(filepath)

# 添加文件到已有的tar包中
addfile('t.tar', 'ttt.txt')
addfile('t.tar', 'ttt')