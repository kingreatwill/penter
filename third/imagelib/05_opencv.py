# pip3 install opencv-python
import cv2
import os
# https://opencv-python-tutroals.readthedocs.io/en/latest/index.html
# https://github.com/ex2tron/OpenCV-Python-Tutorial
# http://codec.wang/opencv-python-introduction-and-installation/
# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_morphological_ops/py_morphological_ops.html
'''
众所周知，虽然Python语法简洁，编写高效，但相比C/C++运行慢很多。
然而Python还有个重要的特性：它是一门胶水语言！Python可以很容易地扩展C/C++。
OpenCV-Python就是用Python包装了C++的实现，背后实际就是C++的代码在跑，所以代码的运行速度跟原生C/C++速度一样快。

Python3调用C程序 https://www.jianshu.com/p/edb8698d1374
'''
print(cv2.getVersionString())

# 保存好的视频检测人脸并截图
def CatchPICFromVideo(window_name, camera_idx, catch_pic_num, path_name):
    cv2.namedWindow(window_name)

    # 视频来源
    cap = cv2.VideoCapture(camera_idx)
    # 如果获取摄像头，参数修改为 0 即可
    #cap = cv2.VideoCapture(0)

    # 告诉OpenCV使用人脸识别分类器(眼睛，左眼，右眼，body，微笑)
    classfier = cv2.CascadeClassifier(r"D:\Programs\Python\Python37\Lib\site-packages\cv2\data\haarcascade_frontalface_alt.xml")

    # 识别出人脸后要画的边框的颜色，RGB格式, color是一个不可增删的数组
    color = (0, 255, 0)

    num = 0
    while cap.isOpened():
        ok, frame = cap.read()  # 读取一帧数据
        if not ok:
            break

        grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 将当前桢图像转换成灰度图像

        # 人脸检测，1.2和2分别为图片缩放比例和需要检测的有效点数
        faceRects = classfier.detectMultiScale(grey, scaleFactor=1.2, minNeighbors=3, minSize=(32, 32))
        if len(faceRects) > 0:  # 大于0则检测到人脸
            for faceRect in faceRects:  # 单独框出每一张人脸
                x, y, w, h = faceRect

                # 将当前帧保存为图片
                img_name = "%s/%d.jpg" % (path_name, num)
                # print(img_name)
                image = frame[y - 10: y + h + 10, x - 10: x + w + 10]
                cv2.imwrite(img_name, image, [int(cv2.IMWRITE_PNG_COMPRESSION), 9])

                num += 1
                if num > (catch_pic_num):  # 如果超过指定最大保存数量退出循环
                    break

                # 画出矩形框
                cv2.rectangle(frame, (x - 10, y - 10), (x + w + 10, y + h + 10), color, 2)

                # 显示当前捕捉到了多少人脸图片了，这样站在那里被拍摄时心里有个数，不用两眼一抹黑傻等着
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(frame, 'num:%d/100' % (num), (x + 30, y + 30), font, 1, (255, 0, 255), 4)

                # 超过指定最大保存数量结束程序
        if num > (catch_pic_num): break

        # 显示图像
        cv2.imshow(window_name, frame)
        c = cv2.waitKey(10)
        if c & 0xFF == ord('q'):
            break

            # 释放摄像头并销毁所有窗口
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    # 连续截100张图像
    CatchPICFromVideo("get face", r"C:\Users\35084\Desktop\003.mp4", 100, r"C:\Users\35084\Desktop\003")