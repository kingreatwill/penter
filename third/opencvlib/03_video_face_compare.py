"""
https://pypi.org/simple/dlib/

先安装cmake或者dlib
https://cmake.org/download/

pip install face_recognition -i  http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
pip install opencv_python -i  http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
"""

def demo0():
    import face_recognition
    import time

    picture_of_me = face_recognition.load_image_file('dilireba_1.jpg')
    my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]

    start = time.clock()
    unknown_picture = face_recognition.load_image_file('E:\\PycharmProjects\\Face_python\\data\\dataset\\images\\dilireba\\dilireba_4.jpg')
    unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]

    results = face_recognition.compare_faces([my_face_encoding], unknown_face_encoding)
    end = time.clock()
    print(end - start)
    if results[0]:
        print("迪丽热巴")


def demo1():
    import cv2

    capture = cv2.VideoCapture("rtsp://admin:L2608EFF@192.168.31.17:554/cam/realmonitor?channel=1&subtype=0&unicast=true&proto=Onvif")
    classfier = cv2.CascadeClassifier(
        r"D:\Program Files\Python38\Lib\site-packages\cv2\data\haarcascade_frontalface_alt.xml")
    # 识别出人脸后要画的边框的颜色，RGB格式, color是一个不可增删的数组
    color = (0, 255, 0)
    while (True):
        # 获取一帧
        ret, frame = capture.read()
        # 将这帧转换为灰度图
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # 人脸检测，1.2和2分别为图片缩放比例和需要检测的有效点数
        faceRects = classfier.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=3, minSize=(32, 32))
        if len(faceRects) > 0:  # 大于0则检测到人脸
            for faceRect in faceRects:  # 单独框出每一张人脸
                x, y, w, h = faceRect
                # 画出矩形框
                cv2.rectangle(frame, (x - 10, y - 10), (x + w + 10, y + h + 10), color, 2)
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(frame, 'haha' , (x + 30, y + 30), font, 1, (255, 0, 255), 4)


        cv2.imshow('frame', frame)
        if cv2.waitKey(1) == ord('q'):
            break

# 视频身份识别
def demo2():
    import face_recognition
    import cv2
    # 定义编码方式并创建VideoWriter对象
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    outfile = cv2.VideoWriter('output.avi', fourcc, 25., (640, 480))
    video_capture = cv2.VideoCapture("rtsp://admin:L2608EFF@192.168.31.17:554/cam/realmonitor?channel=1&subtype=0&unicast=true&proto=Onvif")

    obama_img = face_recognition.load_image_file(r"E:\code\penter\third\opencvlib\jinwei.jpg")
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


def demo3():
    import face_recognition
    import cv2

    # This is a demo of running face recognition on live video from your webcam. It's a little more complicated than the
    # other example, but it includes some basic performance tweaks to make things run a lot faster:
    #   1. Process each video frame at 1/4 resolution (though still display it at full resolution)
    #   2. Only detect faces in every other frame of video.

    # PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
    # OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
    # specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.

    # Get a reference to webcam #0 (the default one)
    video_capture = cv2.VideoCapture("rtsp://admin:L2608EFF@192.168.31.17:554/cam/realmonitor?channel=1&subtype=0&unicast=true&proto=Onvif")

    # Load a sample picture and learn how to recognize it.
    enter_image = face_recognition.load_image_file("E:\code\penter\third\opencvlib\jinwei.jpg")
    enter_face_encoding = face_recognition.face_encodings(enter_image)[0]

    # Load a second sample picture and learn how to recognize it.
    Tongliya_image = face_recognition.load_image_file("E:\\PycharmProjects\\Face_python\\data\\dataset\\images\\test\\TongLiYa.jpg")
    Tongliya_face_encoding = face_recognition.face_encodings(Tongliya_image)[0]

    Tangyan_image = face_recognition.load_image_file("E:\\PycharmProjects\\Face_python\\data\\dataset\\images\\test\\TangYan.jpg")
    Tangyan_face_encoding = face_recognition.face_encodings(Tangyan_image)[0]

    # Tangyan_image =


    # Create arrays of known face encodings and their names
    known_face_encodings = [
        enter_face_encoding,
        Tongliya_face_encoding,
        Tangyan_face_encoding
    ]
    known_face_names = [
        "enter",
        "Tong Liya",
        "Tang Yan"
    ]

    # Initialize some variables
    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True

    while True:
        # Grab a single frame of video
        ret, frame = video_capture.read()

        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]

        # Only process every other frame of video to save time
        if process_this_frame:
            # Find all the faces and face encodings in the current frame of video
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
                # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown"

                # If a match was found in known_face_encodings, just use the first one.
                if True in matches:
                    first_match_index = matches.index(True)
                    name = known_face_names[first_match_index]

                face_names.append(name)

        process_this_frame = not process_this_frame

        # Display the results
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 255), 2)

            # Draw a label with a name below the face
            # cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 255, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 0, 255), 2)

        # Display the resulting image
        cv2.imshow('Video', frame)

        # Hit 'q' on the keyboard to quit!
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release handle to the webcam
    video_capture.release()
    cv2.destroyAllWindows()




# 识别成功的再推送rtsp
# https://www.cnblogs.com/Manuel/p/15006727.html

if __name__ =="__main__":
    demo2()