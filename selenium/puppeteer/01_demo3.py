import asyncio

from pyppeteer import launch

app_agent = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Mobile Safari/537.36'
pc_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'


async def get_page_source_async(url, selector):
    browser = await launch(headless=False,)
    page = await browser.newPage()
    await page.setUserAgent(pc_agent)
    await page.setJavaScriptEnabled(enabled=True)
    await page.goto(url, {"waitUntil": 'networkidle0'})
    await page.waitForSelector(selector)
    page_html = await page.content()
    print(page_html)
    await browser.close()
    return page_html


def get_page_source(url, selector):
    coroutine = get_page_source_async(url, selector)
    loop = asyncio.get_event_loop()
    task = asyncio.ensure_future(coroutine)
    loop.run_until_complete(task)
    return task.result()


if "__main__" == __name__:
    get_page_source('https://www.toutiao.com/i6827512913318642187/', ".article-box")
