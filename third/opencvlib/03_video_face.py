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
