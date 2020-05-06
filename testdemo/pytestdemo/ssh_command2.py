import paramiko


def ssh_command(ip, port, username, password, command):
    # 创建SSH对象
    client = paramiko.SSHClient()
    # 允许连接不在know_hosts文件中的主机
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # 连接服务器
    client.connect(ip, port, username, password)
    # 将SSHClient建立连接的对象得到一个Transport对象，
    # 以Transport对象的exec_command()在服务端执行命令
    ssh_session = client.get_transport().open_session()
    if ssh_session.active:
        ssh_session.exec_command(command)
        receive = ssh_session.recv(1024)
        print(receive.decode('utf-8'))
    # 关闭连接
    client.close()


ssh_command('192.168.1.175', 22, 'root', '远程主机登陆密码', 'ls')