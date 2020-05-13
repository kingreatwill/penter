"""
模式  意义

*   匹配所有

?   匹配任何单个字符

[seq]   匹配 seq 中的任何字符

[!seq]   匹配任何不在 seq 中的字符

"""

import fnmatch
import os

for file in os.listdir('.'):
    if fnmatch.fnmatch(file, '*.py'):
        print(file)

print(fnmatch.filter(os.listdir('.'), '*.py'))
print([n for n in os.listdir('.') if fnmatch.fnmatch(n, '*.py')])

import re

regex = fnmatch.translate('*.py')
print(regex)

reobj = re.compile(regex)
print(reobj.match('foobar.py'))