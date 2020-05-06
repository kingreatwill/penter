"""
平常我们功能测试用例非常多时，比如有1千条用例，假设每个用例执行需要1分钟，如果单个测试人员执行需要1000分钟才能跑完
当项目非常紧急时，会需要协调多个测试资源来把任务分成两部分，于是执行时间缩短一半，如果有10个小伙伴，那么执行时间就会变成十分之一，大大节省了测试时间
为了节省项目测试时间，10个测试同时并行测试，这就是一种分布式场景
同样道理，当我们自动化测试用例排常多的时候， 一条条按顺序执行会非常慢，pytest-xdist的出现就是为了让自动化测试用例可以分布式执行，从而节省自动化测试时间
pytest-xdist是属于进程级别的并发

原则
用例之间是独立的，用例之间没有依赖关系，用例可以完全独立运行【独立运行】
用例执行没有顺序，随机顺序都能正常执行【随机执行】
每个用例都能重复运行，运行结果不会影响其他用例【不影响其他用例】


测试运行并行化：如果有多个CPU或主机，则可以将它们用于组合的测试运行。 这样可以加快开发速度或使用远程计算机的特殊资源。
--looponfail：在子进程中重复运行测试。 每次运行之后，pytest都会等到项目中的文件更改后再运行之前失败的测试。 重复此过程，直到所有测试通过，然后再次执行完整运行。
跨平台覆盖：您可以指定不同的Python解释程序或不同的平台，并在所有这些平台上并行运行测试。

pip3 install pytest-xdist -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com

pytest -s -n auto
# -n auto：可以自动检测到系统的CPU核数；从测试结果来看，检测到的是逻辑处理器的数量，即假12核
pytest -s -n 2
# 可以指定需要多少个CPU来跑用例

pytest -s -n auto --html=report.html --self-contained-html

#  pytest-xdist默认是无序执行的，可以通过 --dist 参数来控制顺序

--dist=loadscope
将按照同一个模块module下的函数和同一个测试类class下的方法来分组，然后将每个测试组发给可以执行的worker，确保同一个组的测试用例在同一个进程中执行
目前无法自定义分组，按类class分组优先于按模块module分组

 --dist=loadfile
 按照同一个文件名来分组，然后将每个测试组发给可以执行的worker，确保同一个组的测试用例在同一个进程中执行



 pytest-xdist是让每个worker进程执行属于自己的测试用例集下的所有测试用例,这意味着在不同进程中，不同的测试用例可能会调用同一个scope范围级别较高（例如session）的fixture，该fixture则会被执行多次，这不符合scope=session的预期

如何解决了？虽然pytest-xdist没有内置的支持来确保会话范围的夹具仅执行一次，但是可以通过使用锁定文件进行进程间通信来实现。




pytest-xdist分布式测试的原理

xdist会产生一个或多个workers，workers都通过master来控制
每个worker负责执行完整的测试用例集，然后按照master的要求运行测试，而master机不执行测试任务

--dist-mode选项

each：master将完整的测试索引列表分发到每个worker

load：master将大约25%的测试用例以轮询的方式分发到各个worker，剩余的测试用例则会等待workers执行完测试用例以后再分发

可以使用  pytest_xdist_make_scheduler  这个hook来实现自定义测试分发逻辑。

分布式：https://codespeak.net/execnet/example/test_info.html
https://github.com/pytest-dev/pytest-xdist
"""

import pytest
from filelock import FileLock



# import execnet, os
# gw = execnet.makegateway()
# ch = gw.remote_exec("import os; channel.send(os.getcwd())")
# res = ch.receive()
# assert res == os.getcwd()


@pytest.fixture(scope="session")
def login():
    print("====登录功能，返回账号，token===")
    with FileLock("session.lock"):
        name = "testyy"
        token = "npoi213bn4"
        # web ui自动化
        # 声明一个driver，再返回

        # 接口自动化
        # 发起一个登录请求，将token返回都可以这样写

    yield name, token
    print("====退出登录！！！====")