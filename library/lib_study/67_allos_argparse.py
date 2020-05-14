import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', "-s", dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
print(parser.parse_args(['--sum', '7', '-1', '42']))
# 调用 parse_args() 将返回一个具有 integers 和 accumulate 两个属性的对象。
# integers 属性将是一个包含一个或多个整数的列表，
# 而 accumulate 属性当命令行中指定了 --sum 参数时将是 sum() 函数，否则则是 max() 函数。
print(args.accumulate(args.integers))
# python 67_allos_argparse.py -h

# 最大值
# python 67_allos_argparse.py 1 3 5

# 求和
# python 67_allos_argparse.py 1 3 5 --sum


"""
class argparse.ArgumentParser(prog=None, usage=None, description=None, epilog=None, 
parents=[], formatter_class=argparse.HelpFormatter, prefix_chars='-', fromfile_prefix_chars=None, 
argument_default=None, conflict_handler='error', add_help=True, allow_abbrev=True)

prog - 程序的名称（默认：sys.argv[0]）
usage - 描述程序用途的字符串（默认值：从添加到解析器的参数生成）
description - 在参数帮助文档之前显示的文本（默认值：无）
epilog - 在参数帮助文档之后显示的文本（默认值：无）
parents - 一个 ArgumentParser 对象的列表，它们的参数也应包含在内
formatter_class - 用于自定义帮助文档输出格式的类
prefix_chars - 可选参数的前缀字符集合（默认值：'-'）
fromfile_prefix_chars - 当需要从文件中读取其他参数时，用于标识文件名的前缀字符集合（默认值：None）
argument_default - 参数的全局默认值（默认值： None）
conflict_handler - 解决冲突选项的策略（通常是不必要的）
add_help - 为解析器添加一个 -h/--help 选项（默认值： True）
allow_abbrev - 如果缩写是无歧义的，则允许缩写长选项 （默认值：True）

E:\openjw\penter\library\lib_study>python 67_allos_argparse.py -h
usage: 67_allos_argparse.py [-h] [--sum] N [N ...]    67_allos_argparse.py 可以用 prog='myprogram' 指定
                                                      usage: 后面的  usage='%(prog)s [options]'

Process some integers.

positional arguments:
  N           an integer for the accumulator

optional arguments:
  -h, --help  show this help message and exit
  --sum       sum the integers (default: find the max)
epilog参数内容，默认无

formatter_class
class argparse.RawDescriptionHelpFormatter
class argparse.RawTextHelpFormatter
class argparse.ArgumentDefaultsHelpFormatter
class argparse.MetavarTypeHelpFormatter
"""
# parser = argparse.ArgumentParser(prog='PROG', usage='%(prog)s [options]')
# parser.add_argument('--foo', nargs='?', help='foo help')
# parser.add_argument('bar', nargs='+', help='bar help')
# parser.print_help()

print("--------------重点add_argument() 方法")
"""
ArgumentParser.add_argument(name or flags...[, action][, nargs][, const][, default][, type][, choices][, required][, help][, metavar][, dest])

name or flags - 一个命名或者一个选项字符串的列表，例如 foo 或 -f, --foo。
action - 当参数在命令行中出现时使用的动作基本类型。
nargs - 命令行参数应当消耗的数目。
const - 被一些 action 和 nargs 选择所需求的常数。
default - 当参数未在命令行中出现时使用的值。
type - 命令行参数应当被转换成的类型。
choices - 可用的参数的容器。
required - 此命令行选项是否可省略 （仅选项可用）。
help - 一个此选项作用的简单描述。
metavar - 在使用方法消息中使用的参数值示例。
dest - 被添加到 parse_args() 所返回对象上的属性名。

# 位置参数 name
parser.add_argument('integers', metavar='N', type=int, nargs='+',help='an integer for the accumulator')
# 选项 flags
parser.add_argument('--sum',"-s", dest='accumulate', action='store_const',const=sum, default=max,help='sum the integers (default: find the max)')
当 parse_args() 被调用，选项会以 - 前缀识别，剩下的参数则会被假定为位置参数

# nargs https://docs.python.org/zh-cn/3/library/argparse.html#nargs
N （一个整数）。命令行中的 N 个参数会被聚集到一个列表中。 例如:
'?'。如果可能的话，会从命令行中消耗一个参数，并产生一个单一项。如果当前没有命令行参数，则会产生 default 值。
'*'。所有当前命令行参数被聚集到一个列表中。注意通过 nargs='*'来实现多个位置参数通常没有意义，但是多个选项是可能的。
'+'。和 '*' 类似，所有当前命令行参数被聚集到一个列表中。另外，当前没有至少一个命令行参数时会产生一个错误信息。
argarse.REMAINDER。所有剩余的命令行参数被聚集到一个列表中。这通常在从一个命令行功能传递参数到另一个命令行功能中时有用:

# const
对 'store_const' 和 'append_const' 动作， const 命名参数必须给出。对其他动作，默认为 None。

# default

# type
一般的内建类型和函数可以直接被 type 参数使用


# action https://docs.python.org/zh-cn/3/library/argparse.html#action
'store' - 存储参数的值。这是默认的动作。例如:
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo')
>>> parser.parse_args('--foo 1'.split())
Namespace(foo='1')

'store_const' - 存储被 const 命名参数指定的值。 'store_const' 动作通常用在选项中来指定一些标志。例如:
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo', action='store_const', const=42)
>>> parser.parse_args(['--foo'])
Namespace(foo=42)

'store_true' and 'store_false'
'append'
'append_const'
'count'
'help'
'version'
'extend'
自定义 class FooAction(argparse.Action):
"""
