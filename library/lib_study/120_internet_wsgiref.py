# Web服务器网关接口（Python Web Server Gateway Interface，缩写为WSGI）
# 是为Python语言定义的Web服务器和Web应用程序或框架之间的一种简单而通用的接口。
# WSGI 没有官方的实现, 因为WSGI更像一个协议. 只要遵照这些协议,WSGI应用(Application)都可以在任何服务器(Server)上运行, 反之亦然。
# https://www.python.org/dev/peps/pep-3333/
# https://docs.python.org/zh-cn/3/library/wsgiref.html
# 如：Django ，Flask 这两个最知名
# WSGI是基于现存的CGI标准而设计的
# 类似于Java中的"servlet" API

from wsgiref.util import setup_testing_defaults
from wsgiref.simple_server import make_server

# A relatively simple WSGI application. It's going to print out the
# environment dictionary after being updated by setup_testing_defaults
def simple_app(environ, start_response):
    setup_testing_defaults(environ)

    status = '200 OK'
    headers = [('Content-type', 'text/plain; charset=utf-8')]

    start_response(status, headers)

    ret = [("%s: %s\n" % (key, value)).encode("utf-8")
           for key, value in environ.items()]
    return ret

with make_server('', 8000, simple_app) as httpd:
    print("Serving on port 8000...")
    httpd.serve_forever()


# import sys
# import os
# import mimetypes
# from wsgiref import simple_server, util
#
# def app(environ, respond):
#
#     fn = os.path.join(path, environ['PATH_INFO'][1:])
#     if '.' not in fn.split(os.path.sep)[-1]:
#         fn = os.path.join(fn, 'index.html')
#     type = mimetypes.guess_type(fn)[0]
#
#     if os.path.exists(fn):
#         respond('200 OK', [('Content-Type', type)])
#         return util.FileWrapper(open(fn, "rb"))
#     else:
#         respond('404 Not Found', [('Content-Type', 'text/plain')])
#         return [b'not found']
#
# if __name__ == '__main__':
#     path = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
#     port = int(sys.argv[2]) if len(sys.argv) > 2 else 8000
#     httpd = simple_server.make_server('', port, app)
#     print("Serving {} on port {}, control-C to stop".format(path, port))
#     try:
#         httpd.serve_forever()
#     except KeyboardInterrupt:
#         print("Shutting down.")
#         httpd.server_close()

