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

"""
如果出现：AttributeError: module 'cv2.cv2' has no attribute 'estimateRigidTransform'
解决方案：
方案一：安装低版本opencv     pip install opencv-python==3.4.9.31
方案二：替换estimateRigidTransform方法
方案二的第一种方法 https://github.com/zeusees/HyperLPR/issues/233
mat_, inliers = cv2.estimateAffine2D(org_pts, target_pts) 代替 mat_ = cv2.estimateRigidTransform(org_pts, target_pts, True)
需要注意的是 estimateAffine2D方法要返回两个值，虽然第二个返回值inliers可能没用，但一定要加上。
如果在estimateRigidTransform的方法中第三个参数fullfine为flase的话，可能需要使用estimateAffinePartial2D方法代替。

方案二的第二种方法  https://github.com/zeusees/HyperLPR/issues/222
estimateAffinePartial2D返回一个元组然后第0位对应的原来estimateRigidTransform的返回值
https://docs.opencv.org/master/d9/d0c/group__calib3d.html#gad767faff73e9cbd8b9d92b955b50062d
231应该改成
mat_ = cv2.estimateAffinePartial2D(org_pts, target_pts, True)[0]

以上两个方法的区别：
根据表述我们可以使用estimateAffine2D和estimateAffinePartial2D两个方法代替使用，但是到底应该选择哪一个方法进行替代，
还需要看estimateRigidTransform方法的第三个参数fullAffine的取值。

fullAffine为true表示的是六自由度的仿射变换，对应的方法为estimateAffine2D
fullAffine为false表示的是四自由度的仿射变换，对应的方法为estimateAffinePartial2D
以上两个方法的具体使用参考文档：opencv
https://docs.opencv.org/4.0.0/dc/d6b/group__video__track.html#ga762cbe5efd52cf078950196f3c616d48

注意： 使用estimateAffine2D和estimateAffinePartial2D方法需要两个返回值，第一个返回值对应的是方法estimateRigidTransform的返回值，第二个返回值表示的是内点inliers，它的具体作用尚未得知。
"""