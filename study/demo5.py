import math

x = 10 * 3.25
y = 200 * 200
print(repr((x, y, ('Google', 'Runoob'))))
print(str((x, y, ('Google', 'Runoob'))))
hello = 'hello, runoob\n'
print(hello)
print(repr(hello))

# 输出一个平方与立方的表:
#  rjust() 方法, 它可以将字符串靠右, 并在左边填充空格。还有类似的方法, 如 ljust() 和 center()。
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x * x).rjust(3), end=' ')
    print(repr(x * x * x).rjust(4))

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x * x, x * x * x))

# zfill(), 它会在数字的左边填充 0，如下所示：
print('12'.zfill(5))
print('-3.14'.zfill(7))
print('3.14159265359'.zfill(5))

print('{}网址： "{}!"'.format('xxx', 'www.xxx.com'))
print('{1} 和 {0}'.format('Google', 'Runoob'))
print('{name}网址： {site}'.format(name='xxx', site='www.xxx.com'))
print('站点列表 {0}, {1}, 和 {other}。'.format('Google', 'Runoob', other='Taobao'))
print('常量 PI 的值近似为： {}。'.format(math.pi))

# !a (使用 ascii()), !s (使用 str()) 和 !r (使用 repr()) 可以用于在格式化某个值之前对其进行转化:
print('xxxx： {!r}。'.format("mmmmm"))

print('常量 PI 的值近似为 {0:.3f}。'.format(math.pi))

# 后传入一个整数, 可以保证该域至少有这么多的宽度。 用于美化表格时很有用。
table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
for name, number in table.items():
  print('{0:10} ==> {1:10d}'.format(name, number))

# 传入一个字典, 然后使用方括号 [] 来访问键值 :
print('Runoob: {0[Runoob]:d}; Google: {0[Google]:d}; Taobao: {0[Taobao]:d}'.format(table))

# 也可以通过在 table 变量前使用 ** 来实现相同的功能：双星号（**）将参数以字典的形式导入:
print('Runoob: {Runoob:d}; Google: {Google:d}; Taobao: {Taobao:d}'.format(**table))
