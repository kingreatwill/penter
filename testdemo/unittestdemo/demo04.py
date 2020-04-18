# coding: utf-8
# author: Archer

import unittest
import ddt
import requests

# 接口参数，用列表[]包裹起来，每组数据则是字典格式
test_data = [{
    "clientCode": "韩",
    "topic": "测试接口",
    "content": "测试接口",
    "resrcType": "0",
    "assert": "200"   # assert并不是接口需要的参数，是为了对返回结果进行断言而加在这里的预期结果
},
    {
        "clientCode": "",
        "topic": "测试接口2",
        "content": "测试接口2",
        "resrcType": "0",
        "assert": "400"
    },
    {
        "clientCode": "韩",
        "topic": "",
        "content": "测试接口2",
        "resrcType": "0",
        "assert": "400"
    }]


@ddt.ddt
class Test(unittest.TestCase):
    def setUp(self):
        self.url = 'http://192.168.X.XXX:7001/XXX/api/XXXise/info/XXX/save.v'

    @ddt.data(*test_data) # ddt.file_data、ddt.unpack
    def test_ddt(self, value):   # 定义一个变量value来接收ddt.data中的数据
        r = requests.post(self.url, value)
        print(r.json())
        self.assertTrue(value['assert'] in r.text)   # 利用参数组合中的assert参数进行断言


if __name__ == '__main__':
    unittest.main()