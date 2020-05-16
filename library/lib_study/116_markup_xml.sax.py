import xml.sax
# https://docs.python.org/zh-cn/3/library/xml.sax.handler.html
# https://docs.python.org/zh-cn/3/library/xml.sax.utils.html
# https://docs.python.org/zh-cn/3/library/xml.sax.reader.html

# https://docs.python.org/zh-cn/3/library/pyexpat.html

xml_str = '<html><title>Foo</title> <p>Some text <div>and more</div></p> </html>'

import xml.parsers.expat

# 3 handler functions
def start_element(name, attrs):
    print('Start element:', name, attrs)
def end_element(name):
    print('End element:', name)
def char_data(data):
    print('Character data:', repr(data))

p = xml.parsers.expat.ParserCreate()

p.StartElementHandler = start_element
p.EndElementHandler = end_element
p.CharacterDataHandler = char_data

p.Parse("""<?xml version="1.0"?>
<parent id="top"><child1 name="paul">Text goes here</child1>
<child2 name="fred">More text</child2>
</parent>""", 1)