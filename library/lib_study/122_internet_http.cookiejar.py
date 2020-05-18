import http.cookiejar, urllib.request

"""
CookieJar：管理HTTP cookie值、存储HTTP请求生成的cookie、向传出的HTTP请求添加cookie的对象。整个cookie都存储在内存中，对CookieJar实例进行垃圾回收后cookie也将丢失。

FileCookieJar (filename,delayload=None,policy=None)：从CookieJar派生而来，用来创建FileCookieJar实例，检索cookie信息并将cookie存储到文件中。
filename是存储cookie的文件名。delayload为True时支持延迟访问访问文件，即只有在需要时才读取文件或在文件中存储数据。

MozillaCookieJar (filename,delayload=None,policy=None)：从FileCookieJar派生而来，创建与Mozilla浏览器 cookies.txt兼容的FileCookieJar实例。

LWPCookieJar (filename,delayload=None,policy=None)：从FileCookieJar派生而来，创建与libwww-perl标准的 Set-Cookie3 文件格式兼容的FileCookieJar实例。
"""
# 获取cookie
if __name__ == '__main__':
    url = 'http://www.baidu.com/'
    headers = {
        'User-Agent': 'Mozilla/5.0(Windows NT 10.0; WOW64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.3427.400 QQBrowser/9.6.12513.400'
    }

    cookie = http.cookiejar.CookieJar()
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    resp = opener.open(url)

    cookieStr = ''
    for item in cookie:
        cookieStr = cookieStr + item.name + '=' + item.value + ';'
    print(cookieStr)

#获取网站的cookie并保存cookie到文件中
import urllib.request
from http import cookiejar


def save_cookie(url, cookie_filename):
    cookie = cookiejar.MozillaCookieJar(cookie_filename)
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    resp = opener.open(url)
    cookieStr = ''
    for item in cookie:
        cookieStr = cookieStr + item.name + '=' + item.value + ';'
    print(cookieStr)
    cookie.save()


if __name__ == '__main__':
    url = 'http://www.baidu.com/'
    headers = {
        'User-Agent': 'Mozilla/5.0(Windows NT 10.0; WOW64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.3427.400 QQBrowser/9.6.12513.400'
    }
    cookie_filename = 'cookie.txt'
    req = urllib.request.Request(url, headers=headers)
    save_cookie(req, cookie_filename)

# 获取文件中的cookie访问链接

import urllib.request
from http import cookiejar


def load_cookie(url, cookie_filename):
    cookie = cookiejar.MozillaCookieJar()
    cookie.load(cookie_filename)
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    resp = opener.open(req)
    cookieStr = ''
    for item in cookie:
        cookieStr = cookieStr + item.name + '=' + item.value + ';'
    print(cookieStr)


if __name__ == '__main__':
    url = 'http://www.baidu.com/'
    headers = {
        'User-Agent': 'Mozilla/5.0(Windows NT 10.0; WOW64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.3427.400 QQBrowser/9.6.12513.400'
    }
    cookie_filename = 'cookie.txt'
    req = urllib.request.Request(url, headers=headers)
    load_cookie(req, cookie_filename)


# 使用cookiejar和post用户名和密码模拟人人网用户登入
import urllib.request
import urllib.parse
from http import cookiejar

if __name__ == '__main__':
    # 人人网的很早的登入网站（最新的登入网站做了校验机制，现在不好登入...）
    url = 'http://www.renren.com/PLogin.do'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36'}
    # post的data数据，email是用户名，password是密码，这个是登入网站的input标签的name属性值
    data = {'email': 'xxxxxxxxx', 'password': 'xxxxxxx'}
    # 转成url编码
    data = urllib.parse.urlencode(data).encode('utf-8')
    # 保存cookie的文件名称
    cookie_filename = 'renren_cookie.txt'
    # 获取cookie对象
    cookie = cookiejar.MozillaCookieJar(cookie_filename)
    # 构建一个cookie的处理器
    handler = urllib.request.HTTPCookieProcessor(cookie)
    # 获取一个opener对象
    opener = urllib.request.build_opener(handler)
    # 获取一个请求对象
    req = urllib.request.Request(url, data)
    # 给opener添加请求头，使用的是元组的方式
    opener.addheaders = [('User-Agent',
                          'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36')]
    # 请求服务器，返回响应对象，这时cookie已经随着resp对象携带过来了
    resp = opener.open(req)
    # 保存cookie到文件
    cookie.save()
    # 将响应的内容写入到文件
    with open('renren_login.html', 'wb')as f:
        f.write(resp.read())


#
# cj = http.cookiejar.CookieJar()
# opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
# r = opener.open("http://python.org/")
#
# print(r)
#
# import os, http.cookiejar, urllib.request
#
# cj = http.cookiejar.MozillaCookieJar()
# cj.load(os.path.join(os.path.expanduser("~"), ".netscape", "cookies.txt"))
# opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
# r = opener.open("http://python.org/")
# print(r)
#
# import urllib.request
# from http.cookiejar import CookieJar, DefaultCookiePolicy
#
# policy = DefaultCookiePolicy(
#     rfc2965=True, strict_ns_domain=DefaultCookiePolicy.DomainStrict,
#     blocked_domains=["ads.net", ".ads.net"])
# cj = CookieJar(policy)
# opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
# r = opener.open("http://example.com/")
