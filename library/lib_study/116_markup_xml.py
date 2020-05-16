"""
sax2是The Simple API for xml的意思，是一种解析xml的方式。
解析xml主要有二种方式，
一个是dom，比较常用，解析完成以后再内存形成一个结构，
另外一个方式就是一种事件解析方式，就是在解析到一定的内容抛出事件，继续向后处理，xml读取完成，也就解析完成，xml的内容并不存入内存。

xml.etree.ElementTree： ElementTree API，一个简单而轻量级的XML处理器

xml.dom：DOM API 定义
xml.dom.minidom：最小的 DOM 实现
xml.dom.pulldom：支持构建部分 DOM 树

xml.sax：SAX2 基类和便利函数
xml.parsers.expat：Expat解析器绑定
"""

"""
XML 漏洞
XML 处理模块对于恶意构造的数据是不安全的。 攻击者可能滥用 XML 功能来执行拒绝服务攻击、访问本地文件、生成与其它计算机的网络连接或绕过防火墙。

种类                          |sax        |etree      |minidom        |pulldom        |xmlrpc
billion laughs              |易受攻击     |易受攻击    |易受攻击         |易受攻击        |易受攻击
quadratic blowup            |易受攻击       |易受攻击   |易受攻击           |易受攻击       |易受攻击
external entity expansion   |安全 (4)     |安全 (1)     |安全 (2)         |安全 (4)     |安全 (3)
DTD retrieval               |安全 (4)     |安全         |安全         |安全 (4)         |安全
decompression bomb          |安全         |安全         |安全         |安全             |易受攻击

1. xml.etree.ElementTree 不会扩展外部实体并在实体发生时引发 ParserError。
2. xml.dom.minidom 不会扩展外部实体，只是简单地返回未扩展的实体。
3. xmlrpclib 不扩展外部实体并省略它们。
4. 从 Python 3.7.1 开始，默认情况下不再处理外部通用实体。
"""