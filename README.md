# penter
[python标准库](https://docs.python.org/zh-cn/3/library/index.html)

[ Python 第三方包索引](https://pypi.org/)


## 生成requirements.txt
1.
```
pip freeze > requirements.txt

//pip install pycryptodome -i https://pypi.doubanio.com/simple/
//pip install -i https://pypi.doubanio.com/simple/ -r requirements.txt
```
2.
```
pip install pipreqs
// 生成
pipreqs .
pipreqs --encoding=utf-8 .
// 更新
pipreqs --force .
pipreqs --force --encoding=utf-8 .
```

## #!/usr/bin/python3
```
关于脚本第一行的 #!/usr/bin/python 的解释，相信很多不熟悉 Linux 系统的同学需要普及这个知识，脚本语言的第一行，只对 Linux/Unix 用户适用，用来指定本脚本用什么解释器来执行。

有这句的，加上执行权限后，可以直接用 ./ 执行，不然会出错，因为找不到 python 解释器。

#!/usr/bin/python 是告诉操作系统执行这个脚本的时候，调用 /usr/bin 下的 python 解释器。

#!/usr/bin/env python 这种用法是为了防止操作系统用户没有将 python 装在默认的 /usr/bin 路径里。当系统看到这一行的时候，首先会到 env 设置里查找 python 的安装路径，再调用对应路径下的解释器程序完成操作。
#!/usr/bin/python 相当于写死了 python 路径。

#!/usr/bin/env python 会去环境设置寻找 python 目录，可以增强代码的可移植性，推荐这种写法。

分成两种情况：

（1）如果调用 python 脚本时，使用:

python script.py 
#!/usr/bin/python 被忽略，等同于注释

（2）如果调用python脚本时，使用:

./script.py 
#!/usr/bin/python 指定解释器的路径

PS：shell 脚本中在第一行也有类似的声明。

python2 
可能还需要指定编码
# -*- coding: UTF-8 -*-

Python3.X 源码文件默认使用utf-8编码，所以可以正常解析中文，无需指定 UTF-8 编码
```

## Python3 * 和 ** 运算符
### 1. 算数运算
```
*  代表乘法
** 代表乘方
```
### 2. 函数形参
*args 和 **kwargs 主要用于函数定义。

你可以将不定数量的参数传递给一个函数。不定的意思是：预先并不知道, 函数使用者会传递多少个参数给你, 所以在这个场景下使用这两个关键字。其实并不是必须写成 *args 和 **kwargs。  *(星号) 才是必须的. 你也可以写成 *ar  和 **k 。而写成 *args 和**kwargs 只是一个通俗的命名约定。

python函数传递参数的方式有两种：

- 位置参数（positional argument）
- 关键词参数（keyword argument）

*args 与 **kwargs 的区别，两者都是 python 中的可变参数：

- *args 表示任何多个无名参数，它本质是一个 tuple
- **kwargs 表示关键字参数，它本质上是一个 dict

如果同时使用 *args 和 **kwargs 时，必须 *args 参数列要在 **kwargs 之前。
```
>>> def fun(*args, **kwargs):
...     print('args=', args)
...     print('kwargs=', kwargs)
... 
>>> fun(1, 2, 3, 4, A='a', B='b', C='c', D='d')
args= (1, 2, 3, 4)
kwargs= {'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd'}
```
使用 *args
```
>>> def fun(name, *args):
...     print('你好:', name)
...     for i in args:
...         print("你的宠物有:", i)
... 
>>> fun("Geek", "dog", "cat")
你好: Geek
你的宠物有: dog
你的宠物有: cat
```
使用 **kwargs
```
>>> def fun(**kwargs):
...     for key, value in kwargs.items():
...         print("{0} 喜欢 {1}".format(key, value))
... 
>>> fun(Geek="cat", cat="box")
Geek 喜欢 cat
cat 喜欢 box
```

### 3. 函数实参
如果函数的形参是定长参数，也可以使用 *args 和 **kwargs 调用函数，类似对元组和字典进行解引用：
```
>>> def fun(data1, data2, data3):
...     print("data1: ", data1)
...     print("data2: ", data2)
...     print("data3: ", data3)
... 
>>> args = ("one", 2, 3)
>>> fun(*args)
data1:  one
data2:  2
data3:  3
>>> kwargs = {"data3": "one", "data2": 2, "data1": 3}
>>> fun(**kwargs)
data1:  3
data2:  2
data3:  one
```

### 4. 序列解包
https://blog.csdn.net/yilovexing/article/details/80576788

序列解包没有 **。
```
>>> a, b, *c = 0, 1, 2, 3  
>>> a  
0  
>>> b  
1  
>>> c  
[2, 3]
```