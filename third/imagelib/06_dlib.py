"""
# https://github.com/vipstone/faceai
# https://www.cnblogs.com/vipstone/p/8964656.html



下载训练模型
训练模型用于是人脸识别的关键，用于查找图片的关键点。

下载地址：http://dlib.net/files/

下载文件：shape_predictor_68_face_landmarks.dat.bz2

当然你也可以训练自己的人脸关键点模型，这个功能会放在后面讲。

下载好的模型文件，我的存放地址是：C:\Python36\Lib\site-packages\dlib-data\shape_predictor_68_face_landmarks.dat.bz2

解压：shape_predictor_68_face_landmarks.dat.bz2得到文件：shape_predictor_68_face_landmarks.dat
"""

def demo1():
    import cv2
    import dlib

    path = "lenna.jpg"
    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 人脸分类器
    detector = dlib.get_frontal_face_detector()
    # 获取人脸检测器
    # r"E:\bigdata\ai\dlib\data\shape_predictor_68_face_landmarks.dat"
    # r"E:\bigdata\ai\dlib\data\shape_predictor_5_face_landmarks.dat"
    predictor = dlib.shape_predictor(
        r"E:\bigdata\ai\dlib\data\shape_predictor_68_face_landmarks.dat"
    )

    dets = detector(gray, 1)
    for face in dets:
        shape = predictor(img, face)  # 寻找人脸的68个标定点
        # 遍历所有点，打印出其坐标，并圈出来
        for pt in shape.parts():
            pt_pos = (pt.x, pt.y)
            cv2.circle(img, pt_pos, 2, (0, 255, 0), 1)
        cv2.imshow("image", img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()




# 视频识别人脸
def demo2():
    import cv2
    import dlib

    detector = dlib.get_frontal_face_detector()  # 使用默认的人类识别器模型

    def discern(img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        dets = detector(gray, 1)
        for face in dets:
            left = face.left()
            top = face.top()
            right = face.right()
            bottom = face.bottom()
            cv2.rectangle(img, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.imshow("image", img)
        else:
            cv2.imshow("image", img)

    cap = cv2.VideoCapture(r"E:\bigdata\ai\video\1.mp4")
    while (1):
        ret, img = cap.read()
        discern(img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


# cnn狗识别
def demo3():
    import cv2
    import dlib
    cnn_face_detector = dlib.cnn_face_detection_model_v1(r"E:\bigdata\ai\dlib\data\mmod_dog_hipsterizer.dat")

    for f in ["../imagelib/dog1.png"]:
        # opencv 读取图片，并显示
        img = cv2.imread(f, cv2.IMREAD_COLOR)

        # opencv的bgr格式图片转换成rgb格式
        b, g, r = cv2.split(img)
        img2 = cv2.merge([r, g, b])

        # 进行检测
        dets = cnn_face_detector(img, 1)

        # 打印检测到的人脸数
        print("Number of faces detected: {}".format(len(dets)))
        # 遍历返回的结果
        # 返回的结果是一个mmod_rectangles对象。这个对象包含有2个成员变量：dlib.rectangle类，表示对象的位置；dlib.confidence，表示置信度。
        for i, d in enumerate(dets):
            face = d.rect
            print(
                "Detection {}: Left: {} Top: {} Right: {} Bottom: {} Confidence: {}".format(i, face.left(), face.top(),
                                                                                            face.right(),
                                                                                            d.rect.bottom(),
                                                                                            d.confidence))

            # 在图片中标出人脸
            left = face.left()
            top = face.top()
            right = face.right()
            bottom = face.bottom()
            cv2.rectangle(img, (left, top), (right, bottom), (0, 255, 0), 3)
            cv2.namedWindow(f, cv2.WINDOW_AUTOSIZE)
            cv2.imshow(f, img)

    k = cv2.waitKey(0)
    cv2.destroyAllWindows()

