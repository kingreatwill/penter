# import socket
#
# obj = socket.socket()
# obj.connect(('127.0.0.1', 8001))
#
# content = str(obj.recv(1024), encoding='utf-8')
# print(content)
#
# obj.close()
#
# import socket
#
# obj = socket.socket()
# obj.connect(('127.0.0.1', 8002))
#
# content = str(obj.recv(1024), encoding='utf-8')
# print(content)
#
# obj.close()

import socket

obj = socket.socket()
obj.connect(('127.0.0.1', 8001))

while True:
    inp = input('>>>')
    obj.sendall(bytes(inp, encoding='utf-8'))
    ret = str(obj.recv(1024),encoding='utf-8')
    print(ret)

obj.close()