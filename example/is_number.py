
#  isdigit() 方法检测字符串是否只由数字组成。
print ("234".isdigit())

# isnumeric() 方法检测字符串是否只由数字组成，数字可以是： Unicode 数字，全角数字（双字节），罗马数字，汉字数字。
#
# 指数类似 ² 与分数类似 ½ 也属于数字。
str = "runoob2016"
print (str.isnumeric())

str = "23443434"
print (str.isnumeric())

#s = '²3455'
s = '\u00B23455'
print(s.isnumeric())
# s = '½'
s = '\u00BD'
print(s.isnumeric())

a = "\u0030" #unicode for 0
print(a.isnumeric()) # true

b = "\u00B2" #unicode for ²
print(b.isnumeric()) # true

c = "10km2"
print(c.isnumeric()) # false

print("²".isnumeric()) # true

print("----------------")

# s.isdigit、isdecimal 和 s.isnumeric 区别

# isdigit()
#
# True: Unicode数字，byte数字（单字节），全角数字（双字节）
#
# False: 汉字数字，罗马数字，小数
#
# Error: 无


# isdecimal()
#
# True: Unicode数字，，全角数字（双字节）
#
# False: 罗马数字，汉字数字，小数
#
# Error: byte数字（单字节）

# isnumeric()
#
# True: Unicode 数字，全角数字（双字节），汉字数字
#
# False: 小数，罗马数字
#
# Error: byte数字（单字节）

num = "1"  #unicode
num.isdigit()   # True
num.isdecimal() # True
num.isnumeric() # True

num = "1" # 全角
num.isdigit()   # True
num.isdecimal() # True
num.isnumeric() # True

num = b"1" # byte
num.isdigit()   # True
# num.isdecimal() # AttributeError 'bytes' object has no attribute 'isdecimal'
# num.isnumeric() # AttributeError 'bytes' object has no attribute 'isnumeric'

num = "IV" # 罗马数字
num.isdigit()   # False
num.isdecimal() # False
num.isnumeric() # False

num = "四" # 汉字
num.isdigit()   # False
num.isdecimal() # False
num.isnumeric() # True
print("----------------")

def is_number1(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False


#教程代码当出现多个汉字数字时会报错，通过遍历字符串解决
#对汉字表示的数字也可分辨
def is_number(s):
    try:  # 如果能运行float(s)语句，返回True（字符串s是浮点数）
        float(s)
        return True
    except ValueError:  # ValueError为Python的一种标准异常，表示"传入无效的参数"
        pass  # 如果引发了ValueError这种异常，不做任何事情（pass：不做任何事情，一般用做占位语句）
    try:
        import unicodedata  # 处理ASCii码的包
        for i in s:
            unicodedata.numeric(i)  # 把一个表示数字的字符串转换为浮点数返回的函数
            #return True
        return True
    except (TypeError, ValueError):
        pass
    return False



# 测试字符串和数字
print(is_number('foo'))  # False
print(is_number('1'))  # True
print(is_number('1.3'))  # True
print(is_number('-1.37'))  # True
print(is_number('1e3'))  # True

# 测试 Unicode
# 阿拉伯语 5
print(is_number('٥'))  # True
# 泰语 2
print(is_number('๒'))  # True
# 中文数字
print(is_number('四'))  # True 四十四
# 版权号
print(is_number('©'))  # False