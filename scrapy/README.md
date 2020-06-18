
1. 创建项目 scrapy startproject tutorial

2. 在tutorial/spiders下创建爬虫

3. 在项目顶层运行 scrapy crawl quotes
https://doc.scrapy.org/en/latest/intro/tutorial.html
https://doc.scrapy.org/en/latest/topics/spiders.html

```
scrapy.cfg：配置文件

spiders：存放你Spider文件，也就是你爬取的py文件

items.py：相当于一个容器，和字典较像

middlewares.py：定义Downloader Middlewares(下载器中间件)和Spider Middlewares(蜘蛛中间件)的实现

pipelines.py:定义Item Pipeline的实现，实现数据的清洗，储存，验证。

settings.py：全局配置

```