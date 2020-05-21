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