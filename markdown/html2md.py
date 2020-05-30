import os
import re
import time
import typing

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

import tomd
import execjs  # pip install PyExecJS
import requests
from urllib.parse import urlparse
from pyquery import PyQuery as pq
from dataclasses import dataclass, field

driver = None
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}


def get_page_source(url, xpath):
    driver = webdriver.Chrome()
    driver.get(url)
    #time.sleep(3)
    # 等待特定网页元素加载完毕
    is_disappeared = WebDriverWait(driver, 10, 0.5, ignored_exceptions=TimeoutException).until(
        lambda x: x.find_element_by_css_selector(xpath).is_displayed())
    return pq(driver.page_source)


@dataclass
class Wanted:
    img_tag: str = "img"
    xpath: str = ".content"
    title: typing.Callable = lambda q: q("title").text().split("-")[0]
    find_img: typing.Callable = lambda q: q.attr('src')
    page_source: typing.Callable = lambda url, xpath: pq(url=url,
                                                         opener=lambda url, **kw: requests.get(url,
                                                                                               headers=headers).content)

    def pathed(self, p):
        pattern = "[`~!@#$%^&-+=\\?:\"|,/;'\\[\\]·~！@#￥%……&*（）+=\\{\\}\\|《》？：“”【】、；‘'，。\\、\\-\s]"
        return re.sub(pattern, "", p)

    # 保存md文件;
    def save_md(self, title, md_txt):
        title = self.pathed(title)
        save_path = './' + title
        if not os.path.exists(save_path):
            os.mkdir(save_path)  # 如果本文档目录不存在, 就创建;
        # 保存文件;
        with open(save_path + '/' + title + ".md", 'w', encoding='utf-8') as f:
            f.write(md_txt)

    # 保存图片;
    def save_pic(self, org_url, title, index, url) -> str:
        blog_url = urlparse(org_url)
        img_url = ""
        if url.startswith("http://") or url.startswith("https://"):
            img_url = url
        elif url.startswith("//"):
            img_url = blog_url.scheme + ":" + url
        else:
            if url.startswith("/"):
                img_url = blog_url.scheme + "://" + blog_url.netloc + url
            else:
                sp = blog_url.path.split("/")
                img_url = blog_url.scheme + "://" + blog_url.netloc + blog_url.path.replace(sp[len(sp) - 1], "") + url

        title = self.pathed(title)
        img_name = title + "_" + str(index) + ".jpg"
        save_path = './' + title + "/img"
        if not os.path.exists(save_path):
            os.makedirs(save_path)  # 如果本文档目录不存在, 就创建;
        img_headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
            'Referer': blog_url.scheme + "://" + blog_url.netloc
        }
        # 保存图片文件;
        with open(save_path + '/' + img_name, 'wb') as f:
            f.write(requests.get(img_url, headers=img_headers).content)
        return "img/" + img_name


class Html2md:
    def __init__(self, url, title="", xpath=""):
        self.url = url
        self.title = title
        self.xpath = xpath
        self.rule = self.get_rule(self.url)
        if not self.xpath:
            self.xpath = self.rule.xpath
        # get加载页面;
        self.rootQ = self.rule.page_source(self.url, self.xpath)
        if not self.title:
            self.title = self.rule.title(self.rootQ)

    # 获取url规则;
    def get_rule(self, url=""):
        if not url:
            url = self.url
        if "www.cnblogs.com" in url:
            return Wanted(xpath="#cnblogs_post_body")
        if "segmentfault.com" in url:
            return Wanted(xpath=".article.fmt.article-content", find_img=lambda q: q.attr('data-src'))
        if "blog.csdn.net" in url:
            return Wanted(xpath="#content_views")
        if "www.jianshu.com" in url:
            return Wanted(xpath="article", find_img=lambda q: q.attr('data-original-src'))
        if "mp.weixin.qq.com" in url:
            return Wanted(xpath="#js_content", find_img=lambda q: q.attr('data-src'))
        if "www.oschina.net" in url:
            return Wanted(xpath=".article-detail")
        if "cloud.tencent.com" in url:
            return Wanted(xpath=".com-markdown-collpase", img_tag="span.lazy-image-holder",
                          find_img=lambda q: q.attr('dataurl'))
        if "zhuanlan.zhihu.com" in url:
            return Wanted(xpath=".Post-RichTextContainer", find_img=lambda q: q.attr('data-actualsrc'))
        if "www.toutiao.com" in url or "m.toutiao.com" in url:
            return Wanted(xpath=".article-box", page_source=get_page_source)
        return Wanted()

    # 转换;
    def convert(self):
        contentQ = self.rootQ(self.xpath)
        # 处理图片;
        index = 1
        for e in contentQ(self.rule.img_tag):
            q = pq(e)
            img_src = self.rule.find_img(q)
            img_src_cur = self.rule.save_pic(self.url, self.title, index, img_src)
            if q[0].tag != "img":
                q.replace_with(pq('<img src="' + img_src_cur + '"/>'))
            else:
                q.attr(src=img_src_cur)
            index += 1
        # 转换成markdown;
        self.rule.save_md(self.title, tomd.convert(contentQ))


if "__main__" == __name__:
    urls = [
        "https://www.cnblogs.com/kingreatwill/p/9865945.html",
        "https://segmentfault.com/a/1190000022777293",
        "https://cloud.tencent.com/developer/article/1632510",
        "https://www.toutiao.com/i6827512913318642187/",
    ]
    for url in urls:
        Html2md(url).convert()
    if driver:
        driver.quit()
