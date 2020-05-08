import string

# 字符串常量
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)
print(string.hexdigits)
print(string.octdigits)
print(string.punctuation)
print(string.printable)
print(string.whitespace)
print("---------------------")
# 大驼峰
print(string.capwords("acd dEF"))
print("---------------------")
# class string.Formatter 字符串格式化
# str.format() 方法和 Formatter 类共享相同的格式字符串语法
form = string.Formatter()
print(form.format("{}{}", 1, 2))
print(form.vformat("{}{}{name}", (3, 4), {"name": "nihao"}))

print(form.format("my name is {name!r:*^30}", name="data"))

"Harold's a clever {0!s}"  # Calls str() on the argument first
"Bring out the holy {name!r}"  # Calls repr() on the argument first
"More {!a}"  # Calls ascii() on the argument first

for i, v in enumerate(form.parse("my name is{}xxx{}abc{name}!!")):
    print(i, v)
for i, v in enumerate(form.parse("my name is {person[0].name!r:*^30}")):
    print(i, v)
# (literal_text, field_name, format_spec, conversion)

print(form.get_field('name', (), {"name": "nihao"}))
print(form.get_value('name', (), {"name": "nihao"}))
print(form.get_value(form.get_field('name', (), {"name": "nihao"})[1], (), {"name": "nihao"}))

# 不知道怎么使用？？？print(form.check_unused_args('{}', (), {"name": "nihao"}))
# 不知道怎么使用？？？print(form.format_field())
# 不知道怎么使用？？？print(form.convert_field())


print('{:+f}; {:+f}'.format(3.14, -3.14))
print('{: f}; {: f}'.format(3.14, -3.14))
print('{:-f}; {:-f}'.format(3.14, -3.14))

print("int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}".format(42))
print("int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(42))

import datetime

d = datetime.datetime(2020, 5, 6, 20, 15, 58)
print('{:%Y-%m-%d %H:%M:%S}'.format(d))  # '{0:%Y-%m-%d %H:%M:%S}'
# $$ 为转义符号；它会被替换为单个的 $。


print("---------------------")
## class string.Template
"""
$$ 为转义符号；它会被替换为单个的 $。
$identifier 为替换占位符，它会匹配一个名为 "identifier" 的映射键。 
在默认情况下，"identifier" 限制为任意 ASCII 字母数字（包括下划线）组成的字符串，不区分大小写，以下划线或 ASCII 字母开头。 在 $ 字符之后的第一个非标识符字符将表明占位符的终结。
${identifier} 等价于 $identifier。 当占位符之后紧跟着有效的但又不是占位符一部分的标识符字符时需要使用，例如 "${noun}ification"。
"""
t = string.Template('$who likes $what  $$10 ${identifier}')

print(t.safe_substitute({"who":"xxx", "what":"aaa"}))
print(t.substitute(who="xxx", what="aaa")) # ${identifier} 异常

