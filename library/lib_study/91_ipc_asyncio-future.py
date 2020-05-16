# https://docs.python.org/zh-cn/3/library/asyncio-future.html
"""
asyncio.isfuture(obj)
如果 obj 为下面任意对象，返回 True：
一个 asyncio.Future 类的实例，
一个 asyncio.Task 类的实例，
带有 _asyncio_future_blocking 属性的类似 Future 的对象。

asyncio.wrap_future(future, *, loop=None)
将一个 concurrent.futures.Future 对象封装到 asyncio.Future 对象中。
"""
import asyncio
import time

now = lambda: time.time()


async def do_some_work(x):
    print('Waiting: ', x)
    await asyncio.sleep(x)
    return 'Done after {}s'.format(x)


start = now()

coroutine = do_some_work(2)
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(coroutine)
loop.run_until_complete(task)

print('Task ret: ', task.result())
print('TIME: ', now() - start)

print("----------------------Future 对象")


async def set_after(fut, delay, value):
    # Sleep for *delay* seconds.
    await asyncio.sleep(delay)

    # Set *value* as a result of *fut* Future.
    fut.set_result(value)


async def main():
    # Get the current event loop.
    loop = asyncio.get_running_loop()

    # Create a new Future object.
    fut = loop.create_future()

    # Run "set_after()" coroutine in a parallel Task.
    # We are using the low-level "loop.create_task()" API here because
    # we already have a reference to the event loop at hand.
    # Otherwise we could have just used "asyncio.create_task()".
    loop.create_task(
        set_after(fut, 1, '... world'))

    print('hello ...')

    # Wait until *fut* has a result (1 second) and print it.
    print(await fut)


asyncio.run(main())
