# json 提供了与标准库 marshal 和 pickle 相似的API接口。
# https://docs.python.org/zh-cn/3/library/json.html

import json

print(json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}]))

print(json.dumps("\"foo\bar"))

print(json.dumps('\u1234'))

print(json.dumps('\\'))

print(json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True))

from io import StringIO

io = StringIO()
json.dump(['streaming API'], io)
print(io.getvalue())

# 不要空格
print(json.dumps([1, 2, 3, {'4': 5, '6': 7}], separators=(',', ':')))
# 美化输出
print(json.dumps({'4': 5, '6': 7}, sort_keys=True, indent=4))

# JSON解码:
print(json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]'))
print(json.loads('"\\"foo\\bar"'))
io = StringIO('["streaming API"]')
print(json.load(io))


# 特殊JSON对象解码:
def as_complex(dct):
    if '__complex__' in dct:
        return complex(dct['real'], dct['imag'])
    return dct


print(json.loads('{"__complex__": true, "real": 1, "imag": 2}',
                 object_hook=as_complex))

import decimal

print(json.loads('1.1', parse_float=decimal.Decimal))


# 扩展 JSONEncoder:

class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, complex):
            return [obj.real, obj.imag]
        # Let the base class default method raise the TypeError
        return json.JSONEncoder.default(self, obj)


print(json.dumps(2 + 1j, cls=ComplexEncoder))
print(ComplexEncoder().default(2 + 1j))
print(ComplexEncoder().encode(2 + 1j))

print(list(ComplexEncoder().iterencode(2 + 1j)))

# 从命令行使用 json.tool 来验证并美化输出：https://docs.python.org/zh-cn/3/library/json.html#module-json.tool
"""
$ echo '{"json":"obj"}' | python -m json.tool
{
    "json": "obj"
}

$ python -m json.tool mp_films.json
"""

print(
    "---------- 解码器 class json.JSONDecoder(*, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, strict=True, object_pairs_hook=None)")
"""
默认情况下，解码执行以下翻译:
JSON        Python
object      dict
array       list
string      str
number(int)  int
number(real) float
true        True
false       False
null        None




decode(s)
raw_decode(s)
"""

print("----------编码器 class json.JSONEncoder(*, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, sort_keys=False, indent=None, separators=None, default=None)")

"""
默认支持以下对象和类型：
Python      JSON
dict        object
list, tuple  array
str         string
int, float, int 和 float 派生的枚举       number
True        true
False       false
None        null

default(o)
encode(o)
iterencode(o)
"""


