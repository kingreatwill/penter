# 图像处理第一课
"""
图像属性：
分辨率：400*400
宽度：400px
高度：400px
水平分辨率： 96 dpi
垂直分辨率： 96 dpi
位深度：24
分辨率单位：2

dpi：图像每英寸长度内的像素点数。DPI（Dots Per Inch，每英寸点数）
如果你的显示设备dpi值高，那么你显示的图片就小，如果你的dpi值非常低，那么显示的图片实际尺寸就非常大。
但是不管怎么样设置，并不影响你的文件的实际大小，不影响图片的实际大小。
"""


def pil_demo01():
    # https://pillow.readthedocs.io/en/stable/
    from PIL import Image
    import matplotlib.pyplot as plt

    img = Image.open("./img/lena.jpg")
    print(img.format, img.size, img.mode)
    # img需要转换像素点数组
    import numpy as np
    img_array = np.array(img)

    print(img_array[100, 100])  # RGB
    r = img_array[100, 100, 0]
    g = img_array[100, 100, 1]
    b = img_array[100, 100, 2]
    print(r)
    print(g)
    print(b)

    print(img_array.shape)  # (400,400,3) 3代表三维数组 r,g,b

    plt.figure()  # 图形
    plt.subplot(2, 2, 1)  # 将画板分为2行两列，本幅图位于第一个位置
    plt.imshow(img)
    # 转成灰度图
    # img.convert('L').save("./img/lena1.jpg",dpi=(300.0,300.0), quality = 95)
    plt.subplot(2, 2, 2)  # 将画板分为2行两列，本幅图位于第二个位置
    plt.imshow(img.convert('L'))
    # 二值化
    # img.convert('1').save("./img/lena2.jpg")
    plt.subplot(2, 2, 3)  # 将画板分为2行两列，本幅图位于第3个位置
    plt.imshow(img.convert('1'))
    plt.show()


