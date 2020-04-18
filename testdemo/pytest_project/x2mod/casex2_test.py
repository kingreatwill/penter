# 包没有__init__.py文件也没有conftest.py文件
def test_no_fixture(login):
    print("==没有__init__测试用例，我进入头条了==", login)