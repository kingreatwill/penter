#!/usr/bin/env python
# coding=utf-8
"""
.py 测试文件必须以test_开头（或者以_test结尾）

测试类必须以Test开头，并且不能有 init 方法

测试方法必须以test_开头

断言必须使用 assert
"""
import pytest

def inc(x):
    return x + 1

def test_answer():
    assert inc(3) == 4

if __name__ =="__main__":
    pytest.main()