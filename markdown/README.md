# Markdown to HTML
https://github.com/Python-Markdown/markdown  2.2k
## HTML to Markdown
https://github.com/gaojiuli/tomd   0.466k 最近更新一年前
https://github.com/aaronsw/html2text 2k 好像8年没有更新了

```

python html2md_selenium.py "https://www.toutiao.com/i6827512913318642187/" "https://segmentfault.com/a/1190000022777293"
python html2md_selenium.py "https://www.cnblogs.com/kingreatwill/p/9865945.html" -n filename
python html2md_selenium.py "https://www.cnblogs.com/kingreatwill/p/9865945.html" -s ".css"


python html2md.py "https://www.cnblogs.com/kingreatwill/p/9865945.html"
python html2md.py "https://blog.csdn.net/weixin_33737134/article/details/91773164" -c s
python html2md.py "https://blog.csdn.net/weixin_33737134/article/details/91773164" -c p -less
python html2md.py "https://www.toutiao.com/i6827512913318642187/" -c p 

python html2md.py filename
type filename | python html2md.py
cat filename | python html2md.py

curl -o- https://www.cnblogs.com/kingreatwill/p/9865945.html | python html2md.py


html2md https://www.cnblogs.com/kingreatwill/p/9865945.html
```
打包成exe:pyinstaller -F html2md.py

-F, –onefile 打包dao成一个exe文件。
-D, –onedir 创建一个目录，包含exe文件，但会依赖很多文件（默认回选项）。
-c, –console, –nowindowed 使用控制台，无界面(默认)
-w, –windowed, –noconsole 使用窗答口，无控制台

[WebDriver被识别反爬虫解决办法(Chrome正受到自动化测试软件的控制)](https://blog.csdn.net/weixin_43870646/article/details/105418801)

WebDriver识别原理
     网页只要设置了检查webdriver的Javascript方法，就很容易发现爬虫。使用的方法就是Navigator对象的webdriver属性，用这个属性来判断客户端是否通过WebDriver驱动浏览器。
如果监测到客户端的webdriver属性存在，则无法继续操作获取数据。selenium，Puppeteer都存在WebDriver属性。
```
window.navigator.webdriver
undefined
```

WebDriver识别的绕过方法
     了解了WebDriver识别的原理和返回值后，我们就能相处应对的办法。既然web Driver的识别依赖navigation.webdriver的返回值，那么我们在触发Javascript办法前将navigation.webdriver的返回值改为false或者undefind，问题就解决了。
```
script = 'Object.defineProperty(navigator,"webdriver",{get:() => false,});'
```

```
from selenium.webdriver import Chrome
import time

brower = Chrome(executable_path=r'D:\python\chromedriver_win32\chromedriver.exe')
url = 'http://www.porters.vip/features/webdriver.html'
brower.get(url)
script = 'Object.defineProperty(navigator,"webdriver",{get:() => false,});'
#运行Javascript
brower.execute_script(script)
#定位按钮并点击
brower.find_element_by_css_selector('.btn.btn-primary.btn-lg').click()
#定位到文章内容元素
elements = brower.find_element_by_css_selector('#content')
time.sleep(1)
print(elements.text)
brower.close()
```
这种修改该属性值的办法只在当前页面有效，当浏览器打开新标签或新窗口时需要重新执行改变navigator.webdriver值的JavaScript代码。