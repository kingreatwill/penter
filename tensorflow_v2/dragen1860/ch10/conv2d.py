import tensorflow as tf
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

img_path = "../../../imagelib/img/lena.jpg"  # 图片路径
img = Image.open(img_path).convert("L")  # 读取图片,并转换为灰度图片
img = np.array(img)  # 将<class 'PIL.JpegImagePlugin.JpegImageFile'>类转化为np数组
plt.imshow(img, cmap="gray")
plt.show()  # 显示图片
# 原img数组shape为(512,512)，为满足conv2d()函数输入参数input的格式，
# 扩展维度为(1, 512, 512, 1)，即（图片数，高，宽，通道数）
img = np.expand_dims(img, 0)
img = np.expand_dims(img, 3)
print(img.shape)  # shape(1, 512, 512, 1)
"""
# 边缘检测
[0, 1, 0], [1, -4, 1], [0, 1, 0]
        
# 水平边缘滤波器
[1, 2, 1], [0, 0, 0], [-1, -2, -1]
"""
kernel = np.array(
    [
        # [0, -4, 0], [-4, 16, -4], [0, -4, 0]  # 整体边缘滤波器
        [0, 1, 0],
        [1, -4, 1],
        [0, 1, 0]
        # [1, 0, -1], [2, 0, -2], [1, 0, -1]  # 垂直边缘滤波器
    ]
)
# 原卷积核的shape为(3，3)，为满足conv2d()函数输入参数filter的格式，
# 扩展维度为(3, 3, 1, 1)，即（卷积核高，卷积核宽，输入通道数，输出通道数）
kernel = np.expand_dims(kernel, 2)
kernel = np.expand_dims(kernel, 3)
print("kernel：", kernel.shape)  # shape(3, 3, 1, 1)

# 将img转换为Tensor变量用作输入
input = tf.Variable(img, dtype=tf.float32)
# 将卷积核转换为Tensor变量用作输入
filter = tf.Variable(kernel, dtype=tf.float32)
strides = 1  # [1, 2, 2, 1]  # 横向，纵向步长均设为2

# 卷积运算
output = tf.nn.conv2d(
    input, filter, strides=strides, padding="SAME"
)  # , padding="VALID"
print("output", output.shape)

pic_arr = np.squeeze(output)  # shape(255, 255)
plt.imshow(pic_arr, cmap="gray")
plt.show()
