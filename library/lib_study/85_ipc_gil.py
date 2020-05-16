from threading import Thread
import time

# Python的GIL是什么鬼，多线程性能究竟如何 http://cenalulu.github.io/python/gil-in-python/
# Python GIL全局解释器锁详解（深度剖析）  http://c.biancheng.net/view/5537.html
def my_counter():
    i = 0
    for _ in range(100000000):
        i = i + 1
    return True


def main2():
    thread_array = {}
    start_time = time.time()
    for tid in range(10):
        t = Thread(target=my_counter)
        t.start()
        thread_array[tid] = t
    for i in range(10):
        thread_array[i].join()
    end_time = time.time()
    print("Total time2: {}".format(end_time - start_time))

def main1():
    start_time = time.time()
    for tid in range(10):
        t = Thread(target=my_counter)
        t.start()
        t.join()
    end_time = time.time()
    print("Total time1: {}".format(end_time - start_time))


if __name__ == '__main__':
    main2()
    main1()

