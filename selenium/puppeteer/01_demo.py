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
async def main():
    browser = await launch(headless=True, dumpio=True,
                           args=["--start-maximized", '--no-sandbox', "--disable-infobars", "--log-level=3"])
    # devtools=True,headless=False,appMode
    # executablePath=r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
    # # 启动 pyppeteer 属于内存中实现交互的模拟器
    # browser = await launch({'headless': False, 'args': ['--no-sandbox'], 'dumpio': True})
    page = await browser.newPage()
    await page.setUserAgent(
        'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Mobile Safari/537.36')
    # 是否启用JS，enabled设为False，则无渲染效果
    # await page.setJavaScriptEnabled(enabled=True)

    await page.goto('https://www.toutiao.com/i6827512913318642187/')

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
