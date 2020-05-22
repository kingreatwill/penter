# -*- coding: utf-8 -*-
import sys
import dlib
import cv2
import os
import glob
import numpy as np


def comparePersonData(data1, data2):
    diff = 0
    # for v1, v2 in data1, data2:
    # diff += (v1 - v2)**2
    for i in range(len(data1)):
        diff += (data1[i] - data2[i]) ** 2
    diff = np.sqrt(diff)
    print("欧式距离：",diff)
    if (diff < 0.6):
        print("It's the same person")
    else:
        print("It's not the same person")


def savePersonData(face_rec_class, face_descriptor):
    if face_rec_class.name == None or face_descriptor == None:
        return
    filePath = face_rec_class.dataPath + face_rec_class.name + '.npy'
    vectors = np.array([])
    for i, num in enumerate(face_descriptor):
        vectors = np.append(vectors, num)
        # print(num)
    print('Saving files to :' + filePath)
    np.save(filePath, vectors)
    return vectors


def loadPersonData(face_rec_class, personName):
    if personName == None:
        return
    filePath = face_rec_class.dataPath + personName + '.npy'
    vectors = np.load(filePath)
    print(vectors)
    return vectors


class face_recognition(object):
    def __init__(self):
        self.current_path = os.getcwd()  # 获取当前路径
        self.predictor_path = r"E:\bigdata\ai\dlib\data\shape_predictor_68_face_landmarks.dat"
        self.face_rec_model_path = r"E:\bigdata\ai\dlib\data\dlib_face_recognition_resnet_model_v1.dat"

        self.faces_folder_path = self.current_path + "\\faces\\"
        self.dataPath = self.current_path + "\\data\\"
        self.detector = dlib.get_frontal_face_detector()
        self.shape_predictor = dlib.shape_predictor(self.predictor_path)
        self.face_rec_model = dlib.face_recognition_model_v1(self.face_rec_model_path)

        self.name = None
        self.img_bgr = None
        self.img_rgb = None
        self.detector = dlib.get_frontal_face_detector()
        self.shape_predictor = dlib.shape_predictor(self.predictor_path)
        self.face_rec_model = dlib.face_recognition_model_v1(self.face_rec_model_path)

    def inputPerson(self, name='people', img_path=None):
        if img_path == None:
            print('No file!\n')
            return

        # img_name += self.faces_folder_path + img_name
        self.name = name
        self.img_bgr = cv2.imread(self.current_path + img_path)
        # opencv的bgr格式图片转换成rgb格式
        b, g, r = cv2.split(self.img_bgr)
        self.img_rgb = cv2.merge([r, g, b])

    def create128DVectorSpace(self):
        dets = self.detector(self.img_rgb, 1)
        print("Number of faces detected: {}".format(len(dets)))
        for index, face in enumerate(dets):
            print('face {}; left {}; top {}; right {}; bottom {}'.format(index, face.left(), face.top(), face.right(),
                                                                         face.bottom()))

            shape = self.shape_predictor(self.img_rgb, face)
            face_descriptor = self.face_rec_model.compute_face_descriptor(self.img_rgb, shape)
            # print(face_descriptor)
            # for i, num in enumerate(face_descriptor):
            #   print(num)
            #   print(type(num))

            return face_descriptor


if __name__ == '__main__':
    face_rec = face_recognition()   # 创建对象
    face_rec.inputPerson(name='obama1', img_path='\\faces\\obama1.jpg')  # name中写第一个人名字，img_name为图片名字，注意要放在faces文件夹中
    vector = face_rec.create128DVectorSpace()  # 提取128维向量，是dlib.vector类的对象
    person_data1 = savePersonData(face_rec, vector)   # 将提取出的数据保存到data文件夹，为便于操作返回numpy数组，内容还是一样的

    # 导入第二张图片，并提取特征向量
    face_rec.inputPerson(name='obama2', img_path='\\faces\\obama2.jpg')
    vector = face_rec.create128DVectorSpace()  # 提取128维向量，是dlib.vector类的对象
    person_data2 = savePersonData(face_rec, vector )

    # 计算欧式距离，判断是否是同一个人
    comparePersonData(person_data1, person_data2)

"""
如果data文件夹中已经有了模型文件，可以直接导入：

face_rec = face_recognition()   # 创建对象
person_data1 = loadPersonData(face_rec , 'obama1')   # 创建一个类保存相关信息，后面还要跟上人名，程序会在data文件中查找对应npy文件，比如这里就是'jobs.npy'
person_data2 = loadPersonData(face_rec , 'obama2')  # 导入第二张图片
fc.comparePersonData(person_data1, person_data2) # 计算欧式距离，判断是否是同一个人
"""

