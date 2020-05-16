# https://docs.python.org/zh-cn/3/library/xml.dom.html#objects-in-the-dom

# https://docs.python.org/zh-cn/3/library/xml.dom.minidom.html

# https://docs.python.org/zh-cn/3/library/xml.dom.pulldom.html


print("""
DOM(Document Object Model)，即文档对象模型

Minimal DOM implementation
minidom模块适用于较小的XML文档，因为它将整个文档读到内存中。

而pulldom模块则适用于较大的XML文档，因为它不将整个XML文档读入内存。
""")

print("----------------minidom")
from xml.dom.minidom import parse, parseString

# dom1 = parse('c:\\temp\\mydata.xml')  # parse an XML file by name
#
# datasource = open('c:\\temp\\mydata.xml')
# dom2 = parse(datasource)  # parse an open file

dom3 = parseString('<myxml>Some data<empty/> some more data</myxml>')
print(dom3)

import xml.dom.minidom

document = """\
<slideshow>
<title>Demo slideshow</title>
<slide><title>Slide title</title>
<point>This is a demo</point>
<point>Of a program for processing slides</point>
</slide>

<slide><title>Another demo slide</title>
<point>It is important</point>
<point>To have more than</point>
<point>one slide</point>
</slide>
</slideshow>
"""

dom = xml.dom.minidom.parseString(document)


def getText(nodelist):
    rc = []
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            rc.append(node.data)
    return ''.join(rc)


def handleSlideshow(slideshow):
    print("<html>")
    handleSlideshowTitle(slideshow.getElementsByTagName("title")[0])
    slides = slideshow.getElementsByTagName("slide")
    handleToc(slides)
    handleSlides(slides)
    print("</html>")


def handleSlides(slides):
    for slide in slides:
        handleSlide(slide)


def handleSlide(slide):
    handleSlideTitle(slide.getElementsByTagName("title")[0])
    handlePoints(slide.getElementsByTagName("point"))


def handleSlideshowTitle(title):
    print("<title>%s</title>" % getText(title.childNodes))


def handleSlideTitle(title):
    print("<h2>%s</h2>" % getText(title.childNodes))


def handlePoints(points):
    print("<ul>")
    for point in points:
        handlePoint(point)
    print("</ul>")


def handlePoint(point):
    print("<li>%s</li>" % getText(point.childNodes))


def handleToc(slides):
    for slide in slides:
        title = slide.getElementsByTagName("title")[0]
        print("<p>%s</p>" % getText(title.childNodes))


handleSlideshow(dom)

print("----------------pulldom")
# from xml.dom.pulldom import parse
# from xml.sax import make_parser
# from xml.sax.handler import feature_external_ges
#
# parser = make_parser()
# parser.setFeature(feature_external_ges, True)
# parse(filename, parser=parser)
document = """\
<slideshow>
<title>Demo slideshow</title>

<slide><title>Slide title</title>
<item price="51">This is a demo 51</item>
<point>Of a program for processing slides</point>
</slide>

<item price="53">This is a demo 53</item>

<slide><title>Another demo slide</title>
<point>It is important</point>
<point>To have more than</point>
<point>one slide</point>
</slide>

</slideshow>
"""
from xml.dom import pulldom
import io

doc = pulldom.parse(io.StringIO(document))
for event, node in doc:
    if event == pulldom.START_ELEMENT and node.tagName == 'item':
        if int(node.getAttribute('price')) > 50:
            doc.expandNode(node)
            print(node.toxml())


import xml.dom.pulldom

xml_str = '<html><title>Foo</title> <p>Some text <div>and more</div></p> </html>'
doc = xml.dom.pulldom.parseString(xml_str)

for event, node in doc:
    if event == pulldom.START_ELEMENT and node.tagName == 'p':
        # Following statement only prints '<p/>'
        print(node.toxml())

        doc.expandNode(node)
        # Following statement prints node with all its children '<p>Some text <div>and more</div></p>'
        print(node.toxml())
