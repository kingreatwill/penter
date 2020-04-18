# https://github.com/ftobia/pytest-ordering
# pip install pytest-ordering
import pytest

# 在一个文件中，用例的执行顺序是从上到下的

@pytest.mark.run(order=1)
def test_01():
    print('test01')

@pytest.mark.run(order=2)
def test_02():
    print('test01')

@pytest.mark.last
def test_06():
    print('test01')

def test_04():
    print('test01')

def test_05():
    print('test01')

#@pytest.mark.run(order=3)
def test_13():
    print('test01')

