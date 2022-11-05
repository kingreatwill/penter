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

# 获取捕获的分辨率
# propId可以直接写数字，也可以用OpenCV的符号表示
# width, height = capture.get(3), capture.get(4)
# print(width, height)
# 以原分辨率的一倍来捕获
# capture.set(cv2.CAP_PROP_FRAME_WIDTH, width * 2)
# capture.set(cv2.CAP_PROP_FRAME_HEIGHT, height * 2)
# 经验之谈：某些摄像头设定分辨率等参数时会无效，因为它有固定的分辨率大小支持，一般可在摄像头的资料页中找到。

"""
跟打开摄像头一样，如果把摄像头的编号换成视频的路径就可以播放本地视频了。
回想一下cv2.waitKey()，它的参数表示暂停时间，所以这个值越大，视频播放速度越慢，反之，播放速度越快，通常设置为25或30。
"""
# "rtmp://58.200.131.2:1935/livetv/hunantv" # 湖南卫视
# rtmp_str = 'rtmp://media3.scctv.net/live/scctv_800'  # CCTV

"""
1，RTMP协议直播源
香港卫视：rtmp://live.hkstv.hk.lxdns.com/live/hks  不能使用了

2，RTSP协议直播源

珠海过澳门大厅摄像头监控：rtsp://218.204.223.237:554/live/1/66251FC11353191F/e7ooqwcfbqjoo80j.sdp
大熊兔（点播）：rtsp://184.72.239.149/vod/mp4://BigBuckBunny_175k.mov

3，HTTP协议直播源

香港卫视：http://live.hkstv.hk.lxdns.com/live/hks/playlist.m3u8

CCTV1高清：http://ivi.bupt.edu.cn/hls/cctv1hd.m3u8

CCTV3高清：http://ivi.bupt.edu.cn/hls/cctv3hd.m3u8

CCTV5高清：http://ivi.bupt.edu.cn/hls/cctv5hd.m3u8

CCTV5+高清：http://ivi.bupt.edu.cn/hls/cctv5phd.m3u8

CCTV6高清：http://ivi.bupt.edu.cn/hls/cctv6hd.m3u8

苹果提供的测试源（点播）：http://devimages.apple.com.edgekey.net/streaming/examples/bipbop_4x3/gear2/prog_index.m3u8

"""


import cv2
capture = cv2.VideoCapture("rtsp://admin:L2608EFF@192.168.31.17:554/cam/realmonitor?channel=1&subtype=0&unicast=true&proto=Onvif")#cv2.VideoCapture("rtsp://admin:cqh123456@192.168.1.232/h264/ch1/sub/av_stream")
while(True):
    # 获取一帧
    ret, frame = capture.read()
    # 将这帧转换为灰度图
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', gray)
    if cv2.waitKey(1) == ord('q'):
        break