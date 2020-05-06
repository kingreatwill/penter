# 标准库简介
import os
print(os.getcwd())
#os.chdir('/server/accesslogs')   # Change current working directory
#os.system('mkdir today')   # Run the command mkdir in the system shell
# 一定要使用 import os 而不是 from os import * 。这将避免内建的 open() 函数被 os.open() 隐式替换掉，它们的使用方式大不相同。

# 对于日常文件和目录管理任务， shutil 模块提供了更易于使用的更高级别的接口:
import shutil
# shutil.copyfile('data.db', 'archive.db')
# shutil.move('/build/executables', 'installdir')

# glob 模块提供了一个在目录中使用通配符搜索创建文件列表的函数:
import glob
print(glob.glob('*.py'))

import sys
print(sys.argv)
# argparse 模块提供了一种更复杂的机制来处理命令行参数。 以下脚本可提取一个或多个文件名，并可选择要显示的行数:

import argparse

# parser = argparse.ArgumentParser(prog = 'top',
#     description = 'Show top lines from each file')
# parser.add_argument('filenames', nargs='+')
# parser.add_argument('-l', '--lines', type=int, default=10)
# args = parser.parse_args()
# print(args)
# 当在通过 python top.py --lines=5 alpha.txt beta.txt 在命令行运行时，该脚本会将 args.lines 设为 5 并将 args.filenames 设为 ['alpha.txt', 'beta.txt']。


# 字符串模式匹配
import re
print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))
print(re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat'))


"""
开发高质量软件的一种方法是在开发过程中为每个函数编写测试，并在开发过程中经常运行这些测试。
doctest 模块提供了一个工具，用于扫描模块并验证程序文档字符串中嵌入的测试。
测试构造就像将典型调用及其结果剪切并粘贴到文档字符串一样简单。
这通过向用户提供示例来改进文档，并且它允许doctest模块确保代码保持对文档的真实:
"""
def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

import doctest
doctest.testmod()   # automatically validate the embedded tests



from string import Template
t = Template('${village}folk send $$10 to $cause.')
print(t.substitute(village='Nottingham', cause='the ditch fund'))


import logging
logging.debug('Debugging information')
logging.info('Informational message')
logging.warning('Warning:config file %s not found', 'server.conf')
logging.error('Error occurred')
logging.critical('Critical error -- shutting down')


"""
import threading, zipfile

class AsyncZip(threading.Thread):
    def __init__(self, infile, outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile

    def run(self):
        f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print('Finished background zip of:', self.infile)

background = AsyncZip('mydata.txt', 'myarchive.zip')
background.start()
print('The main program continues to run in foreground.')

background.join()    # Wait for the background task to finish
print('Main program waited until background was done.')
"""

import weakref, gc
class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)
a = A(10)
d = weakref.WeakValueDictionary()
d['primary'] = a  # 需要class对象
#del a
gc.collect()
print(d['primary'])
