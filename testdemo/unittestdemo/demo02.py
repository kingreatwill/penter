import unittest # 1 导入unittest
class TestCase(unittest.TestCase): # 2 集成unittest.TestCase类
    def runTest(self):
        print("11111111")
        self.test_isupper()
    def test_upper(self): # 3 test_开头的方法
        self.assertEqual('foo'.upper(), 'FOO')
        print("test_upper")
    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())
        print("test_isupper")

def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestCase("test_isupper"))
    suite.addTest(TestCase())
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())