from timeit import Timer
print(Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())

print(Timer('a,b = b,a', 'a=1; b=2').timeit())

# profile 和 pstats 模块提供了针对更大代码块的时间度量工具。
# https://docs.python.org/3/library/profile.html

import cProfile
import re
cProfile.run('re.compile("foo|bar")')