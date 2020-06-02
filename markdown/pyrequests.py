import requests
from pyquery import PyQuery as pq


def page_source(use_url, use_selector, **kwargs):
    return pq(url=use_url, opener=lambda url, **kw: requests.get(url,
                                                             headers={
                                                                 'User-Agent': kwargs["useragent"]
                                                             }).content)
