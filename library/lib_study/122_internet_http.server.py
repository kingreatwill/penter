# HTTPServer 是 socketserver.TCPServer 的一个子类
# python -m http.server --cgi 8000
# python -m http.server --directory /tmp/
# python -m http.server 8000 --bind 127.0.0.1
# python -m http.server 8000
import http.server

#class http.server.SimpleHTTPRequestHandler(request, client_address, server, directory=None)
def run(server_class=http.server.HTTPServer, handler_class=http.server.BaseHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

run()

