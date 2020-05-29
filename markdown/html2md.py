import os
import re
import typing
import tomd
import requests
from urllib.parse import urlparse
from pyquery import PyQuery as pq
from dataclasses import dataclass, field

req = requests.Session()
req.headers.update({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'})


@dataclass
class Wanted:
    xpath: str = ".content"
    title: typing.Callable = lambda q: q("title").text().split("-")[0]
    find_img: typing.Callable = lambda q: q.attr('src')

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
        # 保存图片文件;
        with open(save_path + '/' + img_name, 'wb') as f:
            f.write(req.get(img_url).content)
        return "img/" + img_name


class Html2md:
    def __init__(self, url, title="", xpath=""):
        self.url = url
        self.title = title
        self.xpath = xpath
        self.rootQ = pq(url=self.url,
                        opener=lambda url, **kw: req.get(url).content)  # , opener=lambda url, **kw: urlopen(url).read()
        self.rule = self.get_rule(self.url)
        if not self.xpath:
            self.xpath = self.rule.xpath
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
        else:
            return Wanted()

    # 转换;
    def convert(self):
        contentQ = self.rootQ(self.xpath)
        # 处理图片;
        index = 1
        for e in contentQ('img'):
            img_src = self.rule.find_img(pq(e))
            img_src_cur = self.rule.save_pic(self.url, self.title, index, img_src)
            pq(e).attr(src=img_src_cur)
            index += 1
        # 转换成markdown;
        self.rule.save_md(self.title, tomd.convert(contentQ))


if "__main__" == __name__:
    urls = [
        "https://www.cnblogs.com/kingreatwill/p/9865945.html",
        "https://segmentfault.com/a/1190000022777293",
    ]
    for url in urls:
        Html2md(url).convert()
