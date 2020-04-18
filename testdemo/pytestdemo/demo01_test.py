#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest


"""
pytest demo01_test.py

pytest -v 08_mark.py::TestClass::test_method
# -q 简单打印，只打印测试用例的执行结果
# -s 详细打印
# -x 遇到错误时停止测试 
#--maxfail=num，当用例错误个数达到指定数量时，停止测试

pytest -s -k http start.py # 执行测试用例名称包含http的所有用例
pytest -s -k "not http" start.py # 根据用例名称排除某些用例
pytest -s -k "method or weibo" start.py # 同时匹配不同的用例名称
pytest 08_mark.py::TestClass::test_method

pytest start.py::test_answer

pytest start.py::TestClass::test_two

pytest -m login #将运行用 @pytest.mark.login 装饰器修饰的所有测试
"""

def func(x):
    return x + 1


def test_answer():  # 2. 测试方法必须以“test_”开头
    assert (func(3) == 4)


# 断言异常
def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0

# 详细断言异常
def test_zero_division_long():
    with pytest.raises(Exception) as excinfo:
        1 / 0

    # 断言异常类型 type
    assert excinfo.type == ZeroDivisionError
    # 断言异常 value 值
    assert "division by zero" in str(excinfo.value)

# 自定义消息
def test_zero_division_long2():
    with pytest.raises(Exception, match=".*zero.*") as excinfo:
        1 / 0

# 断言装饰器
@pytest.mark.xfail(raises=TypeError)
def test_f1():
    1 / 0

# 断言装饰器
@pytest.mark.xfail(raises=ZeroDivisionError)
def test_f2():
    1 / 0

class TestClass:  # 3 测试类命名以"Test"开头
    def test_one(self): # 2. 测试方法必须以“test_”开头
        x = "this"
        assert ("h" in x)

    def test_two(self):
        x = "hello"
        assert (hasattr(x, "check"))


if __name__ == "__main__":
    pytest.main()
