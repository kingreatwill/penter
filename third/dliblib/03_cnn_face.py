import sys
import dlib
import cv2

# CNN卷积神经网络
# 处理的慢，尤其大图
# 导入cnn模型
cnn_face_detector = dlib.cnn_face_detection_model_v1(r"E:\bigdata\ai\dlib\data\mmod_human_face_detector.dat")

for f in ["../imagelib/lenna.jpg"]:
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
        print("Detection {}: Left: {} Top: {} Right: {} Bottom: {} Confidence: {}".format(i, face.left(), face.top(), face.right(), d.rect.bottom(), d.confidence))

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