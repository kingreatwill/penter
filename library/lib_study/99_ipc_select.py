"""
select --- 等待 I/O 完成
该模块提供了对 select() 和 poll() 函数的访问，这些函数在大多数操作系统中是可用的。
在 Solaris 及其衍生版本上可用 devpoll()，在 Linux 2.5+ 上可用 epoll()，在大多数 BSD 上可用 kqueue()。
注意，在 Windows 上，本模块仅适用于套接字；在其他操作系统上，本模块也适用于其他文件类型（特别地，在 Unix 上也适用于管道）。
本模块不能用于常规文件，不能检测出（自上次读取文件后）文件是否有新数据写入。
"""
#https://www.jianshu.com/p/e26594304e11

# 非阻塞式I/O编程
# import socket
# import select
#
# sk1 = socket.socket()
# sk1.bind(('0.0.0.0', 8001))
# sk1.listen()
#
# sk2 = socket.socket()
# sk2.bind(('0.0.0.0', 8002))
# sk2.listen()
#
# sk3 = socket.socket()
# sk3.bind(('0.0.0.0', 8003))
# sk3.listen()
#
# inputs = [sk1, sk2, sk3, ]
#
# while True:
#     r_list, w_list, e_list = select.select(inputs,[],inputs,1)
#     for sk in r_list:
#         # conn表示每一个连接对象
#         conn, address = sk.accept()
#         conn.sendall(bytes('hello', encoding='utf-8'))
#         conn.close()
#
#     for sk in e_list:
#         inputs.remove(sk)


# 示例2：IO多路复用--使用socket模拟多线程，并实现读写分离
#使用socket模拟多线程，使多用户可以同时连接
import socket
import select

sk1 = socket.socket()
sk1.bind(('0.0.0.0', 8001))
sk1.listen()

inputs = [sk1, ]
outputs = []
message_dict = {}

while True:
    r_list, w_list, e_list = select.select(inputs, outputs, inputs, 1)
    print('正在监听的socket对象%d' % len(inputs))
    print(r_list)
    for sk1_or_conn in r_list:
        #每一个连接对象
        if sk1_or_conn == sk1:
            # 表示有新用户来连接
            conn, address = sk1_or_conn.accept()
            inputs.append(conn)
            message_dict[conn] = []
        else:
            # 有老用户发消息了
            try:
                data_bytes = sk1_or_conn.recv(1024)
            except Exception as ex:
                # 如果用户终止连接
                inputs.remove(sk1_or_conn)
            else:
                data_str = str(data_bytes, encoding='utf-8')
                message_dict[sk1_or_conn].append(data_str)
                outputs.append(sk1_or_conn)

    #w_list中仅仅保存了谁给我发过消息
    for conn in w_list:
        recv_str = message_dict[conn][0]
        del message_dict[conn][0]
        conn.sendall(bytes(recv_str+'好', encoding='utf-8'))
        outputs.remove(conn)

    for sk in e_list:

        inputs.remove(sk)