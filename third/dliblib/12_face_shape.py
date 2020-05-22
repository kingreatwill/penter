# 面部表情跟踪

import sys
import cv2
import dlib
import os
import logging
import datetime
import numpy as np


def cal_face_boundary(img, shape):
    for index_, pt in enumerate(shape.parts()):
        if index_ == 0:
            x_min = pt.x
            x_max = pt.x
            y_min = pt.y
            y_max = pt.y
        else:
            if pt.x < x_min:
                x_min = pt.x

            if pt.x > x_max:
                x_max = pt.x

            if pt.y < y_min:
                y_min = pt.y

            if pt.y > y_max:
                y_max = pt.y

    # print('x_min:{}'.format(x_min))
    # print('x_max:{}'.format(x_max))
    # print('y_min:{}'.format(y_min))
    # print('y_max:{}'.format(y_max))

    # 如果出现负值，即人脸位于图像框之外的情况，应当忽视图像外的部分，将负值置为0
    if x_min < 0:
        x_min = 0

    if y_min < 0:
        y_min = 0

    if x_min == x_max or y_min == y_max:
        return None
    else:
        return img[y_min:y_max, x_min:x_max]


def draw_left_eyebrow(img, shape):
    # 17 - 21
    pt_pos = []
    for index, pt in enumerate(shape.parts()[17:21 + 1]):
        pt_pos.append((pt.x, pt.y))

    for num in range(len(pt_pos) - 1):
        cv2.line(img, pt_pos[num], pt_pos[num + 1], 255, 2)


def draw_right_eyebrow(img, shape):
    # 22 - 26
    pt_pos = []
    for index, pt in enumerate(shape.parts()[22:26 + 1]):
        pt_pos.append((pt.x, pt.y))

    for num in range(len(pt_pos) - 1):
        cv2.line(img, pt_pos[num], pt_pos[num + 1], 255, 2)


def draw_left_eye(img, shape):
    # 36 - 41
    pt_pos = []
    for index, pt in enumerate(shape.parts()[36:41 + 1]):
        pt_pos.append((pt.x, pt.y))

    for num in range(len(pt_pos) - 1):
        cv2.line(img, pt_pos[num], pt_pos[num + 1], 255, 2)

    cv2.line(img, pt_pos[0], pt_pos[-1], 255, 2)


def draw_right_eye(img, shape):
    # 42 - 47
    pt_pos = []
    for index, pt in enumerate(shape.parts()[42:47 + 1]):
        pt_pos.append((pt.x, pt.y))

    for num in range(len(pt_pos) - 1):
        cv2.line(img, pt_pos[num], pt_pos[num + 1], 255, 2)

    cv2.line(img, pt_pos[0], pt_pos[-1], 255, 2)


def draw_nose(img, shape):
    # 27 - 35
    pt_pos = []
    for index, pt in enumerate(shape.parts()[27:35 + 1]):
        pt_pos.append((pt.x, pt.y))

    for num in range(len(pt_pos) - 1):
        cv2.line(img, pt_pos[num], pt_pos[num + 1], 255, 2)

    cv2.line(img, pt_pos[0], pt_pos[4], 255, 2)
    cv2.line(img, pt_pos[0], pt_pos[-1], 255, 2)
    cv2.line(img, pt_pos[3], pt_pos[-1], 255, 2)


def draw_mouth(img, shape):
    # 48 - 59
    pt_pos = []
    for index, pt in enumerate(shape.parts()[48:59 + 1]):
        pt_pos.append((pt.x, pt.y))

    for num in range(len(pt_pos) - 1):
        cv2.line(img, pt_pos[num], pt_pos[num + 1], 255, 2)

    cv2.line(img, pt_pos[0], pt_pos[-1], 255, 2)

    # 60 - 67
    pt_pos = []
    for index, pt in enumerate(shape.parts()[60:]):
        pt_pos.append((pt.x, pt.y))

    for num in range(len(pt_pos) - 1):
        cv2.line(img, pt_pos[num], pt_pos[num + 1], 255, 2)

    cv2.line(img, pt_pos[0], pt_pos[-1], 255, 2)


