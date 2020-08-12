# only Linux
# pip3 install face_recognition
# pip3 install face_recognition -i  http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
# https://github.com/ageitgey/face_recognition
"""
https://github.com/mrzv/dionysus/issues/15

下载的最新cmake编译出错，可以使用vs的cmake（安装vs 要选择c++编译），
C:\Program Files (x86)\Microsoft Visual Studio\2019\Enterprise\Common7\IDE\CommonExtensions\Microsoft\CMake\CMake\bin

如果还有错安装https://cmake.org/download/

https://pypi.org/project/cmake/
https://anaconda.org/conda-forge/cmake
https://anaconda.org/anaconda/cmake
"""
import face_recognition
import cv2


# 识别出人脸的位置
def demo1():
    image = face_recognition.load_image_file("lenna.jpg")
    face_locations = face_recognition.face_locations(image)
    print(face_locations)


# 调用opencv函数显示图片
def demo2():
    image = face_recognition.load_image_file("lenna.jpg")
    face_locations = face_recognition.face_locations(image)
    img = cv2.imread("lenna.jpg")
    cv2.namedWindow("原图")
    cv2.imshow("原图", img)
    # 遍历每个人脸，并标注
    faceNum = len(face_locations)
    for i in range(0, faceNum):
        top = face_locations[i][0]
        right = face_locations[i][1]
        bottom = face_locations[i][2]
        left = face_locations[i][3]

        start = (left, top)
        end = (right, bottom)

        color = (55, 255, 155)
        thickness = 3
        cv2.rectangle(img, start, end, color, thickness)
    # 显示识别结果
    cv2.namedWindow("识别")
    cv2.imshow("识别", img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


# 识别是不是同一个人
def demo3():
    import face_recognition
    known_image = face_recognition.load_image_file("lenna.jpg")
    unknown_image = face_recognition.load_image_file("lenna.jpg")  # "wallhaven-nmekwy.jpg"

    biden_encoding = face_recognition.face_encodings(known_image)[0]
    unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

    results = face_recognition.compare_faces([biden_encoding], unknown_encoding)

    print(results)


# 识别图片中的人脸
def demo4():
    import face_recognition
    jobs_image = face_recognition.load_image_file("lenna.jpg")
    obama_image = face_recognition.load_image_file("wallhaven-nmekwy.jpg")
    unknown_image = face_recognition.load_image_file("lenna.jpg")

    jobs_encoding = face_recognition.face_encodings(jobs_image)[0]
    obama_encoding = face_recognition.face_encodings(obama_image)[0]
    unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

    results = face_recognition.compare_faces([jobs_encoding, obama_encoding], unknown_encoding)
    labels = ['lenna', 'wallhaven']

    print('results:' + str(results))

    for i in range(0, len(results)):
        if results[i] == True:
            print('The person is:' + labels[i])


# 面部特征
def demo5():
    image = face_recognition.load_image_file("lenna.jpg")
    face_landmarks_list = face_recognition.face_landmarks(image)
    print(face_landmarks_list)


# 视频身份识别
def demo6():
    import face_recognition
    import cv2
    # 定义编码方式并创建VideoWriter对象
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    outfile = cv2.VideoWriter('output.avi', fourcc, 25., (640, 480))
    video_capture = cv2.VideoCapture(0)  # r"E:\bigdata\ai\video\output_logo.mp4"

    obama_img = face_recognition.load_image_file(r"C:\Users\35084\Pictures\Camera Roll\jinwei.jpg")
    obama_face_encoding = face_recognition.face_encodings(obama_img)[0]

    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True

    while True:
        ret, frame = video_capture.read()

        small_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)  # 缩小提高性能

        if process_this_frame:
            face_locations = face_recognition.face_locations(small_frame)
            face_encodings = face_recognition.face_encodings(small_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
                match = face_recognition.compare_faces([obama_face_encoding], face_encoding)

                if match[0]:
                    name = "Enter"
                else:
                    name = "unknown"

                face_names.append(name)

        process_this_frame = not process_this_frame  # 处理一帧跳过一帧，提高性能

        for (top, right, bottom, left), name in zip(face_locations, face_names):
            top *= 2  # 放大上面缩小的倍数（如0.25 对应的需要 *4）
            right *= 2
            bottom *= 2
            left *= 2

            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), 2)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (105, 225, 65), 1)
        #outfile.write(frame)  # 写入文件
        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()

if __name__ =="__main__":
    demo2()
