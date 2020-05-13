Python有以下几种类型的文件：

py：Python控制台程序的源代码文件

pyw：Python带用户界面的源代码文件

pyx：Python包源文件

pyc：Python字节码文件,可以 python xx.pyc

pyo：Python优化后的字节码文件  可以 python xx.pyo

pyd：Python的库文件（Python版DLL）、在Linux上是so文件

pyc的作用是用来跨平台使用的，和Java中的Class文件类似。pyc文件是一种字节码文件，可以加快Python解释器的加载速度，当然也可以用来做简单的防源码泄露保护。

pyo则是优化过后的字节码文件，不过pyo更像编译型语言里的中间文件。

py_compile
codeop
```
import py_compile

py_compile.compile(file = "a.py",cfile = "a.pyc",optimize=-1)

py_compile.compile(file = "b.py",cfile = "b.pyo",optimize=1)
```
也可以直接通过Python加载模块来运行：
```
#编译成pyc
python -m py_compile 源代码

#编译成pyo

python -O -m py_compile 源代码
```

调用m.py模块时，当我们在a.py写以下内容时，运行python a.py  会生成m.pyc ??
```
import m
if __name__ == '__main__':
    ...
```

每次Python的解释器都把模块给持久化成了pyc文件，那么当我的模块发生了改变的时候，是不是都要手动地把以前的pyc文件remove掉呢？

当然Python的设计者是不会犯这么白痴的错误的。而这个过程其实就取决于PyCodeObject是如何写入pyc文件中的。

我们来看一下import过程吧：其实他在写入pyc文件的时候，写了一个Long型变量，变量的内容则是文件的最近修改日期，
同理，我们再看下载入pyc：每次在载入之前都会先检查一下py文件和pyc文件保存的最后修改日期，如果不一致则重新生成一份pyc文件

其实Python是否保存成pyc文件和我们在设计缓存系统时是一样的
