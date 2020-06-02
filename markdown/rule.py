import pypuppeteer
import pyselenium
from mod import Wanted


# 获取url规则;
def get_rule(url):
    if "www.cnblogs.com" in url:
        return Wanted(selector="#cnblogs_post_body")
    if "segmentfault.com" in url:
        return Wanted(selector=".article.fmt.article-content", find_img=lambda q: q.attr('data-src'))
    if "blog.csdn.net" in url:
        return Wanted(selector="#content_views")
    if "www.jianshu.com" in url:
        return Wanted(selector="article", find_img=lambda q: q.attr('data-original-src'))
    if "mp.weixin.qq.com" in url:
        return Wanted(selector="#js_content", find_img=lambda q: q.attr('data-src'))
    if "www.oschina.net" in url:
        return Wanted(selector=".article-detail")
    if "cloud.tencent.com" in url:
        return Wanted(selector=".com-markdown-collpase", img_tag="span.lazy-image-holder",
                      find_img=lambda q: q.attr('dataurl'))
    if "zhuanlan.zhihu.com" in url:
        return Wanted(selector=".Post-RichTextContainer", find_img=lambda q: q.attr('data-actualsrc'))
    if "www.toutiao.com" in url or "m.toutiao.com" in url:
        return Wanted(selector=".article-box", page_source=pypuppeteer.page_source)
    return Wanted()
