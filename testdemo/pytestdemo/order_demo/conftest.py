import pytest
# https://docs.pytest.org/en/latest/reference.html?highlight=pytestconfig#_pytest.hookspec.pytest_collection_modifyitems

# pytest -m scenarios_2 -s
# hook函数
def pytest_collection_modifyitems(config, items):
    """ 根据指定的mark参数场景，动态选择case的执行顺序"""
    for item in items:
        scenarios = [
            marker for marker in item.own_markers
            if marker.name.startswith('scenarios')
            and marker.name in config.option.markexpr
        ]
        if len(scenarios) == 1 and not item.get_closest_marker('run'):
           item.add_marker(pytest.mark.run(order=scenarios[0].args[0]))

# 去除mark警告
def pytest_configure(config):
    config.addinivalue_line("markers", "scenarios_1: mark test to run only on named environment")
    config.addinivalue_line("markers", "scenarios_2: this one is for cool tests.")