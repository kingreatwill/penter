# python测试类

## unittest
unittest提供了test cases、test suites、test fixtures、test runner相关的类,让测试更加明确、方便、可控

https://docs.python.org/3/library/unittest.html
### 特点
- test fixture 测试固件
执行测试的准备工作
- test case 测试用例

- test suite 测试套件
多个测试用例集合，suite可以嵌套suite
- test runner
执行测试用例/套件并向用户提供结果。 运行者可以使用图形界面、文本界面，或者返回一个特殊值来表示执行测试的结果。

### 规则
1. 测试文件必须先import unittest
2. 测试类必须继承unittest.TestCase
3. 测试方法必须以“test_”开头
4. 测试类必须要有unittest.main()方法

## pytest
pytest是python的第三方测试框架,是基于unittest的扩展框架,比unittest更简洁,更高效。
pytest可以执行unittest风格的测试用例,无须修改unittest用例的任何代码,有较好的兼容性。 pytest插件丰富,比如flask插件,可用于用例出错重跑;还有xdist插件,可用于设备并行执行

https://docs.pytest.org/en/latest/

https://www.cnblogs.com/poloyy/category/1690628.html
```
pip install -U pytest
pytest --version
```
### 特点
- 非常容易上手，入门简单，文档丰富，文档中有很多实例可以参考
- 能够支持简单的单元测试和复杂的功能测试
- 支持参数化
- 执行测试过程中可以将某些测试跳过（skip），或者对某些预期失败的case标记成失败
- 支持重复执行(rerun)失败的 case
- 支持运行由 nose, unittest 编写的测试 case
- 可生成 html 报告
- 方便的和持续集成工具 jenkins 集成
- 可支持执行部分用例
- 具有很多第三方插件，并且可以自定义扩展

### 规则
1. 测试文件名必须以“test_”开头或者"_test"结尾(如:test_ab.py)
2. 测试方法必须以“test_”开头(类方法或者函数)。
3. 测试类命名以"Test"开头，不能包含 __init__ 方法。
4. 所有的包 pakege 必项要有__init__.py 文件

### 用例前置和后置
pytest提供了模块级、函数级、类级、方法级的setup/teardown，比unittest的setUp/tearDown更灵活。
模块级（setup_module/teardown_module）开始于模块始末，全局的

函数级（setup_function/teardown_function）只对函数用例生效（不在类中）

类级（setup_class/teardown_class）只在类中前后运行一次(在类中)

方法级（setup_method/teardown_method）开始于方法始末（在类中）

类里面的（setup/teardown）运行在调用方法的前后

 pytest还可以在函数前加@pytest.fixture()装饰器，在测试用例中装在fixture函数。fixture的使用范围可以是function,module,class,session。
 firture相对于setup和teardown来说有以下几点优势：
命名方式灵活，不局限于setup和teardown这几个命名
conftest.py 配置里可以实现数据共享，不需要import就能自动找到一些配置，可供多个py文件调用。
scope="module" 可以实现多个.py跨文件共享前置
scope="session" 以实现多个.py跨文件使用一个session来完成多个用例
用yield来唤醒teardown的执行

### 报告
pytest有pytest-HTML、allure插件。

### 失败重跑
pytest支持用例执行失败重跑，pytest-rerunfailures插件。

### 参数化
unittest需依赖ddt库
@pytest.mark.parametrize 装饰器

### 知识点
- 如果只执行 pytest ，会查找当前目录及其子目录下以  test_*.py  或 *_test.py 文件，找到文件后，在文件中找到以  test 开头函数并执行
- 如果只想执行某个文件，可以 pytest start.py
- 加上-q，就是显示简单的结果： pytest -q start.py
- 如果执行python命令 需要pytest.main函数
- 加-v的话，打印的信息更详细

### cmd
```
pytest demo01_test.py

pytest -v 08_mark.py::TestClass::test_method
# -q 简单打印，只打印测试用例的执行结果
# -s 详细打印
# -x 遇到错误时停止测试 
#--maxfail=num，当用例错误个数达到指定数量时，停止测试

pytest -s -k http start.py # 执行测试用例名称包含http的所有用例
pytest -s -k "not http" start.py # 根据用例名称排除某些用例
pytest -s -k "method or weibo" start.py # 同时匹配不同的用例名称
pytest 08_mark.py::TestClass::test_method

pytest start.py::test_answer

pytest start.py::TestClass::test_two

pytest -m login #将运行用 @pytest.mark.login 装饰器修饰的所有测试
```