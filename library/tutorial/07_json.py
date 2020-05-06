year = 2016
event = 'Referendum'

print(f'Results of the {year} {event}')

"""
字符串对象的 str.rjust() 方法通过在左侧填充空格来对给定宽度的字段中的字符串进行右对齐。类似的方法还有 str.ljust() 和 str.center()
"""

import json
print(json.dumps([1, 'simple', 'list']))
print(json.loads('[1, "simple", "list"]'))

# 如果你有一个对象 x,dumps() 函数的另一个变体叫做 dump() ，它只是将对象序列化为 text file 。因此，如果 f 是一个 text file 对象，我们可以这样做:
# json.dump(x, f)
# 要再次解码对象，如果 f 是一个打开的以供阅读的 text file 对象:
#
# x = json.load(f)

"""
pickle - 封存模块
与 JSON 不同，pickle 是一种允许对任意复杂 Python 对象进行序列化的协议。因此，它为 Python 所特有，不能用于与其他语言编写的应用程序通信。默认情况下它也是不安全的：如果数据是由熟练的攻击者精心设计的，则反序列化来自不受信任来源的 pickle 数据可以执行任意代码。
"""