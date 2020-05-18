"""
$ python3 -m timeit '"-".join(str(n) for n in range(100))'
10000 loops, best of 5: 30.2 usec per loop
$ python3 -m timeit '"-".join([str(n) for n in range(100)])'
10000 loops, best of 5: 27.5 usec per loop
$ python3 -m timeit '"-".join(map(str, range(100)))'
10000 loops, best of 5: 23.2 usec per loop
"""
# https://docs.python.org/zh-cn/3/library/timeit.html#timeit-examples
import timeit

print(timeit.timeit('"-".join(str(n) for n in range(100))', number=10000))

print(timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000))

print(timeit.timeit('"-".join(map(str, range(100)))', number=10000))

print(timeit.timeit(lambda: "-".join(map(str, range(100))), number=10000))


# 要让 timeit 模块访问你定义的函数，你可以传递一个包含 import 语句的 setup 参数:
def test():
    """Stupid test function"""
    L = [i for i in range(100)]

if __name__ == '__main__':
    import timeit
    print(timeit.timeit("test()", setup="from __main__ import test"))

# 另一种选择是将 globals() 传递给 globals 参数，这将导致代码在当前的全局命名空间中执行。这比单独指定 import 更方便
def f(x):
    return x**2
def g(x):
    return x**4
def h(x):
    return x**8

import timeit
print(timeit.timeit('[func(42) for func in (f,g,h)]', globals=globals()))