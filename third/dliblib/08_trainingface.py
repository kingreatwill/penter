
def train1():
    import os
    import cv2
    import dlib
    import glob

    # 训练68个特征点

    current_path = os.getcwd()
    faces_path = current_path + '/examples/faces'

    # 训练部分
    # 参数设置
    options = dlib.shape_predictor_training_options()
    options.oversampling_amount = 300
    options.nu = 0.05
    options.tree_depth = 2
    options.be_verbose = True

    # 导入打好了标签的xml文件
    training_xml_path = os.path.join(faces_path, "training_with_face_landmarks.xml")
    # 进行训练，训练好的模型将保存为predictor.dat
    dlib.train_shape_predictor(training_xml_path, "predictor.dat", options)
    # 打印在训练集中的准确率
    print("\nTraining accuracy:{0}".format(dlib.test_shape_predictor(training_xml_path, "predictor.dat")))

    # 导入测试集的xml文件
    testing_xml_path = os.path.join(faces_path, "testing_with_face_landmarks.xml")
    # 打印在测试集中的准确率
    print("\Testing accuracy:{0}".format(dlib.test_shape_predictor(testing_xml_path, "predictor.dat")))


def demo1():
    # coding: utf-8
    #
    #   This example program shows how to use dlib's implementation of the paper:
    #   One Millisecond Face Alignment with an Ensemble of Regression Trees by
    #   Vahid Kazemi and Josephine Sullivan, CVPR 2014

    import os
    import cv2
    import dlib
    import glob

    # 测试部分
    # 导入训练好的模型文件
    predictor = dlib.shape_predictor("predictor.dat")

    detector = dlib.get_frontal_face_detector()
    print("Showing detections and predictions on the images in the faces folder...")
    for f in glob.glob(os.path.join('/examples/faces', "*.jpg")):
        print("Processing file: {}".format(f))
        img = cv2.imread(f)
        img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        dets = detector(img2, 1)
        print("Number of faces detected: {}".format(len(dets)))
        for index, face in enumerate(dets):
            print('face {}; left {}; top {}; right {}; bottom {}'.format(index, face.left(), face.top(), face.right(),
                                                                         face.bottom()))

            # left = face.left()
            # top = face.top()
            # right = face.right()
            # bottom = face.bottom()
            # cv2.rectangle(img, (left, top), (right, bottom), (0, 255, 0), 3)
            # cv2.namedWindow(f, cv2.WINDOW_AUTOSIZE)
            # cv2.imshow(f, img)

            shape = predictor(img, face)
            # print(shape)
            # print(shape.num_parts)
            for index, pt in enumerate(shape.parts()):
                print('Part {}: {}'.format(index, pt))
                pt_pos = (pt.x, pt.y)
                cv2.circle(img, pt_pos, 2, (255, 0, 0), 1)
                # print(type(pt))
            # print("Part 0: {}, Part 1: {} ...".format(shape.part(0), shape.part(1)))
            cv2.namedWindow(f, cv2.WINDOW_AUTOSIZE)
            cv2.imshow(f, img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
