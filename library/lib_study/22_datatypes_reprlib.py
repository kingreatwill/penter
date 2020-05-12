from reprlib import recursive_repr
class MyList(list):
    @recursive_repr()
    def __repr__(self):
        return '<' + '|'.join(map(repr, self)) + '>'

m = MyList('abc')
m.append(m)
m.append('x')
print(m)


import  reprlib
r = reprlib.Repr()
print(r.maxlong)
print(r.repr("sffffffffff12222222222235555555555555568888888888888888888888888888888"))


import reprlib
import sys

class MyRepr(reprlib.Repr):
    def repr_TextIOWrapper(self, obj, level):
        if obj.name in {'<stdin>', '<stdout>', '<stderr>'}:
            return obj.name
        return repr(obj)
"""
<_io.TextIOWr...oding='UTF-8'>
 if hasattr(self, 'repr_' + typename):
            return getattr(self, 'repr_' + typename)(x, level)
"""

aRepr = MyRepr()
print(aRepr.repr(sys.stdin))         # prints '<stdin>'