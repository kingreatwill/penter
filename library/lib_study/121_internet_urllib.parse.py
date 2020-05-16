# https://docs.python.org/zh-cn/3/library/urllib.parse.html
import urllib.parse
params = urllib.parse.urlencode({'spam': 1, 'eggs': 2, 'bacon': 0})
url = "http://www.musi-cal.com/cgi-bin/query?%s" % params
print(url)

import urllib.parse
o = urllib.parse.urlparse('http://www.cwi.nl:80/%7Eguido/Python.html')

print(o)
print(o.scheme)
print(o.port)
print(o.geturl())

# netloc 网络位置部分
# url1 = "scheme://netloc/path;parameters?query#fragment"
# scheme:[//[user:password@]host[:port]][/]path[?query][#fragment]
print(urllib.parse.urlparse('//www.cwi.nl:80/%7Eguido/Python.html'))

print(urllib.parse.urlparse('www.cwi.nl/%7Eguido/Python.html'))

print(urllib.parse.urlparse('help/Python.html'))

print(urllib.parse.urljoin('http://www.cwi.nl/%7Eguido/Python.html', 'FAQ.html'))
print(urllib.parse.urljoin('https://www.cwi.nl/%7Eguido/Python.html', '//www.python.org/%7Eguido'))

print(urllib.parse.urldefrag("https://i.cnblogs.com/EditPosts.aspx?opt=1#name"))


url = 'HTTP://www.Python.org/doc/#'
r1 = urllib.parse.urlsplit(url)
print(r1.geturl())

r2 = urllib.parse.urlsplit(r1.geturl())
print(r2.geturl())
#urlsplit将url分为5个部分
url ="https://i.cnblogs.com/EditPosts.aspx?opt=1#name"
print(urllib.parse.urlsplit(url))


import urllib.parse
#urlparse将url分为6个部分
url ="https://i.cnblogs.com/EditPosts.aspx?opt=1"
url_change = urllib.parse.urlparse(url) # 将url拆分为6个部分
query = url_change.query #取出拆分后6个部分中的查询模块query
lst_query = urllib.parse.parse_qsl(query)  #使用parse_qsl返回列表
dict1 =dict(lst_query)  #将返回的列表转换为字典
dict_query =urllib.parse.parse_qs(query)  #使用parse_qs返回字典
print("使用parse_qsl返回列表  ：",lst_query)
print("将返回的列表转换为字典 ：",dict1)
print("使用parse_qs返回字典   : ",dict_query)

# data = "test=test&test2=test2&test2=test3"
# print(urllib.parse.parse_qsl(data)) #返回列表
# print(urllib.parse.parse_qs(data))  #返回字典


print(urllib.parse.quote("https://i.cnblogs.com/EditPosts.aspx?opt=1"))
print(urllib.parse.quote_plus("https://i.cnblogs.com/EditPosts.aspx?opt=1"))
print(urllib.parse.unquote(urllib.parse.quote("https://i.cnblogs.com/EditPosts.aspx?opt=1")))

