# 打开摄像头并灰度化显示


# 要使用摄像头，需要使用cv2.VideoCapture(0)创建VideoCapture对象，参数0指的是摄像头的编号，如果你电脑上有两个摄像头的话，访问第2个摄像头就可以传入1，依此类推。
# 也可以是视频地址
# r"E:\bigdata\ai\video\1.mp4"
# "rtsp://admin:cqh123456@192.168.1.232/ch1-s1?tcp"

"""
# https://blog.csdn.net/luohenyj/article/details/89403227
String url = "rtsp://admin:123456@114.114.114.114/ch1-s1?tcp";
//海康
//"rtsp://admin:123456@114.114.114.114/ch1-s1?tcp"
//大华
//“rtsp://admin:123456@114.114.114.114/cam/realmonitor?channel=1&subtype=1?tcp”
//宇视
//"rtsp://admin:123456@114.114.114.114/video1?tcp"


https://blog.csdn.net/cug_heshun2013/article/details/79434387
【海康威视】举例说明：
主码流取流:
rtsp://admin:12345@192.0.0.64:554/h264/ch1/main/av_stream
子码流取流:
rtsp://admin:12345@192.0.0.64:554/h264/ch1/sub/av_stream
如果摄像机密码是a12345678,IP是192.168.1.64，RTSP端口默认554未做改动，是H.264编码，那么
主码流取流:
rtsp://admin:a12345678@192.168.1.64:554/h264/ch1/main/av_stream
子码流取流:
rtsp://admin:a12345678@192.168.1.64:554/h264/ch1/sub/av_stream
【如果是H.265编码的，那么将H.264替换成H.265即可】

# https://www.jianshu.com/p/8efcea89b11f
主码流
rtsp://IP:554/h264/ch1/main/av_stream
rtsp://IP:554/ISAPI/streaming/channels/101?auth=YWRtaW46YWRtaW4xMjM0NTY=

子码流
rtsp://IP:554/h264/ch1/sub/av_stream
rtsp://IP:554/ISAPI/streaming/channels/102?auth=YWRtaW46YWRtaW4xMjM0NTY=

第三码流
rtsp://IP:554/ISAPI/streaming/channels/103?auth=YWRtaW46YWRtaW4xMjM0NTY=
rtsp://admin:12345@172.6.10.11:554/Streaming/Channels/103
"""
import cv2
capture = cv2.VideoCapture("rtsp://admin:cqh123456@192.168.1.232/h264/ch1/sub/av_stream")

while(True):
    # 获取一帧
    ret, frame = capture.read()
    # 将这帧转换为灰度图
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', gray)
    if cv2.waitKey(1) == ord('q'):
        break