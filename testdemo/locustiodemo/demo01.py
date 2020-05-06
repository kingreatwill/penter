"""
pip3 install -e git://github.com/locustio/locust.git@master#egg=locustio

pip install locustio
https://docs.locust.io/en/stable/
安装pyzmq：python3 -m pip install pyzmq(如果是以分布式队列运行locust,需要装一种通信队列的库pyzmq)

locust -f demo01.py
# http://localhost:8089/
https://www.jianshu.com/p/cee352e8b565
locust -f test1.py --host=https://www.baidu.com --no-web -c 10 -r 2 -t 1m

-c 设置虚拟用户数
-r 设置每秒启动虚拟用户数
-t 设置设置运行时间

Locust分布式进行性能测试 https://blog.csdn.net/zhengshaolong8125/article/details/78111999
locust -f locustfile.py --master
locust -f locustfile.py --slave --master-host=192.168.0.14

--expect-slaves=X
如果在没有Web UI的情况下运行Locust，在启动主节点时加上--expect-slaves指定选项，以指定预期连接的从节点数。然后，在开始测试之前，将等待这些从属节点连接。
"""
from locust import HttpLocust, TaskSet, task

class UserBehavior(TaskSet):
    @task
    def baidu(self):
        self.client.get("/")

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait=1000
    max_wait=2000
    host="https://www.baidu.com"