def draw_jaw(img, shape):
    # 0 - 16
    pt_pos = []
    for index, pt in enumerate(shape.parts()[0:16 + 1]):
        pt_pos.append((pt.x, pt.y))

    for num in range(len(pt_pos) - 1):
        cv2.line(img, pt_pos[num], pt_pos[num + 1], 255, 2)


# 获取logger实例，如果参数为空则返回root logger
logger = logging.getLogger("PedestranDetect")
# 指定logger输出格式
formatter = logging.Formatter('%(asctime)s %(levelname)-8s: %(message)s')
# 文件日志
# file_handler = logging.FileHandler("test.log")
# file_handler.setFormatter(formatter)  # 可以通过setFormatter指定输出格式
# 控制台日志
console_handler = logging.StreamHandler(sys.stdout)
console_handler.formatter = formatter  # 也可以直接给formatter赋值
# 为logger添加的日志处理器
# logger.addHandler(file_handler)
logger.addHandler(console_handler)
# 指定日志的最低输出级别，默认为WARN级别
logger.setLevel(logging.INFO)

predictor_path = r"E:\bigdata\ai\dlib\data\shape_predictor_68_face_landmarks.dat"  # os.path.join(os.getcwd(), 'shape_predictor_68_face_landmarks.dat')

logger.info(u'导入人脸检测器')
detector = dlib.get_frontal_face_detector()
logger.info(u'导入人脸特征点检测器')
predictor = dlib.shape_predictor(predictor_path)

cap = cv2.VideoCapture(0)  # cv2.VideoCapture(r"E:\bigdata\ai\video\0004.mp4")
cnt = 0
total_time = 0
start_time = 0
while (1):

    ret, frame = cap.read()
    # cv2.imshow("window", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    dets = detector(img, 1)
    if dets:
        logger.info('Face detected')
    else:
        logger.info('No face detected')
    for index, face in enumerate(dets):
        # print('face {}; left {}; top {}; right {}; bottom {}'.format(index, face.left(), face.top(), face.right(),
        #                                                              face.bottom()))
        shape = predictor(img, face)

        # for index_, pt in enumerate(shape.parts()):
        #     pt_pos = (pt.x, pt.y)
        #     cv2.circle(frame, pt_pos, 2, (255, 0, 0), 1)

        features = np.zeros(img.shape[0:-1], dtype=np.uint8)
        for index_, pt in enumerate(shape.parts()):
            pt_pos = (pt.x, pt.y)
            cv2.circle(features, pt_pos, 2, 255, 1)

        draw_left_eyebrow(features, shape)
        draw_right_eyebrow(features, shape)
        draw_left_eye(features, shape)
        draw_right_eye(features, shape)
        draw_nose(features, shape)
        draw_mouth(features, shape)
        draw_jaw(features, shape)

        logger.info('face shape: {} {}'.format(face.right() - face.left(), face.bottom() - face.top()))
        faceROI = cal_face_boundary(features, shape)
        logger.info('ROI shape: {}'.format(faceROI.shape))
        # faceROI = features[face.top():face.bottom(), face.left():face.right()]
        faceROI = cv2.resize(faceROI, (500, 500), interpolation=cv2.INTER_LINEAR)
        # logger.info('face {}'.format(index))
        cv2.imshow('face {}'.format(index), faceROI)

    if cnt == 0:
        start_time = datetime.datetime.now()
        cnt += 1
    elif cnt == 100:
        end_time = datetime.datetime.now()
        frame_rate = float(100) / (end_time - start_time).seconds
        # logger.info(start_time)
        # logger.info(end_time)
        logger.info(u'帧率：{:.2f}fps'.format(frame_rate))
        cnt = 0
    else:
        cnt += 1

    # logger.info(cnt)
