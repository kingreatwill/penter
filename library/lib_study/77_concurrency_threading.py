import threading

print(threading.active_count())
print(threading.current_thread())
print(threading.get_ident())
# print(threading.get_native_id())
print(threading.enumerate())
print(threading.main_thread())
main_data = threading.local()
main_data.x = 10
print(main_data.x)  # 是不是java中的ThreadLocal?


def hook_run(a, b, c):
    print("线程的 run()")


def thread_func1():
    print(threading.enumerate())
    thread_data = threading.local()
    thread_data.x = 20
    print("xxxxxxxxx")


# threading.settrace(hook_run)

t = threading.Thread(target=thread_func1)
t.start()


class Myt(threading.Thread):
    def run(self):
        print('子线程 start')
        print('子线程 end')


t2 = Myt()
t2.start()
print('主线程')

print("wwwww", main_data.x)
"""
with some_lock:
    # do something...
相当于:
some_lock.acquire()
try:
    # do something...
finally:
    some_lock.release()
"""
print("-----------------------------Lock")
lock = threading.Lock()
if lock.acquire():
    # lock.acquire()
    print("lock.locked", lock.locked())
lock.release()
print("lock.release", lock.locked())
print("-----------------------------递归锁 重入锁 RLock，必须同一个线程可以重入")
# 一旦线程获得了重入锁，同一个线程再次获取它将不阻塞；线程必须在每次获取它时释放一次。
rlock = threading.RLock()
if rlock.acquire():
    rlock.acquire()  # 可以再次进入
    print("rlock.locked")
rlock.release()
rlock.release()  # 释放两次
# 再次释放报错 rlock.release()
print("rlock.release")
print("-----------------------------条件锁 Condition")
# 生产者通知消费者消费
# import threading,time
# from random import randint
# class Producer(threading.Thread):
#     def run(self):
#         global L
#         while True:
#             val=randint(0,100)
#             # print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
#             print('生产者',self.name,' Append'+str(val),L)
#             if lock_con.acquire():
#                 L.append(val)
#                 lock_con.notify()
#                 lock_con.release()
#             time.sleep(3)
# class Consumer(threading.Thread):
#     def run(self):
#         global L
#         while True:
#             lock_con.acquire()
#             if len(L)==0:
#                 lock_con.wait()
#             print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
#             print('消费者',self.name,'Delete'+str(L[0]),L)
#             del L[0]
#             lock_con.release()
#             time.sleep(0.5)
# if __name__=='__main__':
#     L=[]
#     lock_con=threading.Condition()
#     threads=[]
#     for i in range(5):
#         threads.append(Producer())
#     threads.append(Consumer())
#     for t in threads:
#         t.start()
#     for t in threads:
#         t.join()
print("-----------------------------信号量锁 Semaphore BoundedSemaphore")
# 控制最大线程数
# 每当调用acquire()时内置计数器-1；
# 调用release() 时内置计数器+1；
# 当计数器为0时，acquire()将阻塞线程直到其他线程调用release()；
# BoundedSemaphore 在调用release()的时候，会校验一下当前信号量的值，是否会大于初始值（只定义了5个信号量，释放了5次后，还要调用release）的场景，会抛出异常
# 而 Semaphore在这种场景下，release()的结果只是None,没有返回信号量对象,并不会抛出异常
# from threading import Thread, Semaphore
# import time
#
#
# def test(a):
#     # 打印线程的名字
#     print(t.name)
#     print(a)
#     time.sleep(2)
#     # 释放 semaphore
#     sem.release()
#
#
# # 设置计数器的值为 5
# sem = Semaphore(5)
# for i in range(10):
#     # 获取一个 semaphore
#     sem.acquire()
#     t = Thread(target=test, args=(i,))
#     t.start()
print("-----------------------------事件 Event")
# set()：可设置Event对象内部的信号标志为True
# clear()：可清除Event对象内部的信号标志为False
# isSet()：Event对象提供了isSet()方法来判断内部的信号标志的状态。当使用set()后，isSet()方法返回True；当使用clear()后，isSet()方法返回False
# wait()：该方法只有在内部信号为True的时候才会被执行并完成返回。当内部信号标志为False时，则wait()一直等待到其为True时才返回

print("-----------------------------定时器 Timer")


def hello():
    print("hello, world")


t = threading.Timer(3.0, hello)
t.start()  # after 3 seconds, "hello, world" will be printed
print("-----------------------------栅栏 Barrier")
# 栅栏类提供一个简单的同步原语，用于应对固定数量的线程需要彼此相互等待的情况。
# 线程调用 wait() 方法后将阻塞，直到所有线程都调用了 wait() 方法。此时所有线程将被同时释放。
# b = threading.Barrier(2)
# b.wait()
# b.wait()
# 需要有两个线程wait()  才会往下执行
# 可以用于并发测试
