# pip install bs4
"""
BeautifulSoup4和 lxml 一样，Beautiful Soup 也是一个HTML/XML的解析器，主要的功能也是如何解析和提取 HTML/XML 数据。

BeautifulSoup支持Python标准库中的HTML解析器,还支持一些第三方的解析器，如果我们不安装它，则 Python 会使用 Python默认的解析器，lxml 解析器更加强大，速度更快，推荐使用lxml 解析器。

Beautiful Soup自动将输入文档转换为Unicode编码，输出文档转换为utf-8编码。你不需要考虑编码方式，除非文档没有指定一个编码方式，这时，Beautiful Soup就不能自动识别编码方式了。然后，你仅仅需要说明一下原始编码方式就可以了。s
"""
# https://pypi.org/project/beautifulsoup4/
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/

from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML","lxml")
# 标准库 BeautifulSoup("<p>Some<b>bad<i>HTML","html.parser")
# BeautifulSoup("<p>Some<b>bad<i>HTML","lxml-xml")
# BeautifulSoup("<p>Some<b>bad<i>HTML","html5lib")
print(soup.prettify())