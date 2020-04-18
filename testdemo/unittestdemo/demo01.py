import unittest # 1 导入unittest
import HTMLTestRunnerNew
class TestStringMethods(unittest.TestCase): # 2 集成unittest.TestCase类
    @classmethod
    def setUpClass(cls):
        print("setUpClass")
    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")
    def setUp(self): # 在每个测试方法之前的指令。
        print("setUp")
    def tearDown(self): # 在每个测试方法之后的指令。
        print("tearDown")
    def test_upper(self): # 3 test_开头的方法
        self.assertEqual('foo'.upper(), 'FOO')
        print("test_upper")

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())
        print("test_isupper")

    def test_split(self):
        print("test_split")
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError): # 断言引发特定的异常
            s.split(2)

"""
python -m unittest test_module1 test_module2
python -m unittest test_module.TestClass
python -m unittest test_module.TestClass.test_method

python -m unittest tests/test_something.py
python -m unittest -v test_module

python -m unittest

python -m unittest -h #帮助

python -m unittest discover -s project_directory -p "*_test.py" # -s 目录 默认 .
python -m unittest discover project_directory "*_test.py"
"""

# 执行脚本加入-v  会输出更详细的内容(python demo01.py -v)
# 执行顺序是根据测试用例名称顺序执行的
# 4 main方法
if __name__ == '__main__':
    unittest.main()
    #unittest.main()