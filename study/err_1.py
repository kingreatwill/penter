import sys


class MyError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

try:
    print("try")
    raise MyError(2*2) #Exception('x的值为: {}'.format(123))
except FileNotFoundError:
    print("except")
else: # 没有异常时执行
    print("else")
finally:
    print("finally")



while True:
    try:
        x = int(input("请输入一个数字: "))
        break
    except ValueError as err:
        print("Unexpected error:", sys.exc_info()[0])
        print("OS error: {0}".format(err))
        print("您输入的不是数字，请再次尝试输入！")
        #raise # 使用 raise 语句抛出一个指定的异常。
    except (RuntimeError, TypeError, NameError):
        pass
    except OSError:
        pass