# pip install lxml

# https://github.com/lxml/lxml



from lxml import etree
test ="""\
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Study/title>
</head>
<body>

<h1>webpage</h1>
<p>source link</p>
<a href="http://www.runoob.com/html/html-tutorial.html" target="_blank">HTML</a> 
<a href="http://www.runoob.com/python/python-tutorial.html" target="_blank">Python</a>
<a href="http://www.runoob.com/cplusplus/cpp-tutorial.html" target="_blank">C++</a> 
<a href="http://www.runoob.com/java/java-tutorial.html" target="_blank">Java</a>
</body>
</html>
"""
html = etree.HTML(test)
a_tags = html.xpath('//a')
print(a_tags)

import lxml.html
html2 = lxml.html.fromstring(test)
