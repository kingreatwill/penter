# 平方根，又叫二次方根，表示为〔√￣〕，如：数学语言为：√￣16=4。语言描述为：根号下16=4。
import math

num = 16
num_sqrt = num ** 0.5
print(' %0.3f 的平方根为 %0.3f'%(num ,num_sqrt))


# 该程序只适用于正数。负数和复数可以使用以下的方式：
import cmath

print(cmath.sqrt(num))

num = -16
num_sqrt = cmath.sqrt(num)
print('{0} 的平方根为 {1:0.3f}+{2:0.3f}j'.format(num, num_sqrt.real, num_sqrt.imag))

# Python 二次方程
# 二次方程式 ax**2 + bx + c = 0
# a、b、c 用户提供，为实数，a ≠ 0

# x= （-b ± sqrt[b² - 4ac]）/2a
# 导入 cmath(复杂数学运算) 模块
import cmath

a = 2 # float(input('输入 a: '))
b = 2 # float(input('输入 b: '))
c = 2 # float(input('输入 c: '))

# 计算
d = (b ** 2) - (4 * a * c)

# 两种求解方式
sol1 = (-b - cmath.sqrt(d)) / (2 * a)
sol2 = (-b + cmath.sqrt(d)) / (2 * a)

print('结果为 {0} 和 {1}'.format(sol1, sol2))

# Python 计算三角形的面积

# 已知三角形底a，高h
# 面积s = ah/2

# 已知三角形三边a,b,c
# p =(a+b+c)/2
# 面积S=sqrt[p(p-a)(p-b)(p-c)]

# 设三角形三边分别为a、b、c，内切圆半径为r
#则三角形面积 s=(a+b+c)r/2

# 设三角形三边分别为a、b、c，外接圆半径为R
# 则三角形面积=abc/4R

# 已知三角形两边a,b,这两边夹角C
# s= a*b*sin C/2

a = 2 # float(input('输入三角形第一边长: '))
b = 2 # float(input('输入三角形第二边长: '))
c = 2 # float(input('输入三角形第三边长: '))

# 计算半周长
s = (a + b + c) / 2

# 计算面积
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
print('三角形面积为 %0.2f' % area)


# 定义一个方法来计算圆的面积
def findArea(r):
    return math.pi * r**2
# 调用方法
print("圆的面积为 %.6f" % findArea(5))

