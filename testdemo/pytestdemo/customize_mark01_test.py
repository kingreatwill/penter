"""
pytest 可以支持自定义标记，自定义标记可以把一个 web 项目划分多个模块，然后指定模块名称执行
譬如我可以标明哪些用例是window下执行的，哪些用例是mac下执行的，在运行代码时候指定mark即可
pytest -s -m weibo customize_mark01_test.py
pytest -s -m "not weibo" customize_mark01_test.py
pytest -s -m "toutiao or weibo" 08_mark.py
如何避免warnings
- 创建一个pytest.ini文件
- 加上自定义mark
- 注意：pytest.ini需要和运行的测试用例同一个目录，或在根目录下作用于全局
https://docs.pytest.org/en/latest/mark.html
或者 您可以在pytest_configure挂钩中以编程方式注册新标记：
"""
import pytest


@pytest.mark.weibo
def test_weibo():
    print("测试微博")


@pytest.mark.toutiao
def test_toutiao():
    print("测试头条")


@pytest.mark.toutiao
def test_toutiao1():
    print("再次测试头条")


@pytest.mark.xinlang
class TestClass:
    def test_method(self):
        print("测试新浪")


def testnoMark():
    print("没有标记测试")



