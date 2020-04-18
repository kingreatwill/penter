import pytest

# 前面讲的，其实都是setup的操作，那么现在就来讲下teardown是怎么实现的
# 用fixture实现teardown并不是一个独立的函数，而是用 yield 关键字来开启teardown操作

# yield注意事项
# 如果yield前面的代码，即setup部分已经抛出异常了，则不会执行yield后面的teardown内容
# 如果测试用例抛出异常，yield后面的teardown内容还是会正常执行

"""
# 官方例子
@pytest.fixture(scope="module")
def smtp_connection():
    with smtplib.SMTP("smtp.gmail.com", 587, timeout=5) as smtp_connection:
        yield smtp_connection  # provide the fixture value

该 smtp_connection 连接将测试完成执行后已经关闭，因为 smtp_connection 对象自动关闭时， with 语句结束。
"""

@pytest.fixture(scope="session")
def open():
    # 会话前置操作setup
    print("===打开浏览器===")
    test = "测试变量是否返回"
    yield test
    # 会话后置操作teardown
    print("==关闭浏览器==")


@pytest.fixture
def login(open):
    # 方法级别前置操作setup
    print(f"输入账号，密码先登录{open}")
    name = "==我是账号=="
    pwd = "==我是密码=="
    age = "==我是年龄=="
    # 返回变量
    yield name, pwd, age
    # 方法级别后置操作teardown
    print("登录成功")


def test_s1(login):
    print("==用例1==")
    # 返回的是一个元组
    print(login)
    # 分别赋值给不同变量
    name, pwd, age = login
    print(name, pwd, age)
    assert "账号" in name
    assert "密码" in pwd
    assert "年龄" in age


def test_s2(login):
    print("==用例2==")
    print(login)


# addfinalizer终结函数 和yield相似
@pytest.fixture(scope="module")
def mytest_addfinalizer(request):
    # 前置操作setup
    print("==再次打开浏览器==")
    test = "test_addfinalizer"

    def fin():
        # 后置操作teardown
        print("==再次关闭浏览器==")

    request.addfinalizer(fin)
    # 返回前置操作的变量
    return test


def test_anthor(mytest_addfinalizer):
    print("==最新用例==", mytest_addfinalizer)