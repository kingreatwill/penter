import fileinput

import tomd
import rule

import pypuppeteer
import pyselenium
import pyrequests

from pyquery import PyQuery as pq

app_agent = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Mobile Safari/537.36'
pc_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'


class Html2md:
    def __init__(self, **kwargs):
        self.html = ""
        self.url = ""
        self.title = ""
        self.selector = ""
        self.client = ""
        self.path = ""
        self.headless = False
        self.useragent = "pc"

        if "html" in kwargs and kwargs["html"]:
            self.contentQ = pq(kwargs["html"])
            return
        if "url" in kwargs and kwargs["url"]:
            self.url = kwargs["url"]
        else:
            raise ValueError("请传入html内容或者url地址")
        if "title" in kwargs and kwargs["title"]:
            self.title = kwargs["title"]
        if "selector" in kwargs and kwargs["selector"]:
            self.selector = kwargs["selector"]
        if "client" in kwargs and kwargs["client"]:
            self.client = kwargs["client"]
        if "path" in kwargs and kwargs["path"]:
            self.path = kwargs["path"]
        if "headless" in kwargs and kwargs["headless"]:
            self.headless = kwargs["headless"]
        if "useragent" in kwargs and kwargs["useragent"]:
            self.useragent = kwargs["useragent"]

        if self.useragent == "pc":
            kwargs["useragent"] = pc_agent
        elif self.useragent == "app":
            kwargs["useragent"] = app_agent
        else:
            kwargs["useragent"] = self.useragent

        self.rule = rule.get_rule(self.url)

        if not self.selector:
            self.selector = self.rule.selector

        # get加载页面;(requests(r)默认,puppeteer(p),selenium(s)
        if self.client in ["requests", "r"]:
            self.rootQ = pyrequests.page_source(self.url, self.selector, **kwargs)
        elif self.client in ["puppeteer", "p"]:
            self.rootQ = pypuppeteer.page_source(self.url, self.selector, **kwargs)
        elif self.client in ["selenium", "s"]:
            self.rootQ = pyselenium.page_source(self.url, self.selector, **kwargs)
        else:
            self.rootQ = self.rule.page_source(self.url, self.selector, **kwargs)
        # 获取标题;
        if not self.title:
            self.title = self.rule.title(self.rootQ)
        # 提取文章内容;
        self.contentQ = self.rootQ(self.selector)

    # 转换;
    def convert(self):
        # 处理图片;
        index = 1
        for e in self.contentQ(self.rule.img_tag):
            q = pq(e)
            img_src = self.rule.find_img(q)
            img_src_cur = self.rule.save_pic(self.url, self.title, index, img_src)
            if q[0].tag != "img":
                q.replace_with(pq('<img src="' + img_src_cur + '"/>'))
            else:
                q.attr(src=img_src_cur)
            index += 1
        # 转换成markdown;
        self.rule.save_md(self.title, tomd.convert(self.contentQ))


import argparse

parser = argparse.ArgumentParser(description='url to markdown.')
parser.add_argument('file', nargs='?', help='需要转换的html内容/url地址/文件地址')
parser.add_argument('--name', "-n", help='保存的文件名', required=False)
parser.add_argument('--selector', "-s", help='post内容选择器', required=False)
parser.add_argument('--client', "-c", help='解析url的工具(requests(r)默认,puppeteer(p),selenium(s))', required=False)
parser.add_argument('--path', "-p", help='指定解析工具的路径', required=False)
parser.add_argument('--headless', "-less", action='store_true', help='是否无浏览器模式, 默认false', default=False, required=False)
parser.add_argument('--user-agent', "-ua", type=str, help='user-agent(pc or app or 自定义)', default="pc", required=False)
args = parser.parse_args()

if "__main__" == __name__:
    adic = args.__dict__
    if isinstance(args.file, str):
        if args.file.startswith("http://") or args.file.startswith("https://"):
            adic["url"] = args.file
    if "url" not in adic:
        adic["html"] = ''.join([line for line in fileinput.input(args.file)])

    Html2md(**adic).convert()
