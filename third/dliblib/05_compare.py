"""
02_68face.py提取68个特征点。这次要在这两个工作的基础之上，将人脸的信息提取成一个128维的向量空间。在这个向量空间上，同一个人脸的更接近，不同人脸的距离更远。度量采用欧式距离，欧氏距离计算不算复杂。
二维情况下：distance = 根号下{(x1-x2)平方 + (y1-y2)平方}
三维情况下：distance = 根号下{(x1-x2)平方 + (y1-y2)平方 + (z1-z2)平方}

将其扩展到128维的情况下即可。
通常使用的判别阈值是0.6，即如果两个人脸的向量空间的欧式距离超过了0.6，即认定不是同一个人；
如果欧氏距离小于0.6，则认为是同一个人。这个距离也可以由自己定，只要效果能更好。
"""
def demo1():
    import sys
    import dlib
    import cv2
    import os
    import glob

    current_path = os.getcwd()  # 获取当前路径
    # 模型路径
    predictor_path =  r"E:\bigdata\ai\dlib\data\shape_predictor_68_face_landmarks.dat"
    face_rec_model_path = r"E:\bigdata\ai\dlib\data\dlib_face_recognition_resnet_model_v1.dat"
    #测试图片路径
    faces_folder_path = "E:\\openjw\\penter\\third\\imagelib\\"

    # 读入模型
    detector = dlib.get_frontal_face_detector()
    shape_predictor = dlib.shape_predictor(predictor_path)
    face_rec_model = dlib.face_recognition_model_v1(face_rec_model_path)

    for img_path in glob.glob(os.path.join(faces_folder_path, "*.jpg")):
        print("Processing file: {}".format(img_path))
        # opencv 读取图片，并显示
        img = cv2.imread(img_path, cv2.IMREAD_COLOR)
        # opencv的bgr格式图片转换成rgb格式
        b, g, r = cv2.split(img)
        img2 = cv2.merge([r, g, b])

        dets = detector(img, 1)   # 人脸标定
        print("Number of faces detected: {}".format(len(dets)))

        for index, face in enumerate(dets):
            print('face {}; left {}; top {}; right {}; bottom {}'.format(index, face.left(), face.top(), face.right(), face.bottom()))

            shape = shape_predictor(img2, face)   # 提取68个特征点
            for i, pt in enumerate(shape.parts()):
                #print('Part {}: {}'.format(i, pt))
                pt_pos = (pt.x, pt.y)
                cv2.circle(img, pt_pos, 2, (255, 0, 0), 1)
                #print(type(pt))
            #print("Part 0: {}, Part 1: {} ...".format(shape.part(0), shape.part(1)))
            cv2.namedWindow(img_path+str(index), cv2.WINDOW_AUTOSIZE)
            cv2.imshow(img_path+str(index), img)

            face_descriptor = face_rec_model.compute_face_descriptor(img2, shape)   # 计算人脸的128维的向量
            print(face_descriptor)

    k = cv2.waitKey(0)
    cv2.destroyAllWindows()

demo1()