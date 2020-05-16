from threading import Thread
from multiprocessing import Process
import os
import time

"""
multiprocessing.set_start_method(method)
设置启动子进程的方法。 method 可以是 'fork' , 'spawn' 或者 'forkserver' 。

注意这最多只能调用一次，并且需要藏在 main 模块中，由 if __name__ == '__main__' 进行保护。
"""

# https://www.cnblogs.com/guapitomjoy/p/11537612.html
def func():
    print('hello pid ', os.getpid())


if __name__ == '__main__':
    # 在主进程开启多个线程，每个线程都跟主进程pid一样
    t1 = Thread(target=func)
    t2 = Thread(target=func)
    t1.start()
    t2.start()

    # 开个多个子进程，每个进程都有不同的pid：
    p1 = Process(target=func)
    p2 = Process(target=func)
    p1.start()
    p2.start()

    print('主线程/主进程pid:', os.getpid())

if __name__ == '__main__':  # 如果不加 可能会重复，因为多进程
    print("------------1")

from multiprocessing import Pool


def f(x):
    return x * x


if __name__ == '__main__':
    with Pool(5) as p:
        print(p.map(f, [1, 2, 3]))

if __name__ == '__main__':
    print("--------------2")


def fname(name):
    print('hello name ', name)


if __name__ == '__main__':
    p = Process(target=fname, args=('bob',))
    p.start()
    p.join()

if __name__ == '__main__':
    print("--------------Queue 通信")

from multiprocessing import Process, Queue


def fq(q):
    q.put([42, None, 'hello'])


if __name__ == '__main__':
    q = Queue()
    p = Process(target=fq, args=(q,))
    p.start()
    print(q.get())  # prints "[42, None, 'hello']"
    p.join()

if __name__ == '__main__':
    print("--------------Pipe 通信")

from multiprocessing import Process, Pipe


def fp(conn):
    conn.send([42, None, 'hello'])
    conn.close()


if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=fp, args=(child_conn,))
    p.start()
    print(parent_conn.recv())  # prints "[42, None, 'hello']"
    p.join()

if __name__ == '__main__':
    print("--------------Lock 同步")
from multiprocessing import Process, Lock


def fl(l, i):
    l.acquire()
    try:
        print('hello world', i)
    finally:
        l.release()


if __name__ == '__main__':
    lock = Lock()
    for num in range(10):
        Process(target=fl, args=(lock, num)).start()

if __name__ == '__main__':
    print("--------------Value, Array 共享内存")

from multiprocessing import Process, Value, Array

def fav(n, a):
    n.value = 3.1415927
    for i in range(len(a)):
        a[i] = -a[i]

if __name__ == '__main__':
    num = Value('d', 0.0)
    arr = Array('i', range(10))

    p = Process(target=fav, args=(num, arr))
    p.start()
    p.join()

    print(num.value)
    print(arr[:])

if __name__ == '__main__':
    print("--------------Manager 服务进程管理")
# Manager() 返回的管理器支持类型： list 、 dict 、 Namespace 、 Lock 、 RLock 、 Semaphore 、 BoundedSemaphore 、 Condition 、 Event 、 Barrier 、 Queue 、 Value 和 Array 。

from multiprocessing import Process, Manager

def fm(d, l):
    d[1] = '1'
    d['2'] = 2
    d[0.25] = None
    l.reverse()

if __name__ == '__main__':
    with Manager() as manager:
        d = manager.dict()
        l = manager.list(range(10))

        p = Process(target=fm, args=(d, l))
        p.start()
        p.join()

        print(d)
        print(l)