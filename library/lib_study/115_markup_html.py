import html

print("-------------快速入门")
hs = html.escape("<>")
print(hs)
hl = html.unescape("&gt; &#62; &#x3e;")
print(hl)

print("-----html.entities")
# https://html.spec.whatwg.org/multipage/named-characters.html#named-character-references
print(html.entities.html5)
print(html.entities.entitydefs)
print(html.entities.name2codepoint)
print(html.entities.codepoint2name)
print("-----html.parser")

from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag, attrs)

    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)

    def handle_data(self, data):
        print("Encountered some data  :", data)


parser = MyHTMLParser()
parser.feed('<html><head><title>Test</title></head>'
            '<body><h1 id="hid">Parse me!</h1></body></html>')


from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start tag:", tag)
        for attr in attrs:
            print("     attr:", attr)

    def handle_endtag(self, tag):
        print("End tag  :", tag)

    def handle_data(self, data):
        print("Data     :", data)

    def handle_comment(self, data):
        print("Comment  :", data)

    def handle_entityref(self, name):
        c = chr(name2codepoint[name])
        print("Named ent:", c)

    def handle_charref(self, name):
        if name.startswith('x'):
            c = chr(int(name[1:], 16))
        else:
            c = chr(int(name))
        print("Num ent  :", c)

    def handle_decl(self, data):
        print("Decl     :", data)

parser = MyHTMLParser()
parser.feed('<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" '
            '"http://www.w3.org/TR/html4/strict.dtd">')

parser.feed('<img src="python-logo.png" alt="The Python logo">')

parser.feed('<h1>Python</h1>')
parser.feed('<style type="text/css">#python { color: green }</style>')

parser.feed('<script type="text/javascript">'
            'alert("<strong>hello!</strong>");</script>')

parser.feed('<!-- a comment -->'
            '<!--[if IE 9]>IE-specific content<![endif]-->')
parser.feed('&gt;&#62;&#x3E;')

# 填充不完整的块给 feed() 执行，handle_data() 可能会多次调用（除非 convert_charrefs 被设置为 True ）:
for chunk in ['<sp', 'an>buff', 'ered ', 'text</s', 'pan>']:
    parser.feed(chunk)

# 解析无效的 HTML (例如：未引用的属性）也能正常运行:
parser.feed('<p><a class=link href=#main>tag soup</p ></a>')
