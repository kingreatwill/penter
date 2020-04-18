import pytest

@pytest.fixture(params=[1,2,3])
def fixture_param(request):
    print("\033[31;1m我是fixture_param，这是第%s次打印\033[0m"%request.param)
    return request.param

def test_fixture_param(fixture_param):
    print("我是test_fixture_param函数")
    # print("我fixture_param现在是：%s"%fixture_param)

# 这个参数indirect=True，一定不能少，要不就会直接把 fixture_param当成测试函数的一个参数来用，加上indirect=True这个参数，才会在fixture的函数中查找
@pytest.mark.parametrize("fixture_param",["a","b"],indirect=True) # ["a","b"] 替换了params=[1,2,3]
@pytest.mark.parametrize("a,b",[(1,6),(2,7),(3,8),(4,9)])
def test_fixture_param_and_parametrize(a,b,fixture_param):
    print("我是测试函数test_fixture_param_and_parametrize，参数a是%s，b是%s"%(a,b))
    # print("我fixture_param现在是：%s"%fixture_param)

if __name__ == '__main__':
    pytest.main()