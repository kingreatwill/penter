import paramiko


def ssh_command(ip, port, username, password, command):
    # 创建SSH对象
    client = paramiko.SSHClient()
    # 允许连接不在know_hosts文件中的主机
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # 连接服务器
    client.connect(ip, port, username, password)
    # 直接使用SSHClient对象的exec_command()在服务端执行命令
    stdin, stdout, stderr = client.exec_command(command)
    receive = stdout.read()
    # 打印输出
    print(receive.decode('utf-8'))
    # 关闭连接
    client.close()


ssh_command('192.168.1.175', 22, 'root', '远程主机登陆密码', 'ls')
