# http://effbot.org/zone/element-index.htm
xml = """\
<?xml version="1.0"?>
<data>
    <country name="Liechtenstein">
        <rank>1</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
        <neighbor name="Austria" direction="E"/>
        <neighbor name="Switzerland" direction="W"/>
    </country>
    <country name="Singapore">
        <rank>4</rank>
        <year>2011</year>
        <gdppc>59900</gdppc>
        <neighbor name="Malaysia" direction="N"/>
    </country>
    <country name="Panama">
        <rank>68</rank>
        <year>2011</year>
        <gdppc>13600</gdppc>
        <neighbor name="Costa Rica" direction="W"/>
        <neighbor name="Colombia" direction="E"/>
    </country>
</data>
"""
import xml.etree.ElementTree as ET
import io

tree = ET.parse(io.StringIO(xml))  # or ET.parse('country_data.xml')
root = tree.getroot()
print(root.tag)

root = ET.fromstring(xml)
print(root.tag)
print(root[0][1].text)

for child in root:
    print(child.tag, child.attrib)

# Element.iter():可帮助递归遍历其下的所有子树（包括子级，子级的子级，等等）。
for neighbor in root.iter('neighbor'):
    print(neighbor.attrib)

# Element.findall() 仅查找当前元素的直接子元素中带有指定标签的元素。
# Element.find() 找带有特定标签的 第一个 子级，然后可以用 Element.text 访问元素的文本内容。
# Element.get 访问元素的属性:
for country in root.findall('country'):
    rank = country.find('rank').text
    name = country.get('name')
    print(name, rank)

# for rank in root.iter('rank'):
#     new_rank = int(rank.text) + 1
#     rank.text = str(new_rank)
#     rank.set('updated', 'yes')
#
# tree.write('output.xml')

# for country in root.findall('country'):
#     rank = int(country.find('rank').text)
#     if rank > 50:
#         root.remove(country)
#
# tree.write('output.xml')


a = ET.Element('a')
b = ET.SubElement(a, 'b')
c = ET.SubElement(a, 'c')
d = ET.SubElement(c, 'd')
ET.dump(a)

print("--------------使用命名空间解析XML")
ns_xml = """\
<?xml version="1.0"?>
<actors xmlns:fictional="http://characters.example.com"
        xmlns="http://people.example.com">
    <actor>
        <name>John Cleese</name>
        <fictional:character>Lancelot</fictional:character>
        <fictional:character>Archie Leach</fictional:character>
    </actor>
    <actor>
        <name>Eric Idle</name>
        <fictional:character>Sir Robin</fictional:character>
        <fictional:character>Gunther</fictional:character>
        <fictional:character>Commander Clement</fictional:character>
    </actor>
</actors>
"""
root = ET.fromstring(ns_xml)
for actor in root.findall('{http://people.example.com}actor'):
    name = actor.find('{http://people.example.com}name')
    print(name.text)
    for char in actor.findall('{http://characters.example.com}character'):
        print(' |-->', char.text)

ns = {'real_person': 'http://people.example.com',
      'role': 'http://characters.example.com'}

for actor in root.findall('real_person:actor', ns):
    name = actor.find('real_person:name', ns)
    print(name.text)
    for char in actor.findall('role:character', ns):
        print(' |-->', char.text)

print("-------------------- XMLPullParser")
parser = ET.XMLPullParser(['start', 'end'])
parser.feed('<mytag>sometext')
print(list(parser.read_events()))

parser.feed(' more text</mytag>')
for event, elem in parser.read_events():
    print(event)
    print(elem.tag, 'text=', elem.text)

print("----------- XPath")
import xml.etree.ElementTree as ET

root = ET.fromstring(xml)

# Top-level elements
print(root.findall("."))

# All 'neighbor' grand-children of 'country' children of the top-level
# elements
print(root.findall("./country/neighbor"))

# Nodes with name='Singapore' that have a 'year' child
print(root.findall(".//year/..[@name='Singapore']"))

# 'year' nodes that are children of nodes with name='Singapore'
print(root.findall(".//*[@name='Singapore']/year"))

# All 'neighbor' nodes that are the second child of their parent
print(root.findall(".//neighbor[2]"))

# All dublin-core "title" tags in the document
print(root.findall(".//{http://purl.org/dc/elements/1.1/}title"))

# 支持的XPath语法 https://docs.python.org/zh-cn/3/library/xml.etree.elementtree.html#supported-xpath-syntax

print(
    "-----Element 元素对象 https://docs.python.org/zh-cn/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element")
elm = root.findall(".//neighbor[2]")[0]
print(elm.tag)
print(elm.text)
print(elm.attrib)
print(elm.get("direction"))
print(elm.items())

print("--------------------使用default_loader加载xml文件")
# import xml.etree.ElementInclude
#
# # 非xml解析，直接返回字符串
# result = xml.etree.ElementInclude.default_loader(
#     href='codes/webpages.xml',
#     parse='text',
#     encoding='utf-8')
# print(':', type(result))
# print(result)
# print('------------------')
#
# # 作为xml解析返回xml.etree.ElementTree.Element对象。
# result = xml.etree.ElementInclude.default_loader(
#     href='codes/webpages.xml',
#     parse='xml',
#     encoding='utf-8')
#
# print(':', type(result))
# print(result)
print("--------------------使用include函数扩展xinclude")
# import xml.etree.ElementInclude
#
# # 由于版本变化，默认的常量值，可以根据已有的文档修改。
# xml.etree.ElementInclude.XINCLUDE_INCLUDE='{http://www.w3.org/2003/XInclude}include'
#
# # 作为xml解析返回xml.etree.ElementTree.Element对象。
# result = xml.etree.ElementInclude.default_loader(
#     href='codes/webpages.xml',
#     parse='xml',
#     encoding='utf-8')
#
# print('xinclude扩展前输出')
# for ele in result:
#     print(type(ele),ele)
#
# xml.etree.ElementInclude.include(result, loader=None)
#
# print('xinclude扩展后输出')
# for ele in result:
#     print(type(ele),ele)


print("-----ElementTree 对象 https://docs.python.org/zh-cn/3/library/xml.etree.elementtree.html#elementtree-objects")
html_xml = """\
<html>
    <head>
        <title>Example page</title>
    </head>
    <body>
        <p>Moved to <a href="http://example.org/">example.org</a>
        or <a href="http://example.com/">example.com</a>.</p>
    </body>
</html>
"""

from xml.etree.ElementTree import ElementTree

tree = ElementTree()
tree.parse(io.StringIO(html_xml))

p = tree.find("body/p")  # Finds first occurrence of tag p in body
print(p.text)

links = list(p.iter("a"))  # Returns list of all links
print(links)

for i in links:  # Iterates through all found links
    i.attrib["target"] = "blank"
#tree.write("output.xhtml")

print("------------------ XMLParser")
from xml.etree.ElementTree import XMLParser
class MaxDepth:                     # The target object of the parser
    maxDepth = 0
    depth = 0
    def start(self, tag, attrib):   # Called for each opening tag.
        self.depth += 1
        if self.depth > self.maxDepth:
            self.maxDepth = self.depth
    def end(self, tag):             # Called for each closing tag.
        self.depth -= 1
    def data(self, data):
        pass            # We do not need to do anything with data.
    def close(self):    # Called when all data has been parsed.
        return self.maxDepth

target = MaxDepth()
parser = XMLParser(target=target)
exampleXml = """
<a>
  <b>
  </b>
  <b>
    <c>
      <d>
      </d>
    </c>
  </b>
</a>"""
parser.feed(exampleXml)
parser.close()

