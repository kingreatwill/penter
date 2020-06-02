import os
import re
import typing
import pyrequests
import requests
from urllib.parse import urlparse
from dataclasses import dataclass, field


@dataclass
class Wanted:
    img_tag: str = "img"
    selector: str = "body"
    title: typing.Callable = lambda q: q("title").text().split("-")[0]
    find_img: typing.Callable = lambda q: q.attr('src')
    page_source: typing.Callable = pyrequests.page_source

    # 处理文件路径中的特殊字符;
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
