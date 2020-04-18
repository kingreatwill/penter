def test_get_info(login):
    name, token = login
    print("***基础用例：获取用户个人信息***")
    print(f"用户名:{name}, token:{token}")