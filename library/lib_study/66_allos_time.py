#该模块提供了各种时间相关的函数。相关功能还可以参阅 datetime 和 calendar 模块。
import os
import time

# 1970年1月1日00:00:00（UTC）
print(time.gmtime(0))
print(time.asctime())
# print(time.pthread_getcpuclockid(os.getpid()))
print(time.time())
print(time.ctime(1589438695))
print(time.gmtime(1589438695))
print(time.localtime(1589438695))
print(time.thread_time())
print(time.get_clock_info("thread_time"))
print(time.process_time())
print(time.perf_counter())
print(time.monotonic())

print(time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime()))
