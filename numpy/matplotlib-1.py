# 中文乱码
import matplotlib
# 查看matplotlib的字体存放目录与查找matplotlibrc文件路径
print( matplotlib.matplotlib_fname())

"""
# https://www.jianshu.com/p/8ed59ac76c06

下载字体 https://www.fontpalace.com/font-download/SimHei/

字体目录就在与matplotlibrc文件同级的font/ttf目录中。也就是 .../matplotlib/mpl-data/fonts/ttf中
，请将下载好的字体，放入这个文件夹

命令行运行如下两个命令，将matplotlib的字体缓存删除
cd ~/.matplotlib/
rm -rf fontList.py3k.cach


修改 matplotlibrc文件设置
找到下面呆着#注释的两行：
#font.family
#font.sans-serif

先将这两行前面的#去掉。再在第二行font.sans-serif的等号后面添加一项：SimHei。

在你的业务代码配置下载字体
plt.rcParams['font.sans-serif'] = ['SimHei'] # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False # 用来正常显示负号

import matplotlib.pyplot as plt
# 支持中文
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


# https://www.cnblogs.com/boydfd/p/11218120.html

"""