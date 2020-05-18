# decorator 装饰器/修饰器  wrapper包装器
# https://blog.csdn.net/luoz_java/article/details/90339876
import time

def deco01(func):
    print("立即执行")
    def wrapper(*args, **kwargs):
        print("this is deco01")
        startTime = time.time()
        func(*args, **kwargs)
        endTime = time.time()
        msecs = (endTime - startTime)*1000
        print("time is %d ms" %msecs)
        print("deco01 end here")
    return wrapper

def deco02(func):
    print("立即执行")
    def xxx(*args, **kwargs):
        print("this is deco02")
        func(*args, **kwargs)
        print("deco02 end here")
    return xxx

@deco01
@deco02
def func(a,b):
    print("hello，here is a func for add :")
    time.sleep(1)
    print("result is %d" %(a+b))

if __name__ == '__main__':
    f = func
    f(3,4)
    print(f.__name__)

print("-----------")
def logging(level):
    print("立即执行")
    def wrapper(func):
        print("xxx立即执行")
        def inner_wrapper(*args, **kwargs):
            print('[{level}]: enter function {func}()'.format(
                level=level,
                func=func.__name__))
            return func(*args, **kwargs)
        return inner_wrapper
    return wrapper

@logging(level='INFO')
def say(something):
    print('say {}!'.format(something))

# 如果没有使用@语法，等同于
# say = logging(level='INFO')(say)
@logging(level='DEBUG')
def do(something):
    print('do {}...'.format(something))

if __name__ == '__main__':
    say('hello')
    do('my work')
"""
[INFO]: enter function say()
say hello!
[DEBUG]: enter function do()
do my work...
"""

print("-----------")
from functools import wraps
import datetime

def logging(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """print log before a function."""
        print('[DEBUG] {}: enter {}()'.format(datetime.datetime.now(), func.__name__))
        return func(*args, **kwargs)
    return wrapper

@logging
def say(something):
    """say something"""
    print('say {}!'.format(something))


say("x")

print(say.__name__)  # say
print(say.__doc__) # say something





print("-------------------------------inspect.unwrap  解包器")
# unwrap方法接受两个参数：func为需要解包装的函数；stop接受一个单参数的函数，
# 作为回调函数，每次会将即将解包装的函数对象传入到回调函数中，如果回调函数返回True，则会提前终止解包，如果没有返回值，或返回Flase，
# unwrap会逐层解包直至装饰链中的最后一个函数对象。
# 另外能正常解包装的前提是装饰器上添加了@wraps(func)装饰器。

from inspect import unwrap
from functools import wraps

__author__ = 'blackmatrix'


def test_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('test_decorator')
        return func(*args, **kwargs)
    return wrapper


def test_decorator2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('test_decorator2')
        return func(*args, **kwargs)
    return wrapper


def test_decorator3(func):
    def wrapper(*args, **kwargs):
        print('test_decorator3')
        return func(*args, **kwargs)
    return wrapper


# 测试只有一个装饰器的情况下，能否正常解包
@test_decorator
def spam():
    print('spam1', '\n')


# 测试两个装饰器情况下，能否正常解包
@test_decorator2
@test_decorator
def spam2():
    print('spam2', '\n')


# 测试多个装饰器情况下，其中一个装饰器的包装器没有使用@wraps
@test_decorator2
@test_decorator3
@test_decorator
def spam3():
    print('spam3', '\n')


def callback(obj):
    obj()

def callback2(obj):
    if obj is spam2:
        print(True)
        obj()
        return True


#spam()
unwrap_spam = unwrap(spam)
unwrap_spam()

unwrap_spam2 = unwrap(spam2)
unwrap_spam2()

#从运行结果可以看出，运行解包后的函数unwrap_spam3，test_decorator2没有被打印出来，说明被成功解包，
# 而装饰器test_decorator3、test_decorator都正常运行（都正常打印值），并没有解包成功。
# 所以，多个装饰器情况下，如果其中一个装饰器没有使用@wraps，那么在装饰链中，unwrap只能解包到未使用@wraps的装饰器。
unwrap_spam3 = unwrap(spam3)
unwrap_spam3()
print("----------")
unwrap_spam2_unwrap = unwrap(spam2, stop=callback)

# 第一次解包的运行结果，解包此时调用依次调用test_decorator2、test_decorator、spam2所以会由如上的输出结果。
# 第二次解包的运行结果，此时回调函数的调用顺序是test_decorator、spam2

print("---------------")
unwrap_spam2_unwrap2 = unwrap(spam2, stop=callback2)