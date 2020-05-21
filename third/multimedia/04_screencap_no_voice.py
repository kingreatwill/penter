# coding: utf-8
from PIL import ImageGrab
import numpy as np
import cv2

fps = 20
start = 3  # 延时录制
end = 15  # 自动结束时间

curScreen = ImageGrab.grab()  # 获取屏幕对象
height, width = curScreen.size

video = cv2.VideoWriter('video02.avi', cv2.VideoWriter_fourcc(*'XVID'), fps, (height, width))

imageNum = 0
while True:
    imageNum += 1
    captureImage = ImageGrab.grab()  # 抓取屏幕
    frame = cv2.cvtColor(np.array(captureImage), cv2.COLOR_RGB2BGR)

    # 显示无图像的窗口
    cv2.imshow('capturing', np.zeros((1, 255), np.uint8))

    # 控制窗口显示位置，方便通过按键方式退出
    cv2.moveWindow('capturing', height - 100, width - 100)
    if imageNum > fps * start:
        video.write(frame)
    # 退出条件
    if cv2.waitKey(50) == ord('q') or imageNum > fps * end:
        break
video.release()
cv2.destroyAllWindows()