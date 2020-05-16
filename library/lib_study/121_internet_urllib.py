"""
urllib.request 打开和读取 URL
urllib.error 包含 urllib.request 抛出的异常
urllib.parse 用于解析 URL
urllib.robotparser 用于解析 robots.txt 文件
"""

import urllib.request

request = urllib.request.Request("https://docs.python.org/zh-cn/3/library/urllib.request.html")  # , headers=header
response = urllib.request.urlopen(request)
print(request.data)
print(request.type)
print(request.host)

print(response.getcode())
print(response.geturl())
print(response.info())
# 二进制内容 response.read()

import urllib.request

with urllib.request.urlopen('http://www.python.org/') as f:
    print(f.read(30))
    print(f.read(10).decode('utf-8'))


# import urllib.request
# # Create an OpenerDirector with support for Basic HTTP Authentication...
# auth_handler = urllib.request.HTTPBasicAuthHandler()
# auth_handler.add_password(realm='PDQ Application',
#                           uri='https://mahler:8092/site-updates.py',
#                           user='klem',
#                           passwd='kadidd!ehopper')
# opener = urllib.request.build_opener(auth_handler)
# # ...and install it globally so it can be used with urlopen.
# urllib.request.install_opener(opener)
# urllib.request.urlopen('http://www.example.com/login.html')


# import urllib.request
# req = urllib.request.Request('http://www.example.com/')
# req.add_header('Referer', 'http://www.python.org/')
# # Customize the default User-Agent header value:
# req.add_header('User-Agent', 'urllib-example/0.1 (Contact: . . .)')
# r = urllib.request.urlopen(req)

# import urllib.request
# opener = urllib.request.build_opener()
# opener.addheaders = [('User-agent', 'Mozilla/5.0')]
# opener.open('http://www.baidu.com/')

import urllib.request
import urllib.parse
params = urllib.parse.urlencode({'spam': 1, 'eggs': 2, 'bacon': 0})
url = "http://www.musi-cal.com/cgi-bin/query?%s" % params
print(url)
# with urllib.request.urlopen(url) as f:
#     print(f.read().decode('utf-8'))

"""
The following example uses the POST method instead. Note that params output from urlencode is encoded to bytes before it is sent to urlopen as data:

>>>
import urllib.request
import urllib.parse
data = urllib.parse.urlencode({'spam': 1, 'eggs': 2, 'bacon': 0})
data = data.encode('ascii')
with urllib.request.urlopen("http://requestb.in/xrbl82xr", data) as f:
    print(f.read().decode('utf-8'))

The following example uses an explicitly specified HTTP proxy, overriding environment settings:

>>>
import urllib.request
proxies = {'http': 'http://proxy.example.com:8080/'}
opener = urllib.request.FancyURLopener(proxies)
with opener.open("http://www.python.org") as f:
    f.read().decode('utf-8')

The following example uses no proxies at all, overriding environment settings:

>>>
import urllib.request
opener = urllib.request.FancyURLopener({})
with opener.open("http://www.python.org/") as f:
    f.read().decode('utf-8')

"""

print("---------")
import urllib.request
local_filename, headers = urllib.request.urlretrieve('http://python.org/')
print(local_filename)
html = open(local_filename)
html.close()