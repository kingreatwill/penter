# 打开一个文件
import os

f = open("foo.txt", "w")

num = f.write( "Python 是一个非常好的语言。\n是的，的确非常好!!\n" )
print(num) # 字符数
# 关闭打开的文件
f.close()


#为了读取一个文件的内容，调用 f.read(size), 这将读取一定数目的数据, 然后作为字符串或字节对象返回。
#size 是一个可选的数字类型的参数。 当 size 被忽略了或者为负, 那么该文件的所有内容都将被读取并且返回。
#以下实例假定文件 foo.txt 已存在（上面实例中已创建）：
# 打开一个文件
f = open("foo.txt", "r")

str = f.read()
print(str)

# 关闭打开的文件
f.close()

# f.readline() 会从文件中读取单独的一行。换行符为 '\n'。f.readline() 如果返回一个空字符串, 说明已经已经读取到最后一行。
# 打开一个文件
f = open("foo.txt", "r")

str = f.readline()
print(str)

# 关闭打开的文件
f.close()

# f.readlines() 将返回该文件中包含的所有行。
# 打开一个文件
f = open("foo.txt", "r")

str = f.readlines()
print(str)

# 关闭打开的文件
f.close()

# 打开一个文件
f = open("foo.txt", "r")

for line in f:
    print(line, end='')

# 关闭打开的文件
f.close()

# seek(x,0) ： 从起始位置即文件首行首字符开始移动 x 个字符
# seek(x,1) ： 表示从当前位置往后移动x个字符
# seek(-x,2)：表示从文件的结尾往前移动x个字符
f = open('foo.txt', 'rb+')

f.seek(5)     # 移动到文件的第六个字节
print( f.read(1))

f.seek(-3, 2) # 移动到文件的倒数第三字节
print( f.read(1))

f.close()

os.remove("foo.txt")
