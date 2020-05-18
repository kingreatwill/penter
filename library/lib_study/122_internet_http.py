# https://docs.python.org/zh-cn/3/library/http.html
"""
http.client 是一个低层级的 HTTP 协议客户端；对于高层级的 URL 访问请使用 urllib.request
    https://docs.python.org/zh-cn/3/library/http.client.html
http.server 包含基于 socketserver 的基本 HTTP 服务类
    https://docs.python.org/zh-cn/3/library/http.server.html
    不推荐在生产环境中使用 http.server 。它只实现了基本的安全检查功能。
http.cookies 包含一些有用来实现通过 cookies 进行状态管理的工具
     https://docs.python.org/zh-cn/3/library/http.cookies.html#module-http.cookies
http.cookiejar 提供了 cookies 的持久化
    https://docs.python.org/zh-cn/3/library/http.cookiejar.html#module-http.cookiejar
"""
from http import HTTPStatus

print(HTTPStatus.OK)

print(HTTPStatus.OK == 200)

print(HTTPStatus.OK.value)

print(HTTPStatus.OK.phrase)

print(HTTPStatus.OK.description)

print(len(list(HTTPStatus)))

for hs in HTTPStatus:
    print(hs.value, "    :", hs.phrase)
#  (例如 http.HTTPStatus.OK 也可以是 http.client.OK)
# 3.8 新版功能: 添加了 451 UNAVAILABLE_FOR_LEGAL_REASONS 状态码。

"""

"""