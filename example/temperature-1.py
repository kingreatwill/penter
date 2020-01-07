
# 用户输入摄氏温度
# 接收用户输入
celsius = 37 # float(input('输入摄氏温度: '))

# 计算华氏温度
fahrenheit = (celsius * 1.8) + 32
print('%0.1f 摄氏温度转为华氏温度为 %0.1f ' % (celsius, fahrenheit))

print('{0:0.1f} 摄氏温度转为华氏温度为 {1:0.1f} '.format(celsius, fahrenheit))

# 摄氏温度转华氏温度的公式为 celsius * 1.8 = fahrenheit - 32。

a = input("请输入带有符号的温度值: ")
if a[-1] in ['F','f']:
    C = (eval(a[0:-1]) - 32)/1.8
    print("转换后的温度是{:.1f}C".format(C))
elif a[-1] in ['C','c']:
    F = 1.8*eval(a[0:-1]) + 32
    print("转换后的温度是{:.1f}F".format(F))
else:
    print("输入格式错误")