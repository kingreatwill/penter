"""
pytest中可以用python的assert断言，也可以写多个断言，但一个失败，后面的断言将不再执行

可以看到，第二行即使断言失败，后面的断言还是会继续执行
这有助于我们分析和查看到底一共有哪些断言是失败的
而且最后的代码也还会正常执行，比直接用assert更高效

pip3 install pytest-assume -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com
"""
import pytest
def test_add1():
    assert 1 + 4 == 5
    assert 1 + 3 == 3
    assert 2 + 5 == 7
    assert 2 + 5 == 9
    print("测试完成")

def test_add2():
    pytest.assume(1 + 4 == 5)
    pytest.assume(1 + 3 == 3)
    pytest.assume(2 + 5 == 7)
    pytest.assume(2 + 5 == 9)
    print("测试完成")

