# -*- coding:utf-8 -*-

import zipfile


def addzip():
    f = zipfile.ZipFile('F:/libzip/test.zip', 'w', zipfile.ZIP_DEFLATED)
    for i in ["F:/libzip/1.txt", "F:/libzip/2.txt", "F:/libzip/3/4.txt"]:
        # file = i.split('/')[-1]
        # f.write(i, file)  # 这个file是文件名，意思是直接把文件添加到zip没有文件夹层级， f.write(i)这种写法，则会出现上面路径的层级
        f.write(i)
    f.close()


def unzip():
    zf = zipfile.ZipFile('F:/libzip/test.zip')
    zf.extractall(path="F:/libzip/unzip")  # , pwd=""
    zf.close()
#
# if __name__ == '__main__':
#     addzip()
addzip()
unzip()