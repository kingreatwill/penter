# 文本自动换行与填充
import textwrap

print(textwrap.wrap("123456789cccccxxxxxx", width=8))
print(textwrap.wrap("123456789cccccxxxxxx", width=8, max_lines=2, placeholder="!!!"))

# 对 text 中的单独段落自动换行，并返回一个包含被自动换行段落的单独字符串,特别要说明的是，fill() 接受与 wrap() 完全相同的关键字参数。
print(textwrap.fill("123456789cccccxxxxxx", width=8))
# fill() 是以下语句的快捷方式 "\n".join(wrap(text, ...))
print("\n".join(textwrap.wrap("123456789cccccxxxxxx", 8)))

print(textwrap.shorten("Hello  world!", width=12))
print(textwrap.shorten("Hello  world!", width=11, placeholder="..."))

# 移除 text 中每一行的任何相同前缀空白符。#
# 这可以用来清除三重引号字符串行左侧空格，而仍然在源码中显示为缩进格式。
# 请注意制表符和空格符都被视为是空白符，但它们并不相等：以下两行 "  hello" 和 "\thello" 不会被视为具有相同的前缀空白符。#
# 只包含空白符的行会在输入时被忽略并在输出时被标准化为单个换行符。
def test():
    # end first line with \ to avoid the empty line!
    s = '''\
    hello
      world
    '''
    print(repr(s))          # prints '    hello\n      world\n    '
    print(repr(textwrap.dedent(s)))  # prints 'hello\n  world\n'

test()

# textwrap.indent(text, prefix, predicate=None)
# 将 prefix 添加到 text 中选定行的开头。
print(textwrap.indent("s 456\n 789", '  '))
# 可选的 predicate 参数可用来控制哪些行要缩进
print(textwrap.indent("s 456\n 789", '+ ', lambda line: True))


# class textwrap.TextWrapper(**kwargs)
wrapper = textwrap.TextWrapper(initial_indent="* ")
print(wrapper.wrap("xxx xxxx"))