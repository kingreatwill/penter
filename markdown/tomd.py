from pyquery import PyQuery as pq

__all__ = ['Tomd', 'convert']

MARKDOWN = {
    'h1': "#",
    'h2': "##",
    'h3': "###",
    'h4': "####",
    'h5': "#####",
    'h6': "######",
    "blockquote": ">",
    "li": "-",
    "hr": "---",
    "p": "\n"
}

INLINE = {
    'em': ('*', '*'),
    'strong': ('**', '**'),
    'b': ('**', '**'),
    'i': ('*', '*'),
    'del': ('~~', '~~'),
    "code": ('`', '`')
}

split_str = "++++++++++++++++++"


class Tomd:
    def __init__(self, html=''):
        self.html = html
        self._markdown = ""

    def convert(self, param):
        d = None
        if isinstance(param, pq):
            d = param
        elif isinstance(param, str):
            d = pq(param)
        if not d:
            return ""

        d('head').remove()
        # 先处理图片, 防止图片在span或a中;
        for e in d('img'):
            inline_mark = f"![{pq(e).attr('alt')}]({pq(e).attr('src')})"
            pq(e).replace_with(inline_mark)

        for e in d('span'):
            inline_mark = pq(e).text()
            pq(e).replace_with(inline_mark)

        for e in d('a'):
            href = pq(e).attr('href')
            if href and "http" in href:
                inline_mark = f"[{pq(e).text()}]({href})"
                pq(e).replace_with(inline_mark)

        for e in d('thead'):
            inline_mark = pq(e).outer_html() + '|------' * (pq(e)('th').length - 1)
            pq(e).replace_with(inline_mark)

        for e in d('th,td'):
            inline_mark = "|" + pq(e).text()
            pq(e).replace_with(inline_mark)

        for e in d('pre'):
            inline_mark = "```" + split_str + pq(e).html() + split_str + "```" + split_str
            pq(e).replace_with(inline_mark)

        selectors = ','.join(INLINE.keys())
        for e in d(selectors):
            inline_mark = INLINE.get(e.tag)[0] + pq(e).text() + INLINE.get(e.tag)[1]
            pq(e).replace_with(inline_mark)

        selectors = ','.join(MARKDOWN.keys())
        for e in d(selectors):
            inline_mark = split_str + MARKDOWN.get(e.tag) + " " + pq(e).text() + split_str
            pq(e).replace_with(inline_mark)

        self._markdown = d.text().replace(split_str, '\n')

        return self._markdown

    @property
    def markdown(self):
        self.convert(self.html)
        return self._markdown


_inst = Tomd()
convert = _inst.convert
