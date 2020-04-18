"""
pip3 install pytest-rerunfailures -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com

命令行参数：--reruns n（重新运行次数），--reruns-delay m（等待运行秒数）

装饰器参数：reruns=n（重新运行次数），reruns_delay=m（等待运行秒数）

pytest --reruns 5 --reruns-delay 10 -s


不可以和fixture装饰器一起使用： @pytest.fixture()
该插件与pytest-xdist的 --looponfail 标志不兼容
该插件与核心--pdb标志不兼容
"""

import pytest

# 如果指定了用例的重新运行次数，则在命令行添加--reruns对这些用例是不会生效的
@pytest.mark.flaky(reruns=5,  reruns_delay=2)
def test_example():
    import random
    assert random.choice([True, False, False])