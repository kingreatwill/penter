# 第三方模块 regex , 提供了与标准库 re 模块兼容的API接口, 同时还提供了额外的功能和更全面的Unicode支持。

import re

prog = re.compile('foo')
"""
Pattern.flags
正则匹配标记。这是可以传递给 compile() 的参数，任何 (?…) 内联标记，隐性标记比如 UNICODE 的结合。

Pattern.groups
捕获到的模式串中组的数量。

Pattern.groupindex
映射由 (?P<id>) 定义的命名符号组合和数字组合的字典。如果没有符号组，那字典就是空的。
"""

print(prog.match("foo too"))  # match从字符串第一个位置 如果你想定位 string 的任何位置，使用 search() 来替代（也可参考 search() vs. match() ）
print(prog.search("my foo too"))
print(prog.fullmatch("foo"))

print(re.match('foo', "Foo too", re.IGNORECASE))

print(re.findall('foo', "Foo too foo", re.IGNORECASE))
print(re.finditer('foo', "Foo too foo", re.IGNORECASE))

print(re.split(r'\W+', 'Words, words, words.'))
print(re.split(r'\W+', 'Words, words, words.', 1))

print(re.split(r'(\W+)', 'Words, words, words.'))
print(re.split(r'(\W+)', 'Words, words, words.', 2))

print(re.sub(r'def\s+([a-zA-Z_][a-zA-Z_0-9]*)\s*\(\s*\):',
             r'static PyObject*\npy_\1(void)\n{',
             'def myfunc():'))

print(re.subn(r'def\s+([a-zA-Z_][a-zA-Z_0-9]*)\s*\(\s*\):',
              r'static PyObject*\npy_\1(void)\n{',
              'def myfunc():'))

print(re.escape('http://www.python.org'))

match = re.search('foo', "Foo too", re.IGNORECASE)
if match:
    print(match[0])
    print(match.group())




import regex
# pip install regex
print(regex.match(r'(?(?=\d)\d+|\w+)', '123abc'))
print(regex.match(r'(?(?=\d)\d+|\w+)', 'abc123'))


