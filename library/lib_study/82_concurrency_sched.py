import sched

# 进程调度

"""
class sched.scheduler(timefunc=time.monotonic, delayfunc=time.sleep)
scheduler 类定义了一个调度事件的通用接口。 它需要两个函数来实际处理“外部世界” —— timefunc 应当不带参数地调用，并返回一个数字（“时间”，可以为任意单位）。 
delayfunc 函数应当带一个参数调用，与 timefunc 的输出相兼容，并且应当延迟其所指定的时间单位。 
每个事件运行后还将调用 delayfunc 并传入参数 0 以允许其他线程有机会在多线程应用中运行。
"""

import sched, time

s = sched.scheduler(time.time, time.sleep)


def print_time(a='default'):
    print("From print_time", time.time(), a)


def print_some_times():
    print(time.time())
    s.enter(10, 1, print_time)
    s.enter(5, 2, print_time, argument=('positional',))
    s.enter(5, 1, print_time, kwargs={'a': 'keyword'})  # 比上面的先输出，因为级别高！
    s.run()
    print(time.time())


print_some_times()
