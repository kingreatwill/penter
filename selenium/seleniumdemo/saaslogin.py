from selenium import webdriver
from time import sleep

# 1. 设置浏览器驱动
#driver = webdriver.Chrome()
# driver = webdriver.Firefox()   # Firefox浏览器
# driver = webdriver.Chrome()    # Chrome浏览器
# driver = webdriver.Ie()        # Internet Explorer浏览器
# driver = webdriver.Edge()      # Edge浏览器
# driver = webdriver.Opera()     # Opera浏览器
# driver = webdriver.PhantomJS()   # PhantomJS
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
driver = webdriver.Remote(command_executor='http://192.168.110.216:9999/wd/hub', desired_capabilities=DesiredCapabilities.EDGE)

# do_options = webdriver.ChromeOptions()
# do_options.binary_location = r'D:/doreadme/doreadme.exe'  #指定路径

#2. 打开网址
driver.get('https://saas.lingcb.net/')
# 打印当前页面title
title = driver.title
print("title:"+title)
# 打印当前页面URL
now_url = driver.current_url
print("url:"+now_url)

#3. 控制浏览器操作
driver.set_window_size(480, 800) # 设置浏览器宽480、高800显示
sleep(1)
driver.maximize_window() # 浏览器全屏显示
sleep(1)
driver.get("https://www.baidu.com/") #访问百度页面
sleep(1)
driver.back() #返回
sleep(1)
driver.forward() #前进
sleep(1)
driver.back() #返回
#4. 元素定位
# driver.find_element_by_id("id")
# driver.find_element_by_name("name")
# driver.find_element_by_class_name("title") # class="title"
# driver.find_element_by_tag_name("input")

# driver.find_element_by_link_text("hao123")
# driver.find_element_by_partial_link_text("hao") # 匹配部分

# 通过xpath定位，xpath定位有N种写法，这里列几个常用写法:
# driver.find_element_by_xpath("//*[@id='kw']")
# driver.find_element_by_xpath("//*[@name='wd']")
# driver.find_element_by_xpath("//input[@class='s_ipt']")
# driver.find_element_by_xpath("/html/body/form/span/input")
# driver.find_element_by_xpath("//span[@class='soutu-btn']/input")
# driver.find_element_by_xpath("//form[@id='form']/span/input")
# driver.find_element_by_xpath("//input[@id='kw' and @name='wd']")

# 通过css定位，css定位有N种写法，这里列几个常用写法:
# driver.find_element_by_css_selector("#kw")
# driver.find_element_by_css_selector("[name=wd]")
# driver.find_element_by_css_selector(".s_ipt")
# driver.find_element_by_css_selector("html > body > form > span > input")
# driver.find_element_by_css_selector("span.soutu-btn> input#kw")
# driver.find_element_by_css_selector("form#form > span > input")

t_element = driver.find_element_by_class_name("title")
cc_element = driver.find_element_by_xpath("//input[@placeholder='公司代码']")
u_element = driver.find_element_by_xpath("//input[@placeholder='请输入账户名']")
pwd_element = driver.find_element_by_xpath("//input[@placeholder='请输入密码']")

login_element = driver.find_element_by_class_name("btn-login")

#5. 元素属性和事件
# 常用属性
print(t_element.text) # 获取元素的文本。
print(t_element.size) # 返回元素的尺寸(比如输出：{'height': 44, 'width': 280})。

# 常用方法
print(t_element.get_attribute("class")) # 获得属性值。
print(t_element.is_displayed()) # 返回一个元素是否可见， 如果可见则返回 True， 否则返回 False。

sleep(1)
cc_element.clear() # 清除文本
cc_element.send_keys("lcb") # 模拟按键输入
sleep(1)
u_element.send_keys("0007") # 模拟按键输入
sleep(1)
pwd_element.send_keys("111111") # 模拟按键输入
sleep(1)
# 引入 Keys 模块模拟键盘事件
from selenium.webdriver.common.keys import Keys
u_element.send_keys(Keys.BACK_SPACE) # 删除多输入的一个7
sleep(1)
u_element.send_keys(Keys.SPACE) # 输入空格键
sleep(1)
u_element.send_keys("教程") # 输入"教程"
sleep(1)
u_element.send_keys(Keys.CONTROL, 'a')# ctrl+a 全选输入框内容
sleep(1)
u_element.send_keys(Keys.CONTROL, 'x')# ctrl+x 剪切输入框内容
sleep(1)
u_element.send_keys(Keys.CONTROL, 'v')# ctrl+v 粘贴内容到输入框
sleep(1)
u_element.clear()
u_element.send_keys("0003") # 模拟按键输入
sleep(1)
# send_keys(Keys.F1) 键盘 F1....F12
# u_element.send_keys(Keys.ENTER) # 通过回车键来代替单击操作
# Keys.TAB 制表键(Tab)
# Keys.ESCAPE 回退键（Esc）

login_element.click() # 单击元素
# xxx_element.submit() #submit()方法用于提交表单。 例如， 在搜索框输入关键字之后的“回车” 操作， 就可以通过该方法模拟
sleep(1)



#6. 鼠标事件
# 在 WebDriver 中， 将这些关于鼠标操作的方法封装在 ActionChains 类提供。
# 引入 ActionChains 类 from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.action_chains import ActionChains

# ActionChains 类提供了鼠标操作的常用方法：
# perform()： 执行所有 ActionChains 中存储的行为；
# context_click()： 右击；
# double_click()： 双击；
# drag_and_drop()： 拖动；
# move_to_element()： 鼠标悬停。

# 对定位到的元素执行鼠标悬停操作
ActionChains(driver).context_click(pwd_element).context_click(u_element).move_to_element(cc_element).perform()
sleep(1)


#7. 断言



# 窗口操作

# 当前窗口句柄
lcb_handle = driver.current_window_handle

# 新开一个窗口，通过执行js来新开一个窗口
js = 'window.open("https://www.baidu.com/");'
driver.execute_script(js)

sleep(1)
# 切换到新标签页的窗口 百度
driver.switch_to.window(driver.window_handles[-1])
sleep(1)
driver.switch_to.window(lcb_handle)
sleep(1)
driver.close()
sleep(1)

# driver.get("https://www.baidu.com")
# actions = ActionChains(driver)
# about = driver.find_element_by_link_text('新闻')
# # 在新的标签页打开“新闻”页面
# actions.key_down(Keys.CONTROL).click(about).key_up(Keys.CONTROL).perform()


# 切换到新标签页的窗口 百度（因为上面driver.close()了，所以要激活）
driver.switch_to.window(driver.window_handles[-1])
# 截取当前窗口，并指定截图图片的保存位置
driver.get_screenshot_as_file("D:\\baidu_img.png")
sleep(1)
driver.quit()
# close() 关闭单个窗口
# quit() 关闭所有窗口


# 测试报告 测试用例
# 以上方式优点：独立，可以单独执行
# 缺点：不具备大规模测试条件，维护成本大
# https://www.cnblogs.com/dydxw/p/10475046.html
# http://www.testclass.net/selenium_python/element-wait