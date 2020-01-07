x=1
y=2
# 创建临时变量，并交换
temp = x
x = y
y = temp
print('交换后 x 的值为: {},y 的值为: {}'.format(x,y))

# 不使用临时变量
x=1
y=2
x,y = y,x
print('交换后 x 的值为: {},y 的值为: {}'.format(x,y))

# 不使用临时变量2
x=1
y=2

x = x + y
y = x - y
x = x - y

print('交换后 x 的值为: {},y 的值为: {}'.format(x,y))

# 不使用临时变量3 异或形式
x=1
y=2
x = x ^ y
y = x ^ y
x = x ^ y
print('交换后 x 的值为: {},y 的值为: {}'.format(x,y))
