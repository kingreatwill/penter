
## Python 框架
https://github.com/mitsuhiko/pluginbase

## Python插件机制实现
https://github.com/winway/simple-plugin
https://github.com/erhuabushuo/plugin_template
### import机制原理
模块（module）：其实就是一个py文件，里面定义了各种变量，函数，类。

模块除了内建模块（可以用过dir(__builtins__)查看有哪些内建函数），就是非内建模块，这一部分模块就需要用import导入。
非内建模块经常需要按照第三方库，一般第三方模块在"安装路径\Python\Python35\Lib\site-packages"目录下。

包（package）：一个有层次结构的文件目录，里面包含了模块和一些子包，要求包中必须带有一个__init__.py文件。

1. import package

读这个包的__init__.py，也就是说导入包的本质是执行包下面的__init__.py文件，执行结束后会包名的目录下生成一个"__pycache__ / __init__.cpython-36.pyc" 文件。

2. import module

读整个模块的内容

3. import package1.package2.package3.module4

package读取__init__.py，module读取整个模块内容，按顺序读

> 注意：因为package是读取__init__.py，所以调用的时候必须在__init__.py有引用的东西才能调用，否则会报错。


对于python来说，所有被加载到内存的模块都是放在sys.modules里面，所以执行import时会首先去该列表中查询是否已添加。
如果已经在sys.modules中，那就简单了，只需要将该module的name添加到我们正在调用该module的本地空间中。
如果还没有放在sys.modules中，就需要在sys.path所有路径的目录中去按顺序查找该模块的文件，
这些文件一般后缀为".py"、".pyo"、".pyc"、".pyd"、".dll"，找到这些模块后就可以将这些模块添加到sys.modules中，再将module name导入到本地。



### 机制
Python的__import__方法可以动态地加载Python文件，即以某个py脚本的文件名作为__import__的参数，在程序运行的时候加载py脚本程序模块。对应的import关键字则是静态加载依赖的py模块。
```
描述
__import__() 函数用于动态加载类和函数 。
如果一个模块经常变化就可以使用 __import__() 来动态载入。

语法
__import__ 语法：
__import__(name[, globals[, locals[, fromlist[, level]]]])

参数说明：
    name -- 模块名
```
需要动态加载的py脚本若存放在任意的目录下，则需要首先需要增加脚本查找路径：
sys.path.append(modulePath)



### 应用示例
```
# 增加查找路径
sys.path.append(modulePath)
# 加载脚本
module = __import__(moduleName)   
# 保存脚本对象，否则会被析构             
self.modules[moduleName] = module
# 调用插件中的方法初始化
module.InitModule(self)
```