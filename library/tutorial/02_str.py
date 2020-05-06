print('C:\some\name')
print(r'C:\some\name')

print("""Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")
#等价于上面的
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")


# 相邻的两个或多个 字符串字面值 （引号引起来的字符）将会自动连接到一起.
text = ('Put several strings within parentheses '
'to have them joined together.')

print(type(text)) # 字符串
print(text)

print('Py' 'thon')

print(text[0])
# text[0]= 'X' # Python 中的字符串不能被修改
