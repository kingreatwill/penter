import markdown


def demo():
    with open("some_file.txt", "r", encoding="utf-8") as input_file:
        text = input_file.read()
    # https://python-markdown.github.io/extensions/
    # , extensions=[MyExtClass(), 'myext', 'path.to.my.ext:MyExtClass']
    # 1. 支持自定义类
    # 2. 官方扩展https://python-markdown.github.io/extensions/#officially-supported-extensions
    # 3. 第三方扩展https://github.com/Python-Markdown/markdown/wiki/Third-Party-Extensions
    #  output_format='xhtml' Default
    html = markdown.markdown(text, extensions=['toc'], output_format='html5')


if __name__ == '__main__':
    demo()