def cv2_demo01():
    # opencv默认是BGR 而PIL是RGB
    # https://docs.opencv.org/master/d3/df2/tutorial_py_basic_ops.html
    import cv2
    import matplotlib.pyplot as plt
    # img 为图像像素点数组(<class 'numpy.ndarray'>)
    img = cv2.imread('./img/lena.jpg')
    # img = cv.imread(文件名,[,参数])
    # 第二个参数是一个标志，它指定了读取图像的方式。
    # cv.IMREAD_COLOR： 加载彩色图像，任何图像的透明度都会被忽视，如果不传参数，这个值是默认值。
    # cv.IMREAD_GRAYSCALE：以灰度模式加载图像。
    # cv.IMREAD_UNCHANGED：加载图像，包括alpha通道
    # 这三个标志可以简化为 1 、 0 、 -1
    print(type(img)) # <class 'numpy.ndarray'>
    print(img.size)  # 总像素数
    print(img.dtype) # dtype 在调试时非常重要，因为 OpenCV-Python 代码中的大量错误是由无效的数据类型引起的。
    print(img[100, 100])  # BGR
    b = img[100, 100, 0]
    g = img[100, 100, 1]
    r = img[100, 100, 2]
    r2 = img.item(100, 100, 2)
    print(b)
    print(g)
    print(r, r2)
    print(img.shape)
    # 也可以直接修改 值img[100,100] = [255,255,255]
    # or 只改变red的值 img.itemset((100,100,2),100)
    # 也可以取某一块 到另一块上去
    eye = img[180:220, 180:230]
    img[0:40, 0:50] = eye
    # 灰度图像
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    # 二值图像
    ret, binary = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)
    plt.subplot(221), plt.imshow(img, 'gray'), plt.title('ORIGINAL')
    plt.subplot(222), plt.imshow(img_gray, 'gray'), plt.title('img_gray')
    plt.subplot(223), plt.imshow(binary, 'gray'), plt.title('binary')
    plt.show()
    # plt.imshow(img)
    # plt.show()
    # 拆分通道
    b, g, r = cv2.split(img)
    # or
    # b = img[:,:,0]
    # set 单通道
    # img[:,:,2] = 0
    # or
    rows, cols, chn = img.shape
    # 拆分通道
    # b = img[:, :, 0]
    # g = np.zeros((rows, cols), dtype=img.dtype) # img[:,:,1] = 0
    # r = np.zeros((rows, cols), dtype=img.dtype) # img[:,:,2] = 0

    # 合成一张新图 完成 BGR 至 RGB 的转换
    img1 = cv2.merge((r, g, b)) # 注意rgb的顺序
    # or 完成 BGR 至 RGB 的转换
    #img3 = img[:, :, ::-1]
    # or 完成 BGR 至 RGB 的转换
    #img4 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # 图片写入
    #cv2.imwrite("demo.jpg", img1)
    plt.imshow(img1)
    plt.show()

    # cv2.imshow("img", img)
    # cv2.waitKey(0)
    # cv.waitKey(delay)是一个键盘绑定函数。其参数是以毫秒为单位的时间。该函数等待任何键盘事件指定的毫秒。
    # 如果您在这段时间内按下任何键，程序将继续运行。如果 0 被传递，它将无限期地等待一次敲击键。
    # cv2.destroyAllWindows()

    # ROI（Region of Interest）表示感兴趣区域
    BLUE = [255, 0, 0]
    # 复制
    replicate = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_REPLICATE)
    # 边框将是边框元素的镜像，例如：fedcba | abcdefgh | hgfedcb
    reflect = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_REFLECT)
    # 与上述相同，但略有变化，例如：gfedcb | abcdefgh | gfedcba
    reflect101 = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_REFLECT_101)
    # 无法解释，它看起来像这样：cdefgh | abcdefgh | abcdefg
    wrap = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_WRAP)
    # 添加恒定的彩色边框。 该值应作为下一个参数给出。
    constant = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=BLUE)
    plt.subplot(231), plt.imshow(img1, 'gray'), plt.title('ORIGINAL')
    plt.subplot(232), plt.imshow(replicate, 'gray'), plt.title('REPLICATE')
    plt.subplot(233), plt.imshow(reflect, 'gray'), plt.title('REFLECT')
    plt.subplot(234), plt.imshow(reflect101, 'gray'), plt.title('REFLECT_101')
    plt.subplot(235), plt.imshow(wrap, 'gray'), plt.title('WRAP')
    plt.subplot(236), plt.imshow(constant, 'gray'), plt.title('CONSTANT')
    plt.show()



if __name__ == '__main__':
    pil_demo01()
    cv2_demo01()

"""
https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#fully-supported-formats

https://pillow.readthedocs.io/en/stable/handbook/concepts.html
图像的模式定义了图像中像素的类型和深度。
每个像素使用比特深度的全范围。
1位像素的范围是0-1,8位像素的范围是0-255，以此类推。
im.mode 有以下标准模式：
1 (1-bit pixels, black and white, stored with one pixel per byte)
L (8-bit pixels, black and white)
P (8-bit pixels, mapped to any other mode using a color palette)
RGB (3x8-bit pixels, true color)
RGBA (4x8-bit pixels, true color with transparency mask)
CMYK (4x8-bit pixels, color separation)
YCbCr (3x8-bit pixels, color video format)
Note that this refers to the JPEG, and not the ITU-R BT.2020, standard
LAB (3x8-bit pixels, the L*a*b color space)
HSV (3x8-bit pixels, Hue, Saturation, Value color space)
I (32-bit signed integer pixels)
F (32-bit floating point pixels)
特殊模式：
LA (L with alpha)
PA (P with alpha)
RGBX (true color with padding)
RGBa (true color with premultiplied alpha)
La (L with premultiplied alpha)
I;16 (16-bit unsigned integer pixels)
I;16L (16-bit little endian unsigned integer pixels)
I;16B (16-bit big endian unsigned integer pixels)
I;16N (16-bit native endian unsigned integer pixels)
BGR;15 (15-bit reversed true colour)
BGR;16 (16-bit reversed true colour)
BGR;24 (24-bit reversed true colour)
BGR;32 (32-bit reversed true colour)
"""
