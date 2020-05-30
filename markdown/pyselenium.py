from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from pyquery import PyQuery as pq

app_agent = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Mobile Safari/537.36'
pc_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
# 加载启动项
options = webdriver.ChromeOptions()
options.add_argument('headless')
# 更换头部
options.add_argument('user-agent={}'.format(pc_agent))


def get_page_source(url, xpath):
    driver = webdriver.Chrome(options=options)
    script = '''() =>{ Object.defineProperties(navigator,{ webdriver:{ get: () => false } }) }'''
    driver.execute_script(script)
    driver.get(url)
    is_disappeared = WebDriverWait(driver, 30, 0.5, ignored_exceptions=TimeoutException).until(
        lambda x: x.find_element_by_css_selector(xpath).is_displayed())
    htmQ = pq(driver.page_source)
    driver.quit()
    return htmQ
