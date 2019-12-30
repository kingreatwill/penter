total = 0  # 这是一个全局变量


# 可写函数说明
def sum(arg1, arg2):
    # 返回2个参数的和."
    total = arg1 + arg2  # total在这里是局部变量.
    print("函数内是局部变量 : ", total)
    return total


# 调用sum函数
sum(10, 20)
print("函数外是全局变量 : ", total)

# 以下实例修改全局变量 num：
num = 1 # global 变量
def fun1():
    global num  # 需要使用 global 关键字声明
    print(num)
    num = 123
    print(num)
fun1()
print(num)

# 如果要修改嵌套作用域（enclosing 作用域，外层非全局作用域）中的变量则需要 nonlocal 关键字了
def outer():
    num = 10
    def inner():
        nonlocal num  # nonlocal关键字声明
        num = 100
        print(num)
    inner()
    print(num)
outer()


global_var='this  var  on  global space'
'''
申明global_var这个位置就是全局域，也就是教程中所说的全局作用域，
同时它也是直接声明在文件中的，而不是声明在函数中或者类中的变量
'''
class demo():
  class_demo_local_var='class member'
  '''
  虽然class_demo_local_var在这里是局部变量，这个局部变量的域相对于var_locals是外部域，
  所以可以直接被var_locals所在的更小的局部域访问
  '''
  def localFunc(self):
    var_locals='local_func_var'
    '''
    这里也是局部变量，但是相对于class_demo_local_var变量，却是更小的域，
    因此class_demo_local_var所在的哪个域无法访问到当前域来
    '''
    print(self.class_demo_local_var)#到这里会查找当前域中有没有class_demo_local_var这个变量，然后再到相对于当前域的外部域去查找变量

d = demo()
d.localFunc()