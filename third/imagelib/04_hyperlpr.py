# python3 -m pip install hyperlpr -i  http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
# 安装低版本 pip3 install opencv-python==3.4.9.31 -i  http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
# https://github.com/zeusees/HyperLPR
#查看缺少得共享库 yum whatprovides libSM.so.6
# yum whatprovides libXext.so.6
# yum install libSM-1.2.2-2.el7.x86_64 --setopt=protected_multilib=false   （or yum install libSM.x86_64）

# libXrender.so.1  -》 yum install libXrender-devel.x86_64
# libXext.so.6 -》 yum install libXext.x86_64

# https://github.com/zeusees/HyperLPR/issues/241

#导入包
from hyperlpr import *
#导入OpenCV库
import cv2
#读入图片
image = cv2.imread("car-id.jpg")
#识别结果
print(HyperLPR_plate_recognition(image))
