# 必需参数
# 可写函数说明
def printme(str):
    "打印任何传入的字符串"
    print(str)
    return


# 调用 printme 函数，不加参数会报错
# printme()
printme("你好")
printme(str = "你好")


# 可写函数说明
def printinfo(name, age):
    "打印任何传入的字符串"
    print("名字: ", name)
    print("年龄: ", age)
    return

# 调用printinfo函数
printinfo(age=50, name="runoob")

# 默认参数
# 可写函数说明
def printinfo2(name, age=35):
    "打印任何传入的字符串"
    print("名字: ", name)
    print("年龄: ", age)
    return


# 调用printinfo函数
printinfo2(age=50, name="runoob")
print("------------------------")
printinfo2(name="runoob")


# 不定长参数
# 加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数。
# 可写函数说明
def printinfo3(arg1, *xxx):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    print(xxx)

# 调用printinfo 函数
printinfo3(70, 60, 50)


# 可写函数说明
def printinfo5(arg1, *vartuple):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    for var in vartuple:
        print(var)
    return
# 调用printinfo 函数
printinfo5(10)
printinfo5(70, 60, 50)

# 加了两个星号 ** 的参数会以字典的形式导入。

# 可写函数说明
def printinfo6(arg1, **vardict):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    print(vardict)

# 调用printinfo 函数
printinfo6(1, a=2, b=3)

# 声明函数时，参数中星号 * 可以单独出现，例如:
def f(a,b,*,c):
    return a+b+c
# f(1,2,3)   # 报错
print(f(1, 2, c=3)) # 正常

# python 使用 lambda 来创建匿名函数。
# 可写函数说明
sum = lambda arg1, arg2: arg1 + arg2

# 调用sum函数
print("相加后的值为 : ", sum(10, 20))
print("相加后的值为 : ", sum(20, 20))

##不带参数值的return语句返回None

# Python3.8 新增了一个函数形参语法 / 用来指明函数形参必须使用指定位置参数，不能使用关键字参数的形式。
#
# 在以下的例子中，形参 a 和 b 必须使用指定位置参数，c 或 d 可以是位置形参或关键字形参，而 e 或 f 要求为关键字形参:

# def f(a, b, /, c, d, *, e, f):
#     print(a, b, c, d, e, f)
