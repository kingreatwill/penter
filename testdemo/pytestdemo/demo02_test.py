

"""
Pytest也贴心的提供了类似setup、teardown的方法，并且还超过四个，一共有十种

模块级别：setup_module、teardown_module
函数级别：setup_function、teardown_function，不在类中的方法
类级别：setup_class、teardown_class
方法级别：setup_method、teardown_method
方法细化级别：setup、teardown
"""
import pytest


def setup_module():
    print("=====整个.py模块开始前只执行一次:打开浏览器=====")


def teardown_module():
    print("=====整个.py模块结束后只执行一次:关闭浏览器=====")


def setup_function():
    print("===每个函数级别用例开始前都执行setup_function===")


def teardown_function():
    print("===每个函数级别用例结束后都执行teardown_function====")


def test_one():
    print("one")


def test_two():
    print("two")


class TestCase():
    def setup_class(self):
        print("====整个测试类开始前只执行一次setup_class====")

    def teardown_class(self):
        print("====整个测试类结束后只执行一次teardown_class====")

    def setup_method(self):
        print("==类里面每个用例执行前都会执行setup_method==")

    def teardown_method(self):
        print("==类里面每个用例结束后都会执行teardown_method==")

    def setup(self):
        print("=类里面每个用例执行前都会执行setup=")

    def teardown(self):
        print("=类里面每个用例结束后都会执行teardown=")

    def test_three(self):
        print("three")


def test_four():
    print("four")


if __name__ == '__main__':
    pytest.main() # ["-q", "-s", "-ra", "setup_teardown.py"]