"""
pytest.mark.skip  可以标记无法在某些平台上运行的测试功能，戒者您希望失败的测试功能
希望满足某些条件才执行某些测试用例，否则pytest会跳过运行该测试用例
实际常见场景：跳过非Windows平台上的仅Windows测试，或者跳过依赖于当前不可用的外部资源（例如数据库）的测试
"""
import sys
import pytest

# 当 allow_module_level=True 时，可以设置在模块级别跳过整个模块
# if sys.platform.startswith("win"):
#     pytest.skip("skipping windows-only tests", allow_module_level=True)



@pytest.fixture(autouse=True)
def login():
    print("====登录====")


def test_case01():
    print("我是测试用例11111")


@pytest.mark.skip(reason="不执行该用例！！因为没写好！！")
def test_case02():
    print("我是测试用例22222")


class Test1:

    def test_1(self):
        print("%% 我是类测试用例1111 %%")

    @pytest.mark.skip(reason="不想执行")
    def test_2(self):
        print("%% 我是类测试用例2222 %%")


@pytest.mark.skip(reason="类也可以跳过不执行")
class TestSkip:
    def test_1(self):
        print("%% 不会执行 %%")

def test_function():
    n = 1
    while True:
        print(f"这是我第{n}条用例")
        n += 1
        if n == 5:
            pytest.skip("我跑五次了不跑了")


@pytest.mark.skipif(sys.platform == 'win32', reason="does not run on windows")
class TestSkipIf(object):
    def test_function(self):
        print("不能在window上运行")


"""
可以将 pytest.mark.skip 和 pytest.mark.skipif 赋值给一个标记变量
在不同模块之间共享这个标记变量
若有多个模块的测试用例需要用到相同的 skip 或 skipif ，可以用一个单独的文件去管理这些通用标记，然后适用于整个测试用例集
"""

# 标记
skipmark = pytest.mark.skip(reason="不能在window上运行=====")
skipifmark = pytest.mark.skipif(sys.platform == 'win32', reason="不能在window上运行啦啦啦=====")


@skipmark
class TestSkip_Mark(object):

    @skipifmark
    def test_function(self):
        print("测试标记")

    def test_def(self):
        print("测试标记")


@skipmark
def test_skip():
    print("测试标记")


# importorskip
# 作用：如果缺少某些导入，则跳过模块中的所有测试
#
# 参数列表
#
# modname：模块名
# minversion：版本号
# reasone：跳过原因，默认不给也行
# pexpect = pytest.importorskip("pexpect", minversion="0.3")
# @pexpect
# def test_import():
#     print("test")
