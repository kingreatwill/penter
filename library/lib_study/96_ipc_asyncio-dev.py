# https://docs.python.org/zh-cn/3/library/asyncio-dev.html
# Debug 模式
"""
有几种方法可以启用异步调试模式:
1. 将 PYTHONASYNCIODEBUG 环境变量设置为 1 。
2. 使用 -X dev Python 命令行选项。
3. 将 debug=True 传递给 asyncio.run() 。
4. 调用 loop.set_debug() 。

除了启用调试模式外，还要考虑:
1. 将 asyncio logger 的日志级别设置为 logging.DEBUG，例如，下面的代码片段可以在应用程序启动时运行:
logging.basicConfig(level=logging.DEBUG)
2. 配置 warnings 模块以显示 ResourceWarning 警告。一种方法是使用 -W default 命令行选项。

启用调试模式时:
1. asyncio 检查 未被等待的协程 并记录他们；这将消除“被遗忘的等待”问题。
2. 许多非线程安全的异步 APIs (例如 loop.call_soon() 和 loop.call_at() 方法)，如果从错误的线程调用，则会引发异常。
3. 如果执行I/O操作花费的时间太长，则记录I/O选择器的执行时间。
4. 执行时间超过100毫秒的回调将会载入日志。 属性 loop.slow_callback_duration 可用于设置以秒为单位的最小执行持续时间，这被视为“缓慢”。

asyncio使用 logging 模块，所有日志记录都是通过 "asyncio" logger执行的。
logging.getLogger("asyncio").setLevel(logging.WARNING)
"""



import asyncio
import threading


async def coro_func():
    return await asyncio.sleep(1,result=42)

async def anther(loop):
    # Later in another OS thread:
    future = asyncio.run_coroutine_threadsafe(coro_func(), loop)
    # Wait for the result:
    result = future.result()
    print(result)

def start_loop(loop):
    #  运行事件循环， loop作为参数
    asyncio.set_event_loop(loop)
    loop.run_forever()


thread_loop = asyncio.new_event_loop()  # 创建事件循环
run_loop_thread = threading.Thread(target=start_loop, args=(thread_loop,))  # 新起线程运行事件循环, 防止阻塞主线程
run_loop_thread.start()  # 运行线程，即运行协程事件循环

loop = asyncio.new_event_loop() #asyncio.ProactorEventLoop()  # asyncio.get_event_loop()
asyncio.run(anther(thread_loop)) # loop.run_until_complete(anther(thread_loop))
# anther(thread_loop) 一定要是线程loop


import asyncio
from threading import Thread


async def create_task(event_loop):
    i = 0
    while True:
        # 每秒产生一个任务, 提交到线程里的循环中, event_loop作为参数
        asyncio.run_coroutine_threadsafe(production(i), event_loop)
        await asyncio.sleep(1)
        i += 1


async def production(i):
    while True:
        print("第{}个coroutine任务".format(i))
        await asyncio.sleep(1)


def start_loop(loop):
    #  运行事件循环， loop作为参数
    asyncio.set_event_loop(loop)
    loop.run_forever()


thread_loop = asyncio.new_event_loop()  # 创建事件循环
run_loop_thread = Thread(target=start_loop, args=(thread_loop,))  # 新起线程运行事件循环, 防止阻塞主线程
run_loop_thread.start()  # 运行线程，即运行协程事件循环

main_loop = asyncio.new_event_loop()
main_loop.run_until_complete(create_task(thread_loop))  # 主线程负责create coroutine object
