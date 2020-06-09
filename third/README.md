# python 简单整理常用的第三方库
pip install -U git+https://github.com/madmaze/pytesseract.git
git clone https://github.com/madmaze/pytesseract.git
cd pytesseract && pip install -U .
pip3 install face_recognition -i  http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com

pip install -r requirements.txt

## 图片处理 PIL (Python Image Library)
PIL http://pythonware.com/products/pil/
### Pillow
PIL（Python Imaging Library）是Python中一个强大的图像处理库，但目前其只支持到Python2.7
pillow是PIL的一个分支，虽是分支但是其与PIL同样也具有很强的图像处理库。

https://github.com/python-pillow/Pillow
https://pillow.readthedocs.io/en/stable/handbook/tutorial.html
### OpenCV-Python
pip install opencv-python

### 人脸识别

avatarify AI 实时变脸工具 https://github.com/alievk/avatarify

https://ai.arcsoft.com.cn/manual/docs#/89
https://www.zhihu.com/question/19561362
人脸检测-》检测人脸位置，锁定人脸坐标
人脸跟踪-》精确定位并跟踪面部区域位置
人脸比对-》比较两张人脸的相似度
人脸查找-》在人脸库中查找相似的人脸
人脸属性-》检测人脸性别、年龄、情绪等属性
活体检测-》检测是否真人，预防恶意攻击

场景：
智能楼宇-》人脸闸机、门禁、门锁
智慧零售-》人脸会员机制、人脸支付
智慧教育-》人脸考勤、人证考场验证等
智能机器人-》人脸迎宾、人脸个性化服务
智慧旅游-》人脸闸机、人脸购票、验票
智慧金融-》远程人脸开户、刷脸取款
车牌等识别
货架商品识别与管理

智能安防  智慧城市 智慧工地 智慧电力 智慧工厂 智慧城管 智慧油田  智慧校园 智慧交通 智慧家园
视频告警
视频诊断
视频运维
安全帽识别（口罩）
烟火检测


别墅 家庭防止小偷
重点的街道、路口进行违章摆摊、违停进行检测，公共设施防被盗
海上漂浮物监测、人群聚集，跟随
玩手机检测
公路违停 逆行等
危险区域，周界入侵报警
高速公路团雾告警
睡岗离岗检测
定时间未检修告警
违规载人检测
重点车辆监控
交通信号优化
智能信号灯（根据车流量）
交通事件感知



dlib也有自己的图片标注工具


标注工具labelimg和labelme

矩形标注工具：labelimg
多边形标准工具：labelme


前者官网发布了可执行文件，后者只有python源码，如果需要编译windows exe，可以这样：
pip install labelme

然后运行labelme确保程序可以正常执行

下载源码：

cd  D:\github\wkentaro\labelme-3.16.7

pip install .

pip install pyinstaller

pyinstaller labelme.spec


### 开源
https://github.com/davidsandberg/facenet
https://github.com/ageitgey/face_recognition
https://github.com/cmusatyalab/openface

https://github.com/ChanChiChoi/awesome-Face_Recognition

## http
Requests

## 爬虫
Scrapy
BeautifulSoup

xml解析器有标准库
第三方的lxml，html5lib


## orm
sqlalchemy 如果用Flask可以用这个.
支持了异步https://pypi.org/project/async-sqlalchemy
django自带的ORM
tornado可以试试peewee 星最多


## web
https://www.cnblogs.com/wongbingming/p/11002978.html
https://www.runoob.com/python3/python-uwsgi.html
这个协议旨在解决众多 web 框架和web server软件的兼容问题。
有了WSGI，你不用再因为你使用的web 框架而去选择特定的 web server软件。
常见的web应用框架有：Django，Flask等
常用的web服务器软件有：uWSGI，Gunicorn等

WSGI 对于 application 对象有如下三点要求
必须是一个可调用的对象
接收两个必选参数environ、start_response。
返回值必须是可迭代对象，用来表示http body。

https://stxnext.com/blog/2019/05/31/flask-vs-django-comparison/
### Django

### Flask
https://github.com/pallets/flask
### Tornado
https://github.com/tornadoweb/tornado


## test
### 标准库-test,unittest,doctest
### 第三方：pytest,nose2

## 数据科学
matplotlib.一个绘制数据图的库。对于数据科学家或分析师非常有用。
NumPy.它为Python提供了很多高级的数学方法。
SciPy.这是一个Python的算法和数学工具库，它的功能把很多科学家从Ruby吸引到了Python。
pandas.Pandas是一个强大的分析结构化数据的工具集；它的使用基础是Numpy（提供高性能的矩阵运算）；用于数据挖掘和数据分析，同时也提供数据清洗功能。
nltk.自然语言工具包。我知道大多数人不会用它，但它通用性非常高。如果你需要处理字符串的话，它是非常好的库。



## 其它
### GUI
不介绍，可以看官网，里面也有推荐
### 游戏引擎
Pygame
Pyglet.3D动画和游戏开发引擎