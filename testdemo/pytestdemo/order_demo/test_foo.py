import pytest

def test_1():
    print(1)

@pytest.mark.scenarios_1(1)
def test_2():
    print(2)

@pytest.mark.scenarios_2(3)
def test_3():
    print(3)

@pytest.mark.scenarios_1(2)
@pytest.mark.scenarios_2(1)
def test_4():
    print(4)