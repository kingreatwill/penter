# 人脸聚类
"""
这次再将那些操作综合一下，进行人脸聚类。识别图片中的人脸，并分类。这里使用的是聚类，属于无监督学习。
这里对每个人脸的区分与比对人脸中原理相同，将人脸映射到128D的空间中，计算彼此之间的距离。距离近的视作一个人，距离远的视作不是一个人，而判定的标准阈值由自己选定，通常是0.6。
"""
# 参考：dlib/face_clustering.py
import sys
import os
import dlib
import glob
import cv2

# 指定路径
current_path = os.getcwd()
model_path = current_path + '/model/'
shape_predictor_model = model_path + '/shape_predictor_5_face_landmarks.dat'
face_rec_model = model_path + '/dlib_face_recognition_resnet_model_v1.dat'
face_folder = current_path + '/faces/'
output_folder = current_path + '/output/'

# 导入模型
detector = dlib.get_frontal_face_detector()
shape_detector = dlib.shape_predictor(shape_predictor_model)
face_recognizer = dlib.face_recognition_model_v1(face_rec_model)

# 为后面操作方便，建了几个列表
descriptors = []
images = []
# 遍历faces文件夹中所有的图片
for f in glob.glob(os.path.join(face_folder, "*.jpg")):
    print('Processing file：{}'.format(f))
    # 读取图片
    img = cv2.imread(f)
    # 转换到rgb颜色空间
    img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # 检测人脸
    dets = detector(img2, 1)
    print("Number of faces detected: {}".format(len(dets)))

    # 遍历所有的人脸
    for index, face in enumerate(dets):
        # 检测人脸特征点
        shape = shape_detector(img2, face)
        # 投影到128D
        face_descriptor = face_recognizer.compute_face_descriptor(img2, shape)

        # 保存相关信息
        descriptors.append(face_descriptor)
        images.append((img2, shape))

# 聚类
labels = dlib.chinese_whispers_clustering(descriptors, 0.5)
print("labels: {}".format(labels))
num_classes = len(set(labels))
print("Number of clusters: {}".format(num_classes))

# 为了方便操作，用字典类型保存
face_dict = {}
for i in range(num_classes):
    face_dict[i] = []
# print face_dict
for i in range(len(labels)):
    face_dict[labels[i]].append(images[i])

# print face_dict.keys()
# 遍历字典，保存结果
for key in face_dict.keys():
    file_dir = os.path.join(output_folder, str(key))
    if not os.path.isdir(file_dir):
        os.makedirs(file_dir)

    for index, (image, shape) in enumerate(face_dict[key]):
        file_path = os.path.join(file_dir, 'face_' + str(index))
        dlib.save_face_chip(image, shape, file_path, size=150, padding=0.25)