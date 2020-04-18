import pytest

@pytest.mark.scenarios_2(2)
def test_a():
    print('a')

@pytest.mark.scenarios_1(3)
def test_b():
    print('b')

def test_c():
    print('c')