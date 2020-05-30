# Open web page and take a screenshot:
import asyncio
from pyppeteer import launch
import time
import pyppeteer.chromium_downloader
print('默认版本是：{}'.format(pyppeteer.__chromium_revision__))
print('可执行文件默认路径：{}'.format(pyppeteer.chromium_downloader.chromiumExecutable.get('win64')))
print('win64平台下载链接为：{}'.format(pyppeteer.chromium_downloader.downloadURLs.get('win64')))
# https://www.cnblogs.com/chenhuabin/p/10989895.html
# https://blog.csdn.net/freeking101/article/details/93331204
# pyppeteer(四)--常用函数 https://www.jianshu.com/p/52f9dc6fb7e1
async def main():
    browser = await launch(headless=True, dumpio=True,
                           args=["--start-maximized", '--no-sandbox', "--disable-infobars", "--log-level=3"])
    # devtools=True,headless=False,appMode
    # executablePath=r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"

    """
     # 'args': ['--enable-automation']
    只要你执行navigator.webdriver返回值是true就是浏览器内核访问

    如果不是返回值是undefined

    selenium为了解决这个需进行js 注入

    from selenium import webdriver
    browser = webdriver.Chrome()
    script='''Object.defineProperties(navigator, {webdriver:{get:()=>undefined}})'''
    #js1 = '''() =>{ Object.defineProperties(navigator,{ webdriver:{ get: () => false } }) }'''
    browser.execute_script(script)
    """
    # # 启动 pyppeteer 属于内存中实现交互的模拟器
    # browser = await launch({'headless': False, 'args': ['--no-sandbox'], 'dumpio': True})
    page = await browser.newPage()
    await page.setUserAgent(
        'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Mobile Safari/537.36')
    # 是否启用JS，enabled设为False，则无渲染效果
    # await page.setJavaScriptEnabled(enabled=True)

    await page.goto('https://www.toutiao.com/i6827512913318642187/')
    # , {'timeout': 10000*20}
    # await page.goto(url, {"waitUntil": 'networkidle0'})
    # waitUntil的参数有：load,domcontentloaded,networkidle0,networkidle2
    """
    waitUntil代表什么时候才认为导航加载成功。
    load: window.onload事件被触发时候完成导航,某些情况下它根本不会发生。
    domcontentloaded: Domcontentloaded事件触发时候认为导航成功
    networkidle0: 在 500ms 内没有网络连接时就算成功(全部的request结束),才认为导航结束
    networkidle2: 500ms 内有不超过 2 个网络连接时就算成功(还有两个以下的request),就认为导航完成。
    我们对比了下加载时长 networkidle0> networkidle2>load>domcontentloaded

    """

    # page.waitForSelector(selector)/page.waitForXPath(xpath)
    # 等待目标元素加载完成，默认timeout是30秒，可以辅助确定指定位置元素是否已经加载完成。
    # await page.waitForSelector(selector)
    print(await page.content())
    await browser.close()


asyncio.get_event_loop().run_until_complete(main())

"""
# Pyppeteer 支持字典 和 关键字传参，Puppeteer 只支持字典传参。
# 这里使用字典传参
browser = await launch(
    {
        'headless': False, 
        'dumpio': True, 
        'autoClose': False, 
        'args': [
            '--no-sandbox', 
            '--window-size=1366,850'
        ]
    }
)
await page.setViewport({'width': 1366, 'height': 768})
"""
