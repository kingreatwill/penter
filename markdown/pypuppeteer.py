import asyncio

from pyppeteer import launch
from pyquery import PyQuery as pq


async def get_page_source_async(use_url, use_selector, **kwargs):
    # , args=["--enable-automation"]
    browser = await launch(headless=kwargs["headless"], appMode=False, executablePath=kwargs["path"])
    page = await browser.newPage()
    await page.setUserAgent(kwargs["useragent"])
    await page.setJavaScriptEnabled(enabled=True)
    await page.goto(use_url)#, {"waitUntil": 'networkidle0'}
    await page.waitForSelector(use_selector)
    page_html = await page.content()
    await browser.close()
    return page_html


def page_source(use_url, use_selector, **kwargs):
    coroutine = get_page_source_async(use_url, use_selector, **kwargs)
    loop = asyncio.get_event_loop()
    task = asyncio.ensure_future(coroutine)
    loop.run_until_complete(task)
    return pq(task.result())
