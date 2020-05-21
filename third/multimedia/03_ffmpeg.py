# http://ffmpeg.org/releases/
# https://github.com/FFmpeg/FFmpeg
# http://ffmpeg.org/download.html
# https://ffmpeg.org/documentation.html
# https://www.cnblogs.com/Neeo/articles/11677715.html
# https://github.com/kkroening/ffmpeg-python
"""

FFmpeg主要由一下几个部分组成：

libavcodec：一个包含了所有FFmpeg音视频编解码器的库。 为了保证最优性能和高可复用性,大多数编解码器从头开发的。
非常先进的音频/视频编解码库libavcodec

libavformat：一个包含了所有的普通音视格式的解析器和 产生器的库。

三个实例程序，这三个实例较为复杂，基本可以作为API使用手册：
    ffmpeg：命令行的视频格式转换程序。
    ffplay：视频播放程序。（需要SDL支持）
    ffserver：多媒体服务器



构成FFmpeg主要有三个部分：

第一部分是四个作用不同的工具软件，分别是：ffmpeg.exe，ffplay.exe，ffserver.exe和ffprobe.exe。
ffmpeg.exe：音视频转码、转换器
ffplay.exe：简单的音视频播放器
ffserver.exe：流媒体服务器
ffprobe.exe：简单的多媒体码流分析器

第二部分是可以供开发者使用的SDK，为各个不同平台编译完成的库。如果说上面的四个工具软件都是完整成品形式的玩具，那么这些库就相当于乐高积木一样，我们可以根据自己的需求使用这些库开发自己的应用程序。这些库有：
libavcodec：包含音视频编码器和解码器
libavutil：包含多媒体应用常用的简化编程的工具，如随机数生成器、数据结构、数学函数等功能
libavformat：包含多种多媒体容器格式的封装、解封装工具
libavfilter：包含多媒体处理常用的滤镜功能
libavdevice：用于音视频数据采集和渲染等功能的设备相关
libswscale：用于图像缩放和色彩空间和像素格式转换功能
libswresample：用于音频重采样和格式转换等功能

第三部分是整个工程的源代码，
无论是编译出来的可执行程序还是SDK，都是由这些源代码编译出来的。
FFmpeg的源代码由C语言实现，主要在Linux平台上进行开发。FFmpeg不是一个孤立的工程，它还存在多个依赖的第三方工程来增强它自身的功能。
在当前这一系列的博文/视频中，我们暂时不会涉及太多源代码相关的内容，主要以FFmpeg的工具和SDK的调用为主。到下一系列我们将专门研究如何编译源代码并根据源代码来进行二次开发。
"""

"""
# mp4 里面是分视频和音频的， 两个可以分离
ffmpeg -i 1.mp4
可以看到 Stream #0:0(und): Video: h264 和 Stream #0:1(und): Audio: aac (HE-AAC)

  Metadata:
    major_brand     : mp42
    minor_version   : 0
    compatible_brands: mp42isom
    creation_time   : 2020-05-20T09:21:49.000000Z
  Duration: 00:15:20.02, start: 0.000000, bitrate: 225 kb/s
    Stream #0:0(und): Video: h264 (Main) (avc1 / 0x31637661), yuv420p, 640x360 [SAR 1:1 DAR 16:9], 190 kb/s, 25 fps, 25 tbr, 12800 tbn, 50 tbc (default)
    Metadata:
      creation_time   : 2020-05-20T09:21:49.000000Z
      encoder         : JVT/AVC Coding
    Stream #0:1(und): Audio: aac (HE-AAC) (mp4a / 0x6134706D), 44100 Hz, stereo, fltp, 32 kb/s (default)
    Metadata:
      creation_time   : 2020-05-20T09:21:49.000000Z
"""



# pip install ffmpeg-python
import ffmpeg
def demo1():
    (
        ffmpeg
        .input(r'E:\bigdata\ai\video\1.mp4')
        .hflip() #水平镜像
        .output(r'E:\bigdata\ai\video\output.mp4') #h264
        .run()
    )

# 添加logo
def demo2():
    main = ffmpeg.input(r'E:\bigdata\ai\video\output.mp4')
    logo = ffmpeg.input('../imagelib/lenna.jpg')
    (
        ffmpeg
        .filter([main, logo], 'overlay', 10, 10)
        .output(r'E:\bigdata\ai\video\output_logo.mp4')
        .run()
    )

# https://github.com/kkroening/ffmpeg-python/tree/master/examples#audiovideo-pipeline

# 保留音频
def demo3():
    in1 = ffmpeg.input(r'E:\bigdata\ai\video\0001.mp4')
    in2 = ffmpeg.input(r'E:\bigdata\ai\video\0002.mp4')
    v1 = in1.video.hflip()
    a1 = in1.audio
    v2 = in2.video.filter('reverse').filter('hue', s=0)
    a2 = in2.audio.filter('areverse').filter('aphaser')
    joined = ffmpeg.concat(v1, a1, v2, a2, v=1, a=1).node
    v3 = joined[0]
    a3 = joined[1].filter('volume', 0.8)
    out = ffmpeg.output(v3, a3, r'E:\bigdata\ai\video\01-02.mp4')
    out.run()


#demo3()
