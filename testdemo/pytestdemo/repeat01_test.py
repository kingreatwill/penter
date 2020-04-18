"""
pip3 install pytest-repeat -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com

pytest-repeat不能与unittest.TestCase测试类一起使用。无论--count设置多少，这些测试始终仅运行一次，并显示警告

pytest --html=report.html --self-contained-html  -s --reruns=5 --count=2 repeat01_test.py

如果需要验证偶现问题，可以一次又一次地运行相同的测试直到失败，这个插件将很有用
可以将pytest的 -x 选项与pytest-repeat结合使用，以强制测试运行程序在第一次失败时停止
py.test --count=1000 -x repeat01_test.py
"""
import pytest
def test_example():
    import random
    flag = random.choice([True, False])
    print(flag)
    assert flag


# 如果要在代码中将某些测试用例标记为执行重复多次，可以使用 @pytest.mark.repeat(count)
# pytest -s repeat01_test.py
@pytest.mark.repeat(5)
def test_repeat():
    print("测试用例执行")

"""
--repeat-scope
作用：可以覆盖默认的测试用例执行顺序，类似fixture的scope参数

function：默认，范围针对每个用例重复执行，再执行下一个用例
class：以class为用例集合单位，重复执行class里面的用例，再执行下一个
module：以模块为单位，重复执行模块里面的用例，再执行下一个
session：重复整个测试会话，即所有测试用例的执行一次，然后再执行第二次


pytest -s --count=2 --repeat-scope=class 13repeat.py
"""

