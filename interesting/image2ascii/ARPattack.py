import numpy as np
import cv2


def video2imgs(video_name, size):
    img_list = []
    cap = cv2.VideoCapture(video_name)
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            img = cv2.resize(gray, size, interpolation=cv2.INTER_AREA)
            img_list.append(img)
        else:
            break
    cap.release()

    return img_list


pixels = " .,-'`:!1+*abcdefghijklmnopqrstuvwxyz<>()\/{}[]?234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ%&@#$"


def img2chars(img):
    res = []
    percents = img / 255
    indexes = (percents * (len(pixels) - 1)).astype(np.int)

    height, width = img.shape
    for row in range(height):
        line = ""
        for col in range(width):
            index = indexes[row][col]
            line += pixels[index] + " "
        res.append(line)

    return res


def imgs2chars(imgs):
    video_chars = []
    for img in imgs:
        video_chars.append(img2chars(img))

    return video_chars


import time
import os


def play_video(video_chars):
    """
    播放字符视频
    :param video_chars: 字符画的列表，每个元素为一帧
    :return: None
    """
    # 获取字符画的尺寸
    width, height = len(video_chars[0][0]), len(video_chars[0])

    for pic_i in range(len(video_chars)):
        for line_i in range(height):
            print(video_chars[pic_i][line_i])
        time.sleep(1 / 50)

        os.system("cls")

# https://github.com/benjieming421/----python/tree/master/%E5%AD%97%E7%AC%A6%E5%8A%A8%E7%94%BB
if __name__ == "__main__":
    imgs = video2imgs("BadApple.mp4", (64, 48))
    video_chars = imgs2chars(imgs)
    input("`转换完成！按enter键开始播放")
    play_video(video_chars)