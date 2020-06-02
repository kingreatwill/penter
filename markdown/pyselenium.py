from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from pyquery import PyQuery as pq


def page_source(use_url, use_selector, **kwargs):
    # 加载启动项
    options = webdriver.ChromeOptions()
    if kwargs["headless"]:
        options.add_argument('headless')
    if kwargs["path"]:
        options.binary_location = kwargs["path"]
    options.add_argument('user-agent={}'.format(kwargs["useragent"]))
    # 启动;
    driver = webdriver.Chrome(options=options)
    script = '''() =>{ Object.defineProperties(navigator,{ webdriver:{ get: () => false } }) }'''
    driver.execute_script(script)
    driver.get(use_url)
    is_disappeared = WebDriverWait(driver, 30, 0.5, ignored_exceptions=TimeoutException).until(
        lambda x: x.find_element_by_css_selector(use_selector).is_displayed())
    htmQ = pq(driver.page_source)
    driver.quit()
    return htmQ
