import cv2


def demo1():
    # 而opencv默认通道是bgr的
    flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
    print("显示所有的转换模式：", flags)

    img = cv2.imread('../imagelib/lenna.jpg')
    # 转换为灰度图
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # cv2.cvtColor()用来进行颜色模型转换，参数1是要转换的图片，参数2是转换模式， COLOR_BGR2GRAY表示BGR→Gray
    cv2.imshow('img', img)
    cv2.imshow('gray', img_gray)
    cv2.waitKey(0)


"""
HSV是一个常用于颜色识别的模型，相比BGR更易区分颜色，转换模式用COLOR_BGR2HSV表示。

经验之谈：OpenCV中色调H范围为[0,179]，饱和度S是[0,255]，明度V是[0,255]。
虽然H的理论数值是0°~360°，但8位图像像素点的最大值是255，所以OpenCV中除以了2，某些软件可能使用不同的尺度表示，所以同其他软件混用时，记得归一化。
"""
# 只保留蓝色部分
def demo2():
    import numpy as np
    capture = cv2.VideoCapture(r"E:\bigdata\ai\video\1.mp4")
    # 蓝色的范围，不同光照条件下不一样，可灵活调整
    lower_blue = np.array([100, 110, 110])
    upper_blue = np.array([130, 255, 255])

    while (True):
        # 1.捕获视频中的一帧
        ret, frame = capture.read()

        # 2.从BGR转换到HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # 3.提取蓝色范围的物体 inRange()：介于lower/upper之间的为白色，其余黑色
        mask = cv2.inRange(hsv, lower_blue, upper_blue)

        # 4.只保留原图中的蓝色部分
        res = cv2.bitwise_and(frame, frame, mask=mask)

        cv2.imshow('frame', frame)
        cv2.imshow('mask', mask)
        cv2.imshow('res', res)

        if cv2.waitKey(1) == ord('q'):
            break

demo2()

