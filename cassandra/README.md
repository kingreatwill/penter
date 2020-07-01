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

DESCRIBE keyspaces;
describe tables;
describe table users;
CREATE KEYSPACE excelsior2  WITH replication = {'class': 'SimpleStrategy', 'replication_factor' : 3};
CREATE KEYSPACE excalibur
    WITH replication = {'class': 'NetworkTopologyStrategy', 'DC1' : 1, 'DC2' : 3}
    AND durable_writes = false;
    
SELECT * FROM system.schema_keyspaces;


CREATE TABLE sample_times (a int, b timestamp, c timeuuid, d bigint, PRIMARY KEY (a,b,c,d));
INSERT INTO sample_times (a,b,c,d) VALUES (1, toUnixTimestamp(now()), 50554d6e-29bb-11e5-b345-feff819cdc9f, toTimestamp(now()));

INSERT INTO sample_times (a,b,c,d) VALUES (2, toUnixTimestamp(now()), now(), toTimestamp(now()));

SELECT a, b, toDate(c), toDate(d) FROM sample_times



CREATE TABLE user_articles (
    user_id uuid,
    uploaded_date timestamp,
    article_id uuid,
    title test,
    abstract test,
    PRIMARY KEY (user_id, uploaded_date, article_id)
) WITH CLUSTERING ORDER BY (uploaded_date DESC, article_id ASC);

SELECT *
FROM user_articles
WHERE user_id = 12345
ORDER BY uploaded_date DESC;


Apache Cassandra 各种 key 介绍:https://zhuanlan.zhihu.com/p/64898337
"""
CREATE TABLE cc.cc_customers (
    id text PRIMARY KEY,
    county text,
    name text
);

CREATE TABLE cc.cc_transactions (
    customerid text,
    year int,
    month int,
    id timeuuid,
    amount int,
    card text,
    status text,
    PRIMARY KEY ((customerid, year, month), id)
);
CREATE TABLE cc.cc_balance (
    customerid text,
    card text,
    balance int,
    updated_at timestamp,
    PRIMARY KEY ((customerid, card))
);

/* 1*/    val includedStatuses = Set("COMPLETED", "REPAID")
/* 2*/    val now = new Date();
/* 3*/    sc.cassandraTable("cc", "cc_transactions")
/* 4*/      .select("customerid", "amount", "card", "status", "id")
/* 5*/      .where("id < minTimeuuid(?)", now)
/* 6*/      .filter(includedStatuses contains _.getString("status"))
/* 7*/      .keyBy(row => (row.getString("customerid"), row.getString("card")))
/* 8*/      .map { case (key, value) => (key, value.getInt("amount")) }
/* 9*/      .reduceByKey(_ + _)
/*10*/      .map { case ((customerid, card), balance) => (customerid, card, balance, now) }
/*11*/      .saveToCassandra("cc", "cc_balance", SomeColumns("customerid", "card", "balance", "updated_at"))
"""

