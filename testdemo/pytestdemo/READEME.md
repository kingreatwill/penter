## pytest.ini
pytest配置文件可以改变pytest的运行方式，它是一个固定的文件pytest.ini文件，读取配置信息，按指定的方式去运行

- pytest.ini：pytest的主配置文件，可以改变pytest的默认行为
- conftest.py：测试用例的一些fixture配置
- _init_.py：识别该文件夹为python的package包


pytest --help

### marks
作用：测试用例中添加了 @pytest.mark.webtest 装饰器，如果不添加marks选项的话，就会报warnings

格式：list列表类型

写法：
```
[pytest]
markers =
    weibo: this is weibo page
    toutiao: toutiao
    xinlang: xinlang
```

### xfail_strict

作用：设置xfail_strict = True可以让那些标记为@pytest.mark.xfail但实际通过显示XPASS的测试用例被报告为失败

格式：True 、False（默认），1、0

写法：
```
[pytest]

# mark标记说明
markers =
    weibo: this is weibo page
    toutiao: toutiao
    xinlang: xinlang

xfail_strict = True
```
具体代码栗子

未设置 xfail_strict = True 时，测试结果显示XPASS
```
@pytest.mark.xfail()
def test_case1():
    a = "a"
    b = "b"
    assert a != b

collecting ... collected 1 item

02断言异常.py::test_case1 XPASS [100%]

============================= 1 xpassed in 0.02s ==============================
```
已设置 xfail_strict = True 时，测试结果显示failed
```
collecting ... collected 1 item

02断言异常.py::test_case1 FAILED                                         [100%]
02断言异常.py:54 (test_case1)
[XPASS(strict)] 

================================== FAILURES ===================================
_________________________________ test_case1 __________________________________
[XPASS(strict)] 
=========================== short test summary info ===========================
FAILED 02断言异常.py::test_case1
============================== 1 failed in 0.02s ==============================
```

### addopts

作用：addopts参数可以更改默认命令行选项，这个当我们在cmd输入一堆指令去执行用例的时候，就可以用该参数代替了，省去重复性的敲命令工作

比如：想测试完生成报告，失败重跑两次，一共运行两次，通过分布式去测试，如果在cmd中写的话，命令会很长

pytest -v --rerun=2 --count=2 --html=report.html --self-contained-html -n=auto

每次都这样敲不太现实，addopts就可以完美解决这个问题
```
[pytest]

# mark
markers =
    weibo: this is weibo page
    toutiao: toutiao
    xinlang: xinlang

xfail_strict = True

# 命令行参数
addopts = -v --reruns=1 --count=2 --html=reports.html --self-contained-html -n=auto
```
加了addopts之后，我们在cmd中只需要敲pytest就可以生效了！！

### log_cli
作用：控制台实时输出日志

格式：log_cli=True 或False（默认），或者log_cli=1 或 0

加了log_cli=1之后，可以清晰看到哪个package下的哪个module下的哪个测试用例是否passed还是failed；
所以平时测试代码是否有问题的情况下推荐加！！！但如果拿去批量跑测试用例的话不建议加，谁知道会不会影响运行性能呢？

### norecursedirs
作用：pytest 收集测试用例时，会递归遍历所有子目录，包括某些你明知道没必要遍历的目录，遇到这种情况，可以使用 norecursedirs 参数简化 pytest 的搜索工作【还是挺有用的！！！】

默认设置： norecursedirs = .* build dist CVS _darcs {arch} *.egg

正确写法：多个路径用空格隔开
```
[pytest]

norecursedirs = .* build dist CVS _darcs {arch} *.egg venv src resources log report util
```

### 测试用例收集规则
pytest默认的测试用例收集规则

文件名以 test_*.py 文件和 *_test.py
以  test_ 开头的函数
以  Test 开头的类，不能包含 __init__ 方法
以  test_ 开头的类里面的方法
```

[pytest]

python_files =     test_*  *_test  test*
python_classes =   Test*   test*
python_functions = test_*  test*
```

