import configparser
# https://docs.python.org/zh-cn/3/library/configparser.html
# 配置文件是由小节组成的，每个小节都有一个 [section] 标头，加上多个由特定字符串 (默认为 = 或 : 1) 分隔的键/值条目。
# 默认情况下小节名对大小写敏感而键对大小写不敏感 1。 键和值开头和末尾的空格会被移除。 值可以被省略，在此情况下键/值分隔符也可以被省略。
# 值还可以跨越多行，只要其他行带有比值的第一行更深的缩进。 依据解析器的具体模式，空白行可能被视为多行值的组成部分也可能被忽略。
# 配置文件可以包含注释，要带有指定字符前缀 (默认为 # 和 ; 1)。 注释可以单独出现于原本的空白行，并可使用缩进
config = configparser.ConfigParser()
config['DEFAULT'] = {'ServerAliveInterval': '45',
                     'Compression': 'yes',
                     'CompressionLevel': '9'}
config['bitbucket.org'] = {}
config['bitbucket.org']['User'] = 'hg'
config['topsecret.server.com'] = {}
topsecret = config['topsecret.server.com']
topsecret['Port'] = '50022'  # mutates the parser
topsecret['ForwardX11'] = 'no'  # same here
config['DEFAULT']['ForwardX11'] = 'yes'
with open('57_fileformats_configparser.ini', 'w') as configfile:
    config.write(configfile)

config_r = configparser.ConfigParser()
print(config_r.sections())
config_r.read('57_fileformats_configparser.ini')
print(config.sections())
print(config['bitbucket.org']['UseR'])  # hg   (不区分大小写)
# 最后一个类型的处理最为有趣，因为简单地将值传给 bool() 是没有用的，bool('False') 仍然会是 True。
# 为解决这个问题配置解析器还提供了 getboolean()。
# 这个方法对大小写不敏感并可识别 'yes'/'no', 'on'/'off', 'true'/'false' 和 '1'/'0' 1 等布尔值。 例如:
topsecret = config['topsecret.server.com']

print(topsecret.getboolean('ForwardX11'))
print(config['bitbucket.org'].getboolean('ForwardX11'))
print(config.getboolean('bitbucket.org', 'Compression'))

# 也可以用get来获取，当没有值的给个回退值
print(topsecret.get('Cipher'))
print(topsecret.get('Cipher', '3des-cbc'))


print("---------------class configparser.BasicInterpolation")
"""
[Paths]
home_dir: /Users
my_dir: %(home_dir)s/lumberjack
my_pictures: %(my_dir)s/Pictures

[Escape]
gain: 80%%  # use a %% to escape the % sign (% is the only character that needs to be escaped)

在上面的例子里，ConfigParser 的 interpolation 设为 BasicInterpolation()，这会将 %(home_dir)s 求解为 home_dir 的值 (在这里是 /Users)。 
%(my_dir)s 的将被实际求解为 /Users/lumberjack。 所有插值都是按需进行的，这样引用链中使用的键不必以任何特定顺序在配置文件中指明。

当 interpolation 设为 None 时，解析器会简单地返回 %(my_dir)s/Pictures 作为 my_pictures 的值，并返回 %(home_dir)s/lumberjack 作为 my_dir 的值。
"""
print("---------------class configparser.ExtendedInterpolation")
"""
parser = ConfigParser(interpolation=ExtendedInterpolation())

[Paths]
home_dir: /Users
my_dir: ${home_dir}/lumberjack
my_pictures: ${my_dir}/Pictures

[Escape]
cost: $$80  # use a $$ to escape the $ sign ($ is the only character that needs to be escaped)


[Common]
home_dir: /Users
library_dir: /Library
system_dir: /System
macports_dir: /opt/local

[Frameworks]
Python: 3.2
path: ${Common:system_dir}/Library/Frameworks/

[Arthur]
nickname: Two Sheds
last_name: Jackson
my_dir: ${Common:home_dir}/twosheds
my_pictures: ${my_dir}/Pictures
python_dir: ${Frameworks:path}/Python/Versions/${Frameworks:Python}


一个用于插值的替代处理程序实现了更高级的语法，它被用于 zc.buildout 中的实例。 扩展插值使用 ${section:option} 来表示来自外部小节的值。 
插值可以跨越多个层级。 为了方便使用，section: 部分可被省略，插值会默认作用于当前小节（可能会从特殊小节获取默认值）。

例如，上面使用基本插值描述的配置，使用扩展插值将是这个样子:
"""