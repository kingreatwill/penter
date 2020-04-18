
"""
pytest会默认读取conftest.py里面的所有fixture
conftest.py 文件名称是固定的，不能改动
conftest.py只对同一个package下的所有测试用例生效
不同目录可以有自己的conftest.py，一个项目中可以有多个conftest.py
测试用例文件中不需要手动import conftest.py，pytest会自动查找
"""
# 最顶层的conftest，一般写全局的fixture，在Web UI自动化中，可能会初始化driver

import pytest

@pytest.fixture(scope="session")
def login():
    print("====登录功能，返回账号，token===")
    name = "testyy"
    token = "npoi213bn4"
    yield name, token
    print("====退出登录！！！====")


@pytest.fixture(autouse=True)
def get_info(login):
    name, token = login
    print(f"== 每个用例都调用的外层fixture：打印用户token： {token} ==")