code = compile('a + 5', 'file.py', 'eval')
a = 5
print(eval(code))

print("-------------")

import parser

st = parser.expr('a + 5')
code = st.compile('file.py')
a = 5
print(eval(code))

print("-------------")


def load_suite(source_string):
    st = parser.suite(source_string)
    return st, st.compile()


def load_expression(source_string):
    st = parser.expr(source_string)
    return st, st.compile()


st, c = load_suite("print(1)")
eval(c)

"""
ST Objects
Ordered and equality comparisons are supported between ST objects. Pickling of ST objects (using the pickle module) is also supported.

parser.STType
The type of the objects returned by expr(), suite() and sequence2st().

ST objects have the following methods:

ST.compile(filename='<syntax-tree>')
Same as compilest(st, filename).

ST.isexpr()
Same as isexpr(st).

ST.issuite()
Same as issuite(st).

ST.tolist(line_info=False, col_info=False)
Same as st2list(st, line_info, col_info).

ST.totuple(line_info=False, col_info=False)
Same as st2tuple(st, line_info, col_info).
"""
