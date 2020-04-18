# coding = utf-8
import unittest
import warnings
from selenium import webdriver
from time import sleep
# 驱动文件路径
driverfile_path = r'D:\coship\Test_Framework\drivers\IEDriverServer.exe'

class CmsLoginTest(unittest.TestCase):
    def setUp(self):
        # 这行代码的作用是忽略一些告警打印
        warnings.simplefilter("ignore", ResourceWarning)
        self.driver = webdriver.Ie(executable_path=driverfile_path)
        self.driver.get("http://172.21.13.83:28080/")

    def tearDown(self):
        self.driver.quit()

    def test_login1(self):
        '''用户名、密码为空'''
        self.driver.find_element_by_css_selector("#imageField").click()
        error_message1 = self.driver.find_element_by_css_selector("[for='loginName']").text
        error_message2 = self.driver.find_element_by_css_selector("[for='textfield']").text
        self.assertEqual(error_message1, '用户名不能为空')
        self.assertEqual(error_message2, '密码不能为空')

    def test_login3(self):
        '''用户名、密码正确'''
        self.driver.find_element_by_css_selector("[name='admin.loginName']").send_keys("autotest")
        self.driver.find_element_by_css_selector("[name='admin.password']").send_keys("111111")
        self.driver.find_element_by_css_selector("#imageField").click()
        sleep(1)
        self.driver.switch_to.frame("topFrame")
        username = self.driver.find_element_by_css_selector("#nav_top>ul>li>a").text
        self.assertEqual(username,"autotest")

    def test_login2(self):
        '''用户名正确，密码错误'''
        self.driver.find_element_by_css_selector("[name='admin.loginName']").send_keys("autotest")
        self.driver.find_element_by_css_selector("[name='admin.password']").send_keys("123456")
        self.driver.find_element_by_css_selector("#imageField").click()
        error_message = self.driver.find_element_by_css_selector(".errorMessage").text
        self.assertEqual(error_message, '密码错误,请重新输入!')

    def test_login4(self):
        '''用户名不存在'''
        self.driver.find_element_by_css_selector("[name='admin.loginName']").send_keys("test007")
        self.driver.find_element_by_css_selector("[name='admin.password']").send_keys("123456")
        self.driver.find_element_by_css_selector("#imageField").click()
        error_message = self.driver.find_element_by_css_selector(".errorMessage").text
        self.assertEqual(error_message, '用户不存在!')


if __name__ == "__main__":
    # 构造测试套件
    suite = unittest.TestSuite()
    suite.addTest(CmsLoginTest("test_login1"))
    suite.addTest(CmsLoginTest("test_login2"))
    suite.addTest(CmsLoginTest("test_login4"))
    suite.addTest(CmsLoginTest("test_login3"))
    # 执行测试
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

"""
if __name__ == "__main__":
    # 构造测试套件
    suite = unittest.TestSuite()
    test_cases = [CmsLoginTest("test_login1"),CmsLoginTest("test_login2"),CmsLoginTest("test_login4"),
                  CmsLoginTest("test_login3")]
    suite.addTests(test_cases)
    # 执行测试
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
多个文件 可以导入
import unittest
from cmslogin import CmsLoginTest
from smelogin import SmeLoginTest

if __name__ == "__main__":
    # 构造测试套件
    suite = unittest.TestSuite()
    test_cases = [CmsLoginTest("test_login1"),CmsLoginTest("test_login2"),CmsLoginTest("test_login4"),
                  CmsLoginTest("test_login3"),SmeLoginTest("test_login1"),SmeLoginTest("test_login2")]
    suite.addTests(test_cases)
    # 执行测试
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

还可以用addTests + TestLoader方法来添加用例，但是这种方法是无法对case进行排序的
import unittest
from cmslogin import CmsLoginTest
from smelogin import SmeLoginTest

if __name__ == "__main__":
    # 构造测试套件
    suite = unittest.TestSuite()
    # 第一种方法：传入'模块名.TestCase名'
    suite.addTests(unittest.TestLoader().loadTestsFromName('cmslogin.CmsLoginTest'))
    suite.addTests(unittest.TestLoader().loadTestsFromName('smelogin.SmeLoginTest'))
    # 这里还可以把'模块名.TestCase名'放到一个列表中
    suite.addTests(unittest.TestLoader().loadTestsFromNames(['cmslogin.CmsLoginTest','smelogin.SmeLoginTest']))
    # 第二种方法：传入TestCase
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(CmsLoginTest))
    # 执行测试
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
    
测试报告
import HTMLTestRunner  #用来生成报告的模块
f = open('test.html','wb')  #以二进制模式打开一个文件
runner = HTMLTestRunner.HTMLTestRunner(f,title='unittest用例标题',description='这是用例描述')
runner.run(suite)  #运行用例（用例集合) 
    
"""