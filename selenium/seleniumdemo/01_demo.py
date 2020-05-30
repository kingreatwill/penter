from selenium import webdriver
import os, time

# 加载启动项
option = webdriver.ChromeOptions()
option.add_argument('headless')
# 更换头部
option.add_argument('user-agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Mobile Safari/537.36')

# 定义截图地址&图片格式
screen_path = os.path.dirname(os.getcwd()) + '/report/Screenshots/'
rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
screen_name = screen_path + rq + '.png'

# 打开chrome浏览器

# driver = webdriver.Chrome(chrome_options=option)

# 版本更新，需要options 代替chrome_option
driver = webdriver.Chrome(options=option)

# 定义url 地址
url = 'https://www.toutiao.com/i6827512913318642187/'

driver.get(url=url)
time.sleep(2)
print(driver.page_source)
# 截图
# print(screen_name)
# driver.save_screenshot(screen_name)
# time.sleep(3)

# 退出并关闭浏览器
driver.quit()

"""
只要你执行navigator.webdriver返回值是true就是浏览器内核访问

如果不是返回值是undefined

selenium为了解决这个需进行js 注入

from selenium import webdriver
browser = webdriver.Chrome()
script='''Object.defineProperties(navigator, {webdriver:{get:()=>undefined}})'''
#js1 = '''() =>{ Object.defineProperties(navigator,{ webdriver:{ get: () => false } }) }'''
browser.execute_script(script)
"""