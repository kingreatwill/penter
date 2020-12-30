[Selenium系列](https://www.cnblogs.com/poloyy/category/1680176.html)

在Linux中使用selenium（环境部署）
1、安装chrome
用下面的命令安装Google Chrome
yum install https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm
也可以先下载至本地，然后安装
wget https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm
yum install ./google-chrome-stable_current_x86_64.rpm
 
安装必要的库
yum install mesa-libOSMesa-devel gnu-free-sans-fonts wqy-zenhei-fonts
 
2、安装 chromedriver（末尾附chrome和chromedriver的对应版本）
chrome官网
wget https://chromedriver.storage.googleapis.com/2.38/chromedriver_linux64.zip
淘宝源（推荐）
wget http://npm.taobao.org/mirrors/chromedriver/2.41/chromedriver_linux64.zip
 
将下载的文件解压，放在如下位置
unzip chromedriver_linux64.zip
mv chromedriver /usr/bin/
给予执行权限
chmod +x /usr/bin/chromedriver
 
3、运行代码，查看是否成功（python下）
from selenium import webdriver
driver = webdriver.Chrome()