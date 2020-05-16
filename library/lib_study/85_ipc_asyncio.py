import asyncio

print("-------------------快速入门")


async def mainasync():
    print('Hello ...')
    await asyncio.sleep(1)
    print('... World!')


async def addasync(x, y):
    r = x + y
    print(r)
    return r


# Python 3.7+
asyncio.run(mainasync())
f = asyncio.run(addasync(45, 23))
print(f)
print("-------------------asyncio-task")
import asyncio
import time


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main2():
    print(f"started at {time.strftime('%X')}")
    await say_after(1, 'hello')
    await say_after(2, 'world')
    print(f"finished at {time.strftime('%X')}")


#  用时3s
asyncio.run(main2())


async def main3():
    task1 = asyncio.create_task(
        say_after(1, 'hello'))

    task2 = asyncio.create_task(
        say_after(2, 'world'))

    print(f"started at {time.strftime('%X')}")
    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    await task1
    await task2
    print(f"finished at {time.strftime('%X')}")


#  用时2s
asyncio.run(main3())


async def main33():
    task1 = asyncio.create_task(
        say_after(1, 'hello'))

    task2 = asyncio.create_task(
        say_after(2, 'world'))

    print(f"started at {time.strftime('%X')}")
    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    await asyncio.gather(task1, task2)
    print(f"finished at {time.strftime('%X')}")

#  用时2s
asyncio.run(main33())
print("-------------可等待 对象有三种主要类型: 协程 async , 任务 asyncio.create_task 和 Future  asyncio.Future.")
"""
async def main():
    await function_that_returns_a_future_object()

    # this is also valid:
    await asyncio.gather(
        function_that_returns_a_future_object(),
        some_python_coroutine()
    )

# In Python 3.7+
task = asyncio.create_task(coro())

# This works in all Python versions but is less readable
task = asyncio.ensure_future(coro())
"""


async def nested():
    return 42


async def main4():
    print("1协程 await ", await nested())  # will print "42".


asyncio.run(main4())


async def main5():
    # Schedule nested() to run soon concurrently
    # with "main()".
    task = asyncio.create_task(nested())

    # task.add_done_callback()

    # task.cancel()
    # "task" can now be used to cancel "nested()", or
    # can simply be awaited to wait until it is complete:
    print("2任务 await ", await task)


asyncio.run(main5())


async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({i})...")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")


async def main6():
    # Schedule three calls *concurrently*:
    await asyncio.gather(
        factorial("A", 2),
        factorial("B", 3),
        factorial("C", 4),
    )


asyncio.run(main6())

print("--------------asyncio.shield（屏障） 屏蔽取消操作：res = await shield(something())")
print("--------------coroutine asyncio.wait_for(aw, timeout, *, loop=None)")
async def eternity():
    # Sleep for one hour
    await asyncio.sleep(3600)
    print('yay!')

async def main7():
    # Wait for at most 1 second
    try:
        await asyncio.wait_for(eternity(), timeout=1.0)
    except asyncio.TimeoutError:
        print('timeout!')

asyncio.run(main7())
print("--------------coroutine asyncio.wait(aws, *, loop=None, timeout=None, return_when=ALL_COMPLETED) 与 wait_for() 不同，wait() 在超时发生时不会取消可等待对象。")
print("--------------asyncio.as_completed(aws, *, loop=None, timeout=None)")
"""
并发地运行 aws 集合中的 可等待对象。返回一个 Future 对象的迭代器。返回的每个 Future 对象代表来自剩余可等待对象集合的最早结果。
"""
print("------------asyncio.run_coroutine_threadsafe(coro, loop)")
"""
# Create a coroutine
coro = asyncio.sleep(1, result=3)

# Submit the coroutine to a given loop
future = asyncio.run_coroutine_threadsafe(coro, loop)

# Wait for the result with an optional timeout argument
assert future.result(timeout) == 3
"""

print("-------asyncio.current_task(loop=None)")
print("-------asyncio.all_tasks(loop=None)")
