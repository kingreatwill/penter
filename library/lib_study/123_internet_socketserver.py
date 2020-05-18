"""
https://docs.python.org/zh-cn/3/library/socketserver.html

+------------+
| BaseServer |
+------------+
      |
      v
+-----------+        +------------------+
| TCPServer |------->| UnixStreamServer |
+-----------+        +------------------+
      |
      v
+-----------+        +--------------------+
| UDPServer |------->| UnixDatagramServer |
+-----------+        +--------------------+
class socketserver.BaseServer(server_address, RequestHandlerClass)
class socketserver.TCPServer(server_address, RequestHandlerClass, bind_and_activate=True)
class socketserver.UDPServer(server_address, RequestHandlerClass, bind_and_activate=True)
class socketserver.UnixStreamServer(server_address, RequestHandlerClass, bind_and_activate=True)
class socketserver.UnixDatagramServer(server_address, RequestHandlerClass, bind_and_activate=True)

class socketserver.ForkingTCPServer
class socketserver.ForkingUDPServer
class socketserver.ThreadingTCPServer
class socketserver.ThreadingUDPServer
"""
# https://docs.python.org/zh-cn/3/library/socketserver.html#socketserver-udpserver-example
# https://docs.python.org/zh-cn/3/library/socketserver.html#asynchronous-mixins
import socketserver


class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        # just send back the same data, but upper-cased
        self.request.sendall(self.data.upper())


if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()




class MyTCPHandler(socketserver.StreamRequestHandler):

    def handle(self):
        # self.rfile is a file-like object created by the handler;
        # we can now use e.g. readline() instead of raw recv() calls
        self.data = self.rfile.readline().strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        # Likewise, self.wfile is a file-like object used to write back
        # to the client
        self.wfile.write(self.data.upper())