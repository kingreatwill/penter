from sympy import *
x = symbols("x")  # 符号x，自变量
y = -pow(10,-11)*pow(x,6) + pow(10,-8)*pow(x,5) - 4*pow(10,-6)*pow(x,4) + 0.0006*pow(x,3) - 0.0428*pow(x,2) + 1.7561*x + 16.528 #公式

dify = diff(y,x) #求导
print(dify)  #打印导数

#给定x值，求对应导数的值

for i in range(0,305,5):
    print(dify.subs('x',i))


x2 = symbols("x2")  # 符号x2，自变量
y2 = pow(x2,2)

dify2 = diff(y2,x2) #求导
print(dify2)  #打印导数