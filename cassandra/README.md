# 安装Cassandra

http://cassandra.apache.org/download/

## Installation from RPM packages
- For the <release series> specify the major version number, without dot, and with an appended x.
- The latest <release series> is 311x.
- For older releases, the <release series> can be one of 30x, 22x, or 21x.
- (Not all versions of Apache Cassandra are available, since building RPMs is a recent addition to the project.)
- Add the Apache repository of Cassandra to /etc/yum.repos.d/cassandra.repo, for example for the latest 3.11 version:
```
[cassandra]
name=Apache Cassandra
baseurl=https://www.apache.org/dist/cassandra/redhat/311x/
gpgcheck=1
repo_gpgcheck=1
gpgkey=https://www.apache.org/dist/cassandra/KEYS
```
- Install Cassandra, accepting the gpg key import prompts:
```
sudo yum install cassandra
```
- Start Cassandra (will not start automatically):
```
service cassandra start
```
Systemd based distributions may require to run systemctl daemon-reload once to make Cassandra available as a systemd service. This should happen automatically by running the command above.

- Make Cassandra start automatically after reboot:
```
chkconfig cassandra on
```


## 网上教程

yum install https://www.apache.org/dist/cassandra/redhat/311x/cassandra-3.11.5-1.noarch.rpm

//设置文件夹权限
chown -R cassandra.cassandra /var/lib/cassandra/ 

//启动服务
service cassandra  start

chkconfig cassandra on

//看查看集群信息
nodetool status


##  使用密码登陆
//修改配置文件 authenticator 项
authenticator: AllowAllAuthenticator
改为 PasswordAuthenticator

//使用默认用户名和密码登陆
cqlsh -ucassandra -pcassandra

### 设置用户名和密码
// 创建新用户和密码
cassandra@cqlsh> CREATE USER ncc with PASSWORD '123456' SUPERUSER;
cassandra@cqlsh> quit

// 测试登陆
cqlsh -uncc -p123456


// 删除原来的默认账号
DROP USER cassandra ;
