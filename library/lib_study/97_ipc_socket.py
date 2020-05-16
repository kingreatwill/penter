import socket

print("--------------socket.create_connection(address[, timeout[, source_address]])")
print(
    "--------------socket.create_server(address, *, family=AF_INET, backlog=None, reuse_port=False, dualstack_ipv6=False)")
# addr = ("", 8080)  # all interfaces, port 8080
# if socket.has_dualstack_ipv6(): # 3.8 新版功能.
#     print("ip v6")
#     s = socket.create_server(addr, family=socket.AF_INET6, dualstack_ipv6=True)
# else:
#     print("ip v4")
#     s = socket.create_server(addr)

print(socket.getaddrinfo("baidu.com", 80, proto=socket.IPPROTO_TCP))
print(socket.gethostbyname("baidu.com"))
print(socket.gethostbyaddr("127.0.0.1"))

print(socket.gethostname())

print("-----------https://docs.python.org/zh-cn/3/library/socket.html#example")