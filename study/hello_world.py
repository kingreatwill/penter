import keyword
import logging
import sys
from random import random


logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')

x = 'runoob'; sys.stdout.write(x + '\n')
x = 'runoob'
tuple = ('runoob', 786, 2.23, 'john', 70.2)
list = ['runoob', 786, 2.23, 'john', 70.2]# del list[2]
student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
# student2 = set(("Tom", "Jim", "Mary"))
# 元组是不允许更新的。而列表是允许更新的
print(x * 2)
print(x[1:5])
print(x[1:])
print(x[:5])
print(x[:-1])
print(x[-2:])

print(x[1:5:2])  # 2 是步长
print(tuple[1:5:2])
print(list[1:5:2])

dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}

# print(dict["2"]) 报错
print(dict[2])
print(dict.keys())
print(dict.values())

print(1 / 2)

print(1 // 2)  # 整除

print(2 ** 3)  # 幂

'''
is 与 == 区别：

is 用于判断两个变量引用对象是否为同一个(同一块内存空间)， == 用于判断引用变量的值是否相等。
'''

count = 0
while count < 5:
    print(count, " is  less than 5")
    count = count + 1
else:
    print(count, " is not less than 5")


for num in range(10,20):  # 迭代 10 到 20 之间的数字
   for i in range(2,num): # 根据因子迭代
      if num%i == 0:      # 确定第一个因子
         j=num/i          # 计算第二个因子
         pass
         print ('%d 等于 %d * %d' % (num,i,j))
         break            # 跳出当前循环
   else:                  # 循环的 else 部分
       print (num, '是一个质数')
else:                  # 循环的 else 部分
   print ('xxx')

print(random())

print(abs(20))

# 保留的关键字
print(keyword.kwlist)

ipt = input("\n\n按下 enter 键后退出。")
# 不换行输出
print(ipt, end=" ")
print(sys.argv)
print(sys.path)

# 复数( (complex)) - 复数由实数部分和虚数部分构成，可以用a + bj,或者complex(a,b)表示， 复数的实部a和虚部b都是浮点型。
print(3.14j)
print(type("a"), type(1), type(1.00), type(3j))

# type()不会认为子类是一种父类类型。
# isinstance()会认为子类是一种父类类型。
print(type(1) == int)
print(isinstance(1, int))

def af():
    '''这是文档字符串'''
    pass
print(af.__doc__)

print(1 | 2 | 4 ) # 不要简单的理解为相加！！！

# 0xA0F # 十六进制
# 0o37 # 八进制

print(True - False)